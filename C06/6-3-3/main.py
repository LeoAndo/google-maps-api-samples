# -*- coding: utf-8 -*-
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
import os

class MainHandler(webapp.RequestHandler):
    def get(self):
        template_values = {}
        libraries = [];
        libraries.append({"latlng":[35.672406, 139.706156], "name": u"中央図書館"})
        libraries.append({"latlng":[35.655375, 139.699971], "name": u"こもれび大和田図書館"})
        libraries.append({"latlng":[35.67225, 139.667192],  "name": u"笹塚図書館"})
        libraries.append({"latlng":[35.678713, 139.669714], "name": u"笹塚こども図書館"})
        libraries.append({"latlng":[35.656594, 139.709764],  "name": u"渋谷図書館"})
        libraries.append({"latlng":[35.668501, 139.687124], "name": u"富ケ谷図書館"})
        libraries.append({"latlng":[35.674967, 139.677675], "name": u"西原図書館"})
        libraries.append({"latlng":[35.680735, 139.681658], "name": u"本町図書館"})
        libraries.append({"latlng":[35.68196, 139.695984], "name": u"代々木図書館"})
        libraries.append({"latlng":[35.649273, 139.716714], "name": u"臨川みんなの図書館"})
        template_values["libraries"] = libraries
        
        template_file = "index.html"
        path = os.path.join(os.path.dirname(__file__), './templates', template_file)
        self.response.out.write(template.render(path, template_values))


def main():
    application = webapp.WSGIApplication([('/', MainHandler)], debug=True)
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()
