class CadastroCliente:
    def __init__(self):
        self.clientes_cadastrados=[]
        
    def cadastrar_cliente(self, cliente):
        if cliente.idade < 18:
            return "Cliente não pode ser cadastrado pois é menor de idade!"
        
        self.clientes_cadastrados.append(cliente)
        if len (self.clientes_cadastrados) > 0:
            return "Cliente cadastrado com sucesso!"
        
        
    