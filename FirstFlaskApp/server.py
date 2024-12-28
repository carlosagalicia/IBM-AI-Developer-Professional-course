from flask import Flask, jsonify, request
import requests
from urllib.parse import quote
app = Flask("My first Application")

data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]


@app.route('/')
def home():
    course = request.args.get("course")
    rating = request.args.get("rating")
    if course and rating:
        return {"message": f"{course} with rating {rating}"}
    else:
        return "Hello World"
        # return "<b> My first Flask application in action! <b>"
        # return {"message" : "Hello World"}
        # return jsonify(message="Hello World")


@app.route('/health', methods=["GET", "POST"])
def health():
    if request.method == "GET":
        return jsonify(dict(status="OK", method="GET")), 200
    elif request.method == "POST":
        return jsonify(dict(status="OK", method="POST")), 200


@app.route('/author')
def get_author():
    res = requests.get("https://openlibrary.org/search/authors.json?q=Michael Crichton")
    if res.status_code == 200:
        return {"message": res.json()}
    elif res.status_code == 404:
        return {"message": "Something went wrong"}, 404
    else:
        return {"message": "Server error"}, 500


@app.route("/book/<isbn>")
def get_book(isbn):
    escaped_isbn = quote(isbn)
    res = requests.get(f"https://openlibrary.org/isbn/{escaped_isbn}.json")
    if res.status_code == 200:
        return {"message": res.json()}
    elif res.status_code == 404:
        return {"message": "Book not found"}, 404
    else:
        return {"message": "Server error"}, 500


@app.route("/network/<uuid:uuid>")
def uuid(uuid):
    res = requests.get("https://anotherapi/getnetwork/{uuid}.json")
    if res.status_code == 200:
        return {"message": res.json()}
    elif res.status_code == 404:
        return {"message": "Something went wrong"}, 404
    else:
        return {"message": "Server error"}, 500


@app.route("/data")
def get_data():
    try:
        if data and len(data) > 0:
            return {"message": f"Data of length {len(data)} found"}
        else:
            return {"message": "Data is empty"}, 500
    except NameError:
        return {"message": "Data not found"}, 404


@app.route("/name_search")
def search():
    res = request.args.get("q")
    if res:
        for person in data:
            if person["first_name"] == res:
                return person, 200
        return {"message": "person not found"}, 404
    elif not res:
        return {"message": "Invalid input parameter"}, 422


@app.route("/count")
def count():
    try:
        return {"data count": len(data)}, 200
    except:
        return {"message": "data not defined"}, 500


@app.route("/person/<uuid:uuid>")
def find_by_uuid(uuid):
    for person in data:
        if person["id"] == str(uuid):
            return person, 200
    return {"message": "person not found"}, 404


@app.route("/person/<uuid:uuid>", methods=["DELETE"])
def delete_by_uuid(uuid):
    for person in data:
        print(type(person["id"]))
        if person["id"] == str(uuid):
            data.remove(person)
            return {"message": "Person with ID deleted"}, 200
    return {"message": "person not found"}, 404


@app.route("/person", methods=["POST"])
def create_person():
    new_person = request.get_json()
    if new_person:
        return {"message": "Person created successfully"}, 201
    else:
        return {"message": "Invalid input, no data provided"}, 400


@app.errorhandler(404)
def api_not_found(error):
    return {"message": "API not found"}, 404
