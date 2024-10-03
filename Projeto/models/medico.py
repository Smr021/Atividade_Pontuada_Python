from projeto.models.funcionario        import Funcionario
from projeto.models.endereco           import Endereco
from projeto.models.enums.sexo         import Sexo
from projeto.models.enums.estadoCivil  import EstadoCivil
from projeto.models.enums.setor        import Setor

class Medico(Funcionario):
    def __init__(self,id:str,nome:str,telefone:str,email:str,
                 endereco: Endereco,
                 sexo: Sexo ,
                 estadoCivil:EstadoCivil, 
                 dataNascimento: str ,cpf:str,rg:str,matricula:str,setor:Setor,salario:float,crm:str) -> None:
        super().__init__(id, nome ,telefone ,email ,endereco ,sexo ,estadoCivil ,dataNascimento,cpf,rg,matricula,setor,salario)
        self.crm = self._verificar_crm(crm)

    def _verificar_crm(self,valor):
        '''Método para verificação do crm'''
        self._verificar_crm_tipo_invalido_retorna_erro(valor)
        self._verificar_crm_vazio_invalido_retorna_erro(valor)

        self.crm = valor
        return self.crm
    

    """Método para verificação do crm invalido"""
    def _verificar_crm_tipo_invalido_retorna_erro(self,valor):
        if not isinstance (valor,str):
            raise TypeError('O crm deve ser um texto.')

    def _verificar_crm_vazio_invalido_retorna_erro(self,valor):
         if not valor.strip(): 
            raise TypeError('O crm não pode estar vazio.')

    