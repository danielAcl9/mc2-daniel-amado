import sys
def main():
    val = 4
    matIni = [[0 for columns in range(val+1)] for rows in range(val)]
    matFin = [0 for i in range(val)]

    matIni = [[2, 1, 4, -4, -1], [5, 5, 3, -2, 3], [2, 2, -1, 0, 9], [0, 5, -2, 1, 11]]
    
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