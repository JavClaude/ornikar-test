from dataclasses import dataclass


@dataclass
class EntrainerUnModeleCommand:
    taille_du_test: float
    temps_maximum_pour_entrainer_le_modele: int
