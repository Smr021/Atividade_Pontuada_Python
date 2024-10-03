import pytest
from models.juridica                import Juridica
from models.endereco                import Endereco
from models.enums.unidadeFederativa import UnidadeFederativa

# Boas práticas de Programação.
@pytest.fixture

def juridica_valida():
    juridica = Juridica(12,"Fuboca","71912345678","fuboca@gmail.com", Endereco("Rua A","12","Perto","1234567","Salvador",UnidadeFederativa.BAHIA),"12345678","021024")
    return juridica


def test_cnpj_valido(juridica_valida):
    assert juridica_valida.cnpj == "12345678"

def test_inscricaoEstadual_valido(juridica_valida):
    assert juridica_valida.inscricaoEstadual == "021024"

def test_cnpj_tipo_invalido_retornar_mensagem_erro():
    with pytest.raises(TypeError, match = "O cnpj precisa ser uma sequência de texto."):
        Juridica(12,"Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A","12","Perto","1234567","Salvador",UnidadeFederativa.BAHIA),123,"021024")

def test_cnpj_vazio_invalido_retornar_mensagem_erro():   
    with pytest.raises(TypeError, match = "O campo do cnpj não pode ser deixado em branco."):  
        Juridica(12,"Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A","12","Perto","1234567","Salvador",UnidadeFederativa.BAHIA),"","021024")

def test_inscricaoEstadual_tipo_invalido_retornar_mensagem_erro():
    with pytest.raises(TypeError, match = "A inscrição estadual precisa ser uma sequência de texto."):
        Juridica(12,"Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A","12","Perto","1234567","Salvador",UnidadeFederativa.BAHIA),"12345678",22)

def test_inscricaoEstadual_vazio_invalido_retornar_mensagem_erro():
    with pytest.raises(TypeError, match = "O campo da inscrição estadual não pode ser deixado em branco."):        
        Juridica(12,"Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A","12","Perto","1234567","Salvador",UnidadeFederativa.BAHIA),"12345678","")

