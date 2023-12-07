class CadastroCliente:
    def __init__(self):
        delf.clientes_cadastrados=[]
        
    def cadastrar_cliente(self, cliente):
        self.clientes_cadastrados.append(cliente)
        return "Cliente cadastrado com sucesso!"