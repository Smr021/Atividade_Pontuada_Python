import pytest
from models.funcionario                      import Funcionario
from models.endereco                         import Endereco
from models.enums.unidadeFederativa          import UnidadeFederativa
from models.enums.sexo                       import Sexo
from models.enums.estadoCivil                import EstadoCivil
from models.enums.setor                      import Setor

# Boas práticas de progamação.
@pytest.fixture

def funcionario_valido():
    funcionario = Funcionario(12,"Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A","12","Perto","1234567","Salvador",UnidadeFederativa.BAHIA),Sexo.MASCULINO,EstadoCivil.DONZELO,"25/10/2005","123.456.789-00","12.345.567-89","021024",Setor.JURIDICO,10000)
    return funcionario

def test_cpf_valido(funcionario_valido):
    assert funcionario_valido.cpf == "123.456.789-00"

def test_rg_valido(funcionario_valido):
    assert funcionario_valido.rg == "12.345.567-89"   

def test_matricula_valida(funcionario_valido):
    assert funcionario_valido.matricula == "021024" 

def test_salario_valirio(funcionario_valido):
    assert funcionario_valido.salario == 10000       


def test_verificar_cpf_tipo_invalido():
    with pytest.raises(TypeError,match = 'O CPF deve ser um texto.'):
        Funcionario(12,"Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A","12","Perto","1234567","Salvador",UnidadeFederativa.BAHIA),Sexo.MASCULINO,EstadoCivil.DONZELO,"25/10/2005",12,"12.345.567-89","021024",Setor.JURIDICO,10000)

def test_verificar_cpf_vazio_invalido():
    with pytest.raises(TypeError,match = 'O CPF não pode estar vazio.'):
        Funcionario(12,"Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A","12","Perto","1234567","Salvador",UnidadeFederativa.BAHIA),Sexo.MASCULINO,EstadoCivil.DONZELO,"25/10/2005","","12.345.567-89","021024",Setor.JURIDICO,10000)
        

def test_verificar_rg_tipo_invalido():
    with pytest.raises(TypeError,match = 'O RG deve ser um texto.'):
        Funcionario(12,"Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A","12","Perto","1234567","Salvador",UnidadeFederativa.BAHIA),Sexo.MASCULINO,EstadoCivil.DONZELO,"25/10/2005","123.456.789-00",12,"021024",Setor.JURIDICO,10000)

def test_verificar_rg_vazio_invalido():
    with pytest.raises(TypeError,match = 'O RG não pode estar vazio.'):
        Funcionario(12,"Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A","12","Perto","1234567","Salvador",UnidadeFederativa.BAHIA),Sexo.MASCULINO,EstadoCivil.DONZELO,"25/10/2005","123.456.789-00","","021024",Setor.JURIDICO,10000)

def test_verificar_matricula_tipo_invalido():
    with pytest.raises(TypeError,match = 'A Matricula deve ser um texto.'):
        Funcionario(12,"Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A","12","Perto","1234567","Salvador",UnidadeFederativa.BAHIA),Sexo.MASCULINO,EstadoCivil.DONZELO,"25/10/2005","123.456.789-00","12.345.567-89",12,Setor.JURIDICO,10000)

def test_verificar_matricula_vazio_invalido():
    with pytest.raises(TypeError,match = 'A Matricula não pode estar vazio.'):
        Funcionario(12,"Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A","12","Perto","1234567","Salvador",UnidadeFederativa.BAHIA),Sexo.MASCULINO,EstadoCivil.DONZELO,"25/10/2005","123.456.789-00","12.345.567-89","",Setor.JURIDICO,10000)

def test_salario_vazio_invalido_retornar_mensagem_erro():
    with pytest.raises(ValueError, match = "O campo do salario não pode ser deixado em branco."):
        Funcionario(12,"Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A","12","Perto","1234567","Salvador",UnidadeFederativa.BAHIA),Sexo.MASCULINO,EstadoCivil.DONZELO,"25/10/2005","123.456.789-00","12.345.567-89","021024",Setor.JURIDICO,None)

def test_verificar_salario_tipo_invalido():
    with pytest.raises(ValueError,match = 'O salario deve ser um numero.'):
        Funcionario(12,"Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A","12","Perto","1234567","Salvador",UnidadeFederativa.BAHIA),Sexo.MASCULINO,EstadoCivil.DONZELO,"25/10/2005","123.456.789-00","12.345.567-89","021024",Setor.JURIDICO,"12")

def test_verificar_salario_negativo_invalido():
    with pytest.raises(ValueError,match = 'O salario não pode ser negativo.'):
        Funcionario(12,"Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A","12","Perto","1234567","Salvador",UnidadeFederativa.BAHIA),Sexo.MASCULINO,EstadoCivil.DONZELO,"25/10/2005","123.456.789-00","12.345.567-89","021024",Setor.JURIDICO,-100)

#def test_verificar_salario_vazio_invalido():
   # with pytest.raises(ValueError,match = "O campo do salario não pode ser deixado em branco."):
       # Funcionario(12,"Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A","12","Perto","1234567","Salvador",UnidadeFederativa.BAHIA),Sexo.MASCULINO,EstadoCivil.DONZELO,"25/10/2005","123.456.789-00","12.345.567-89","021024",Setor.JURIDICO,None)


