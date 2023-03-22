from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from flask_restful import Resource, Api
import json

Weapon  = {
        "Axe" :{
            "name" : "Axe",
            "locations" : "no" 
        },        
        "Fire Wand" :{
            "name" : "Fire Wand",
            "locations" : "no"
        },
        "Cross" :{
            "name" : "Cross",
            "locations" : "no" 
        },
        "King Bible" :{
            "name" : "Cross",
            "locations" : "no" 
        },
        "Knife" :{
            "name" : "Knife",
            "locations" : "no" 
        },
        "Magic Wand" :{
            "name" : "Magic Wand",
            "locations" : "no" 
        },
        "Garlic" :{
            "name" : "Garlic",
            "locations" : "no" 
        },
        "Santa Water" :{
            "name" : "Santa Water",
            "locations" : "no" 
        },
        "Peachone" :{
            "name" : "Peachone",
            "locations" : "no" 
        },
        "Ebony Wings" :{
            "name" : "Ebony Wings",
            "locations" : "no" 
        },
        "Lightning Ring" :{
            "name" : "Lightning Ring",
            "locations" : ["Tiny Bridge"]
        },
        "Song of Mana" :{
            "name" : "Song of Mana",
            "locations" : "no" 
        },
        "Pentagram" :{
            "name" : "Pentagram",
            "locations" : "no" 
        },
        "Phiera Der Tuphello" :{
            "name" : "Phiera Der Tuphello",
            "locations" : "no" 
        },
        "Eight The Sparrow" :{
            "name" : "Eight The Sparrow",
            "locations" : "no" 
        },
        "Runetracer" :{
            "name" : "Runetracer",
            "locations" : "no" 
        },
        "Gatti Amari" :{
            "name" : "Gatti Amari",
            "locations" : "no" 
        },
        "Shadow Pinion" :{
            "name" : "Shadow Pinion",
            "locations" : "no" 
        },
        "Laurel" :{
            "name" : "Laurel",
            "locations" : "no" 
        },
        "Clock Lancet" :{
            "name" : "Clock Lancet",
            "locations" : "no" 
        },
        "Vento Sacro" :{
            "name" : "Vento Sacro",
            "locations" : ["Tiny Bridge"]
        },
        "Bracelet" :{
            "name" : "Bracelet",
            "locations" : "no" 
        },
        "Victory Sword" :{
            "name" : "Victory Sword",
            "locations" : "no" 
        },
        "Flames of Mispell" : {
            "name" : "Flames of Mispell",
            "locations" : "no" 
        },
        "Silver Wind" :{
            "name" : "Silver Wind",
            "locations" : "no" 
        },
        "Four Seasons" :{
            "name" : "Four Seasons",
            "locations" : "no" 
        },
        "Summon Night" :{
            "name" : "Summon Night",
            "locations" : "no" 
        },
        "Mirage Robe" :{
            "name" : "Mirage Robe",
            "locations" : "no" 
        },
        "Mille Bolle Bleu" :{
            "name" : "Mille Bolle Bleu",
            "locations" : "no" 
        },
        "Night Sword" :{
            "name" : "Night Sword",
            "locations" : "no" 
        }
},

Item = {
        "Candelabrador":{
            "name" : "Candelabrador",
            "locations" : ["Dairy Plant"]
        },
        "Spinach":{
            "name" : "Spinach",
            "locations" : ["Mad Forest"]
        },
        "Clover":{
            "name" : "Clover",
            "locations" : ["Mad Forest"]
        },
        "Spellbinder":{
            "name" : "Spellbinder",
            "locations" : ["Gallo Tower"]
        },
        "Bracer":{
            "name" : "Bracer",
            "locations" : ["Gallo Tower"]
        },
        "Empty Tome":{
            "name" : "Empty Tome",
            "locations" : ["Inlaid Library"]
        },
        "Hollow Heart":{
            "name" : "Hollow Heart",
            "locations" : ["Mad Forest"]
        },
        "Pummarola":{
            "name" : "Pummarola",
            "locations" : ["Mad Forest"]
        },
        "Attract Orb":{
            "name" : "Attract Orb",
            "locations" : ["Dairy Plant", "Tiny Bridge"]
        },
        "Duplicator":{
            "name" : "Duplicator",
            "locations" : ["Capella Magna"]
        },
        "Skull O'Maniac":{
            "name" : "Skull O'Maniac",
            "locations" : ["Mad Forest"]
        },
        "Crown":{
            "name" : "Crown",
            "locations" : ["Capella Magna"]
        },
        "Tiragisu":{
            "name" : "Tiragisu",
            "locations" : ["Capella Magna"]
        },
        "Armor":{
            "name" : "Armor",
            "locations" : ["Dairy Plant"]
        },
        "Stone Mask":{
            "name" : "Stone Mask",
            "locations" : ["Inlaid Library"]
        },
        "Wings":{
            "name" : "Wings",
            "locations" : ["Dairy Plant", "Tiny Bridge"]
        },
        "Metaglio Left":{
            "name" : "Metaglio Left",
            "locations" : ["Mad Forest", "Inlaid Library", "Dairy Plant",  "Gallo Tower", "Capella Magna", "Moongolow", "Boss Rash"]
        },
        
        "Metaglio Right":{
            "name" : "Metaglio Right",
            "locations" : ["Mad Forest", "Inlaid Library", "Dairy Plant",  "Gallo Tower", "Capella Magna", "Moongolow", "Boss Rash"]
        },
        "Gold Ring":{
            "name" : "Gold Ring",
            "locations" : ["Mad Forest", "Inlaid Library", "Dairy Plant",  "Gallo Tower", "Capella Magna", "Moongolow", "Boss Rash"]
        },
        "Silver Ring": {
            "name" : "Silver Ring",
            "locations" : ["Mad Forest", "Inlaid Library", "Dairy Plant",  "Gallo Tower", "Capella Magna", "Moongolow", "Boss Rash"]
        },

        "Torrona's Box":{
            "name" : "Torrona's Box",
            "locations" : "no"
        }
    },

Union = {
        "Tri-Bracelet":{
            "name":"Tri-Bracelet",
            "weapon" : ["Bi-Bracelet"],
            "item" : []
        },
        "Bi-Bracelet":{
            "name":"Bi-Bracelet",
            "weapon" : ["Bracelet"],
            "item" : []
        },
        "Vanderlier":{
            "name":"Vanderlier",
            "weapon" : ["Ebony Wings", "Peachone"],
            "item" : []
        },
        "Fuwalafuwaloo":{
            "name":"Fuwalafuwaloo",
            "weapon" : ["Vento Sacro", "Bloody Tear"],
            "item" : []
        }

    },

Evolve ={
        "Death Spiral":{
            "name":"Death Spiral",
            "weapon" : ["Axe"],
            "item" : ["Candelabrador"]
        },
        "Heaven Sword":{
            "name":"Heaven Sword",
            "weapon" : ["Cross"],
            "item" : ["Clover"]
        },

        "Hellfire":{
            "name":"Hellfire",
            "weapon" : ["Fire Wand"],
            "item" : ["Spinach"]
        },
        
        "Unholy Vespers":{
            "name":"Unholy Vespers",
            "weapon" : ["King Bible"],
            "item" : ["Spellbinder"]
        },

        "Thousand Edge":{
            "name":"Thousand Edges",
            "weapon" : ["Knife"],
            "item" : ["Bracer"]
        },
        "Holy Wand":{
            "name": "Holy Wand",
            "weapon" : ["Magic wand"],
            "item" : ["Empty Tome"]
        },
        "Bloody Tear":{
            "name":"Bloody Tear",
            "weapon" : ["Whip"],
            "item" : ["Hollow Heart"]
        },
        "Soul Eater":{
            "name":"Soul Eater",
            "weapon" : ["Garlic"],
            "item" : ["Pummarola"]
        },
        "La Borra":{
            "name":"La Borra",
            "weapon" : ["Santa Water"],
            "item" : ["Attract Orb"]
        },
        
        "Thunder Loop":{
            "name":"Thunder Loop",
            "weapon" : ["Lightning Ring"],
            "item" : ["Duplicator"]
        },
        "Mannajja":{
            "name":"MAnnajja",
            "weapon" : ["Song of Mana"],
            "item" : ["Skull O'Maniac"]
        },
        "Gorgeous Moon":{
            "name":"Gorgeous Moon",
            "weapon" : ["Pentagram"],
            "item" : ["Crown"]
        },
        "Phieraggi":{
            "name":"Phieraggi",
            "weapon" : ["Eight The Sparrow" , "Phierra Der Tuphello"],
            "item" : ["Tiragisu"]
        },
        "No Future":{
            "name":"No Future",
            "weapon" : ["Runetracer"],
            "item" : ["Armor"]
        },
        "Vicious Hunger":{
            "name":"Vicious Hunger",
            "weapon" : ["Gatti Amari"],
            "item" : ["Stone Mask"]
        },
        "Valkyrie Turner":{
            "name":"Valkyrie Turner",
            "weapon" : ["Shadow Pinion"],
            "item" : ["Wings"]
        },
        "Crimson Shroud":{
            "name":"Crimson Shroud",
            "weapon" : ["Laurel"],
            "item" : ["Metaglio Left", "Metaglio Right"]
        },
        "Infinite Corridor":{
            "name":"Infinite Corridor",
            "weapon" : ["Clock Lancet"],
            "item" : ["Silver Ring", "Gold Ring"]
        },

        "Sole Solution":{
            "name":"Sole Solution",
            "weapon" : ["Victory Sword"],
            "item" : ["Torrona's Box"]
        },
        "Ashes of Muspell":{
            "name":"Ashes of Muspell",
            "weapon" : ["Flames of Mispell"],
            "item" : ["Torrona's Box"]
        },
        "Festive Winds":{
            "name":"Festive Winds",
            "weapon" : ["Silver Wind"],
            "item" : ["Pummarola"]
        },
        "Godai Shuffle":{
            "name":"Godai Shuffle",
            "weapon" : ["Four Seasons"],
            "item" : ["Spinach", "Candelabrador"]
        },
        "Echo Night":{
            "name":"Echo Night",
            "weapon" : ["Summon Night"],
            "item" : ["Duplicator"]
        },
        "J`Odore":{
            "name":"J'Odore",
            "weapon" : ["Mirage Robe"],
            "item" : ["Attractorb"]
        },
        "Boo Boo Boolle":{
            "name":"Boo Boo Boolle",
            "weapon" : ["Mille Bolle Blu"],
            "item" : ["Spellbinder"]
        },
        "Muramasa":{
            "name":"Muramasa",
            "weapon" : ["Night Sword"],
            "item" : ["Stone Mask"]
        }
    }
app = Flask(__name__)
api = Api(app)
class VampWeapon(Resource):
    def get(self):
        return Weapon

class VampItem(Resource):
    def get(self):
        return Item

class VampEvolve(Resource):
    def get(self):
        return Evolve

class VampUnion(Resource):
    def get(self):
        return Union

api.add_resource(VampWeapon, '/vampweapon')
api.add_resource(VampItem, '/vampitem')
api.add_resource(VampEvolve, '/vampevolve')
api.add_resource(VampUnion, '/vampunion')

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db, )
login = LoginManager(app)
login.login_view = 'login'

if __name__ == '__main__':
    app.run(debug=True)


from app import routes, models

