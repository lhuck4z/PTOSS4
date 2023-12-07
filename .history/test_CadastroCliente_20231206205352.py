from Cliente import Cliente
from CadastroCliente import CadastroCliente

def teste_cliente_cadastrado_com_sucesso():
    cliente = Cliente()
    cadastro_cliente = CadastroCliente()
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    assert resposta == "Cliente cadastrado com sucesso!" == resposta
    