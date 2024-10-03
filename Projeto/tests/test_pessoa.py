import pytest
from abc                            import ABC, abstractmethod
from models.pessoa                  import Pessoa
from models.endereco                import Endereco
from models.enums.unidadeFederativa import UnidadeFederativa

# Boas práticas de progamação.
@pytest.fixture

def pessoa_valida():
    pessoa = Pessoa(7,"Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A", "12","Perto","12345","Salvador",UnidadeFederativa.BAHIA))
    return pessoa

def test_id_valido(pessoa_valida):
    assert pessoa_valida.id == 7

def test_nome_valido(pessoa_valida):
    assert pessoa_valida.nome == "Fuboca"

def test_telefone(pessoa_valida):    
    assert pessoa_valida.telefone == "71912345678"

def test_email(pessoa_valida):
    assert pessoa_valida.email == "fuboca@gmail.com"


def test_id_tipo_invalido_retornar_mensagem_de_erro():
    with pytest.raises(TypeError, match = "O ID deve ser um número inteiro."):
        Pessoa("12", "Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A", "12","Perto","12345","Salvador",UnidadeFederativa.BAHIA))

def test_id_negativo_retornar_mensagem_de_erro():
    with pytest.raises(ValueError,match = "O ID não pode ser negativo."):
        Pessoa(-1,"Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A", "12","Perto","12345","Salvador",UnidadeFederativa.BAHIA))        

def test_id_vazio_invalido_retornar_mensagem_de_erro():
    with pytest.raises(ValueError, match = "O campo do ID não pode ser deixado em branco."):
        Pessoa(None,"Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A", "12","Perto","12345","Salvador",UnidadeFederativa.BAHIA))

def test_nome_tipo_invalido_retornar_mensagem_de_erro():
    with pytest.raises(TypeError, match = "O nome precisa ser uma sequência de texto."):
        Pessoa(7,12,"71912345678","fuboca@gmail.com",Endereco("Rua A", "12","Perto","12345","Salvador",UnidadeFederativa.BAHIA))

def test_nome_vazio_invalido_retornar_mensagem_de_erro():
    with pytest.raises(TypeError, match = "O campo do nome não pode ser deixado em branco."):
        Pessoa(7,"","71912345678","fuboca@gmail.com",Endereco("Rua A", "12","Perto","12345","Salvador",UnidadeFederativa.BAHIA))  

def test_telefone_tipo_invalido_retornar_mensagem_de_erro():
    with pytest.raises(TypeError, match = "O campo do telefone não pode ser deixado em branco."):
        Pessoa(7,"Fuboca",12,"fuboca@gmail.com",Endereco("Rua A", "12","Perto","12345","Salvador",UnidadeFederativa.BAHIA)) 

def test_telefone_vazio_invalido_retornar_mensagem_de_erro():
    with pytest.raises(TypeError, match = "O telefone precisa ser uma sequência de texto."):
        Pessoa(7,"Fuboca","","fuboca@gmail.com",Endereco("Rua A", "12","Perto","12345","Salvador",UnidadeFederativa.BAHIA)) 
def test_telefone_tamanho_invalido_retornar_mensagem_de_erro():
    with pytest.raises(ValueError, match="O telefone deve ter exatamente 11 caracteres."):
        Pessoa(7, "Fuboca", "123456789", "fuboca@gmail.com", Endereco("Rua A", "1234", "Perto", "123456789", "Salvador", UnidadeFederativa.BAHIA))
        
def test_email_tipo_invalido_retornar_mensagem_de_erro():
    with pytest.raises(TypeError, match = "O e-mail precisa ser uma sequência de texto."):
        Pessoa(7,"Fuboca","71912345678",12,Endereco("Rua A", "12","Perto","12345","Salvador",UnidadeFederativa.BAHIA))

def test_email_vazio_invalido_retornar_mensagem_de_erro():
    with pytest.raises(TypeError, match = "O campo do e-mail não pode ser deixado em branco."):
        Pessoa(7,"Fuboca", "71912345678","",Endereco("Rua A", "12","Perto","12345","Salvador",UnidadeFederativa.BAHIA))       