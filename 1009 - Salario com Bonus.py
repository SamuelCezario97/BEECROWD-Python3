nome_vendedor = str(input())

salario_fixo = float(input())
salario_fixo = round(salario_fixo, 2)

dinheiro_vendas = float(input())
dinheiro_vendas = round(dinheiro_vendas, 2)

comissao = dinheiro_vendas*15/100
total = comissao+salario_fixo
total = round(total, 2)

print ("TOTAL = R$ %.2f" %total)