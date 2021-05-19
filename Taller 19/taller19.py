import math

datosX = [1, 3, 5, 7, 9, 11, 13]
datosY = [0.3, 0.7, 1.7, 3.5, 5.5, 27.5, 38.5]
n = len(datosX)

XY = []
X2 = []

sumX = 0.0
sumY = 0.0
sumXY = 0.0
sumX2 = 0.0
promX = 0.0
promY = 0.0


for i in range(len(datosX)):
    X2.append(datosX[i]**2)
    XY.append(datosX[i]*datosY[i])
    #-------------------
    sumX = sumX + datosX[i]
    sumY = sumY + datosY[i]
    sumXY = sumXY + XY[i]
    sumX2 = sumX2 + X2[i]
    promX = sumX / len(datosX)
    promY = sumY / len(datosY)


a1 = ((n * sumXY) - (sumX*sumY)) / ((n * sumX2)-(sumX)**2)

a0 = promY - a1*promX

#print("Suma X = " + sumX)
#print("Suma X^2 = " + sumX2)
#print("Promedio de X = " + promX)
#print()

print("----- Regresión por Mínimo Cuadrado -----")
print(f"Respuesta-> y = {a0} + {a1}x")

# Desviación Estándar
sy = 0.0
st = 0.0

for i in range(len(datosX)):
    st = st + (datosY[i]-promY)**2

sy = math.sqrt(st / len(datosX) - 1)

print(f" Desviación Estándar (Sy) = {sy}")

# Error Estándar
syx = 0.0
sr = 0.0

for i in range(len(datosX)):
    sr = sr + (datosY[i] - a0 - a1*datosX[i])**2

syx = math.sqrt(sr / 5)

print(f"Error estándar = {syx}")

if syx < sy:
    print("El modelo es adecuado")
else:
    print("El modelo no es adecuado")

#Coeficiente de Relación
r = 0.0

r = (math.sqrt((st - sr)/st)*100)
r2 = round(r, 2)

print(f"Coeficiente de Relación = {r2} %")