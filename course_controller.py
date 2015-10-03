import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2

import main_controller
import app.models.course_model as coursemodel

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)



class Index(main_controller._BaseHandler):

    def get(self):
        courses = coursemodel.All()#.order(-models.Greeting.date)
        self.template_values['courses'] = courses 
        template = JINJA_ENVIRONMENT.get_template('app/views/course/index.html')
        self.response.write(template.render(self.template_values))




class Show(main_controller._BaseHandler):

    def get(self):
        id = self.request.get('id')
        course = coursemodel.Get(id = id)
        self.template_values['course'] = course
        template = JINJA_ENVIRONMENT.get_template('app/views/course/show.html')
        self.response.write(template.render(self.template_values))


class New(main_controller._BaseHandler):

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('app/views/course/new.html')
        self.response.write(template.render())

    def post(self):
        self.course = coursemodel.Insert(name=self.request.get('name'), description=self.request.get('description'), lang=self.request.get('lang'))
        self.redirect('/courses')


class Edit(main_controller._BaseHandler):

    def get(self):
        id = self.request.get('id')
        course = coursemodel.Get(id = id)
        self.template_values['course'] = course
        template = JINJA_ENVIRONMENT.get_template('app/views/course/edit.html')
        self.response.write(template.render(self.template_values))

    def post(self):
        id = self.request.get('id')
        self.course = coursemodel.Update(id = id, name=self.request.get('name'), description=self.request.get('description'), lang=self.request.get('lang'))
       
       
        self.redirect('/courses')

class Destroy(main_controller._BaseHandler):

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