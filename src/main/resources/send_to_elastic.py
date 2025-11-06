import requests
import json
from datetime import datetime

url = "http://elasticsearch:9200/jenkins-builds/_doc/"
data = {
    "job": "my-job",
    "build_number": 123,
    "status": "SUCCESS",
    "timestamp": datetime.utcnow().isoformat()
}

response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(data))
print(response.status_code, response.text)
