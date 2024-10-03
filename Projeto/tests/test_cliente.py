import pytest
from models.cliente                  import Cliente
from models.enums.sexo               import Sexo
from models.enums.estadoCivil        import EstadoCivil
from models.endereco                 import Endereco
from models.enums.unidadeFederativa  import UnidadeFederativa

# Boas práticas de programação.
@pytest.fixture
def cliente_valido():
    cliente = Cliente(12,"Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A","12","Perto","1234567","Salvador",UnidadeFederativa.BAHIA),Sexo.MASCULINO,EstadoCivil.DONZELO,"25/10/2005",1234)
    return cliente

def test_protocolo_atendimento_valido(cliente_valido):
    assert cliente_valido.protocoloAtendimento == 1234

def test_protocolo_atendimento_tipo_invalido_retornar_mensagem_erro():
    with pytest.raises(TypeError, match="O protocolo de atendimento deve ser um número inteiro"):
        Cliente(12, "Fuboca", "71912345678", "fuboca@gmail.com", Endereco("Rua A", "12", "Perto", "1234567", "Salvador", UnidadeFederativa.BAHIA), Sexo.MASCULINO, EstadoCivil.DONZELO, "25/10/2005", "123")    

def test_protocolo_atendimento_vazio_invalido_retornar_mensagem_erro():
    with pytest.raises(ValueError, match="O protocolo de atendimento não pode ser deixado em branco."):
        Cliente(12, "Fuboca", "71912345678", "fuboca@gmail.com", Endereco("Rua A", "12", "Perto", "1234567", "Salvador", UnidadeFederativa.BAHIA), Sexo.MASCULINO, EstadoCivil.DONZELO, "25/10/2005",None)

def test_protocolo_atendimento_negativo():
    with pytest.raises(ValueError, match="O protocolo de atendimento não pode ser negativo"):
        Cliente(12, "Fuboca", "71912345678", "fuboca@gmail.com", Endereco("Rua A", "12", "Perto", "1234567", "Salvador", UnidadeFederativa.BAHIA), Sexo.MASCULINO, EstadoCivil.DONZELO, "25/10/2005", -123)