from tilmine.config import Config
import requests
from itertools import chain

SERVER = Config.config['server']
PORTS = Config.config['ports']


def tag_search(form_search):
    query = form_search.data['search']
    tags = _process_tags(query)

    results = []
    for tag in tags:
        tils = requests.post("http://{0}:{1}/til/search/tags".format(SERVER, PORTS['api']),
                             json={"tags": "{0}".format(tag)},
                             headers={'content-type': 'application/json'}).json()
        results.append(tils)

    return list(chain(*results))


def _process_tags(query):
    tags = query.split(',')
    return [tag for tag in tags]
