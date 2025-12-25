import urllib.request
import json

url = 'http://127.0.0.1:5000/predict'
data = {
    'parentalEducation': 'Higher',
    'attendancePercentage': 90.0,
    'previousYearPercentage': 85.0,
    'studyHours': 10,
    'internetAccess': 'Yes'
}

req = urllib.request.Request(url, 
                             data=json.dumps(data).encode('utf-8'), 
                             headers={'Content-Type': 'application/json'})

try:
    with urllib.request.urlopen(req) as response:
        print("Status Code:", response.getcode())
        print("Response:", json.loads(response.read().decode()))
except Exception as e:
    print("Error:", e)
