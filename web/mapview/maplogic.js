(function(exports) {
    "use strict";

    function initMap() {
        exports.map = new google.maps.Map(document.getElementById("map"), {
            center: {
                lat: -34.397,
                lng: 150.644
            },
            zoom: 8
      });
    }

    exports.initMap = initMap;
})((this.window = this.window || {}));

var locations = [
    ['High Park', 43.6465, -79.4637, "/web/locations/highpark.html"],
    ['Cherry Beach', 43.6370, -79.3441, "/web/locations/cherrybeach.html"],
    ['Harbourfront Park', 43.2716, -79.8724, "/web/locations/harbourfront.html"],
    ['Sunnybrook Park', 43.7243, -79.3580, "/web/locations/sunnybrook.html"],
    ['Dufferin Grove Park', 43.6566, -79.4328, "/web/locations/dufferin.html"],
    ['Ashbridges Bay', 43.6618, -79.3117, "/web/locations/ashbridgesbay.html"]
    
];

var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 10,
    center: new google.maps.LatLng(43.6532, -79.3832),
    mapTypeId: google.maps.MapTypeId.ROADMAP
});

var infowindow = new google.maps.InfoWindow();

var marker, i;

for (i = 0; i < locations.length; i++) { 
    marker = new google.maps.Marker({
        position: new google.maps.LatLng(locations[i][1], locations[i][2]),
        map: map,
        url: locations[i][3]
    });

    google.maps.event.addListener(marker, 'click', (function(marker, i) {
        return function() {
            infowindow.setContent(locations[i][0]);
            infowindow.open(map, marker);
            window.location.href = this.url;
        }
    })(marker, i));
}