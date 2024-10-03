from abc             import ABC, abstractmethod
from models.pessoa   import Pessoa
from models.endereco import Endereco


class Juridica(Pessoa,ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.cnpj              = self._verificar_cnpj(cnpj)
        self.inscricaoEstadual = self._verificar_inscricaoEstadual(inscricaoEstadual)

    #Métodos para verificação.
    def _verificar_cnpj(self, valor):
        """Método para verificação de CNPJ."""
        self._verificar_cnpj_tipo_invalido(valor)
        self._verificar_cnpj_vazio_invalido(valor) 

        self.cnpj = valor
        return self.cnpj
    
    def _verificar_inscricaoEstadual(self,valor):
        """Método para verificação de Inscrição Estadual. """
        self._verificar_inscricaoEstadual_tipo_invalida(valor)
        self._verificar_inscricaoEstadual_vazio_invalido(valor)
        
        self.inscricaoEstadual = valor
        return self.inscricaoEstadual
    
    # Métodos Auxiliares.
    def _verificar_cnpj_tipo_invalido(self,valor):
        """Método auxiliar para verificação do CNPJ invalido."""
        if not isinstance(valor,str):
            raise TypeError("O cnpj precisa ser uma sequência de texto.")

    def _verificar_cnpj_vazio_invalido(self,valor):
        """Método auxiliar para verificação do CNJP vazio."""
        if not valor.strip():
            raise TypeError("O campo do cnpj não pode ser deixado em branco.")

    def _verificar_inscricaoEstadual_tipo_invalida(self,valor):
        """Método auxilar para verificação da inscrição estadual invalido."""
        if not isinstance(valor, str):
            raise TypeError("A inscrição estadual precisa ser uma sequência de texto.")

    def _verificar_inscricaoEstadual_vazio_invalido(self,valor):
        """Método auxiliar para verifcação da inscrição estadual vazio."""
        if not valor.strip():
            raise TypeError("O campo da inscrição estadual não pode ser deixado em branco.")
        
        
