segundos = int (input())

formatohoras = [3600, 60, 1]
resultado = []

for hora_minuto_segundo in formatohoras:
    tempo = int(segundos/hora_minuto_segundo)
    segundos -= tempo*segundos
    resultado.append (tempo)

print ("{}:{}:{}".format(resultado[0],resultado[1],resultado[2]))
