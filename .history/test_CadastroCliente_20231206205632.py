from Cliente import Cliente
from CadastroCliente import CadastroCliente

def teste_cliente_cadastrado_com_sucesso():
    cliente = Cliente("Yan", 21, "exemplo@gmail.com")
    cadastro_cliente = CadastroCliente()
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    assert "Cliente cadastrado com sucesso!" == resposta
    