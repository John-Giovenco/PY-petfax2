from flask import ( Blueprint, render_template )
import json

bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route("/")
def index():
    pets = json.load(open('pets.json'))
    return render_template("index.html", pets=pets)

@bp.route('/')
def pet_details(pet_id): 
    pets = json.load(open("pets.json"))
    for pet in pets:
        if pet["pet_id"] == pet_id:
            return render_template('pet_facts.html', pet=pet)
    return "Can't find that pet"
