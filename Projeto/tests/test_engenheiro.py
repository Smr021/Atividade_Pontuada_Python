import pytest
from projeto.models.engenheiro import Engenheiro
from projeto.models.endereco import Endereco
from projeto.models.enums.unidadeFederativa import UnidadeFederativa
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.estadoCivil import EstadoCivil
from projeto.models.enums.setor import Setor

# Boas práticas de progamação.
@pytest.fixture
def engenheiro_valido():
    engenheiro = Engenheiro(515,'Gabriel Fuboca','71555-9555','gabriel.fuboca@gmail.com',Endereco('Rua A', '33','logo ali', '45658-565','salvador',UnidadeFederativa.SAO_PAULO),Sexo.MASCULINO,EstadoCivil.SOLTEIRO,'25/10/2005',"956.745.558-78",'15.457.598-74','0101',Setor.ENGENHARIA,1000,'017')

    return engenheiro
    


def test_verificar_crea_tipo_invalido_retorna_erro(engenheiro_valido):
    assert engenheiro_valido.crea == '017'

#===============================================================================================
def test_verificar_crea_tipo_invalido_retorna_erro():
    with pytest.raises(TypeError,match = 'O CREA deve ser um texto.'):
        Engenheiro(515,'Gabriel Fuboca','71555-9555','gabriel.fuboca@gmail.com',Endereco('Rua A', '33','logo ali', '45658-565','salvador',UnidadeFederativa.SAO_PAULO),Sexo.MASCULINO,EstadoCivil.SOLTEIRO,'25/10/2005',"956.745.558-78",'15.457.598-74','0101',Setor.ENGENHARIA,1000,55)
        

def test_verificar_crea_vazio_invalido_retorna_erro():
    with pytest.raises(TypeError,match = 'O CREA não pode estar vazio.'):
        Engenheiro(515,'Gabriel Fuboca','71555-9555','gabriel.fuboca@gmail.com',Endereco('Rua A', '33','logo ali', '45658-565','salvador',UnidadeFederativa.SAO_PAULO),Sexo.MASCULINO,EstadoCivil.SOLTEIRO,'25/10/2005',"956.745.558-78",'15.457.598-74','0101',Setor.ENGENHARIA,1000,'')
#===============================================================================================



