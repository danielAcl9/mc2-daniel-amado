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

dx1 = [0, 0, 1, 2, 0, 1, 2, 2]
dx2 = [0, 1, 1, 2, 2, 3, 3, 1]
dy = [3.2, 6, 2.2, 2.4, 6.4, 6.6, 3.4, 0.2]
n = len(dx1)

x1_2 = []
x1x2 = []
x2_2 = []
x1y = []
x2y = []
#---------
sumx1 = 0.0
sumx2 = 0.0
sumy = 0.0
sumx1_2 = 0.0
sumx1x2 = 0.0
sumx2_2 = 0.0
sumx1y = 0.0
sumx2y = 0.0

for i in range(n):
    x1_2.append(dx1[i]**2)
    x1x2.append(dx1[i] * dx2[i])
    x2_2.append(dx2[i]**2)
    x1y.append(dx1[i] * dy[i])
    x2y.append(dx2[i] * dy[i])
    #-----------------------------
    sumx1 = sumx1 + dx1[i]
    sumx2 = sumx2 + dx2[i]
    sumy = sumy + dy[i]
    sumx1_2 = sumx1_2 + x1_2[i]
    sumx1x2 = sumx1x2 + x1x2[i]
    sumx2_2 = sumx2_2 + x2_2[i]
    sumx1y = sumx1y + x1y[i]
    sumx2y = sumx2y + x2y[i]

varMat = [[n, sumx1 ,sumx2, sumy],
     [sumx1, sumx1_2, sumx1x2, sumx1y],
     [sumx2, sumx1x2, sumx2_2, sumx2y]]

final = gauss(varMat)

print("Sistema de Ecuaciones Lineales: \n" + 
        f"{n}a0 + {sumx1}a1 + {sumx2}a2 = {sumy}\n" + 
        f"{sumx1}a0 + {sumx1_2}a1 + {sumx1x2}a2 = {sumx1y}\n" + 
        f"{sumx2}a0 + {sumx1x2}a1 + {sumx2_2}a2 = {sumx2y}\n")

a0 = final[0]
a1 = final[1]
a2 = final[2]

print("Se resuelve por Gauss-Jordan\n" + 
        f"a0 = {a0}\n" + 
        f"a1 = {a1}\n" + 
        f"a2 = {a2}\n")

print("Se construye la función lineal múltiple\n" + 
        f"y = {a0} + {a1}x + {a2}x2\n")

st = 0.0
sr = 0.0
promy = sumy / n

for i in range(n):
    st = st + (dy[i] - promy)**2
    sr = sr + ((dy[i] - a0 - a1*dx1[i] - a2*dx2[i])**2)

sy = math.sqrt(st / (n - 1))
syx = math.sqrt(sr / (n - (2+1)))
r = (math.sqrt((st - sr) / st) * 100)
r2 = round(r, 2)

if syx < sy:
    print("El modelo es adecuado\n")
else:
    print("El modelo no es adecuado\n")

print("Desviación Estándar\n" + 
        f"sy = {sy}\n" + 
        "Error Estándar\n" + 
        f"sy/x = {syx}\n" + 
        "Coeficiente de Correlación\n" + 
        f"r = {r2}%")