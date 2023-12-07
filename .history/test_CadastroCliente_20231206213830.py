from Cliente import Cliente
from CadastroCliente import CadastroCliente

def teste_cliente_cadastrado_com_sucesso():
    cliente = Cliente("Yan", 21, "exemplo@gmail.com")
    cadastro_cliente = CadastroCliente()
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    assert "Cliente cadastrado com sucesso!" == resposta
    
def teste_cliente_menor_de_idade():
    cliente = Cliente("Yan", 17, "fulando@hotmail.com")
    cadastro_cliente = CadastroCliente()
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    assert "Cliente não pode ser cadastrado pois é menor de idade!" == resposta

def teste_email_incorreto():
    cliente = Cliente("Yan", 18, "fulandohotmail.com")
    cadastro_cliente = CadastroCliente()
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    assert "Email Inválido!" == resposta
    