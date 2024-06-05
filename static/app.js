const popularPlacesIds = ['2', '6', '10'];  // contains the ids of the popular places to highlight


document.addEventListener('DOMContentLoaded', () => {  // event listener waits for the DOM to fully load before executing the callback function
    fetch('/api/places')                               // makes a get request to endpoint to retrieve a list of places
        .then(response => response.json())             // converts to json
        .then(data => {
            const popularPlaces = data.filter(place => popularPlacesIds.includes(place.id.toString()));   // filters retrieved places to get popular place IDs

            updatePopularPlaces(popularPlaces);   // calls updatePopularPlaces function below with the filtered popular places
        })
        .catch(error => console.error('Error fetching places:', error));
});

// updates DOM with the popular places
function updatePopularPlaces(popularPlaces) {
    const popularPlacesDiv = document.getElementById('popular-places');      // selects the HTML element where the popular places will be displayed

    popularPlacesDiv.innerHTML = '';                                         // clears any existing content in the popular places container

    popularPlaces.forEach(place => {                                         // iterates thru all popular places
        const placeElement = document.createElement('div');                  // creates a new div element for each place
        placeElement.className = 'col-md-4';
        placeElement.innerHTML = `
            <div class="card" style="width: 25rem;">
                <a href="/view/${place.id}">
                    <img src="${place.image}" class="card-img-top" alt="${place.hotel}">
                </a>
                <div class="card-body">
                    <h5 class="card-title">${place.hotel}</h5>
                    <p class="card-text">${place.location}</p>
                    <p class="card-text">${place.description}</p>
                    <a href="/view/${place.id}" class="btn btn-view">View Place</a>
                </div>
            </div>
        `;
        popularPlacesDiv.appendChild(placeElement);                          // appends the new div element to the popular places container
    });
}

// validates the input fields and sends a POST request to add a new place
function add_place(new_place) {
    //  extract values from the new_place object
    let hotel = new_place["hotel"]
    let location = new_place["location"]
    let description = new_place["description"]
    let avg_nightly = new_place["avg_nightly"]
    let amenities = new_place["amenities"]
    let nearby_attractions = new_place["nearby_attractions"]
    let transportation = new_place["transportation"]
    let avg_rating = new_place["avg_rating"]
    let reviews = new_place["reviews"]
    let image = new_place["image"]
    $(".warning").remove();

    // validates all input fields + displays warning messages if any fields are empty/invalid
    let valid = true;
    if (!hotel) {
        $("<span class='warning text-danger'>Enter hotel name.</span>").insertAfter("#hotel");
        $("#hotel").focus();
        valid = false;
    }
    else if (!location) {
        $("<span class='warning text-danger'>Enter location of destination.</span>").insertAfter("#location");
        $("#location").focus();
        valid = false;
    }
    else if (!description) {
        $("<span class='warning text-danger'>Enter description of destination.</span>").insertAfter("#description");
        $("#description").focus();
        valid = false;
    }
    else if (!avg_nightly) {
        $("<span class='warning text-danger'>Enter average nightly amount.</span>").insertAfter("#avg_nightly");
        $("#avg_nightly").focus();
        valid = false;
    }
    else if (!amenities) {
        $("<span class='warning text-danger'>Enter hotel amenities.</span>").insertAfter("#amenities");
        $("#amenities").focus();
        valid = false;
    }
    else if (!nearby_attractions) {
        $("<span class='warning text-danger'>Enter nearby attractions.</span>").insertAfter("#nearby_attractions");
        $("#nearby_attractions").focus();
        valid = false;
    }
    else if (!transportation) {
        $("<span class='warning text-danger'>Enter transportation in area.</span>").insertAfter("#transportation");
        $("#transportation").focus();
        valid = false;
    }
    else if (!avg_rating) {
        $("<span class='warning text-danger'>Enter average hotel rating.</span>").insertAfter("#avg_rating");
        $("#avg_rating").focus();
        valid = false;
    }
    else if (!reviews) {
        $("<span class='warning text-danger'>Enter average reviews rating from 1-5.</span>").insertAfter("#reviews");
        $("#reviews").focus();
        valid = false;
    }
    else if (!image) {
        $("<span class='warning text-danger'>Enter image url.</span>").insertAfter("#image");
        $("#image").focus();
        valid = false;
    }
    else if (!$.isNumeric(avg_nightly)) {
        $("<span class='warning text-danger'>Average nightly must be a number.</span>").insertAfter("#avg_nightly");
        $("#avg_nightly").focus();
        valid = false;
    }
    else if (!$.isNumeric(avg_rating)) {
        $("<span class='warning text-danger'>Average rating must be a number.</span>").insertAfter("#avg_rating");
        $("#avg_rating").focus();
        valid = false;
    }
    else if (!$.isNumeric(reviews)) {
        $("<span class='warning text-danger'>Average rating must be a number.</span>").insertAfter("#reviews");
        $("#reviews").focus();
        valid = false;
    }

    // if all fields are valid, it constructs the data_to_save object with the new place's details
    if (valid) {
        let data_to_save = {
            "hotel": hotel, "location": location, "description": description, "avg_nightly": avg_nightly, "amenities": amenities, "nearby_attractions": nearby_attractions, "transportation": transportation,
            "avg_rating": avg_rating, "reviews": reviews, "image": image
        }
        $.ajax({                             // sends ajax post request to the '/add' endpoint with the new place data
            type: "POST",
            url: "/add",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(data_to_save),
            success: function (result) {
                $("#successMessage").empty();
                $("#successMessage").append(`<span>New place successfully created!</span> <a href='/view/${result.id}'>See it here.</a>`);
                $('#successMessage').show();
                $('#addPlaceForm').trigger("reset");
                $('#hotel').focus();
            },
            error: function (error) {
                console.log("Error saving place:", error);
            }
        });

    }
}
