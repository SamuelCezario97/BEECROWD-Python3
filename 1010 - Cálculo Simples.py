peca1 = input().split()
codigo1 = int(peca1[0])
unidade1 = int(peca1[1])
valor_unidade1 = float(peca1[2])

peca2 = input().split()
codigo2 = int(peca2[0])
unidade2 = int(peca2[1])
valor_unidade2 = float(peca2[2])

valor_total = unidade1*valor_unidade1+unidade2*valor_unidade2

print("VALOR A PAGAR: R$ %.2f" %valor_total)