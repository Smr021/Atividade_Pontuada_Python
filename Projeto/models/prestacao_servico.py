from models.juridica import Juridica
from models.endereco import Endereco

class Prestacao_servico(Juridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str, contratoInicio: str, contratoFim: str ) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricaoEstadual)
        self.contratoInicio = self._verificar_contratoInicio(contratoInicio)
        self.contratoFim    = self._verificar_contratoFim(contratoFim)

    """Métodos para verificação."""   
    def _verificar_contratoInicio(self, valor):
        """Métodoss para verificação de contrato incio."""
        self._verificar_contratoInicio_tipo_invalido(valor)
        self._verificar_contratoInicio_vazio_invalido(valor)

        self.contratoInicio = valor
        return self.contratoInicio

    def _verificar_contratoFim(self, valor):
        """Métodos para verificação de contrato fim."""
        self._verificar_contratoFim_tipo_invalido(valor)
        self._verificar_contratoFim_vazio_invalido(valor) 

        self.contratoFim = valor
        return self.contratoFim
    
    # Métodos auxiliares.
    def _verificar_contratoInicio_tipo_invalido(self, valor):
        """Método auxiliar para verificação de contrato incio invalido."""
        if not isinstance(valor, str):
            raise TypeError("O contrato inicio deve ser um texto.")
        
    def _verificar_contratoInicio_vazio_invalido(self, valor):
        """Método auxiliar para verificação de contrato inicio vazio"""  
        if not valor.strip():
            raise TypeError("O contrato inicio não pode estar vazio.")

    def _verificar_contratoFim_tipo_invalido(self, valor):
        """Método auxiliar para verificação de contrato fim invalido."""
        if not isinstance(valor, str):
            raise TypeError("O contrato fim deve ser um texto.")

    def _verificar_contratoFim_vazio_invalido(self, valor):
        """Método auxiliar para verificação de contrato fim vazio."""
        if not valor.strip():
            raise TypeError("O contrato fim não pode estar vazio.")          