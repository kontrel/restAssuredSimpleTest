#!/usr/bin/env python3
import json
import requests
import os
from datetime import datetime

ELASTIC_URL = os.getenv("ELASTIC_URL", "http://elasticsearch:9200")
INDEX_NAME = os.getenv("ELASTIC_INDEX", "jenkins-test-results")
JSON_FILE = "test-results.json"

def send_to_elasticsearch():
    with open(JSON_FILE, "r", encoding="utf-8") as f:
        test_data = json.load(f)

    payload = {
        "timestamp": datetime.utcnow().isoformat(),
        "job_name": os.getenv("JOB_NAME", "unknown_job"),
        "build_number": os.getenv("BUILD_NUMBER", "0"),
        "results": test_data
    }

    response = requests.post(
        f"{ELASTIC_URL}/{INDEX_NAME}/_doc/",
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload)
    )

    if response.status_code in (200, 201):
        print(f"✅ Wysłano dane do Elasticsearch: {response.json()['_id']}")
    else:
        print(f"❌ Błąd wysyłki: {response.status_code} - {response.text}")

if __name__ == "__main__":
    send_to_elasticsearch()
