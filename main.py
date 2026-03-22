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
    menu()