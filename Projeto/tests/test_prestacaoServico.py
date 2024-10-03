import pytest
from models.prestacao_servico        import Prestacao_servico
from models.endereco                import Endereco
from models.enums.unidadeFederativa import UnidadeFederativa

# Boas práticas de programação.
@pytest.fixture
def prestacao_servico_valido():
    prestacao_servico = Prestacao_servico(12,"Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A","12","Perto","1234567","Salvador",UnidadeFederativa.BAHIA),"12345678","021024","011024","021025")
    return prestacao_servico

def test_contratoInicio_valido(prestacao_servico_valido):
    assert prestacao_servico_valido.contratoInicio == "011024"

def test_contratoFim_invalido(prestacao_servico_valido):
    assert prestacao_servico_valido.contratoFim == "021025"    

def test_contratoInicio_tipo_invalido_retornar_mensagem_erro():
    with pytest.raises(TypeError, match = "O contrato inicio deve ser um texto."):
        Prestacao_servico (12,"Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A","12","Perto","1234567","Salvador",UnidadeFederativa.BAHIA),"12345678","021024",123,"021025")

def test_contratoInicio_vazio_invalido_mensagem_erro():
    with pytest.raises(TypeError, match = "O contrato inicio não pode estar vazio."):
        Prestacao_servico  (12,"Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A","12","Perto","1234567","Salvador",UnidadeFederativa.BAHIA),"12345678","021024","","021025")

def test_contratoFim_tipo_invalido_retornar_mensagem_erro():
    with pytest.raises(TypeError, match = "O contrato fim() deve ser um texto."):
        Prestacao_servico (12,"Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A","12","Perto","1234567","Salvador",UnidadeFederativa.BAHIA),"12345678","021024","011024",123)

def test_contratoFim_vazio_invalido_retornar_mensagem_erro():
    with pytest.raises(TypeError, match = "O contrato fim não pode estar vazio."):
        Prestacao_servico (12,"Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A","12","Perto","1234567","Salvador",UnidadeFederativa.BAHIA),"12345678","021024","011024","")                     
