idade_dias = int(input())

ano_mes_dia = [365, 30, 1]
resultado = []

for dias in ano_mes_dia:
    dias_anos = int(idade_dias/dias)
    resultado.append (dias_anos)
    idade_dias -= dias_anos*dias 

print (resultado [0], "ano(s)")
print (resultado [1], "mes(es)")
print (resultado [2], "dia(s)")
