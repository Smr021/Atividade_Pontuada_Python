import pytest
from models.endereco                import Endereco
from models.enums.unidadeFederativa import UnidadeFederativa

# Boas práticas de programação.
@pytest.fixture

def endereco_valido():
    endereco = Endereco("Rua A", "12", "Perto", "1234567", "Salvador",UnidadeFederativa.BAHIA)
    return endereco


def test_logradouro_valido(endereco_valido):
    assert endereco_valido.logradouro == "Rua A"

def test_numero_valido(endereco_valido):
    assert endereco_valido.numero == "12"

def test_complemento_valido(endereco_valido):
    assert endereco_valido.complemento == "Perto"

def test_cep_valido(endereco_valido):
    assert endereco_valido.cep == "1234567"

def test_cidade_valido(endereco_valido):
    assert endereco_valido.cidade == "Salvador"


def test_logradouro_tipo_invalido_retornar_mensagem_de_erro():
    with pytest.raises(TypeError, match = "O logradouro deve ser um texto"):
        Endereco(12,"12","Perto","1234567","Salvador",UnidadeFederativa.BAHIA)

def test_logradouro_vazio_invalido_retornar_mensagem_de_erro():
    with pytest.raises(TypeError, match = "O logradouro não pode estar vazio."):
        Endereco("","12","Perto","1234567","Salvador",UnidadeFederativa.BAHIA)

def test_numero_vazio_invalido_retornar_mensagem_de_erro():
    with pytest.raises(TypeError, match = "O campo no número não pode estar vazio."):
        Endereco("Rua A", "", "Perto","1234567","Salvador",UnidadeFederativa.BAHIA)

def test_complemento_tipo_invalido_retornar_mensagem_de_erro():
    with pytest.raises(TypeError, match = "O complemento deve ser um texto."):
        Endereco("Rua A","12",12,"1234567","Salvador", UnidadeFederativa.BAHIA)

def test_complemento_vazio_invalido_retornar_mensagem_de_erro():
    with pytest.raises(TypeError, match = "O complemento não pode estar vazio."):
        Endereco("Rua A", "12","","1234567", "Salvador", UnidadeFederativa.BAHIA) 

def test_cep_vazio_invalido_retornar_mensagem_de_erro():
    with pytest.raises(TypeError, match = "O cep não pode estar vazio."):
        Endereco("Rua A", "12", "Perto", "", "salvador", UnidadeFederativa.BAHIA)

def test_cidade_tipo_invalido_retornar_mensagem_de_erro():
    with pytest.raises(TypeError, match = "O campo de cidade deve ter um texto."):
        Endereco("Rua A", "12","Perto","1234567",12,UnidadeFederativa.BAHIA)

def test_cidade_vazio_invalido_retornar_mensagem_de_erro():
    with pytest.raises(TypeError, match = "O campo de cidade não pode estar vazia"):
        Endereco("Rua A", "12","Perto", "1234567","",UnidadeFederativa.BAHIA)