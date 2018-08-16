import os
import sys


def test():
    """ run unittest """
    import unittest
    from users import test
    suite = unittest.TestLoader().loadTestsFromModule(test)
    unittest.TextTestRunner().run(suite)


def run():
    """ run server """
    from users import urls
    if os.environ.get("REQUEST_METHOD", ""):
        from wsgiref.handlers import BaseCGIHandler
        BaseCGIHandler(sys.stdin, sys.stdout, sys.stderr,
                       os.environ).run(urls.urls)
    else:
        from wsgiref.simple_server import WSGIServer, WSGIRequestHandler
        from beaker.middleware import SessionMiddleware

        session_opts = {
            'session.type': 'file',
            'session.cookie_expires': True,
            'session.data_dir': 'var',
        }

        app = SessionMiddleware(urls.urls, session_opts)
        httpd = WSGIServer(('', 8080), WSGIRequestHandler)
        httpd.set_app(app)
        print "Serving HTTP on %s port %s ..." % httpd.socket.getsockname()
        httpd.serve_forever()


def create():
    """ create database """
    from users.model import Base
    from dbconfig import engine
    print "Creating data base..."
    Base.metadata.create_all(engine)
    print "Ok"


if __name__ == "__main__":
    if 'create' in sys.argv:
        create()
    if 'run' in sys.argv:
        test()
        run()
    if 'test' in sys.argv:
        test()
