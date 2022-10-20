import Controller
import os.path

from Dao import DaoCategoria
from Models import Funcionario  

def criaArquivos(*args):
    for i in args:
        if not os.path.exists(i):
            with open(i, 'w') as arq:
                arq.write("")

criaArquivos('categoria.txt', 'clientes.txt', 
            'estoque.txt', 'fornecedores.txt',
            'funcionarios.txt', 'venda.txt')

if __name__ == "__main__":
    while True:
        local = int(input('Digite 1 para acessar( Categorias )\n'
                        'Digite 2 para acessar( Estoque )\n'
                        'Digite 3 para acessar( Fornecedor )\n'
                        'Digite 4 para acessar( Cliente )\n'
                        'Digite 5 para acessar( Funcionario )\n'
                        'Digite 6 para acessar( Vendas )\n'
                        'Digite 7 para ver os produtos mais vendidos\n'
                        'Digite 8 para sair\n'))

        if local == 1:
            cat = Controller.ControllerCategoria()
            while True:
                decidir = int(input('Digite 1 para cadastrar uma categoria\n'
                                    'Digite 2 para remover uma categoria\n'
                                    'Digite 3 para alterar uma categoria\n'
                                    'Digite 4 para mostrar categorias cadastradas\n'
                                    'Digite 5 para sair\n'))

                if decidir ==1:
                    categoria = input('Digite a categoria que deseja cadastrar\n')
                    cat.cadastrarCategoria(categoria)   
                elif decidir == 2:
                    categoria = input('Digite a categoria que deseja remover')
                    cat.removerCategoria(categoria)
                elif decidir == 3:
                    categoria = input('Digite a categoria que deseja alterar')
                    novaCategoria = input('Digite a nova categoria para ser alterado')
                    cat.alterarCategoria(categoria, novaCategoria)
                elif decidir == 4:
                    cat.mostrarCategorias()
                else:
                    break
        
        elif local == 2:
            cat = Controller.ControllerEstoque()
            while True:
                decidir = int(input('Digite 1 para cadastrar um produto\n'
                                    'Digite 2 para remover um produto\n'
                                    'Digite 3 para alterar um produto\n'
                                    'Digite 4 para ver o estoque\n'
                                    'Digite 5 para sair\n'))

                if decidir == 1:
                    nome = input('Digite o  nome do produto\n')
                    preco = input('Digite o preco do produto\n')
                    categoria = input('Digite a categoria do produto\n')
                    quantidade = input('Digite a quantidade que deseja cadastrar doproduto\n')

                    cat.cadastrarProduto(nome, preco, categoria, quantidade)
                
                elif decidir == 2:
                    produto = input('Digite o nome do produto que deseja remover\n')
                    cat.removerProduto(produto)
                
                elif decidir == 3:
                    nomeAlterar = input('Digite o nome do produto que deseja alterar')
                    nome = input('Digite o novo nome do produto para ser alterado')
                    preco = input('Digite o preço do produto')
                    categoria = input('Digite a categoria do produto')
                    quantidade = input('Digite a quantidade do produto a ser armazenada')
                    
                    cat.alterarProduto(nomeAlterar, nome, preco, categoria, quantidade)

                elif decidir == 4:
                    cat.mostrarEstoque()

                else:
                    break
            
        elif local == 3:
            cat = Controller.ControllerFornecedor()
            while True:
                decidir = int(input("Digite 1 para cadastrar um fornecedor\n"
                                    "Digite 2 para remover um fornecedor\n"
                                    "Digite 3 para alterar um fornecedor\n"
                                    "Digite 4 para mostrar fornecedores\n"
                                    "Digite 5 para sair\n"))
                    
                if decidir == 1:
                    nome = input('Digite o nome do fornecedor\n')
                    cnpj = input('Digite o cnpj do fornecedor\n')
                    telefone = input('Digite a telefone do fornecedor\n')
                    categoria = input('Digite a categoria que o fornecedor fornece\n')

                    cat.cadastrarFornecedor(nome, cnpj, telefone, categoria)
                
                elif decidir == 2: 
                    fornecedor = input('Digite o nome do fornecedor que deseja remover')
                    cat.removerFornecedor(fornecedor)

                elif decidir == 3:
                    nomeAlterar = input('Digite o nome do fornecedor que deseja alterar')
                    nome = input('Digite o novo nome do fornecedor para ser alterado')
                    cnpj = input('Digite o cnpj do fornecedor')
                    telefone = input('Digite a categoria do produto')
                    categoria = input('Digite a categoria que o fornecedor fornece')
                    
                    cat.alterarFornecedor(nomeAlterar, nome, cnpj, telefone, categoria)

                elif decidir == 4:
                    cat.mostrarFornecedores()
                
                else:
                    break
        
        elif local == 4:
            cat = Controller.ControllerCliente()
            while True:
                decidir = int(input('Digite 1 para cadastar um cliente\n'
                                    'Digite 2 para remover um cliente\n'
                                    'Digite 3 para alterar um cliente\n'
                                    'Digite 4 para mostar clientes\n'
                                    'Digite 5 para sair\n'))
                
                if decidir == 1:
                    nome = input('Digite o nome do cliente\n')
                    telefone = input('Digite o telefone do cliente\n')
                    cpf = input('Digite o cpf do cliente\n')
                    email = input('Digite o email do cliente\n')
                    endereco = input('Digite o endereço do cliente\n')

                    cat.cadastrarCliente(nome, telefone, cpf, email, endereco)

                elif decidir == 2:
                    cliente = input('Digite o nome do cliente que deseja remover')
                    cat.removerCliente(cliente)

                elif decidir == 3:
                    nomeAlterar = input('Digite o nome do cliente que deseja alterar\n')
                    nome = input('Digite o novo nome do cliente para ser alterado\n')
                    telefone = input('Digite o telefone do cliente\n')
                    cpf = input('Digite o cpf do cliente\n')
                    email = input('Digite o email do cliente\n')
                    endereco = input('Digite o endereço do cliente\n')

                    cat.alteraCliente(nomeAlterar, nome, telefone, cpf, email, endereco)
                
                elif decidir == 4:
                    cat.mostrarClientes()

                else:
                    break

        elif local == 5:
            while True:
                cat = Controller.ControllerFuncionario()

                decidir = int(input('Digite 1 para cadastar um funcionario\n'
                                    'Digite 2 para remover um funcionario\n'
                                    'Digite 3 para alterar um funcionario\n'
                                    'Digite 4 para mostar funcionarios\n'
                                    'Digite 5 para sair\n'))

                if decidir == 1:
                    clt = input('Digite a clt do funcionario')
                    nome = input('Digite o nome do funcionario\n')
                    telefone = input('Digite o telefone do funcionario\n')
                    cpf = input('Digite o cpf do funcionario\n')
                    email = input('Digite o email do funcionario\n')
                    endereco = input('Digite o endereço do funcionario\n')

                    cat.cadastrarFuncionario(clt, nome, telefone, cpf, email, endereco)

                elif decidir == 2:
                    funcionario = input('Digite o nome do funcionario que deseja remover')
                    cat.removerFuncionario(funcionario)

                elif decidir == 3:
                    nomeAlterar = input('Digite o nome do funcionario que deseja alterar')
                    clt = input('digite a clt do novo funcionario')
                    nome = input('Digite o novo nome do funcionario para ser alterado')
                    telefone = input('Digite o telefone do funcionario\n')
                    cpf = input('Digite o cpf do funcionario\n')
                    email = input('Digite o email do funcionario\n')
                    endereco = input('Digite o endereço do funcionario\n')

                    cat.alteraFuncionario(nomeAlterar, clt, nome, telefone, cpf, email, endereco)
                
                elif decidir == 4:
                    cat.mostrarFuncionarios()

                else:
                    break

        elif local == 6:
            cat = Controller.ControllerVenda()
            while True:
                decidir = input('Digite 1 para realizar uma venda\n'
                                'Digite 2 para ver as vendas\n'
                                'Digite 3 para sair\n')

                if decidir == 1:
                    nomeProduto = input('Digite o nome do produto vendido')
                    vendedor =  input('Digite o nome do vendedor')
                    comprador = input('Digite o nome do cliente comprador')
                    quantidade = input('Digite a quantidde vendida do produto')

                    cat.cadastrarVenda(nomeProduto, vendedor, comprador, quantidade)
                
                elif decidir == 2:
                    cat.mostrarVenda()

                else:
                    break
        
        elif local == 7:
            a = Controller.ControllerVenda()
            a.relatorioProdutos()
        
        else:
            break