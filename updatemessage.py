import requests

new_message = "New rolling message"
response = requests.post('http://127.0.0.1:5000//update_message', data={'new_message': new_message})
if response.status_code == 200:
    print("Rolling message updated successfully")
else:
    print("Failed to update rolling message")
