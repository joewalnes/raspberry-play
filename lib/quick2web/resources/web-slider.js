  $(function() {
    $('input[data-type="range"]').each(function(i, el) {
      var sliderControl = $(el);
      var sharedPath = sliderControl.data('shared');
      if (sharedPath) {
        var sliderValue = new SharedValue('/slider-value')
          .open(function() {
            sliderControl.slider('enable'); 
          })
          .close(function() {
            sliderControl.slider('disable');
          })
          .change(function(event, value) {
            sliderControl.val(value).slider('refresh')
          });

        sliderControl.change(function(event, element) {
          sliderValue.set(sliderControl.val());
        });
      }
    });
  });

