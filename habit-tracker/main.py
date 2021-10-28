import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "fershbfuirhe",
    "username": "eshgin",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.json())

graph_endpoint = f"{pixela_endpoint}/eshgin/graphs"

graph_config = {
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "page",
    "type": "int",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": "fershbfuirhe"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()

pixel_endpoint = f"{pixela_endpoint}/eshgin/graphs/graph1"
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "50",
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/eshgin/graphs/graph1/20210813"
update_params = {
    "quantity": "10"
}

response = requests.put(url=update_endpoint, json=update_params, headers=headers)
print(response.text)
