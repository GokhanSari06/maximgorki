// photos source: http://blog.repponen.com/blog/2014/7/28/moscow

$(document).ready(function() {
  $('.container--gallery').magnificPopup({
    delegate: 'a',
    type: 'image',
    mainClass: 'mfp-with-zoom mfp-img-mobile',
    image: {
      verticalFit: true,
    },
    gallery: {
      enabled: true
    },
    zoom: {
      enabled: true,
      duration: 230,
      opener: function(element) {
        return element.find('img');
      }
    }
  });
});