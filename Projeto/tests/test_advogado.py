import pytest
from projeto.models.advogado import Advogado
from projeto.models.endereco import Endereco
from projeto.models.enums.unidadeFederativa import UnidadeFederativa
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.estadoCivil import EstadoCivil
from projeto.models.enums.setor import Setor

# Boas práticas de progamação.
@pytest.fixture
def advogado_valido():
    advogado = Advogado(515,'Gabriel Fuboca','71555-9555','gabriel.fuboca@gmail.com',Endereco('Rua A', '33','logo ali', '45658-565','salvador',UnidadeFederativa.SAO_PAULO),Sexo.MASCULINO,EstadoCivil.SOLTEIRO,'25/10/2005',"956.745.558-78",'15.457.598-74','0101',Setor.ENGENHARIA,1000,'019')
    return advogado
    


def test_verificar_oab_tipo_invalido_retorna_erro(advogado_valido):
    assert advogado_valido.oab == '019'

#===============================================================================================
def test_verificar_oab_tipo_invalido_retorna_erro():
    with pytest.raises(TypeError,match = 'O oab deve ser um texto.'):
        Advogado(515,'Gabriel Fuboca','71555-9555','gabriel.fuboca@gmail.com',Endereco('Rua A', '33','logo ali', '45658-565','salvador',UnidadeFederativa.SAO_PAULO),Sexo.MASCULINO,EstadoCivil.SOLTEIRO,'25/10/2005',"956.745.558-78",'15.457.598-74','0101',Setor.ENGENHARIA,1000,55)
        

def test_verificar_oab_vazio_invalido_retorna_erro():
    with pytest.raises(TypeError,match = 'O oab não pode estar vazio.'):
        Advogado(515,'Gabriel Fuboca','71555-9555','gabriel.fuboca@gmail.com',Endereco('Rua A', '33','logo ali', '45658-565','salvador',UnidadeFederativa.SAO_PAULO),Sexo.MASCULINO,EstadoCivil.SOLTEIRO,'25/10/2005',"956.745.558-78",'15.457.598-74','0101',Setor.ENGENHARIA,1000,'')
#===============================================================================================



