numero_funcionario = int(input())
horas_trabalhadas = int(input())
valor_horas = float(input())
valor_horas = round(valor_horas, 2)

salario = horas_trabalhadas*valor_horas
salario = round(salario, 2)

print ("NUMBER =", numero_funcionario)
print ("SALARY = U$ %.2f" %salario)