area = input().split()

A = float(area[0])
B = float(area[1])
C = float(area[2])
PI = float(3.14159)

area_triangulo_retangulo = A*C/2
area_circulo = PI*C**2
area_trapezio = (A+B)*C/2
area_quadrado = B**2
area_retangulo = A*B

print("TRIANGULO: %.3f" %area_triangulo_retangulo)
print("CIRCULO: %.3f" %area_circulo)
print("TRAPEZIO: %.3f" %area_trapezio)
print("QUADRADO: %.3f" %area_quadrado)
print("RETANGULO: %.3f" %area_retangulo)