"""
WSGI config for rjs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

#import os

#from django.core.wsgi import get_wsgi_application

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rjs.settings')

#application = get_wsgi_application()

#from twisted.web.wsgi import WSGIResource
#from twisted.internet import reactor
def application(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/plain')])
    return ['Hello, world']

#resource = WSGIResource(reactor, reactor.getThreadPool(), application)

