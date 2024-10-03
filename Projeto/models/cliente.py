from models.fisica            import Fisica
from models.endereco          import Endereco
from models.enums.sexo        import Sexo
from models.enums.estadoCivil import EstadoCivil

class Cliente(Fisica):
    def __init__(self, id: str, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str, protocoloAtendimento: int) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento)
        self.protocoloAtendimento = self._verificar_protocolo_atendimento(protocoloAtendimento)

    # Métodos para verificação.
    def _verificar_protocolo_atendimento(self, valor):
        self._verificar_protocolo_atendimento_vazio_invalido(valor)
        self._verificar_protocolo_atendimento_tipo_invalido(valor)
        self._verificar_protocolo_atendimento_negativo(valor)

        self.protocoloAtendimento = valor
        return self.protocoloAtendimento
        
    # Métodos auxiliares.
    def _verificar_protocolo_atendimento_tipo_invalido(self, valor):
        if not isinstance(valor, int):
            raise TypeError("O protocolo de atendimento deve ser um número inteiro")

    def _verificar_protocolo_atendimento_vazio_invalido(self, valor):
        if valor is None:
            raise ValueError("O protocolo de atendimento não pode ser deixado em branco.")
            
    def _verificar_protocolo_atendimento_negativo(self, valor):
        if valor <= 0:
            raise ValueError("O protocolo de atendimento não pode ser negativo.")