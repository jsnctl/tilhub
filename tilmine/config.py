import yaml


def _init_config():
    config = yaml.load(open("./config.yaml", "rb"), Loader=yaml.FullLoader)
    return config


class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls.config = _init_config()
        return cls._instance


config = Config()
