class Venda:
    def __init__(self, cliente, data):
        self.cliente = cliente
        self.data = data
        self.itens = []
        self.valor_total = 0.0

    def adicionar_item(self, produto, qtd):
        self.itens.append({"prod": produto, "qtd": qtd})
        self.valor_total += produto.preco * qtd

    def exibir_nota_fiscal(self):
        print("\n" + "="*40)
        print("          NOTA FISCAL - PET SHOP")
        print("="*40)
        print(f"Data: {self.data}")
        print(f"Cliente: {self.cliente.nome}")
        print(f"CPF: {self.cliente.cpf}")
        print("-" * 40)
        print(f"{'PRODUTO':<20} | {'QTD':<5} | {'SUBTOTAL':<10}")
        
        for item in self.itens:
            p = item["prod"]
            q = item["qtd"]
            subtotal = p.preco * q
            print(f"{p.nome[:20]:<20} | {q:<5} | R$ {subtotal:>8.2f}")
            
        print("-" * 40)
        print(f"TOTAL A PAGAR:           R$ {self.valor_total:>8.2f}")
        print("="*40)
        print("      Obrigado pela preferência! 🐾")
        print("="*40)