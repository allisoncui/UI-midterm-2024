from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, redirect, url_for
app = Flask(__name__)

current_id = 11

places = [
    {
        "id": 1,
        "hotel": "Beachside Retreat - Puerto Viejo, Costa Rica",
        "location": "Puerto Viejo, Costa Rica",
        "description": "A tranquil, budget-friendly beachside hostel known for its vibrant community, located in the heart of Puerto Viejo. Offers easy access to beaches, local markets, and nature reserves.",
        "avg_nightly": 30,
        "amenities": ["shared kitchen", "free wifi", "bike rentals", "lounge", "events"],
        "nearby_attractions": ["Cocles Beach", "Jaguar Rescue Center", "Punta Uva Beach", "Viejo Boardwalk"],
        "transportation": ["bus", "bike", "walk"],
        "avg_rating": 9,
        "reviews": 320,
        "image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/17/b0/4e/dd/hotel-banana-azul.jpg?w=500&h=500&s=1"
    },
    {
        "id": 2,
        "hotel": "Urban Oasis - Barcelona, Spain",
        "location": "Barcelona, Spain",
        "description": "Experience the heart of Barcelona with this centrally located hotel. Perfect for those looking to explore the city's rich history and vibrant nightlife.",
        "avg_nightly": 50,
        "amenities": ["rooftop pool", "city views", "free wifi", "fitness center", "bar"],
        "nearby_attractions": ["Gothic Quarter", "Sagrada Familia", "Park Güell", "Casa Batlló"],
        "transportation": ["metro", "bus", "bike"],
        "avg_rating": 8,
        "reviews": 215,
        "image": "https://images.getaroom-cdn.com/image/upload/s--Keg6RYSw--/c_limit,e_improve,fl_lossy.immutable_cache,h_940,q_auto:good,w_940/v1693976242/47c8c08731d4f0dd348ec77a8ba03213bfbda72c?atc=bc5da95f"
    },
    {
        "id": 3,
        "hotel": "Mountain Lodge - Sapa, Vietnam",
        "location": "Sapa, Vietnam",
        "description": "Nestled in the mountains of Sapa, this affordable lodge offers breathtaking views and a serene atmosphere. Ideal for hikers and nature lovers.",
        "avg_nightly": 25,
        "amenities": ["mountain views", "free wifi", "guided tours", "free breakfast"],
        "nearby_attractions": ["Fansipan Mountain", "Muong Hoa Valley", "Sapa Market", "Ham Rong Mountain"],
        "transportation": ["taxi", "bus", "hike"],
        "avg_rating": 7,
        "reviews": 180,
        "image": "https://content.r9cdn.net/rimg/himg/aa/28/4b/expediav2-2883345-2042280932-922128.jpg?width=1200&height=630&crop=true"
    },
    {
        "id": 4,
        "hotel": "Desert Haven - Marrakech, Morocco",
        "location": "Marrakech, Morocco",
        "description": "A budget-friendly guesthouse offering an authentic Moroccan experience. Enjoy the tranquility of the desert and explore the rich culture of Marrakech.",
        "avg_nightly": 35,
        "amenities": ["rooftop terrace", "free wifi", "Moroccan cuisine", "pool"],
        "nearby_attractions": ["Jemaa el-Fnaa", "Majorelle Garden", "Bahia Palace", "Koutoubia Mosque"],
        "transportation": ["taxi", "bike", "walk"],
        "avg_rating": 9,
        "reviews": 250,
        "image": "https://www.thetimes.co.uk/imageserver/image/%2Fmethode%2Fsundaytimes%2Fprod%2Fweb%2Fbin%2F55e77e26-d3d7-11e9-8b97-d0945d0d0813.jpg?crop=2667%2C1500%2C0%2C0"
    },
    {
        "id": 5,
        "hotel": "City Hostel - Budapest, Hungary",
        "location": "Budapest, Hungary",
        "description": "Stay in the heart of Budapest without breaking the bank. This hostel is close to major attractions and offers comfortable, affordable accommodations.",
        "avg_nightly": 28,
        "amenities": ["free wifi", "communal kitchen", "laundry services", "lounge area"],
        "nearby_attractions": ["The Hungarian Parliament", "Chain Bridge", "Buda Castle", "Heroes' Square"],
        "transportation": ["tram", "metro", "bus"],
        "avg_rating": 6,
        "reviews": 305,
        "image": "https://thesavvybackpacker.com/wp-content/uploads/2018/03/best-hostels-budapest.jpg"
    },
    {
        "id": 6,
        "hotel": "Beach Cabanas - Goa, India",
        "location": "Goa, India",
        "description": "Experience the beach life in Goa with these affordable cabanas. Perfect for travelers looking to relax on the beach and enjoy the local culture.",
        "avg_nightly": 22,
        "amenities": ["beach access", "free wifi", "bike hire", "bar"],
        "nearby_attractions": ["Anjuna Beach", "Fort Aguada", "Chapora Fort", "Baga Beach"],
        "transportation": ["scooter", "taxi", "walk"],
        "avg_rating": 6,
        "reviews": 275,
        "image": "https://media2.thrillophilia.com/images/photos/000/118/079/original/1504360455_7_Rama_Resort_Agonda_Beach_Goa___Wooden_Huts.jpg?width=975&height=600"
    },
    {
        "id": 7,
        "hotel": "Rainforest Retreat - Cairns, Australia",
        "location": "Cairns, Australia",
        "description": "Surrounded by rainforest, this eco-friendly hostel offers an immersive nature experience. Great for adventure seekers and eco-tourists.",
        "avg_nightly": 33,
        "amenities": ["eco-tours", "free wifi", "communal kitchen", "pool"],
        "nearby_attractions": ["Great Barrier Reef", "Daintree Rainforest", "Cairns Esplanade", "Kuranda Village"],
        "transportation": ["bus", "car rental", "bike"],
        "avg_rating": 8,
        "reviews": 195,
        "image": "https://cf.bstatic.com/xdata/images/hotel/max1024x768/242052333.jpg?k=afad4e58ff911fe351c6bbcb61679d951499cf7038d9cd133bea5d35a00a98ef&o=&hp=1"
    },
    {
        "id": 8,
        "hotel": "Historic B&B - Krakow, Poland",
        "location": "Krakow, Poland",
        "description": "Stay in a historic Bed & Breakfast in the heart of Krakow. Affordable rates, cozy atmosphere, and close to major attractions.",
        "avg_nightly": 40,
        "amenities": ["free breakfast", "free wifi", "guided tours", "garden"],
        "nearby_attractions": ["Wawel Castle", "Main Market Square", "Schindler's Factory", "Kazimierz Jewish District"],
        "transportation": ["tram", "walk", "bike"],
        "avg_rating": 6,
        "reviews": 220,
        "image": "https://images.trvl-media.com/lodging/36000000/35290000/35281300/35281222/2dc4cc0d.jpg?impolicy=fcrop&w=1200&h=800&p=1&q=medium"
    },
    {
        "id": 9,
        "hotel": "Lakeside Inn - Pokhara, Nepal",
        "location": "Pokhara, Nepal",
        "description": "Enjoy stunning lake views and easy access to outdoor adventures at this budget-friendly inn in Pokhara. Ideal for travelers seeking tranquility and natural beauty.",
        "avg_nightly": 20,
        "amenities": ["lake views", "free wifi", "rooftop terrace", "travel assistance"],
        "nearby_attractions": ["Phewa Lake", "World Peace Pagoda", "Sarangkot", "International Mountain Museum"],
        "transportation": ["taxi", "bike", "walk"],
        "avg_rating": 7,
        "reviews": 160,
        "image": "https://cf.bstatic.com/xdata/images/hotel/max1024x768/367051007.jpg?k=23bc432458d2ed85b6101df7ba9e6f5d63a892ebb0bb738c811a39dde80da7b9&o=&hp=1"
    },
    {
        "id": 10,
        "hotel": "Seaside Hostel - Penang, Malaysia",
        "location": "Penang, Malaysia",
        "description": "A cozy and affordable hostel located steps from the beach in Penang. Offers a friendly atmosphere and easy access to local cuisine and culture.",
        "avg_nightly": 18,
        "amenities": ["beachfront", "free wifi", "communal kitchen", "lounge area"],
        "nearby_attractions": ["Georgetown", "Penang Hill", "Kek Lok Si Temple", "Batu Ferringhi Beach"],
        "transportation": ["bus", "bike", "walk"],
        "avg_rating": 9,
        "reviews": 200,
        "image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/18/0b/b3/d2/parkroyal-penang-resort.jpg?w=1200&h=-1&s=1"
    }
]


# ROUTES

@app.route('/')
def home():
    return render_template('home.html', places=places)


@app.route('/api/places')
def api_places():
    return jsonify(places)


@app.route('/view/<int:id>')
def place(id):
    place = next((place for place in places if place['id'] == id), None)
    if place is None:
        return "Place cannot be found", 404
    return render_template('place.html', place=place)


# AJAX FUNCTIONS


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').strip()
    if not query:
        return redirect(url_for('home'))

    def highlight(text, searchTerm):
        idx = text.lower().find(searchTerm.lower())
        if idx == -1:
            return text
        return text[:idx] + '<strong>' + text[idx:idx+len(searchTerm)] + '</strong>' + text[idx+len(searchTerm):]

    searched_places = []
    for place in places:
        if query.lower() in place['hotel'].lower() or query.lower() in place['description'].lower() or query.lower() in place['location'].lower():
            highlighted_place = place.copy()
            highlighted_place['hotel'] = highlight(place['hotel'], query)
            highlighted_place['description'] = highlight(place['description'], query)
            highlighted_place['location'] = highlight(place['location'], query)
            searched_places.append(highlighted_place)

    return render_template('results.html', query=query, places=searched_places)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        global current_id
        json_data = request.get_json()
        hotel = json_data["hotel"]
        location = json_data["location"]
        description = json_data["description"]
        avg_nightly = json_data["avg_nightly"]
        amenities = json_data["amenities"]
        nearby_attractions = json_data["nearby_attractions"]
        transportation = json_data["transportation"]
        avg_rating = json_data["avg_rating"]
        reviews = json_data["reviews"]
        image = json_data["image"]

        new_place_entry = {
            "id": current_id,
            "hotel": hotel,
            "location": location,
            "description": description,
            "avg_nightly": avg_nightly,
            "amenities": amenities,
            "nearby_attractions": nearby_attractions,
            "transportation": transportation,
            "avg_rating": avg_rating,
            "reviews": reviews,
            "image": image
        }
        current_id += 1
        places.append(new_place_entry)
        return jsonify({"id": new_place_entry["id"]}), 200
    else:
        return render_template('add_place.html')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    place = next((place for place in places if place['id'] == id), None)
    if not place:
        return "Place not found", 404

    if request.method == 'POST':
        # Process the submitted form and update the place
        json_data = request.get_json()
        place.update({
            "hotel": json_data.get("hotel", place['hotel']),
            "location": json_data.get("location", place['location']),
            "description": json_data.get("description", place['description']),
            "avg_nightly": json_data.get("avg_nightly", place['avg_nightly']),
            "amenities": json_data.get("amenities", place['amenities']),
            "nearby_attractions": json_data.get("nearby_attractions", place['nearby_attractions']),
            "transportation": json_data.get("transportation", place['transportation']),
            "avg_rating": json_data.get("avg_rating", place['avg_rating']),
            "reviews": json_data.get("reviews", place['reviews']),
            "image": json_data.get("image", place['image'])
        })
        return redirect(url_for('place', id=id))
    else:
        # Display the edit form with current values pre-populated
        return render_template('edit_place.html', place=place)


@app.route('/update/<int:id>', methods=['POST'])
def update_place(id):
    place = next((place for place in places if place['id'] == id), None)
    if not place:
        return "Place not found", 404

    # Update the place with the new data from the form
    place['hotel'] = request.form['hotel']
    place['location'] = request.form['location']
    place['description'] = request.form['description']
    place['avg_nightly'] = int(request.form['avg_nightly'])
    place['amenities'] = request.form['amenities'].split(',')
    place['nearby_attractions'] = request.form['nearby_attractions'].split(',')
    place['transportation'] = request.form['transportation'].split(',')
    place['avg_rating'] = float(request.form['avg_rating'])
    place['reviews'] = int(request.form['reviews'])
    place['image'] = request.form['image']

    return redirect(url_for('place', id=id))


if __name__ == '__main__':
    app.run(debug=True)
