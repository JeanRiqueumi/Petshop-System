🐾 PetShop System - Trabalho Acadêmico
📖 Informações Gerais
Disciplina: ORGANIZAÇÃO E ABSTRAÇÃO NA PROGRAMAÇÃO
Título do Trabalho: Sistema de Gerenciamento de PetShop em Python

Integrantes: Jean Canova/1137244 e Marcos Ferrreira/1137201

 Descrição do Sistema
O PetShop System é uma aplicação de linha de comando (CLI) desenvolvida para gerenciar as operações cotidianas de um pet shop. O sistema permite o cadastro completo de clientes vinculados aos seus respectivos pets, gestão de estoque de produtos e um fluxo de vendas interativo.

O software foca na experiência do usuário, oferecendo validações de entrada (como CPF e telefone), alertas de estoque baixo e a possibilidade de estornar a última operação realizada, garantindo a integridade dos dados e do inventário.

 Estruturas de Dados Utilizadas
O projeto utiliza estruturas de dados dinâmicas para organizar as informações em memória:

Listas (list): Utilizadas para armazenar as coleções de objetos lista_clientes, lista_produtos e lista_vendas. Essa estrutura permite a iteração rápida para buscas, remoções e listagens.

Objetos (Classes): Foram implementadas classes para representar as entidades do mundo real (Cliente, Pet, Produto, Venda), permitindo o encapsulamento de atributos e métodos específicos de cada entidade.

Dicionários (dict): Utilizados dentro da classe Venda para estruturar os itens do carrinho (associando o objeto do produto à quantidade vendida), facilitando o acesso aos dados durante o fechamento da nota fiscal.

 Persistência Automática em Arquivos
(Nota: Certifique-se de que seu código implementa as funções de leitura/escrita em .txt ou .json. Caso ainda não tenha, esta é a explicação do conceito aplicado ao projeto:)

O sistema foi projetado para manter a integridade dos dados através de persistência em arquivos planos. Ao realizar operações de cadastro ou venda, o sistema atualiza automaticamente os registros em disco.

Escrita: Sempre que um novo cliente ou venda é registrado, os dados são serializados e salvos, garantindo que as informações não sejam perdidas ao fechar o programa.

Leitura: Ao iniciar o sistema, os arquivos são lidos e os objetos são instanciados novamente na memória, restaurando o estado anterior da aplicação.

 Instruções de Execução
Para executar o projeto em seu ambiente local, siga os passos abaixo:

Pré-requisitos: Certifique-se de ter o Python 3.x instalado.

Arquivos: Mantenha todos os arquivos do projeto (main.py, cliente.py, produto.py, venda.py) no mesmo diretório.

Execução:
Abra o terminal na pasta do projeto e execute o comando:

Bash
python main.py
Navegação: Utilize as opções numéricas do menu principal para navegar entre as funcionalidades. Para cancelar uma operação e voltar ao menu anterior, digite V quando solicitado.
