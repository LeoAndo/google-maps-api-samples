# -*- coding: utf-8 -*-
import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
from google.appengine.ext import db

class MainHandler(webapp.RequestHandler):
    def get(self):
        template_values = {}
        
        places = Place.all().filter("bicycleParking = ", False)
        libraries = []
        for place in places:
            libraries.append({"name" : place.name,
                              "latlng" : [place.location.lat, place.location.lon],
                              "bicycleParking" : place.bicycleParking })
        template_values["libraries"] = libraries
        
        template_file = "index.html"
        path = os.path.join(os.path.dirname(__file__), './templates', template_file)
        self.response.out.write(template.render(path, template_values))

class Place(db.Model):
    name = db.StringProperty()
    location = db.GeoPtProperty()
    bicycleParking = db.BooleanProperty()
    
class ControlPanelHandler(webapp.RequestHandler):
    def get(self):
        template_values = {}
        template_file = "form.html"
        path = os.path.join(os.path.dirname(__file__), './templates', template_file)
        self.response.out.write(template.render(path, template_values))
        
    def post(self):
        self.response.out.write('<html><body>You wrote:<pre>')
        for arg in self.request.arguments():
            self.response.out.write("%s : %s \n" % (arg, self.request.get(arg)))
        self.response.out.write('</pre></body></html>')
            
        lat = float(self.request.get("lat"))
        lng = float(self.request.get("lng"))
        
        place = Place(key_name = self.request.get("keyName"))
        place.name = self.request.get("name")
        place.location = db.GeoPt(lat, lng)
        place.bicycleParking = bool(self.request.get("bicycleParking"))
        place.put()

def main():
    application = webapp.WSGIApplication([('/', MainHandler),
                                          ('/control/', ControlPanelHandler)
                                          ], debug=True) 
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()
