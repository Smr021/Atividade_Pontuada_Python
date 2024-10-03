from Projeto.models.funcionario        import Funcionario
from Projeto.models.endereco           import Endereco
from Projeto.models.enums.sexo         import Sexo
from Projeto.models.enums.estadoCivil  import EstadoCivil
from Projeto.models.enums.setor        import Setor

class Engenheiro(Funcionario):
    def __init__(self,id:str,nome:str,telefone:str,email:str,
                 endereco: Endereco,
                 sexo: Sexo ,
                 estadoCivil:EstadoCivil, 
                 dataNascimento: str ,cpf:str,rg:str,matricula:str,setor:Setor,salario:float,crea:str) -> None:
        super().__init__(id, nome ,telefone ,email ,endereco ,sexo ,estadoCivil ,dataNascimento,cpf,rg,matricula,setor,salario)
        self.crea = self._verificar_crea(crea)
    
    # Métodos de verificar
    def _verificar_crea(self,valor):
        '''Método para verificação do CREA'''
        self._verificar_crea_tipo_invalido_retorna_erro(valor)
        self._verificar_crea_vazio_invalido_retorna_erro(valor)

        self.crea = valor
        return self.crea
    

    def _verificar_crea_tipo_invalido_retorna_erro(self,valor):
        """Método para verificação do CREA invalido"""
        if not isinstance (valor,str):
            raise TypeError('O CREA deve ser um texto.')

    def _verificar_crea_vazio_invalido_retorna_erro(self,valor):
         """Método para verificação do CREA vazio"""
         if not valor.strip(): 
            raise TypeError('O CREA não pode estar vazio.')

    