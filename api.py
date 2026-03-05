import requests

BASE_URL = "http://localhost:5000"

def get_inventory():
    return requests.get(f"{BASE_URL}/inventory").json()

def add_material(data):
    return requests.post(f"{BASE_URL}/add_material", json=data)

def update_usage(data):
    return requests.post(f"{BASE_URL}/update_usage", json=data)

def get_variance():
    return requests.get(f"{BASE_URL}/variance").json()