import requests
import configuration
import data


# Запрос для создания нового пользователя и получение токена.
def post_new_user():
    url = configuration.BASE_URL + configuration.CREATE_USER
    return requests.post(url, json=data.CREATE_USER, headers=data.HEADERS)


response_token = post_new_user()
data.AUTH_TOKEN["Authorization"] = "Bearer " + response_token.json()["authToken"]
print(response_token.status_code)
print(response_token.json())


# Запрос для создания нового набора.
def post_new_client_kit(kit_body, auth_token):
    url = configuration.BASE_URL + configuration.CREATE_KITS
    return requests.post(url,json=kit_body, headers=auth_token)


response = post_new_client_kit(data.CREATE_KIT, data.AUTH_TOKEN)
print(response.status_code)
print(response.json())1