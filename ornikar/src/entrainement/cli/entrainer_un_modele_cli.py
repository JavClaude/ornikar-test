import argparse

from ornikar.src.entrainement.usecases.entrainer_un_modele_command import (
    EntrainerUnModeleCommand,
)
from ornikar.src.entrainement.usecases.entrainer_un_modele_command_handler import (
    EntrainerUnModeleCommandHandler,
)


def main() -> None:
    argument_parser = argparse.ArgumentParser("Entrainer un modèle CLI")
    argument_parser.add_argument(
        "--test-size", dest="test_size", type=float, default=0.2
    )
    argument_parser.add_argument(
        "--temps-max-pour-entrainer-le-modele",
        dest="temps_max_pour_entrainer_le_modele",
        type=int,
        default=30,
        help="Temps (en secondes) maximum aloué au processus d'optimisation",
    )

    arguments = argument_parser.parse_args()

    commande = EntrainerUnModeleCommand(
        arguments.test_size, arguments.temps_max_pour_entrainer_le_modele
    )
    entrainer_un_modele_handler = EntrainerUnModeleCommandHandler()
    entrainer_un_modele_handler.executer_le_cas_d_usage(commande)
