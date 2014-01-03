from twisted.web import server, resource
from twisted.internet import reactor
from string import split
import subprocess

class HelloResource(resource.Resource):
    isLeaf = True
    numberRequests = 0
                
    def render_GET(self, request):
        self.numberRequests += 1
        request.setHeader("content-type", "text/plain")
        items=split(request.path,'/')[1:]
        if items[0]=='c':
            retour=subprocess.call('adb connect %s' % items[1],shell=True)
            print "connexion avec %s" % items[1]
        elif items[0]=='d':
            retour=subprocess.call('adb disconnect %s' % items[1],shell=True)
            print "Deconnexion avec %s" % items[1]
        return "OK\n"

reactor.listenTCP(8555, server.Site(HelloResource()))
reactor.run()
