from projeto.models.funcionario        import Funcionario
from projeto.models.endereco           import Endereco
from projeto.models.enums.sexo         import Sexo
from projeto.models.enums.estadoCivil  import EstadoCivil
from projeto.models.enums.setor        import Setor

class Advogado(Funcionario):
    def __init__(self,id:str,nome:str,telefone:str,email:str,
                 endereco: Endereco,
                 sexo: Sexo ,
                 estadoCivil:EstadoCivil, 
                 dataNascimento: str ,cpf:str,rg:str,matricula:str,setor:Setor,salario:float,oab:str) -> None:
        super().__init__(id, nome ,telefone ,email ,endereco ,sexo ,estadoCivil ,dataNascimento,cpf,rg,matricula,setor,salario)
        self.oab = self._verificar_oab(oab)

    def _verificar_oab(self,valor):
        '''Método para verificação do oab'''
        self._verificar_oab_tipo_invalido_retorna_erro(valor)
        self._verificar_oab_vazio_invalido_retorna_erro(valor)

        self.oab = valor
        return self.oab
    

    """Método para verificação do oab invalido"""
    def _verificar_oab_tipo_invalido_retorna_erro(self,valor):
        if not isinstance (valor,str):
            raise TypeError('O oab deve ser um texto.')

    def _verificar_oab_vazio_invalido_retorna_erro(self,valor):
         if not valor.strip(): 
            raise TypeError('O oab não pode estar vazio.')

    