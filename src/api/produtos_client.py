import requests

class ProdutosClient:
    BASE_URL = "https://compassuol.serverest.dev"
    def listar_produtos(self):
        return requests.get(f"{self.BASE_URL}/produtos")

    def buscar_produto(self, produto_id):
        return requests.get(
            f"{self.BASE_URL}/produtos/{produto_id}")

    def cadastrar_produto(self, payload, token):
        return requests.post(f"{self.BASE_URL}/produtos", json=payload, headers={"Authorization": token})

    def atualizar_produto(self, produto_id, payload, token):
        return requests.put(f"{self.BASE_URL}/produtos/{produto_id}", json=payload, headers={"Authorization": token})

    def excluir_produto(self, produto_id, token):
        return requests.delete(f"{self.BASE_URL}/produtos/{produto_id}", headers={"Authorization": token})
