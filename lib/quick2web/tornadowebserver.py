import os
import webserver

from socket import gethostname
from tornado import websocket
from tornado.ioloop import IOLoop
from tornado.web import Application, StaticFileHandler

class TornadoWebServer(webserver.WebServer):

  def __init__(self,
        port,
        debug = False,
        quick2web_resources = os.path.join(os.path.dirname(__file__), 'resources'),
        ioloop = IOLoop.instance()):
    self.handlers = []
    self.application = None
    self.ioloop = ioloop
    self.port = port
    self.url = 'http://%s:%d/' % (gethostname(), self.port)
    self.settings = dict(
      debug = debug # Auto reload app when Python code changes on disk, stack traces on error pages
    )
    if quick2web_resources:
      self.static_files('/quick2web/', quick2web_resources)

  def static_files(self, path, directory_on_disk, default_filename='index.html'):
    self.handlers.append((path + '(.*)', StaticFileHandler, dict(path=directory_on_disk, default_filename=default_filename)))

  def websocket(self, path, handler):
    self.handlers.append((path, TornadoWebSocketAdapter, dict(handler=handler)))

  def run(self, **kwargs):
    self.application = Application(self.handlers, **self.settings)
    self.application.listen(self.port)
    self.ioloop.start()


class TornadoWebSocketAdapter(websocket.WebSocketHandler):

  def __init__(self, application, request, handler, **kwargs):
    websocket.WebSocketHandler.__init__(self, application, request, **kwargs)
    self.handler = handler
    self.connection = TornadoWebSocketConnection(self)

  def open(self):
    self.handler.on_open(self.connection)

  def on_message(self, message):
    self.handler.on_message(self.connection, str(message))

  def on_close(self):
    self.handler.on_close(self.connection)

  def select_subprotocol(self, subprotocols):
    # Workaround an issue in some versions of WebKit.
    return subprotocols[0] if len(subprotocols) else None

  def allow_draft76(self):
    # Support older WebSocket protocol versions.
    return True

class TornadoWebSocketConnection(webserver.WebSocketConnection):

  def __init__(self, tornado_handler):
    self.tornado_handler = tornado_handler

  def send(self, message):
    self.tornado_handler.write_message(str(message))

  def close(self):
    self.close()

  def __str__(self):
    return 'WebSocketConnection' # TODO: id, url, remote source, open time

