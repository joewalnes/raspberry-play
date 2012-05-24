#!/usr/bin/env python

from webserver import *

class SharedValueHandler(WebSocketHandler):

  def __init__(self, value=None):
    self.value = value
    self.connections = set()

  def on_open(self, connection):
    connection.send(self.value)
    self.connections.add(connection)

  def on_close(self, connection):
    self.connections.remove(connection)

  def on_message(self, connection, message):
    print 'New value: %s' % message
    self.value = message
    for other_connection in self.connections:
      other_connection.send(message)

def main():
  webserver = TornadoWebServer(port=8888, debug=True)
  webserver.static_files('/static/', './static')
  webserver.websocket('/slider-value', SharedValueHandler(0))
  print 'Listening on %s' % webserver.url
  webserver.run()

if __name__ == '__main__':
  main()

