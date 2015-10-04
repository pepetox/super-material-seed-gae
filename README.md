Super seed based in google guestbook example. You can see live example here:

https://super-material-seed-gae.appspot.com/

# Super seed

This application is a good start point to make incredible projects. 

Features:

--There are a folder structure to help to maintain the code when get bigget based on rails folder system. 


    Controllers: (in main folder)

      The main_controller.py thats manage the landing page and has the _BaseHandler for use in the rest of handlers of the application.
      The course controller is a good example for a CRUD controller

    Models: (in app/models)
      The course_model has logic to manage the data

    Views: (in app/views)
      There is a base.html with the header and the footer, the other views use this as parent template
      In the course folder there are examples for the crud views (edit, index, new, show)

--Strong consistence or Eventual consistence
  Data are stored in App Engine (NoSQL)
  High Replication Datastore (HRD) and retrieved using a strongly consistent
  (ancestor) query.

--Upload and Download by csv files

  In the index view you can upload or download a csv with the data

--Google based auth

  Anybody can see the main page but the login is required to enter in the course zone.



Super seed based in google guestbook example. You can see live example here:

https://super-material-seed-gae.appspot.com/

## Products
- [App Engine][1]

## Language
- [Python][2]

## APIs
- [NDB Datastore API][3]
- [Users API][4]

## Dependencies
- [webapp2][5]
- [jinja2][6]
- [Materializecss][7]

[1]: https://developers.google.com/appengine
[2]: https://python.org
[3]: https://developers.google.com/appengine/docs/python/ndb/
[4]: https://developers.google.com/appengine/docs/python/users/
[5]: http://webapp-improved.appspot.com/
[6]: http://jinja.pocoo.org/docs/
[7]: http://materializecss.com/
