import sys
def main():
    val = int(input("Ingrese la cantidad de valores desconocidos: "))
    matIni = [[0 for columns in range(val+1)] for rows in range(val)]
    matFin = [0 for i in range(val)]

    #Llenando la matriz inicial
    for i in range(val):
        for j in range(val+1):
            print(f"Ingrese el valor de la matriz a despejar M[{i}][{j}]")
            matIni[i][j] = float(input())
    
    #Método Gauss-Jordan
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
        matFin[i] = matIni[i][val]/matIni[i][i]

    #Resultados
    print("\n\n Resultado final: \n")
    for i in range(val):
        print(f"matFin{i} = {matFin[i]}")

if __name__ == '__main__':
    main()