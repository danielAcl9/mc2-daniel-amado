import math

def gauss(matIni): 
    #Método Gauss-Jordan
    val = len(matIni)
    matFin = []
    cont = 0
    for i in range(val):
        if matIni[i][i] == 0:
            cont2 = matIni[cont + 1]
            matIni[cont + 1] = matIni[cont]
            matIni[i] = cont2
        
        for j in range(val):
            if i != j:
                cont3 = matIni[j][i]/matIni[i][i]

                for k in range(val+1):
                    matIni[j][k] = matIni[j][k] - cont3 * matIni[i][k]
        cont += 1

    for i in range(val):
        matFin.append(matIni[i][val]/matIni[i][i])
    
    return matFin

datosX = [1, 3, 5, 7, 9, 11, 13]
datosY = [0.3, 0.7, 1.8, 3, 5, 7.2, 9.8]
n = len(datosX)

X2 = []
X3 = []
X4 = []
XY = []
X2Y = []
#-----------------------------
sumX = 0.0
sumY = 0.0
sumX2 = 0.0
sumX3 = 0.0
sumX4 = 0.0
sumXY = 0.0
sumX2Y = 0.0

promY = 0.0

for i in range(n):
    X2.append(datosX[i]**2)
    X3.append(datosX[i]**3)
    X4.append(datosX[i]**4)
    XY.append(datosX[i] * datosY[i])
    X2Y.append(X2[i] * datosY[i])
    #----------------------
    sumX = sumX + datosX[i]
    sumY = sumY + datosY[i]
    sumX2 = sumX2 + X2[i]
    sumX3 = sumX3 + X3[i]
    sumX4 = sumX4 + X4[i]
    sumXY = sumXY + XY[i]
    sumX2Y = sumX2Y + X2Y[i]

promY = sumY / n

varMat = [[n, sumX ,sumX2, sumY],
     [sumX, sumX2, sumX3, sumXY],
     [sumX2, sumX3, sumX4, sumX2Y]]

final = gauss(varMat)

print("Sistema de Ecuaciones Lineales: \n" + 
        f"{n}a0 + {sumX}a1 + {sumX2}a2 = {sumY}\n" + 
        f"{sumX}a0 + {sumX2}a1 + {sumX3}a2 = {sumXY}\n" + 
        f"{sumX2}a0 + {sumX3}a1 + {sumX4}a2 = {sumX2Y}\n")

#Variables
a0 = final[0]
a1 = final[1]
a2 = final[2]

print("Se resuelve por Gauss-Jordan\n" + 
        f"a0 = {a0}\n" + 
        f"a1 = {a1}\n" + 
        f"a2 = {a2}\n")


print("Ecuación de la línea:\n" + 
      f"y = {a0} + {a1}x + {a2}x^2")

#Desviación Estándar
sy = 0.0
st = 0.0

for i in range(n):
    st = st + (datosY[i]-promY)**2

sy = math.sqrt(st / (n - 1))

print("-----------------------------")
print(f"Desviación Estándar = {sy}")

#Error Estándar
syx = 0.0
sr = 0.0

for i in range(n):
    sr = sr + (datosY[i] - a0 - a1*datosX[i]-a2*X2[i])**2

syx = math.sqrt(sr / ((n - 3)))

print(f"Error estándar = {syx}")

if syx < sy:
    print("El modelo es adecuado")
else:
    print("El modelo no es adecuado")

#Coeficiente de Relación
r = 0.0

r = (((st - sr)/st)**0.5)*100
r2 = round(r, 2)

print(f"Coeficiente de Relación = {r2} %")