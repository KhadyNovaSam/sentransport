// src/StatReseau.js
import './StatReseau.css';

function StatReseau({ lignes }) {
  const totalArrets = lignes.reduce((sum, l) => sum + l.arrets, 0);
  const maxLigne = lignes.reduce((max, l) => l.arrets > max.arrets ? l : max, lignes[0]);

  return (
    <div className="stat-reseau">
      <div className="stat">{lignes.length} lignes</div>
      <div className="stat">{totalArrets} arrêts au total</div>
      <div className="stat">Ligne {maxLigne.numero} : la plus longue ({maxLigne.arrets} arrêts)</div>
    </div>
  );
}

export default StatReseau;