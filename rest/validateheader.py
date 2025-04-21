import requests

BASE_URL= "https://reqres.in/"

import requests
BASE_URL= "https://reqres.in/"

try:
    response = requests.get(BASE_URL + "api/users?page=2")

    response.raise_for_status()
    print("Request successful")
except requests.exceptions.RequestException as e:
    print("Request failed:", str(e))



response = requests.get(BASE_URL + "api/users?page=2")
print(response.headers['Content-Type'])
assert response.status_code == 200, "Unexpected status code: " + str(response.status_code)


invalid_response = requests.get(BASE_URL + "1/nonexistent")  # Using an invalid URL
assert invalid_response.status_code == 404, "Expected a 404 status code, but got: " + str(invalid_response.status_code)