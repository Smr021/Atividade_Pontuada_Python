import pytest
from models.fisica                           import Fisica
from models.endereco                         import Endereco
from models.enums.unidadeFederativa          import UnidadeFederativa
from models.enums.sexo                       import Sexo
from models.enums.estadoCivil                import EstadoCivil

# Boas práticas de progamação.
@pytest.fixture
def fisica_valida():
    fisica = Fisica(12,"Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A","12","Perto","1234567","Salvador",UnidadeFederativa.BAHIA),Sexo.MASCULINO,EstadoCivil.DONZELO,"25/10/2005")
    return fisica

def test_dataNascimento_invalido(fisica_valida):
    assert fisica_valida.dataNascimento == "25/10/2005"
    

def test_verificar_dataNascimento_tipo_invalido_retornar_mensagem_erro():
    with pytest.raises(TypeError,match = 'A data de nascimento deve ser um texto.'):
        Fisica(12,"Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A","12","Perto","1234567","Salvador",UnidadeFederativa.BAHIA),Sexo.MASCULINO,EstadoCivil.DONZELO,25)

def test_verificar_dataNascimento_vazio_invalido_retornar_erro():
    with pytest.raises(TypeError,match = "A data de nascimento não pode estar vazio."):
        Fisica(12,"Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A","12","Perto","1234567","Salvador",UnidadeFederativa.BAHIA),Sexo.MASCULINO,EstadoCivil.DONZELO,"") 
    
