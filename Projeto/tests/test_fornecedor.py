import pytest
from models.fornecedor              import Fornecedor
from models.endereco                import Endereco
from models.enums.unidadeFederativa import UnidadeFederativa


# Boas práticas de programação.
@pytest.fixture
def fornecedor_valido():
    fornecedor = Fornecedor(12,"Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A", "12","Perto","1234567","Salvador",UnidadeFederativa.BAHIA),"123456789","021024", "Arroz")
    return fornecedor

def test_fornecedor_produto_valido(fornecedor_valido):
    assert fornecedor_valido.produto == "Arroz"

def test_produto_tipo_invalido_mensagem_erro():
        with pytest.raises(TypeError, match = "O produto deve ser um texto."):
            Fornecedor(12,"Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A","12","Perto","12345678","Salvador",UnidadeFederativa.BAHIA),"123456789","021024", 12)


def test_produto_vazio_invalido_mensagem_erro():
         with pytest.raises(TypeError, match = "O produto não pode estar vazio."):
            Fornecedor(12,"Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A","12","Perto","12345678","Salvador",UnidadeFederativa.BAHIA),"123456789","021024", "")