from abc               import ABC, abstractmethod
from models.endereco   import Endereco

@abstractmethod
class Pessoa(ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.id       = self._verificar_id(id)
        self.nome     = self._verificar_nome(nome)
        self.telefone = self._verificar_telefone(telefone)
        self.email    = self._verificar_email(email)
        self.endereco = endereco

    # Método para verificação.
    def _verificar_id(self,valor):
        """Método para verificação de ID."""
        self._verificar_id_vazio_invalido(valor)
        self._verificar_id_tipo_invalido(valor)
        self._verificar_id_negativo(valor)
        

        self.id = valor
        return self.id

    def _verificar_nome(self,valor):
        """Método para verificação de nome."""
        self._verificar_nome_tipo_invalido(valor)
        self._verificar_nome_vazio_invalido(valor) 

        self.nome = valor
        return self.nome

    def _verificar_telefone(self,valor):
        """Método para verificação de telefone."""
        self._verificar_telefone_tipo_invalido(valor)
        self._verificar_telefone_vazio_invalido(valor)
        self._verificar_telefone_tamanho_invalido(valor)

        self.telefone = valor
        return self.telefone

    def _verificar_email(self,valor):
        """Método para verificação do e-mail."""
        self._verificar_email_tipo_invalido(valor)
        self._verificar_email_vazio_invalido(valor)

        self.email = valor
        return self.email

    # Métodos Auxiliares.
    def _verificar_id_tipo_invalido(self,valor):
        """"Método auxiliar para verificação do ID do tipo invalido."""
        if not isinstance(valor,int):
            raise TypeError("O ID deve ser um número inteiro.")
        
    def _verificar_id_negativo(self,valor):   
        """Método auxiliar para verificação do ID do tipo negativo."""
        if valor <= 0:
            raise ValueError("O ID não pode ser negativo.") 
        
    def _verificar_id_vazio_invalido(self,valor):
        """Método auxiliar para verificação do ID do tipo vazio."""
        if valor == None:
            raise ValueError("O campo do ID não pode ser deixado em branco.")   
         


    def _verificar_nome_tipo_invalido(self,valor):
        """"Método auxiliar para verificação do nome do tipo invalido."""  
        if not isinstance (valor, str):
            raise TypeError ("O nome precisa ser uma sequência de texto.")
        
    def _verificar_nome_vazio_invalido(self,valor):
        """"Método auxiliar para verificação do nome do tipo vazio."""
        if not valor.strip():
            raise TypeError("O campo do nome não pode ser deixado em branco.")  

    def _verificar_telefone_tipo_invalido(self,valor):
        """"Método auxiliar para verificação do telefone do tipo invalido."""
        if not isinstance (valor, str):
            raise TypeError ("O campo do telefone não pode ser deixado em branco.")

    def _verificar_telefone_vazio_invalido(self,valor):
        """Método auxiliar para verifcação do telefone do tipo invalido."""
        if not valor.strip():
            raise TypeError ("O telefone precisa ser uma sequência de texto.")
        
    def _verificar_telefone_tamanho_invalido(self, valor):
        """Método auxiliar para verificar o tamanho do telefone."""
        if len(valor) != 11:
            raise ValueError("O telefone deve ter exatamente 11 caracteres.")    

    def _verificar_email_tipo_invalido(self,valor):
        """Método auxuliar para verificação do e-mail do tipo invalido."""
        if not isinstance (valor, str):
            raise TypeError ("O e-mail precisa ser uma sequência de texto.")

    def _verificar_email_vazio_invalido(self,valor):
        """Método auxiliar para verificação do e-maiel do tipo."""
        if not valor.strip():
            raise TypeError ("O campo do e-mail não pode ser deixado em branco.")
            
