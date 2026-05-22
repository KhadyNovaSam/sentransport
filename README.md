# 🚍 SenTransport

Application web pour la gestion et la visualisation des lignes de bus à Dakar.  
Ce projet combine **React** (front‑end) et **Flask** (back‑end API) pour offrir une interface interactive permettant de consulter les lignes, les arrêts et de calculer l’arrêt le plus proche de l’utilisateur.

---

## 📌 Fonctionnalités
- Affichage des lignes de bus disponibles (`/lignes`).
- Consultation des détails d’une ligne spécifique (`/lignes/<id>`).
- Liste des arrêts avec coordonnées GPS (`/arrets`).
- Calcul et affichage de l’arrêt le plus proche de la position de l’utilisateur (`/arrets/proche/<lat>/<lon>`).
- Carte interactive avec :
  - Marqueurs pour les arrêts de bus.
  - Cercle ou icône distincte pour la position de l’utilisateur.
  - Mise en évidence de l’arrêt le plus proche.

---

## 🛠️ Technologies utilisées
- **Front‑end** : React, React‑Leaflet, CSS.
- **Back‑end** : Flask, Flask‑CORS.
- **Données** : JSON (`lignes_ddd.json`, `arrets.json`).
- **API externe** : OpenStreetMap (tiles pour la carte).

---

## ⚙️ Installation et lancement

### 1. Cloner le projet
```bash
git clone https://github.com/ton-compte/SenTransport.git
cd SenTransport
