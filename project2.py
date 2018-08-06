from project1 import Shelf, Sensor
import cherrypy,threading

@cherrypy.expose
class StringGeneratorWebService(object):

    @cherrypy.tools.accept(media='text/plain')
    def GET(self,message):
        try:
            numer=int(message)
            if numer>=1 and numer <=24 and Shelf.status=='waiting':
                polka=Shelf(numer)
                #polka.turn_on()
                threadObj= threading.Thread(target=polka.turn_on)
                threadObj.start()
            elif Shelf.status=='running':
                return 'Proszę czekać, nie włożono książki'
            else:
                return "Podano nieprawidłowy numer półki"
        except ValueError:
            if message.lower()=='test' and Shelf.status=='waiting':
                threadObj= threading.Thread(target=Shelf.test)
                threadObj.start()
            elif message.lower()=='check' and Shelf.status=='running':
                return 'Proszę czekać, nie włożono książki'
            elif message.lower()=='check' and Shelf.status=='waiting':
                return 'ok'
            else:
                return "Nierozpoznany komunikat"
        if Shelf.status=='waiting':
            return 'OK'


if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        }
    }
    cherrypy.config.update(
    {'server.socket_host': '0.0.0.0' } ) 
    cherrypy.quickstart(StringGeneratorWebService(), '/', conf)
