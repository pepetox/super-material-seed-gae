import os
import urllib
import logging

from google.appengine.api import users
from google.appengine.ext import ndb



class Course(ndb.Model):
    """A main model for representing an individual coursebook entry."""
    author = ndb.UserProperty(indexed=True)
    name = ndb.StringProperty(indexed=True)
    description = ndb.StringProperty(indexed=False)
    lang = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)

def All():
    return Course.query()


def Get(id):
    logging.info('lanzado el get')
    
    return Course.get_by_id(int(id))


def Update(id, name, description, lang):
    course = Course(id=id, name=name, description=description, lang = lang)
    course.put()
    return course


def Insert(name, description, lang):
    
    user = users.get_current_user()
    if user:
        course = Course(name=name, description=description, lang = lang)
        course.put()
        return course

def Delete(id):
    key = ndb.Key(Course, id)
    key.delete()

