import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb


class Author(ndb.Model):
    """Sub model for representing an author."""
    identity = ndb.StringProperty(indexed=False)
    email = ndb.StringProperty(indexed=False)


class Greeting(ndb.Model):
    """A main model for representing an individual Guestbook entry."""
    author = ndb.StructuredProperty(Author)
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)


#model with expando

class FlexEmployee(ndb.Expando):
  name = ndb.StringProperty()
  age = ndb.IntegerProperty()

#emp = FlexEmployee(name='Sandy', location='SF')
#FlexEmployee.query(ndb.GenericProperty('location') == 'SF')

##KIND OF PROPERTIES

# IntegerProperty  64-bit signed integer
# FloatProperty Double-precision floating-point number
# BooleanProperty Boolean
# StringProperty  Unicode string; up to 1500 bytes, indexed
# TextProperty  Unicode string; unlimited length, not indexed
# BlobProperty  Uninterpreted byte string:
# if you set indexed=True, up to 1500 bytes, indexed;
# if indexed is False (the default), unlimited length, not indexed.
# Optional keyword argument: compressed.
# DateTimeProperty  Date and time (see Date and Time Properties)
# DateProperty  Date (see Date and Time Properties)
# TimeProperty  Time (see Date and Time Properties)
# GeoPtProperty Geographical location. This is a ndb.GeoPt object. The object has attributes lat and lon, both floats. You can construct one with two floats like ndb.GeoPt(52.37, 4.88) or with a string ndb.GeoPt("52.37, 4.88"). (This is actually the same class as db.GeoPt)
# KeyProperty Datastore key
# Optional keyword argument: kind=kind, to require that keys assigned to this property always have the indicated kind. May be a string or a Model subclass.
# BlobKeyProperty Blobstore key
# Corresponds to BlobReferenceProperty in the old db API, but the property value is a BlobKey instead of a BlobInfo; you can construct a BlobInfo from it using BlobInfo(blobkey)
# UserProperty  User object.
# StructuredProperty  Includes one kind of model inside another, by value (see Structured Properties)
# class Contact(ndb.Model):
#   name = ndb.StringProperty()
#   addresses = ndb.StructuredProperty(Address, repeated=True)
# guido = Contact(name='Guido',
#                 addresses=[Address(type='home',
#                                    city='Amsterdam'),
#                            Address(type='work',
#                                    street='Spear St',
#                                    city='SF')])
# LocalStructuredProperty Like StructuredProperty, but on-disk representation is an opaque blob and is not indexed (see Structured Properties).
# Optional keyword argument: compressed.
# JsonProperty  Value is a Python object (such as a list or a dict or a string) that is serializable using Python's json module; the Datastore stores the JSON serialization as a blob. Unindexed by default.
# Optional keyword argument: compressed.
# PickleProperty  Value is a Python object (such as a list or a dict or a string) that is serializable using Python's pickle protocol; the Datastore stores the pickle serialization as a blob. Unindexed by default.
# Optional keyword argument: compressed.
# GenericProperty Generic value
# Used mostly by the Expando class, but also usable explicitly. Its type may be any of int, long, float, bool, str, unicode, datetime, Key, BlobKey, GeoPt, User, None.
# ComputedProperty  Value computed from other properties by a user-defined function. (See Computed Properties.)

##REPEAT
#tags = ndb.StringProperty(repeated=True)


