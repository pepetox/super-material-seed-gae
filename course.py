import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2

import app.models.coursemodel as coursemodel

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)



class Index(webapp2.RequestHandler):

    def get(self):
        courses = coursemodel.All()#.order(-models.Greeting.date)
        template_values = { 'courses': courses }
        template = JINJA_ENVIRONMENT.get_template('app/views/course/index.html')
        self.response.write(template.render(template_values))




class Show(webapp2.RequestHandler):

    def get(self):
        id = self.request.get('id')
        course = coursemodel.Get(id = id)
        template_values = {
            'course': course
        }
        template = JINJA_ENVIRONMENT.get_template('app/views/course/show.html')
        self.response.write(template.render(template_values))


class New(webapp2.RequestHandler):

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('app/views/course/new.html')
        self.response.write(template.render())

    def post(self):
        self.course = coursemodel.Insert(name=self.request.get('name'), description=self.request.get('description'), lang=self.request.get('lang'))
        self.redirect('/courses')


class Edit(webapp2.RequestHandler):

    def get(self):
        id = self.request.get('id')
        course = coursemodel.Get(id = id)
        template_values = {
            'course': course
        }
        template = JINJA_ENVIRONMENT.get_template('app/views/course/edit.html')
        self.response.write(template.render(template_values))

    def post(self):
        id = self.request.get('id')
        self.course = coursemodel.Update(id = id, name=self.request.get('name'), description=self.request.get('description'), lang=self.request.get('lang'))
       
       
        self.redirect('/courses')

class Destroy(webapp2.RequestHandler):

    def get(self):
        id = self.request.get('id')
        course = coursemodel.Delete(id = int(id))
        self.redirect('/courses')


app = webapp2.WSGIApplication([
    ('/courses', Index),
    ('/courses/show', Show),
    ('/courses/new', New),
    ('/courses/edit', Edit),
    ('/courses/destroy', Destroy)
], debug=True)