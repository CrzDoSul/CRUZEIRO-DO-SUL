# TIPOS DE DADOS
# Os tipos de dados mais comuns são:
# int, float, bool e str. Existem outros, mas os mais comuns são esses!

# int - são os números inteiros
# números inteiro(...-3,-2,-1,0,1,2,3,...)
print(type(45))
print(type(-15))
print(45 + (-15))

# float - são os números reais
# são aqueles dados que possuem parte fracionária(3.14, 7.0, 5.5, etc...)
print(type(3.14))
print(type(1.52))
print(3.14 + 1.52)

# str - é o tipo string. Strings são uma cadeia de carecteres, um pedaço de texto. 
# Letras, números e caracteres especiais podem ser tipados como str.
print(type("Olá Mundo"))
print(type("7"))
print(type("True"))
print(type("!"))
# não é possível operar aritiméticamente(fazer contas) dados 
# com tipagem de string, mesmo que esses dados sejam números. 
print("70"+"8") # os números nesse caso são concatenados(juntados) em vez de somados.

# bool ou boolean apenas assumir dois valores: verdadeiro ou falso. 
# na lógica computacional também pode assumir 0 ou 1
print(type(True))
print(type(False))