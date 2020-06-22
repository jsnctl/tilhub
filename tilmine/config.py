import yaml
from pathlib import Path

TILMINE_ROOT = str(Path(__file__).parent)
print(TILMINE_ROOT)


def _init_config():
    config = yaml.load(open(TILMINE_ROOT + "/config.yaml", "rb"),
                       Loader=yaml.FullLoader)
    return config


class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls.config = _init_config()
        return cls._instance


config = Config()
