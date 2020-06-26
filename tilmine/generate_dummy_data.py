import requests
import numpy as np


users = ['jsnctl', 'topo', 'chappie', 'test_user', 'dhh']
tils = [
    {"til": "Docker for Mac default binds to no particular address 0.0.0.0, not to loopback 127.0.0.1",
     "tags": ["docker", "mac", "python"]},
    {"til": "PySpark might need spark.executorEnv.PYTHONHASHSEED set to a random int, as 3.3+/Spark 2+ doesnt seem to "
            "set this on the executors",
     "tags": ["spark", "python"]},
    {"til": "If in client mode then PySpark will need to have spark.driver.memory set in init vs. at runtime (e.g. "
            "spark-submit --driver-memory 10G)",
     "tags": ["spark", "python"]},
    {"til": "s3a filesystem support ships with Hadoop2.4 but 2.5+ require additional hadoop-aws dependency",
     "tags": ["aws", "hadoop"]},
    {"til": "For aws-cli on a Mac, dont even bother with the suggested pip-based install. brew install awscli works "
            "seamlesslyy",
     "tags": ["aws", "hadoop", "mac"]},
]

for _ in range(100):

    til = np.random.choice(tils, 1)[0]
    user = np.random.choice(users, 1)[0]

    response = requests.post("http://localhost:5000/til",
                  json={'user': user,
                        'til': til['til'],
                        'tags': til['tags']},
                  headers={'content-type': 'application/json'})

    print(response.text)

