from models.juridica import Juridica
from models.endereco import Endereco

class Fornecedor(Juridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str, produto: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricaoEstadual)
        self.produto = self._verificar_produto(produto)

    """Método para verificação."""
    def _verificar_produto(self, valor):
        """Método para verificação de produto."""
        self._verificar_produto_tipo_invalido(valor)
        self._verificar_produto_vazio_invalido(valor)

        self.produto = valor
        return self.produto
    
    # Métodos auxiliares.
    def _verificar_produto_tipo_invalido(self, valor):
        """Método auxiliar para verificação de produto invalido.""" 
        if not isinstance(valor, str):
            raise TypeError("O produto deve ser um texto.")
        
    def _verificar_produto_vazio_invalido(self, valor):
        """Método auxiliar para verificação de produtp vazio."""  
        if not valor.strip():
            raise TypeError("O produto não pode estar vazio.")