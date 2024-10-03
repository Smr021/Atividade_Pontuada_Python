    # =========================== #
    #        Samir Santos         #
    #                             #
    #        Gabrel Bittecurt     #
    #                             #
    #        Turma 91210          #
    #                             #
    #        Senai || Fieb        #
    #                             #
    #        Salvador/BA          #
    # =========================== #

import os 
import sys
os.system("cls || clear")
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from Projeto.models.advogado import Advogado
from Projeto.models.engenheiro import Engenheiro
from Projeto.models.funcionario import Funcionario
from Projeto.models.endereco import Endereco
from Projeto.models.cliente import Cliente
from Projeto.models.fisica import Fisica
from Projeto.models.medico import Medico
from Projeto.models.enums.unidadeFederativa import UnidadeFederativa
from Projeto.models.enums.sexo import Sexo
from Projeto.models.enums.estadoCivil import EstadoCivil
from Projeto.models.enums.setor import Setor

funcionario = Funcionario(12,"Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A","12","Perto","1234567","Salvador",UnidadeFederativa.BAHIA),Sexo.MASCULINO,EstadoCivil.DONZELO,"25/10/2005","123.456.789-00","12.345.567-89","021024",Setor.JURIDICO,10000)
advogado = Advogado(515,'Gabriel Fuboca','71555-9555','gabriel.fuboca@gmail.com',Endereco('Rua A', '33','logo ali', '45658-565','salvador',UnidadeFederativa.SAO_PAULO),Sexo.MASCULINO,EstadoCivil.SOLTEIRO,'25/10/2005',"956.745.558-78",'15.457.598-74','0101',Setor.ENGENHARIA,1000,'019')
cliente = Cliente(12,"Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A","12","Perto","1234567","Salvador",UnidadeFederativa.BAHIA),Sexo.MASCULINO,EstadoCivil.DONZELO,"25/10/2005",1234)
fisica = Fisica(12,"Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A","12","Perto","1234567","Salvador",UnidadeFederativa.BAHIA),Sexo.MASCULINO,EstadoCivil.DONZELO,"25/10/2005")
medico = Medico(515,'Gabriel Fuboca','71555-9555','gabriel.fuboca@gmail.com',Endereco('Rua A', '33','logo ali', '45658-565','salvador',UnidadeFederativa.SAO_PAULO),Sexo.MASCULINO,EstadoCivil.SOLTEIRO,'25/10/2005',"956.745.558-78",'15.457.598-74','0101',Setor.ENGENHARIA,1000,'017')
engenheiro = Engenheiro(515,'Gabriel Fuboca','71555-9555','gabriel.fuboca@gmail.com',Endereco('Rua A', '33','logo ali', '45658-565','salvador',UnidadeFederativa.SAO_PAULO),Sexo.MASCULINO,EstadoCivil.SOLTEIRO,'25/10/2005',"956.745.558-78",'15.457.598-74','0101',Setor.ENGENHARIA,1000,'017')


# Inicia o test no terminal
if __name__ == '__main__':
    os.system('pytest ')

print(funcionario)
