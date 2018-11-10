

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
        // if marker exists, hide it
        if (marker && marker.setMap) {
            marker.setMap(null);
        }

        marker = new google.maps.Marker({
            position: latLng,
            map: map,
        });
        var data = {
            'lat' : e.latLng.lat(),
            'lng' : e.latLng.lng(),
        };
        fire_ajax_request(data)
    });

}
// Handle form
$("#mainForm").submit(function( event ) {

    var formData = {
        'lat' : $('#latValue').val(),
        'lng' : $('#lngValue').val(),
    };

    fire_ajax_request(formData);
    // stop the form from submitting the normal way and refreshing the page
    event.preventDefault();
});


function fire_ajax_request(coor_object){
    // process the form
    $.ajax({
        type        : 'GET', // define the type of HTTP verb we want to use (POST for our form)
        url         : '/data', // the url where we want to POST
        data        : coor_object, // our data object
        dataType    : 'json', // what type of data do we expect back from the server
        encode          : true,
        statusCode: {
            200: function (response) {
                $('.result').html("<h3>" + response.result + "</h3>")
            },
            403: function (response) {
                $('.result').html("<h3> Oopsy! out of coverage area :(</h3>")
            },
            500: function (response) {
                $('.result').html("<h3> Missing or incorrect values</h3>")
            }
        }
    });
}