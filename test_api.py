import requests
import json
url = "http://127.0.0.1:8000/api/submit-inquiry/"
data = {"name": "Test Name", "email": "test@example.com", "phone": "123", "selected_plan": "Starter"}
headers = {'Content-Type': 'application/json', 'Origin': 'http://localhost:5173'}
print('sending request to', url)
try:
    response = requests.post(url, json=data, headers=headers)
    print(response.status_code, response.text)
except Exception as e:
    print(e)
