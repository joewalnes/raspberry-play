class WebServer(object):

  def static_files(self, path, directory_on_disk, default_filename='index.html'):
    pass

  def websocket(self, path, handler):
    pass

  def run(self):
    pass


class WebSocketHandler(object):

  def on_open(self, connection):
    pass

  def on_close(self, connection):
    pass

  def on_message(self, connection, message):
    pass


class WebSocketConnection(object):

  def send(self, message):
    pass

  def close(self):
    pass
