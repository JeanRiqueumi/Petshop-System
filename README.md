 PetShop System - Gerenciador de Vendas e Clientes
Um sistema robusto de linha de comando (CLI) desenvolvido em Python para gestão completa de um PetShop. O projeto aplica conceitos avançados de Programação Orientada a Objetos (POO), garantindo modularidade e fácil manutenção.

 Principais Funcionalidades
Gestão de Clientes e Pets: Cadastro de proprietários com validação de CPF e vínculo direto com múltiplos pets.

Controle de Estoque Inteligente: * Listagem com alertas visuais (⚠️) para produtos com estoque baixo (menos de 20 unidades).

Baixa automática de estoque no momento da venda.

Fluxo de Vendas Completo:

Interface de venda interativa com subtotal em tempo real.

Opção de cancelamento de venda antes da finalização.

Emissão de Nota Fiscal detalhada.

Segurança de Dados: * Sistema de estorno da última venda (undo) com devolução automática de itens ao estoque.

Validação rigorosa de entradas numéricas e formatação de CPF/Telefone.

🛠️ Tecnologias e Conceitos Aplicados
Linguagem: Python 3.x

Arquitetura: Modular (Classes separadas por responsabilidade).

Conceitos de POO: Encapsulamento, Composição (Cliente possui Pets) e Listas de Objetos.

UX no Terminal: Limpeza de tela dinâmica (cls/clear) e navegação facilitada com opção de "Voltar".

📂 Estrutura de Arquivos
Para o pleno funcionamento, o projeto está organizado da seguinte forma:

main.py: Ponto de entrada do sistema e gerenciamento de menus.

cliente.py: Definição das classes Cliente e Pet.

produto.py: Definição da classe Produto e lógica de estoque.

venda.py: Lógica de processamento de itens, totalizadores e nota fiscal.

🔧 Como Testar
Clone o repositório:

Bash
git clone https://github.com/seu-usuario/petshop-system.git
Acesse a pasta do projeto:

Bash
cd petshop-system
Execute o script principal:

Bash
python main.py

Desenvolvido por: Jean Canova - 1137244 e Marcos Ferreira - 1137201.
