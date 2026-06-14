import requests

class LoginClient:
    BASE_URL = "https://compassuol.serverest.dev"
    def login(self, payload):
        return requests.post(f"{self.BASE_URL}/login", json=payload )
