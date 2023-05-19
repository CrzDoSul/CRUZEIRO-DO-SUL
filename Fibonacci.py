print("Sequência de Fibonacci")
num = int(input("Digite quantos termos da sequência o programa deve calcular: "))

fibonacci = [1,1]
count = 0
while (count < num):
    if num > 2:
        fibonacci.append(fibonacci[count] + fibonacci[count+1]) #criação dos termos seguintes   
    count += 1 #incremento do contador

#Retirar termos de acordo com a situação - Precisei usar isso pois o array inicia startado com 2 termos [1, 1] - gambiarra!
if (num == 1):
    fibonacci.pop()
elif(num >=3):
    fibonacci.pop()
    fibonacci.pop()

print(fibonacci)