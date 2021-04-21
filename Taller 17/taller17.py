import math

datosX = [1.2, 2.4, 3.6, 4.8, 6, 7]
datosY = [0.8, 1, 1.5, 2, 2.9, 3.6]
n = len(datosX)

sumX = 0.0
sumX2 = 0.0
#------------------
sumXLnY = 0.0
sumLnY = 0.0

x2 = []
LnY = []
XLnY = []

for i in range(len(datosX)):
    x2.append(datosX[i]**2)
    LnY.append(math.log(datosY[i]))
    XLnY.append(datosX[i]*LnY[i])
    #-------------------
    sumX = sumX + datosX[i]
    sumX2 = sumX2 + x2[i]
    promX = sumX / len(datosX)
    sumLnY = sumLnY + LnY[i]
    sumXLnY = sumXLnY + XLnY[i]

promLnY = sumLnY / len(datosY)

a1 = ((n * sumXLnY) - (sumX*sumLnY)) / ((n * sumX2)-(sumX)**2)

a0 = promLnY - a1*promX

print("----- Regresión por Mínimo Cuadrado -----")
print(f"Respuesta-> y = {a0} + {a1}x")

alpha = math.pow(math.e, a0)
beta = a1

print("----- Modelo Exponencial -----")
print(f"Respuesta-> y = {alpha}e^{beta}x")
