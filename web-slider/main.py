#!/usr/bin/env python

from quick2web import WebServer, SharedValue

def main():
  webserver = WebServer(port=8888, debug=True)
  webserver.static_files('/static/', 'static')
  webserver.websocket('/slider-value', SharedValue(0, on_change=slider_updated))
  print 'Listening on %s' % webserver.url
  webserver.run()

def slider_updated(value, connection):
  # TODO: Communicate with LED bar graph
  print 'Slider value: ', value

if __name__ == '__main__':
  main()

