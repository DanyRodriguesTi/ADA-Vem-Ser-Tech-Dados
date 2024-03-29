# Sistema de Cadastro

Tua missão é construir um sistema de cadastro de pessoas. Ele precisará atender aos seguintes requisitos:


## Menu principal
Ao iniciar o programa o seguinte menu deve ser imprimido:

```
Boas vindas ao nosso sistema:

1 - Inserir usuário
2 - Excluir usuário
3 - Atualizar usuário
4 - Informações de um usuário
5 - Informações de todos os usuários
6 - Sair

```

### Inicialização

O programa deve iniciar lendo um arquivo com usuários já cadastrados - recomenda-se ter uma função dedicada apenas a ler e a salvar o arquivo.

### 1 - Inserir usuário
Você deverá criar uma função que recebe as seguintes informações: _nome_, _tefone_ e _endereço_.

Detalhes... Em sistemas de cadastro é convencionado adicionar automaticamente as seguintes informações:
- _id_: um número inteiro aleatório ou incremental que identifica um usuário (o id não pode se repetir);
- _status_: um valor booleano que indica se o usuário está ativo ao não. Por padrão esse valor é True

Além disto, a sua função que adiciona usuários no sistema deve ser capaz de receber um número N de cadastros de uma só vez e, também, caso algum campo não seja enviado, um valor padrão (*default*) deve ser utilizado. O único campo que deve ser obrigatório é o nome, o telefone e o endereço, caso o usuário não coloque no cadastro, o valor *Nao Informado* deve ser colocado em seu lugar.

Caso o usuário tente inserir um cadastro que já existe, mas está desativado (mesmo nome, telefone e endereço), o sistema deve apenas tornar o cadastro antigo *True*, e não criar um novo cadastro.

### 2 - Excluir usuário
Bem aqui vamos usar o _id_ e o _status_. Em sistemas em produção é evitado ao máximo a aplicação de *delete*, *remove* ou qualquer outra função que apague em definitivo um dado. 

Para isso usamos o que é chamado de _Exclusão Lógica_. Que em síntese muda o _status_ do usuário de *True* para *False*.

Você receberá do usuário o _id_ de um outro usuário dentro da base, e por fim vai alterar o valor do _status_ de True para False.

Caso o _id_ digitado não estiver dentro da base imprima uma mensagem de erro e peça novamente o _id_. Exemplo:
```
Usuário não encontrado!

Insira o ID do usuário:
```

Aqui, igualmente à adição de usuário, deve ser criada uma função dedicada apenas à exclusão, e esta função deve ser capaz de receber um número qualquer de *IDs* para fazer a exclusão lógica dos mesmos.

### 3 - Atualizar usuário
Ao selecionar essa opção você deverá pedir o _id_ de um usuário:

```
Insira o ID do usuário:
```

Caso o _id_ digitado não estiver dentro da base imprima uma mensagem de erro e peça novamente o _id_. Exemplo:
```
Usuário não encontrado!

Insira o ID do usuário:
```

Ao inseri um _id_ correto imprima o seguinte sub menu:
```
Qual informação deseja alterar?
1 - Nome
2 - Tefone
3 - Endereço
```
E ao escolher a opção peça a nova informação da seguinte forma:

```
1
Insira o nome:
```

Aqui, igualmente à adição de usuário, deve ser criada uma função dedicada apenas à atualização cadastral, e esta função deve ser capaz de receber um número qualquer de *IDs* para fazer a alteração de cada um em sequência.


## 4 - Exibir informações de um usuário
Ao selecionar essa opção imprima o seguinte sub menu:
```
4
Insira o ID do usuário:
```

E deverá ser inserido o _id_ do usuário que deseja imprimir.
Se o _id_ inserido não for encontrado na base imprima uma mensagem de erro e peça o _id_ novamente. Exemplo:
```
Usuário não encontrado!

Insira o ID do usuário:
```

No momento que inserir um ID válido imprimir:

```
Nome: João da Silva
Tefone: 2345678
Endereço: Rua sete
```

Aqui, igualmente à adição de usuário, deve ser criada uma função dedicada apenas à exibição das informações, e esta função deve ser capaz de receber um número qualquer de *IDs* para fazer a exibição dos dados.

### 5 - Informações de todos os usuários
Ao selecionar essa opção imprima as informações de todos os usuários

```
ID: 1
Nome: João da Silva
Tefone: 2345678
Endereço: Rua sete

ID: 2
Nome: Maria Aparecida
Tefone: 2345678
Endereço: Rua cinco

ID: 3
Nome: Alceu Maroto
Tefone: 2345678
Endereço: Avenida trinta e um
```

Novamente uma função deve ser criada exclusivamente para isto. Esta função vai apenas verificar quais *IDs* estão com o *status* ativo e exibir na tela estes *IDs*. Isto pode ser feito aproveitando da função anterior também!

### 6 - Sair

Encerre o programa.

Aqui, o arquivo que foi lido inicialmente para começarmos o projeto já com cadastros na abse deve ser sobrescrito com o novo arquivo com as novas modificações feitas pelo sistema!

Recomenda-se que a função lá do início, criada para ler este arquivo, também seja capaz de salvá-lo ao final atualizado - por simplicidade.


## Observações
- A cada vez que você encerrar uma operação do programa imprima novamente o menu principal;
- O sistema deverá iniciar com uma lista predefinida de CINCO (5) usuários que deverá ser lida do arquivo enviado juntamente com este trabalho. Ou seja, o programa não começará do zero, já deve iniciar com usuários no sistema;
- Usem somente estruturas e técnicas que vimos nas aulas.

## Exemplos


### Função para ler/salvar o arquivo

```py
def lerSalvarArquivo(ler=True, nomeArquivo='projetoModuloII.json'):
    if ler:
        # Criar o passo-a-passo para ler o arquivo e retornar para a função principal o arquivo lido
    else:
        # Criar o passo-a-passo para salvar o arquivo e não é necessário retornar nada
```


### Função para adicionar usuários

```py
def addUsuario(**usuario):
```

### Função para excluir usuários

```py
def excluirUsuario(*ids):
```

### Função para editar usuários

```py
def editUsuario(*ids):
```

### Função para exibir alguns usuários

```py
def exibirAlgunsUsuarios(*ids):
```

### Função para exibir todos os usuários

```py
def exibirTodosUsuarios():
```

### Função para encerrar o programa

```py
def encerrarPrograma(arquivo, nomeArquivo='projetoModuloII.json'):
```

### Cabeçalho-exemplo

```py
menu_str = """
\nBoas vindas ao nosso sistema:

1 - Inserir usuário
2 - Excluir usuário
3 - Atualizar usuário
4 - Informações de um usuário
5 - Informações de todos os usuários
6 - Sair\n
"""

sub_menu = """
\nQual informação deseja alterar?
1 - Nome
2 - Tefone
3 - Endereço
\n
"""
```

- Obs.: Estes códigos e funções são apenas sugestões! Vocês podem colocar o nome que quiserem e receber os argumentos que quiserem. A única exigência é que exista uma função dedicada a cada etapa do projeto!

- Dica: O uso de dicionários vai ajudar muito neste projeto, inclusive o formato de arquivo *.json* é compatível em formato com o dicionário!
