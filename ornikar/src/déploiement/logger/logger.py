import logging

from rich.logging import RichHandler


class LoggerFactory:
    @staticmethod
    def construire_le_logger() -> logging.Logger:
        handler = RichHandler(level=logging.INFO, markup=True)
        formateur_de_log = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formateur_de_log)
        logger = logging.getLogger("Ornikar logger - déploiement")
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        return logger
