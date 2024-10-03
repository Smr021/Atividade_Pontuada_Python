from Projeto.models.funcionario        import Funcionario
from Projeto.models.endereco           import Endereco
from Projeto.models.enums.sexo         import Sexo
from Projeto.models.enums.estadoCivil  import EstadoCivil
from Projeto.models.enums.setor        import Setor

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
    

    def _verificar_oab_tipo_invalido_retorna_erro(self,valor):
        """Método para verificação do oab invalido"""
        if not isinstance (valor,str):
            raise TypeError('O oab deve ser um texto.')

    def _verificar_oab_vazio_invalido_retorna_erro(self,valor):
         """Método para verificação do oab vazio"""
         if not valor.strip(): 
            raise TypeError('O oab não pode estar vazio.')

    