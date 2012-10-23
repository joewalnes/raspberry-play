from quick2web import WebServer, SharedValue

def main():
  webserver = WebServer(port=8888, debug=True)

  webserver.websocket('/slider-value',
      SharedValue(20, on_change=slider_updated))

  webserver.static_files('/', './static')
  print('Listening on %s' % webserver.url)
  webserver.run()

def slider_updated(value, connection):
  # TODO: Communicate with LED bar graph
  print('Slider value: ', value)

if __name__ == '__main__':
  main()
