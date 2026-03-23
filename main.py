import os
from datetime import datetime
from cliente import Cliente, Pet
from produto import Produto
from venda import Venda

lista_clientes = []
lista_produtos = []
lista_vendas = []

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def input_numerico(mensagem, min_digitos=None, max_digitos=None, permitir_cancelar=True):
    while True:
        aviso = " (ou 'V' para Voltar): " if permitir_cancelar else ": "
        valor = input(mensagem + aviso).strip()

        if permitir_cancelar and valor.upper() == 'V':
            return 'VOLTAR'
        
        if valor.isdigit():
            if max_digitos and len(valor) > max_digitos:
                print(f"Erro: Máximo de {max_digitos} dígitos!")
                continue
            if min_digitos and len(valor) < min_digitos:
                print(f"Erro: Mínimo de {min_digitos} dígitos!")
                continue
            return valor
        else:
            print("Erro: Digite apenas números!")

def popular_dados():
    lista_produtos.extend([
        Produto("1", "Antipulga", 100.0, 10),
        Produto("2", "Ração Monello", 19.90, 10000),
        Produto("3", "Sabonete Antipulgas", 15.0, 20),
        Produto("4", "Suplemento Vitaminas", 212.90, 10),
        Produto("5", "Vermifugo Oral", 70.0, 20),
        Produto("6", "Coleira Passeio", 25.0, 10),
        Produto("7", "Shampoo Pet", 50.0, 25),
        Produto("8", "Petiscos Pacote", 5.0, 50),
        Produto("9", "Areia Gatos 5kg", 35.0, 50),
        Produto("10", "Pote para Ração", 15.0, 30)
    ])
    c1 = Cliente("11122233344", "Yudi SBT", "54940028922")
    c1.adicionar_pet(Pet("PS2", "Cão", "Pitbull"))

    c2 = Cliente("12345678910", "Lauren", "54998223456")
    c2.adicionar_pet(Pet("Tobi", "Cão", "Labrador"))
    c2.adicionar_pet(Pet("Ravena", "Cão", "Golden"))
    
    c3 = Cliente("00112233445", "Yudi SBT", "54940028922")
    c3.adicionar_pet(Pet("Tom", "Gato", "Ragdoll"))

    lista_clientes.extend([c1, c2, c3])


def cadastrar_cliente():
    limpar_tela()
    print("--- CADASTRO DE CLIENTE ---")
    cpf = input_numerico("CPF (11 dígitos)", min_digitos=11, max_digitos=11)
    if cpf == 'VOLTAR': return

    if any(c.cpf == cpf for c in lista_clientes):
        print("Erro: CPF já cadastrado!")
        input("\nEnter para continuar...")
        return

    nome = input("Nome: ")
    tel = input_numerico("Telefone")
    if tel == 'VOLTAR': return

    novo_c = Cliente(cpf, nome, tel)
    print("\n--- DADOS DO PET ---")
    p_nome = input("Nome do Pet: ")
    p_esp = input("Espécie: ")
    p_rac = input("Raça: ")
    
    novo_c.adicionar_pet(Pet(p_nome, p_esp, p_rac))
    lista_clientes.append(novo_c)
    print("\n Cliente cadastrado!")
    input("\nEnter para continuar...")

def remover_cliente():
    limpar_tela()
    print("--- REMOVER CLIENTE ---")
    cpf = input_numerico("Digite o CPF do cliente para remover")
    if cpf == 'VOLTAR': return

    cliente = next((c for c in lista_clientes if c.cpf == cpf), None)
    if cliente:
        lista_clientes.remove(cliente)
        print(f" Cliente {cliente.nome} removido com sucesso!")
    else:
        print(" Cliente não encontrado.")
    input("\nEnter para continuar...")

def cadastrar_produto():
    limpar_tela()
    print("--- CADASTRO DE PRODUTO ---")
    id_p = input_numerico("ID")
    if id_p == 'VOLTAR': return
    
    nome = input("Nome: ")
    preco = float(input_numerico("Preço", permitir_cancelar=False))
    qtd = int(input_numerico("Qtd Inicial", permitir_cancelar=False))
    
    lista_produtos.append(Produto(id_p, nome, preco, qtd))
    print("\n Produto adicionado!")
    input("\nEnter para continuar...")

def realizar_venda():
    limpar_tela()
    print("--- NOVA VENDA ---")
    cpf = input_numerico("CPF do Cliente")
    if cpf == 'VOLTAR': return
    
    cliente = next((c for c in lista_clientes if c.cpf == cpf), None)
    if not cliente:
        print(" Erro: Cliente não encontrado!")
        input("\nEnter para continuar...")
        return

    venda = Venda(cliente, datetime.now().strftime("%d/%m/%Y %H:%M"))
    
    while True:
        limpar_tela()
        print(f"🛒 Venda: {cliente.nome} | Total: R${venda.valor_total:.2f}")
        id_p = input("\nID do Produto (ou 'S' para Finalizar, 'C' para Cancelar Venda): ").upper()
        
        if id_p == 'C':

            for item in venda.itens:
                item['prod'].qtd += item['qtd']
            print("\n Venda Cancelada e Estoque Restaurado!")
            input("\nEnter para continuar...")
            return
        
        if id_p == 'S': break
        
        prod = next((p for p in lista_produtos if p.id == id_p), None)
        if prod and prod.qtd > 0:
            try:
                q_input = input_numerico(f"Quantidade de {prod.nome} (Estoque: {prod.qtd})")
                if q_input == 'VOLTAR': continue
                q = int(q_input)
                
                if q <= prod.qtd:
                    prod.qtd -= q
                    venda.adicionar_item(prod, q)
                else:
                    print(" Estoque insuficiente!")
                    input("\nEnter para continuar...")
            except ValueError: pass
        else:
            print(" Produto não encontrado ou sem estoque!")
            input("\nEnter para continuar...")

    if venda.valor_total > 0:
        lista_vendas.append(venda)
        limpar_tela() 
        venda.exibir_nota_fiscal() 
    else:
        print("\nNota: Venda vazia.")
    input("\nPressione Enter para continuar...")

def estornar_ultima_venda():
    limpar_tela()
    print("--- ESTORNAR ÚLTIMA VENDA ---")
    if not lista_vendas:
        print("Nenhuma venda para estornar.")
    else:
        venda = lista_vendas.pop() # Remove a última
        for item in venda.itens:
            item['prod'].qtd += item['qtd'] # Devolve ao estoque
        print(f" Venda de R${venda.valor_total:.2f} estornada. Estoque atualizado!")
    input("\nEnter para continuar...")

def listar_clientes():
    limpar_tela()
    print("--- LISTA DE CLIENTES ---")
    for c in lista_clientes:
        print(f"Dono: {c.nome} | CPF: {c.cpf}")
        for p in c.pets:
            print(f"  └─ Pet: {p.nome} ({p.especie})")
    input("\nEnter para voltar...")

def listar_produtos():
    limpar_tela()
    print("--- 📦 ESTOQUE DE PRODUTOS ---")
    print(f"{'ID':<10} | {'NOME':<20} | {'PREÇO':<12} | {'QTD':<8}")
    print("-" * 55)
    for p in lista_produtos:
        aviso = "⚠️" if p.qtd < 20 else ""
        print(f"{p.id:<10} | {p.nome:<20} | R$ {p.preco:>8.2f} | {p.qtd:<8} {aviso}")
    input("\nEnter para voltar...")

def menu():
    while True:
        limpar_tela()
        print("================================")
        print("       PETSHOP SYSTEM          ")
        print("================================")
        print("1. Cadastrar Cliente/Pet")
        print("2. Remover Cliente")
        print("3. Cadastrar Produto")
        print("4. Realizar Venda")
        print("5. Estornar Última Venda")
        print("6. Listar Clientes")
        print("7. Listar Estoque")
        print("8. Histórico de Vendas")
        print("0. Sair")
        print("================================")
        
        op = input("\nEscolha: ")
        
        if op == "1": cadastrar_cliente()
        elif op == "2": remover_cliente()
        elif op == "3": cadastrar_produto()
        elif op == "4": realizar_venda()
        elif op == "5": estornar_ultima_venda()
        elif op == "6": listar_clientes()
        elif op == "7": listar_produtos()
        elif op == "8": 
            limpar_tela()
            for v in lista_vendas: print(f"{v.data} - {v.cliente.nome} - R${v.valor_total:.2f}")
            input("\nEnter para voltar...")
        elif op == "0": break

if __name__ == "__main__":
    popular_dados()
    menu()