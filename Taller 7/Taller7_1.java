import java.util.Scanner;

import org.graalvm.compiler.debug.CloseableCounter;

import java.util.Scanner;

public class Taller7_1 {
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
      
        System.out.println("Digite el valor");
        double value = sc.nextDouble();

        double error_esperado = (0.5 * Math.pow(10, -7)) * 100;
        double error_aproximado = 100;
        int count = 0;
        int power = 0;

        double x = 0;
        double y = 0;

        do{

            if(count%2==0){

                y = x;
                x = x + Math.pow(value, power)/factorial(power);
                count++;
                power++;
            } else {

                y = x;
                x = x - Math.pow(value, power)/factorial(power);
                count++;
                power++;
            }

            //calculo del error
            error_aproximado = Math.abs(( x - y ) / x ) * 100;

            System.out.println("----------------------------------------------------------");
            System.out.println("La iteracion actual es: " + count);
            System.out.println("El valor de la iteracion #" + count+ " es: " + x);
            System.out.println("Su error aproximado es: " + error_aproximado);
            System.out.println("----------------------------------------------------------");
            System.out.println("\n\n");

        } while (error_aproximado > error_esperado);

    }

    private static double factorial(int n)
    {   
        double rta = 1;
        for (int i = 2; i <= n; i++)
        {
            rta *= i;
        }

        return rta;
    }
}
