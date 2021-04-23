import math
datosX = [2, 3, 4, 5, 6, 7, 8, 9, 10]
datosY = [1, 1.2, 1.5, 2.1, 2.8, 3.8, 5, 6.5, 8.5]
n = len(datosX)

#----- Regresión Lineal -----

sumX = 0.0
sumY = 0.0
sumXY = 0.0
sumX2 = 0.0

xy = []
x2 = []   

for i in range(len(datosX)):
    xy.append(datosX[i]*datosY[i])
    x2.append(datosX[i]**2)
    sumX = sumX + datosX[i]
    sumY = sumY + datosY[i]
    sumXY = sumXY + xy[i]
    sumX2 = sumX2 + x2[i]
    promX = sumX / len(datosX)
    promY = sumY / len(datosY)

a1 = ((n * sumXY) - (sumX*sumY)) / ((n * sumX2)-(sumX)**2)

a0 = promY - a1*promX

print("----- Respuesta Regresión Lineal -----")
print(f"y = {a0} + {a1}x")

#----- Regresión Exponencial -----

sumX = 0.0
sumX2 = 0.0
sumXLnY = 0.0
sumLnY = 0.0

x2 = []
LnY = []
XLnY = []

for i in range(len(datosX)):
    x2.append(datosX[i]**2)
    LnY.append(math.log(datosY[i]))
    XLnY.append(datosX[i]*LnY[i])
    sumX = sumX + datosX[i]
    sumX2 = sumX2 + x2[i]
    promX = sumX / n
    sumLnY = sumLnY + LnY[i]
    sumXLnY = sumXLnY + XLnY[i]

promLnY = sumLnY / len(datosY)

a1 = ((n * sumXLnY) - (sumX*sumLnY)) / ((n * sumX2) - math.pow(sumX, 2))
a0 = promLnY - a1*promX
alpha = math.pow(math.e, a0)
beta = a1

print("----- Respuesta Modelo Exponencial -----")
print(f"y = {alpha} * e^{beta}x")

#----- Ecuación de Potencias -----

sumLogX = 0.0
sumLogY = 0.0
sumLogX_LogY = 0.0
sumLogX2 = 0.0

LogX = []
LogY = []
LogX_LogY = []
LogX2 = []

for i in range(len(datosX)):
    LogX.append(math.log10(datosX[i]))
    LogY.append(math.log10(datosY[i]))
    LogX_LogY.append(LogX[i]*LogY[i])
    LogX2.append(math.pow(LogX[i], 2))
    #------------------------------
    sumLogX = sumLogX + LogX[i]
    sumLogY = sumLogY + LogY[i]
    sumLogX_LogY = sumLogX_LogY + LogX_LogY[i]
    sumLogX2 = sumLogX2 + LogX2[i]

promLogX = sumLogX / n
promLogY = sumLogY / n

a1 = ((n * sumLogX_LogY) - (sumLogX * sumLogY) ) / ((n * sumLogX2) - math.pow(sumLogX, 2))
a0 = promLogY - (a1 * promLogX)
alpha = math.pow(10, a0)
beta = a1

print("----- Respuesta Modelo Ecuación de Potencias -----")
print(f"y = {alpha} * x^{beta}")

#----- Razón de Crecimiento -----

sum1X = 0.0
sum1Y = 0.0
sum1X1Y = 0.0
sum1X2 = 0.0

X = []
Y = []
XY = []
X2 = []

for i in range(len(datosX)):
    X.append(1/datosX[i])
    Y.append(1/datosY[i])
    XY.append(X[i] * Y[i])
    X2.append(math.pow(X[i], 2))
    #------------------------
    sum1X = sum1X + X[i]
    sum1Y = sum1Y + Y[i]
    sum1X1Y = sum1X1Y + XY[i]
    sum1X2 = sum1X2 + X2[i]

prom1X = sum1X / n
prom1Y = sum1Y / n

a1 = ((n * sum1X1Y) - (sum1X * sum1Y)) / ((n * sum1X2) - math.pow(sum1X, 2))
a0 = prom1Y - (a1 * prom1X)

alpha = 1 / a0
beta = a1 / a0

print("----- Respuesta Razón de Cambio -----")
print(f"y = {alpha} * (x / {beta} + x)")