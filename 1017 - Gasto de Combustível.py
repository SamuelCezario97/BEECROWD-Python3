valor_entrada = int(input())

notas100 = int(valor_entrada/100)
valor = valor_entrada - (notas100*100)

notas50 = int(valor/50)
valor = valor - (notas50*50)

notas20 = int(valor/20)
valor = valor - (notas20*20)

notas10 = int(valor/10)
valor = valor - (notas10*10)

notas5 = int(valor/5)
valor = valor - (notas5*5)

notas2 = int(valor/2)
valor = valor - (notas2*2)

notas1 = int(valor/1)

print (valor_entrada)
print (notas100, "nota (s) de R$ 100,00")
print (notas50, "nota (s) de R$ 50,00")
print (notas20, "nota (s) de R$ 20,00")
print (notas10, "nota (s) de R$ 10,00")
print (notas5, "nota (s) de R$ 5,00")
print (notas2, "nota (s) de R$ 2,00")
print (notas1, "nota (s) de R$ 1,00")