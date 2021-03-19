import math

e = math.e
valorAprox = 0
xi = 0.75
x = 0.005

valorReal = 0.47001061473053796

for i in range(16):
    if(i%2 == 0):
        valorAprox += (e**(-xi))*(x**i)/math.factorial(i)
    else:
        valorAprox -= (e**(-xi))*(x**i)/math.factorial(i)

    error = (abs(valorAprox - valorReal) / valorReal)*100
    print("Valor aproximado (" + str(i) + "): " + str(valorAprox))
    print("Porcentaje de Error: " + str(error) + "%")

print("Valor final calculado " + str(valorAprox))


