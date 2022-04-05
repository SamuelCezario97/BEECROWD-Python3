A = 11
B = 11

while A > 10.0:
    A = float(input())
    A = round(A, 1)
    if A <= 10:
        A = A*3.5/11
while B > 10.0:
    B = float(input())
    B = round(B, 1)
    if B <= 10:
        B = B*7.5/11
MEDIA = B + A

if MEDIA > 10:
    MEDIA = 10

print ("MEDIA = %.5f" %MEDIA)