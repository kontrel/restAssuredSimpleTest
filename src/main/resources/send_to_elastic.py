#!/usr/bin/env python3
from datetime import datetime
from elasticsearch import Elasticsearch

# Połączenie z Elasticsearch
es = Elasticsearch("http://localhost:9200")  # zmień host i port

# Dane do wysłania
doc = {
    "job": "my-job",
    "build_number": 123,
    "status": "SUCCESS",
    "timestamp": datetime.utcnow().isoformat()
}

# Wysłanie do indeksu 'jenkins-builds'
res = es.index(index="jenkins-builds", document=doc)
print(res)
