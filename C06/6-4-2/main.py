# -*- coding: utf-8 -*-
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
from google.appengine.ext import db
import os
from geo.geomodel import GeoModel
from geo import geotypes
import simplejson

"""===========================
(1)GeoModelを継承してPlaceクラスを作る
=========================="""
class Place(GeoModel):
    name = db.StringProperty()
    
"""===========================
(2)地点を登録する
=========================="""
class SetupHandler(webapp.RequestHandler):
    def get(self):
        places = [];
        places.append({"latlng":[35.672406, 139.706156], "name": u"中央図書館", "keyName" : "central"})
        places.append({"latlng":[35.655375, 139.699971], "name": u"こもれび大和田図書館", "keyName" : "komorebi"})
        places.append({"latlng":[35.67225, 139.667192],  "name": u"笹塚図書館", "keyName" : "sasadaku"})
        places.append({"latlng":[35.678713, 139.669714], "name": u"笹塚こども図書館", "keyName" : "sasadaku_children"})
        places.append({"latlng":[35.656594, 139.709764],  "name": u"渋谷図書館", "keyName" : "shibuya"})
        places.append({"latlng":[35.668501, 139.687124], "name": u"富ケ谷図書館", "keyName" : "tomigaya"})
        places.append({"latlng":[35.674967, 139.677675], "name": u"西原図書館", "keyName" : "nishihara"})
        places.append({"latlng":[35.680735, 139.681658], "name": u"本町図書館", "keyName" : "honmachi"})
        places.append({"latlng":[35.68196, 139.695984], "name": u"代々木図書館", "keyName" : "yoyogi"})
        places.append({"latlng":[35.649273, 139.716714], "name": u"臨川みんなの図書館", "keyName" : "rinsen"})
        
        for place in places:
            p = Place(key_name = place["keyName"])
            p.location = db.GeoPt(place["latlng"][0], place["latlng"][1])
            p.update_location()     #geocellを計算
            p.name = place["name"]
            p.put()
        self.response.out.write(u"地点を登録しました")

"""===========================
(3)地図を表示
=========================="""
class MainHandler(webapp.RequestHandler):
    def get(self):
        template_file = "map.html"
        path = os.path.join(os.path.dirname(__file__), './templates', template_file)
        self.response.out.write(template.render(path, {}))
        
"""===========================
(4)現在位置のパラメータを元に施設を検索する
=========================="""
class MapHandler(webapp.RequestHandler):
    def get(self):
        places = []
        pos = self.request.get("latlng").split(",")
        pos = geotypes.Point(float(pos[0]), float(pos[1]))
        radius = int(self.request.get("radius"))
        base_query = Place.all()
        for place in Place.proximity_fetch(base_query, pos,  max_distance=radius):
            places.append({"lat" : place.location.lat,
                           "lng" : place.location.lon,
                           "keyName" : place.key().name(),
                           "name" : place.name
                           })
        json = simplejson.dumps(places)
        self.response.out.write(json)

def main():
    application = webapp.WSGIApplication([('/', MainHandler),
                                          ('/proximity', MapHandler),
                                          ('/setup', SetupHandler),
                                          ], debug=True)
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()
