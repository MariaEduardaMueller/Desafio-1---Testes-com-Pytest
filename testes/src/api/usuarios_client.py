# Criação de classe para facilitar o entendimento e treinar meus conhecimentos.

import requests

class UsuariosClient:
    BASE_URL = "https://compassuol.serverest.dev"
    def listar_usuarios(self):
        return requests.get(f"{self.BASE_URL}/usuarios")
    def buscar_usuario(self, usuario_id):
        return requests.get(f"{self.BASE_URL}/usuarios/{usuario_id}")
    def cadastrar_usuario(self, payload):
        return requests.post(f"{self.BASE_URL}/usuarios", json=payload)
    def atualizar_usuario(self, usuario_id, payload):
        return requests.put(f"{self.BASE_URL}/usuarios/{usuario_id}", json=payload)
    def excluir_usuario(self, usuario_id):
        return requests.delete(f"{self.BASE_URL}/usuarios/{usuario_id}")
