print("Sequência de Fibonacci")
num = int(input("Digite quantos termos da sequência o programa deve calcular: "))

fibonacci = [1,1]
count = 0
while (count < num):
    fibonacci.append(fibonacci[count] + fibonacci[count+1]) #criação do proximo termo
    count += 1 #incremento do contador

for i in range(num): #mostrar elementos
    print(fibonacci[i])