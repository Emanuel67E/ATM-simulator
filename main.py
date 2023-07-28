print("Quanto deseja sacar?")
saque = int(input())

while saque < 10 or saque > 600:
    print("Insira um valor valido")
    saque = int(input())

notas = [0, 0, 0, 0, 0]

while saque > 0:
    if saque >= 100:
        notas[0] += 1
        saque -= 100
    elif saque >= 50:
        notas[1] += 1
        saque -= 50
    elif saque >= 10:
        notas[2] += 1
        saque -= 10
    elif saque >= 5:
        notas[3] += 1
        saque -= 5
    elif saque >= 1:
        notas[4] += 1
        saque -= 1

print(f"{notas[0]} notas de 100")
print(f"{notas[1]} notas de 50")
print(f"{notas[2]} notas de 10")
print(f"{notas[3]} notas de 5")
print(f"{notas[4]} moedas de 1")