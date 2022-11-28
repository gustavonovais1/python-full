from Dao import *
from datetime import datetime

class ControllerCategoria:
    def cadastrarCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True
        
        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print('Categoria cadastrada com sucesso!')
        else: 
            print('A categoria que deseja cadastrar já existe!')

    def removerCategoria(self, categoriaRemover):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaRemover, x))

        if len(cat) <= 0:
            print('A categoria que deseja remover não existe!')
        else:
            for i in range(len(x)):
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    break
            print('Categoria removida com sucesso!')

            with open('categoria.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')

        estoque = DaoEstoque.ler()

        estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, 'Sem categoria'), x.quantidade)
        if(x.produto.categoria == categoriaRemover) else(x), estoque))

        with open('estoque.txt', 'w') as arq:
            for i in estoque:
                arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' + i.produto.categoria + '|' + str(i.quantidade))
                arq.writelines('\n')

    def alterarCategoria(self, categoriaAlterar, categoriaAlterada):
        x = DaoCategoria.ler()

        cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))

        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))
            
            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(categoriaAlterada) if(x.categoria == categoriaAlterar) else(x), x))
                print("A alteração foi realizada com sucesso!")
                
                estoque = DaoEstoque.ler()

                estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, categoriaAlterada), x.quantidade)
                if(x.produto.categoria == categoriaAlterar) else(x), estoque))

                with open('estoque.txt', 'w') as arq:
                    for i in estoque:
                        arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' + i.produto.categoria + '|' + str(i.quantidade))
                        arq.writelines('\n')


            else:
                print('A categoria para qual deseja alterar já existe!')

        else:
            print('A categoria que deseja alterar não existe!')

        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

    def mostrarCategorias(self):
        categoria = DaoCategoria.ler()
        if len(categoria) == 0:
            print('Categoria vazia!')
        else:
            for i in categoria:
                print(f'Categoria: {i.categoria}')

class ControllerEstoque:
    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == categoria, y))
        est = list(filter(lambda x: x.produto.nome == nome, x))

        if len(h) > 0:
            if len(est) == 0:
                produto = Produtos(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print('Produto cadastrado com sucesso!')
            else:
                print('Produto já existe em estoque!')
        else:
            print('Categoria inexistente!')

    def removerProduto(self, nome):
        x = DaoEstoque.ler()
        est = list(filter(lambda x: x.produto.nome == nome, x)) 
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x [i]
                    break
            
            print('Produto removido com sucesso!')
        else:
            print('O produto que deseja remover não existe!')

        with open('estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(i.quantidade))
                arq.writelines('\n')

    def alterarProduto(self, nomeAlterar, novoNome, novoPreco, novaCategoria, novaQuantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == novaCategoria, y))
        if len(h) > 0:
            est = list(filter(lambda x: x.produto.nome == nomeAlterar, x))
            if len(est) > 0:
                est = list(filter(lambda x: x.produto.nome == novoNome, x))
                if len(est) == 0:
                    x = list(map(lambda x: Estoque(Produtos(novoNome, novoPreco, novaCategoria), novaQuantidade) if (x.produto.nome == nomeAlterar) else(x), x))
                    print('Produto alterado com sucesso!')
                else:
                    print('O produto para qual deseja alterar já existe!')
            else:
                print('O produto que deseja alterar não existe!')

            with open('estoque.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(i.quantidade))
                arq.writelines('\n')

        else:
            print('A categoria informada não existe!')

    def mostrarEstoque(self):
        estoque = DaoEstoque.ler()
        if len(estoque) == 0:
            print('O estoque está vazio')
        else:
            print('========== Produtos ==========')
            for i in estoque:
                print(f'Nome: {i.produto.nome}\n'
                    f'Preço: {i.produto.preco}\n'
                    f'Categoria: {i.produto.categoria}\n'
                    f'Quantidade: {i.quantidade}')
                print('--------------------')

class ControllerVenda:
    def cadastrarVenda(self, nomeProduto, vendedor, comprador, quantidadeVndida):
        x = DaoEstoque.ler()
        temp = []
        existe = False
        quantidade = False
        
        for i in x:
            if existe == False:
                if i.produto.nome == nomeProduto:
                    existe = True
                    if i.quantidade >= quantidadeVndida:
                        quantidade = True
                        i.quantidade = int(i.quantidade) - int(quantidadeVndida)

                        vendido = Venda(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), vendedor, comprador, quantidadeVndida)

                        valorCompra = int(quantidadeVndida) * int(i.produto.preco)

                        DaoVenda.salvar(vendido)

            temp.append(Estoque(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade))

        arq = open('estoque.txt', 'w')
        arq.write("")

        for i in temp:
            with open('estoque.txt', 'a') as arq:
                arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' + i.produto.categoria + '|' + str(i.quantidade))
                arq.writelines('\n')
        
        if existe == False:
            print('O produto não existe em estoque!')
            return None
        elif not quantidade:
            print('A quantidade vendida não contém em estoque!')
            return None
        else:
            print('Venda realizada com sucesso!')
            return valorCompra

    def relatorioProdutos(self):
        vendas = DaoVenda.ler()
        produtos = []
        for i in vendas:
            nome = i.intensVendido.nome
            quantidade = i.quantidadeVendida
            if len(produtos) == 0:
                tamanho = []
            else:
                tamanho = list(filter(lambda x: x['produto'] == nome, produtos))
            if len(tamanho) > 0:
                produtos = list(map(lambda x: {'produto': nome,  'quantidade': x['quantidade'] + quantidade}
                if (x['produto'] == nome) else(x), produtos ))
            else:
                produtos.append({'produto': nome,  'quantidade': quantidade})

        ordenado = sorted(produtos, key= lambda k: k['quantidade'], reverse=True)
        print('Esses são os produtos mais vendidos.')
        for i in ordenado:
            a = 1
            print(f'========== Produto [{a}]==========')
            print(f" Produto: {i['produto']}\n"
                f" Quantidade: {i['quantidade']}\n")
            a += 1

    def mostrarVenda(self, dataInicio, dataTermino):
        vendas = DaoVenda.ler()
        dataInicio1 = datetime.strptime(dataInicio, '%d/%m/%Y')
        dataTermino1 =  datetime.strptime(dataTermino, '%d/%m/%Y')
        vendasSelecionadas = list(filter(lambda x: datetime.strptime(x.data, '%d/%m/%Y') >= dataInicio1
        and  datetime.strptime(x.data, '%d/%m/%Y') <= dataTermino1, vendas))

        cont = 1
        total = 0
        for i in vendasSelecionadas:
            print(f'========== Venda [{cont}] ==========')
            print(f'Nome: {i.intensVendido.nome}\n'
                f'Categoria: {i.intensVendido.categoria}\n'
                f'Data: {i.data}\n'
                f'Quantidade: {i.quantidadeVendida}\n'
                f'Cliente: {i.comprador}\n'
                f'Vendedor: {i.vendedor}')
            total = int(i.intensVendido.preco) * int(i.quantidadeVendida)
            cont += 1   
        print(f'Total vendido: {total}')

class ControllerFornecedor:
    def cadastrarFornecedor(self, nome, cnpj, telefone, categoria):
        x = DaoFornecedor.ler()
        listaCnpj = list(filter(lambda x: x.cnpj == cnpj, x))
        listaTelefome = list(filter(lambda x: x.telefone == telefone, x))
        if len(listaCnpj) > 0:
            print('O cnpj já existe!')
        elif len(listaTelefome) > 0:
            print('O telefone já existe!')
        else:
            if len(cnpj) == 14 and len(telefone) <= 11 and len(telefone) >= 10:
                DaoFornecedor.salvar(Fornecedor(nome, cnpj, telefone, categoria))
            else:
                print('Digite um cnpj ou telefone válido!')

    def alterarFornecedor(self, nomeAlterar, novoNome, novoCnpj, novoTelefone, novaCategoria ):
        x = DaoFornecedor.ler()

        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            est = list(filter(lambda x: x.cnpj == novoCnpj, x))
            if len(est) == 0:
                x = list(map(lambda x: Fornecedor(novoNome, novoCnpj, novoTelefone, novaCategoria) if( x.nome == nomeAlterar) else(x), x))
            else:
                print('O cnpj já existe!')
        else:
            print('O fornecedor que se deseja alterar não existe!')

        with open ('fornecedores.txt' , 'w') as arq:
            for i in x:
                arq.writelines(i.nome + '|' + i.cnpj + '|' + i.telefone + '|' + str(i.categoria))
                arq.writelines('\n')
            print('Fornecedor alterado com sucesso!')

    def removerFornecedor(self, nome):
        x = DaoFornecedor.ler()

        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print('O fornecedor que se deseja apagar não existe!')

        with open ('fornecedores.txt' , 'w') as arq:
            for i in x:
                arq.writelines(i.nome + '|' + i.cnpj + '|' + i.telefone + '|' + str(i.categoria))
                arq.writelines('\n')
            print('Fornecedor removido com sucesso!')

    def mostrarFornecedores(self):
        fornecedores = DaoFornecedor.ler()
        if len(fornecedores) == 0:
            print('Nenhum fornecedor cadastrado!')

        for i in fornecedores:
            print('========== Fornecedores ==========')
            print(f'Categoria fornecida: {i.categoria}\n'
                f'Nome: {i.nome}\n'
                f'Telefone: {i.telefone}\n'
                f'Cnpj: {i.cnpj}')

class ControllerCliente:
    def cadastrarCliente(self, nome, telefone, cpf, email, endereco):
        x = DaoPessoa.ler()

        listacpf = list(filter(lambda x: x.cpf == cpf, x))
        if len(listacpf) > 0:
            print('O cpf já existe!')
        else:
            if len(cpf) == 11 and len(telefone) <= 11 and len(telefone) >= 10:
                DaoPessoa.salvar(Pessoa(nome, telefone, cpf, email, endereco))
                print('Cliente cadastrado com sucesso!')
            else:
                print('Digite um cnpj ou telefone válido!')

    def alteraCliente(self, nomeAlterar, novoNome, novoTelefone, novoCpf, novaEmail, novoEndereco ):
        x = DaoPessoa.ler()

        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
                x = list(map(lambda x: Pessoa(novoNome, novoTelefone, novoCpf, novaEmail, novoEndereco) if( x.nome == nomeAlterar) else(x), x))
        else:
            print('O cliente que se deseja alterar não existe!')

        with open ('clientes.txt' , 'w') as arq:
            for i in x:
                arq.writelines(i.nome + '|' + i.telefone + '|' + i.cpf + '|' + i.email + '|' + i.endereco)
                arq.writelines('\n')
            print('CLiente alterado com sucesso!')

    def removerCliente(self, nome):
        x = DaoPessoa.ler()

        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print('O cliente que se deseja apagar não existe!')
            return None 

        with open ('clientes.txt' , 'w') as arq:
            for i in x:
                arq.writelines(i.nome + '|' + i.telefone + '|' + i.cpf + '|' + i.email + '|' + i.endereco)
                arq.writelines('\n')
            print('CLiente removido com sucesso!')

    def mostrarClientes(self):
        clientes = DaoPessoa.ler()
        if len(clientes) == 0:
            print('Nenhum fornecedor cadastrado!')

        for i in clientes:
            print('========== Clientes ==========')
            print(f'Nome: {i.nome}\n'
                f'Telefone: {i.telefone}\n'
                f'Cpf: {i.cpf}\n'
                f'Email: {i.email}\n'
                f'Endereço: {i.endereco}')

class ControllerFuncionario:
    def cadastrarFuncionario(self, clt, nome, telefone, cpf, email, endereco):
        x = DaoFuncionario.ler()

        listacpf = list(filter(lambda x: x.cpf == cpf, x))
        listaClt = list(filter(lambda x: x.clt == clt, x))
        if len(listacpf) > 0:
            print('O cpf já existe!')
        elif len(listaClt) > 0:
            print('Já existe um funcionario com essa clt')
        else:
            if len(cpf) == 11 and len(telefone) <= 11 and len(telefone) >= 10:
                DaoFuncionario.salvar(Funcionario(clt, nome, telefone, cpf, email, endereco))
                print('Funconario cadastrado com sucesso!')
            else:
                print('Digite um cpf ou telefone válido!')

    def alteraFuncionario(self, nomeAlterar, novaClt, novoNome, novoTelefone, novoCpf, novaEmail, novoEndereco ):
        x = DaoFuncionario.ler()

        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
                x = list(map(lambda x: Funcionario(novaClt, novoNome, novoTelefone, novoCpf, novaEmail, novoEndereco) if( x.nome == nomeAlterar) else(x), x))
        else:
            print('O funcionario que se deseja alterar não existe!')

        with open ('funcionarios.txt' , 'w') as arq:
            for i in x:
                arq.writelines(i.clt + '|' + i.nome + '|' + i.telefone + '|' + i.cpf + '|' + i.email + '|' + i.endereco)
                arq.writelines('\n')
            print('CLiente alterado com sucesso!')

    def removerFuncionario(self, nome):
        x = DaoFuncionario.ler()

        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print('O funcionario que se deseja apagar não existe!')
            return None 

        with open ('funcionarios.txt' , 'w') as arq:
            for i in x:
                arq.writelines(i.nome + '|' + i.telefone + '|' + i.cpf + '|' + i.email + '|' + i.endereco)
                arq.writelines('\n')
            print('Funcionario removido com sucesso!')

    def mostrarFuncionarios(self):
        funcionarios = DaoFuncionario.ler()
        if len(funcionarios) == 0:
            print('Nenhum funcionarios cadastrado!')

        for i in funcionarios:
            print('========== FUncionarios ==========')
            print(f'Nome: {i.nome}\n'
                f'Telefone: {i.telefone}\n'
                f'Email: {i.email}\n'
                f'Endereço: {i.endereco}\n'
                f'Cpf: {i.cpf}\n'
                f'Clt: {i.clt}')
