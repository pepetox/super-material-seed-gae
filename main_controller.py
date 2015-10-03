import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2



JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)




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

        template = JINJA_ENVIRONMENT.get_template('app/views/index.html')
        self.response.write(template.render(self.template_values))




app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
