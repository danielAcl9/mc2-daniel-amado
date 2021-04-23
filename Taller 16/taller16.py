datosX = [0, 1, 3, 5, 6, 8, 9, 12]
datosY = [14, 10, 12, 6, 8, 5, 4, 1]

n = len(datosX)

sumX = 0.0
sumY = 0.0
sumXY = 0.0
sumX2 = 0.0

xy = []
x2 = []

for x in range(len(datosX)):
    xy.append(x)
    x2.append(x)

for i in range(len(datosX)):
    xy[i]  = datosX[i]*datosY[i]
    x2[i] = datosX[i]**2
    sumX = sumX + datosX[i]
    sumY = sumY + datosY[i]
    sumXY = sumXY + xy[i]
    sumX2 = sumX2 + x2[i]
    promX = sumX / len(datosX)
    promY = sumY / len(datosY)

a1 = ((n * sumXY) - (sumX*sumY)) / ((n * sumX2)-(sumX)**2)

a0 = promY - a1*promX

#pruebas
print(f"Suma de X: {sumX}")
print(f"Suma de Y: {sumY}")
print(f"Suma de XY: {sumXY}")
print(f"Suma de X^2: {sumX2}")
print(f"Promedio X: {promX}")
print(f"Promedio Y: {promY}")

print("---------------")
print(f"Respuesta-> y = {a0} + {a1}x")
