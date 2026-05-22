import json
import math
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Charger les données des lignes
with open("lignes_ddd.json", "r", encoding="utf-8") as f:
    lignes = json.load(f)

# Charger les données des arrêts
with open("arrets.json", "r", encoding="utf-8") as f:
    arrets = json.load(f)

# --- ROUTES ---

@app.route("/")
def accueil():
    return jsonify({
        "message": "Bienvenue sur l'API SenTransport !",
        "endpoints": ["/lignes", "/lignes/<id>", "/arrets", "/arrets/proche/<lat>/<lon>"]
    })

@app.route("/lignes")
def get_lignes():
    return jsonify(lignes)

@app.route("/lignes/<int:ligne_id>")
def get_ligne(ligne_id):
    ligne = next((l for l in lignes if l["id"] == ligne_id), None)
    if ligne is None:
        return jsonify({"erreur": "Ligne non trouvée"}), 404
    return jsonify(ligne)

@app.route("/arrets")
def get_arrets():
    return jsonify(arrets)

# Fonction Haversine pour calculer la distance en km
def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  # rayon de la Terre en km
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

@app.route("/arrets/proche/<float:lat>/<float:lon>")
def get_arret_proche(lat, lon):
    if not arrets:
        return jsonify({"erreur": "Aucun arrêt disponible"}), 404
    
    arret_proche = min(
        arrets,
        key=lambda a: haversine(lat, lon, a["lat"], a["lon"])
    )
    
    return jsonify({
        "message": f"Arrêt le plus proche : {arret_proche['nom']}",
        "details": arret_proche
    })

# --- MAIN ---
if __name__ == "__main__":
    app.run(debug=True, port=5000)
