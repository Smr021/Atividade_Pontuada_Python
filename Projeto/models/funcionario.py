from abc                               import ABC, abstractmethod
from models.fisica                     import Fisica
from models.endereco                   import Endereco
from models.enums.sexo                 import Sexo
from models.enums.estadoCivil          import EstadoCivil
from models.enums.setor                import Setor

@abstractmethod
class Funcionario(Fisica,ABC):
    def __init__(self,id:str,nome:str,telefone:str,email:str,
                 endereco: Endereco,
                 sexo: Sexo ,
                 estadoCivil:EstadoCivil, 
                 dataNascimento: str ,cpf:str,rg:str,matricula:str,setor:Setor,salario:int) -> None:
        super().__init__(id, nome ,telefone ,email ,endereco ,sexo ,estadoCivil ,dataNascimento)
        self.cpf         = self._verificar_cpf(cpf)
        self.rg          = self._verificar_rg(rg)   
        self.matricula   = self._verificar_matricula(matricula)
        self.setor       = setor
        self.salario     = self._verificar_salario(salario)

# Métodos para verificação.

    def _verificar_cpf(self,valor):
        '''Método para verificação do CPF'''
        self._verificar_cpf_tipo_invalido(valor)
        self._verificar_cpf_vazio_invalido(valor)

        self.cpf = valor
        return self.cpf    
    
    def _verificar_rg(self,valor):
        '''Método para verificação do RG'''
        self._verificar_rg_tipo_invalido(valor)
        self._verificar_rg_vazio_invalido(valor)
        
        self.rg = valor
        return self.rg
    
    def _verificar_matricula(self,valor):
        '''Método para verificação da matricula'''
        self._verificar_matricula_tipo_invalido(valor)
        self._verificar_matricula_vazio_invalido(valor)

        self.matricula = valor
        return self.matricula
    
    def _verificar_salario(self,valor):
        '''Método para verificação do salario'''
        self._verificar_salario_vazio_invalido(valor)
        self._verificar_salario_tipo_invalido(valor)
        self._verificar_salario_negativo_invalido(valor)
        

        self.salario = valor
        return self.salario

    # Métodos auxiliares.

    def _verificar_cpf_tipo_invalido(self,valor):
        """Método para verificação do CPF invalido."""
        if not isinstance (valor,str):
            raise TypeError('O CPF deve ser um texto.')

    def _verificar_cpf_vazio_invalido(self,valor):
        """Método para verificação do CPF vazio."""
        if not valor.strip(): 
            raise TypeError('O CPF não pode estar vazio.')
         
    def _verificar_rg_tipo_invalido(self,valor):
        """Método para verificação do RG invalido."""
        if not isinstance (valor,str):
            raise TypeError('O RG deve ser um texto.')

    def _verificar_rg_vazio_invalido(self,valor):
         """Método para verificação do RG vazio."""
         if not valor.strip(): 
            raise TypeError('O RG não pode estar vazio.')

    def _verificar_matricula_tipo_invalido(self,valor):
        """Método para verificação da Matricula invalida."""
        if not isinstance (valor,str):
            raise TypeError("A Matricula deve ser um texto.")

    def _verificar_matricula_vazio_invalido(self,valor):
         """Método para verificação Matricula vazia."""
         if not valor.strip(): 
            raise TypeError("A Matricula não pode estar vazio.")
         
    def _verificar_salario_vazio_invalido(self,valor):
        """Método para verificação do Salário vazio."""
        if valor is None:
            raise ValueError("O campo do salario não pode ser deixado em branco.")

    def _verificar_salario_tipo_invalido(self,valor):
        """Método para verificação do Salário invalido."""
        if not isinstance (valor, (int, float)):
            raise ValueError("O salario deve ser um numero.")
        
    def _verificar_salario_negativo_invalido(self, valor):
        """Método para verificar salário negativo.""" 
        if valor <= 0:
            raise ValueError ("O salario não pode ser negativo.")

    


   # def _verificar_salario(self, valor):
    #        raise ValueError('O campo do salario não pode ser deixado em branco.')
    #    if valor is None or valor == '':
#
    #    if not isinstance(valor, (int, float)):
    #        raise TypeError('O salario deve ser um numero.')
#
    #    if valor < 0:
    #        raise ValueError('O salario não pode ser negativo.')
#
    #    return valor


    def __str__(self) -> str:
        return (
            f"{super().__str__()}"   
            f"\nMatrícula: {self.matricula}"
            f"Setor: {self.setor.value}"
            f"\nSalário: R$ {self.salario} reais"  
            f"\nSalário final: R$ {self.salario_final()} reais"
            )