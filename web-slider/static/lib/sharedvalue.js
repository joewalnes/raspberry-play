function SharedValue(path) {
  this.value = undefined;
  this.updating = false;
  var ws = new ReconnectingWebSocket('ws://' + document.location.host + path);
  ws.onopen = $.proxy(function() {
    $(this).trigger('open', this.value);
  }, this);
  ws.onclose = $.proxy(function() {
    $(this).trigger('close', this.value);
  }, this);
  ws.onmessage = $.proxy(function(ev) {
    this.value = JSON.parse(ev.data);
    this.updating = true;
    try {
      $(this).trigger('change', this.value);
    } finally {
      this.updating = false;
    }
  }, this);
  this.websocket = ws;
}

SharedValue.prototype.set = function(value) {
  var oldValue = this.value;
  this.value = value;
  if (!this.updating && value != oldValue) { // Prevent re-entrance loops
    this.websocket.send(JSON.stringify(value));
  }
  return this;
};

SharedValue.prototype.get = function() {
  return this.value;
};

// Convenience jQuery style event handlers

SharedValue.prototype.open = function(handler) {
  $(this).on('open', handler);
  return this;
};

SharedValue.prototype.close = function(handler) {
  $(this).on('close', handler);
  return this;
};

SharedValue.prototype.change = function(handler) {
  $(this).on('change', handler);
  return this;
};
