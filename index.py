import tornado.ioloop
import tornado.web
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        json_files = ''
        for fle in os.listdir(os.path.dirname(os.path.abspath(__file__))):
            if fle.endswith('.json'):
                li = '<li><a href="javascript:void(0)">' + fle + '</a></li>'
                json_files += li

        self.render('index.html', lis=json_files)

class JsonHandler(tornado.web.RequestHandler):
    def get(self, slug):
        with open(slug) as f:
            slug = f.read().replace('"', '\\"')

        self.render('index_json.html', slug=slug)



class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/json/([^/]+)", JsonHandler),
            # Add more paths here
            #(r"/KillTornado/", StopTornado),
            #(r"/tables/", ReturnQuery),
            #(r"/tables/localhost8888", MainHandler)
        ]
        settings = {
            "template_path": os.path.dirname(os.path.abspath(__file__)),
            "static_path": os.path.dirname(os.path.abspath(__file__)),
        }
        print str(settings)
        tornado.web.Application.__init__(self, handlers, **settings)

def make_app():
    return Application()

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    print 'Go to http://localhost:8000'
    tornado.ioloop.IOLoop.current().start()
