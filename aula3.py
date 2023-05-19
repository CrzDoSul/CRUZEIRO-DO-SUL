# Variáveis:
# é onde o programa armazena e opera diversos tipos de dados que serão usados ao longo da execução do programa.
# Como o próprio nome diz, os dados podem ser alterados(variar) durante a execução do programa. 
# A tipagem de dados em Python é dinâmica, isto é, não precisamos especificar o tipo de dados quando declaramos uma variável.
# variáveis são declaradas assim:
# nome_da_variavel = valor
# O operador "=" é de atribuição, ele coloca o valor na variável.
# O nome das variáveis podem conter: letras, números e underline_
# O nome das variáveis NÃO podem conter: palavras reservadas(and, if, else, elif, ...), começar com números ou caracteres especiais  

# atribuindo os valores 5 e 10 as variáveis
var1 = 5 
var2 = 10 

# também podemos fazer operações entre as variáveis.
# os valores contidos nas variáveis 'var1' e 'var2' são somados e depois são guardados na variável 'soma'
soma = var1 + var2
print("A soma de", var1, "+", var2, "=", soma)

# Quando uma variável é declarada, um espaço na memória é reservado para armazenar os dados que serão guardados nela.
# Esse espaço reservado tem um endereço na memória, mas podemos usar acessar esse dado guardado na variável através do seu nome.
print("endereço da variável(var1) na memória:", id(var1))
print("endereço da variável(var2) na memória:", id(var2))
print("endereço da variável(soma) na memória:", id(soma))