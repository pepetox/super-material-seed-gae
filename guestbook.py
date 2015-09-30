import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2

import app.models.models as models

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

DEFAULT_GUESTBOOK_NAME = 'default_guestbook'


# We set a parent key on the 'Greetings' to ensure that they are all
# in the same entity group. Queries across the single entity group
# will be consistent. However, the write rate should be limited to
# ~1/second.



def guestbook_key(guestbook_name=DEFAULT_GUESTBOOK_NAME):
    """Constructs a Datastore key for a Guestbook entity.

    We use guestbook_name as the key.
    """
    return ndb.Key('Guestbook', guestbook_name)


class _BaseHandler(webapp2.RequestHandler):
  def initialize(self, request, response):
    super(_BaseHandler, self).initialize(request, response)
    self.user = users.get_current_user()
    if self.user:
        url = users.create_logout_url(self.request.uri)
        url_linktext = 'Logout'
    else:
        url = users.create_login_url(self.request.uri)
        url_linktext = 'Login'

    self.template_values = {
        'user': self.user,
        'url': url,
        'url_linktext': url_linktext,
    }

class MainPage(_BaseHandler):

    def get(self):
        guestbook_name = self.request.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME)
        greetings_query = models.Greeting.query(
            ancestor=guestbook_key(guestbook_name)).order(-models.Greeting.date)
        greetings = greetings_query.fetch(10)
        self.template_values['greetings'] = greetings
        self.template_values['guestbook_name'] = urllib.quote_plus(guestbook_name)
        template = JINJA_ENVIRONMENT.get_template('app/views/index.html')
        self.response.write(template.render(self.template_values))


class Guestbook(_BaseHandler):


    def get(self):
        guestbook_name = self.request.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME)
        greetings_query = models.Greeting.query(
            ancestor=guestbook_key(guestbook_name)).order(-models.Greeting.date)
        greetings = greetings_query.fetch(10)
        self.template_values['greetings'] = greetings
        self.template_values['guestbook_name'] = urllib.quote_plus(guestbook_name)
        template = JINJA_ENVIRONMENT.get_template('app/views/guestbook.html')
        self.response.write(template.render(self.template_values))
        


    def post(self):
        # We set the same parent key on the 'Greeting' to ensure each
        # Greeting is in the same entity group. Queries across the
        # single entity group will be consistent. However, the write
        # rate to a single entity group should be limited to
        # ~1/second.
        guestbook_name = self.request.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME)
        greeting = models.Greeting(parent=guestbook_key(guestbook_name))

        if users.get_current_user():
            greeting.author = models.Author(
                    identity=users.get_current_user().user_id(),
                    email=users.get_current_user().email())

        greeting.content = self.request.get('content')
        greeting.put()

        query_params = {'guestbook_name': guestbook_name}
        self.redirect('/guestbook?' + urllib.urlencode(query_params))


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/guestbook', Guestbook),
    ('/sign', Guestbook),
], debug=True)
