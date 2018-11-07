function initMap() {
    // The location of Paris
    var location = {lat: 48.852767, lng: 2.348584};
    // The map, centered at Paris
    var map = new google.maps.Map(
        document.getElementById('map'), {zoom: 12, center: location});
    // The marker, positioned at Paris
    var marker = new google.maps.Marker({position: location, map: map});

    google.maps.event.addListener(map, 'click', function(e) {
        latLng = e.latLng;
        // if marker exists and has a .setMap method, hide it
        if (marker && marker.setMap) {
            marker.setMap(null);
        }
        marker = new google.maps.Marker({
            position: latLng,
            map: map,
        });

        fire_api(e.latLng.lat(), e.latLng.lng())
    });

}

function fire_api(lat, lng){
    var endpoint = "/data";
    $.getJSON( endpoint, { lat: lat, lon: lng } )
        .done(function( json ) {
            $('.result').html("<h3>" + json.result + "</h3>")
        })
        .fail(function( jqxhr, textStatus, error ) {
             $('.result').html("<h3> Oopsy! out of coverage area :(</h3>")
    });
}