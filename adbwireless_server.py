from twisted.web import server, resource
from twisted.internet import reactor
from string import split
from pyadb import ADB

class AdbWirelessServer(resource.Resource):
    isLeaf = True
                
    def render_GET(self, request):
        adb = ADB('/usr/bin/adb')
        retour=''
        items=split(request.path,'/')[1:]
        if items[0]=='c':
            retour=adb.connect_remote(items[1])
        elif items[0]=='d':
            retour=adb.disconnect_remote(items[1])
        print "adb : %s" % retour 
        return "OK\n"

reactor.listenTCP(8555, server.Site(AdbWirelessServer()))
reactor.run()
