A = 11
B = 11
C = 11

while A > 10.0:
    A = float(input())
    A = round(A, 1)
    if A <= 10:
        A = A*2/10
while B > 10.0:
    B = float(input())
    B = round(B, 1)
    if B <= 10:
        B = B*3/10
while C > 10.0:
    C = float(input())
    C = round(C, 1)
    if C <= 10:
        C = C*5/10
MEDIA = C + B + A

print ("MEDIA = %.1f" %MEDIA)