import java.util.Scanner;


public class Taller7_2 {
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
        double z = 0;

        do{

            y = z; 
            x = x + Math.pow(value, power)/factorial(power);
            z = 1/x;
           
            count++;
            power++;

            error_aproximado = Math.abs(( z - y ) / z ) * 100;

            System.out.println("----------------------------------------------------------");
            System.out.println("La iteracion actual es: " + count);
            System.out.println("El valor de la iteracion #" + count+ " es: " + x);
            System.out.println("Su error aproximado es: " + error_aproximado);
            System.out.println("----------------------------------------------------------");
            System.out.println("\n\n");

        }  while (error_aproximado > error_esperado);

        
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
