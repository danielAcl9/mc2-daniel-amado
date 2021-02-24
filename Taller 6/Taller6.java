import java.util.Scanner;
class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Digite el angulo en grados");
        double angulo = Math.toRadians(sc.nextDouble());
        
        double error_esperado = ((0.5 * Math.pow(10,-8)) * 100);

        int contador = 0, k = 0;
        double x = 0, y = 0;

        double error_aproximado = 100;

        do {
            y = x;
            x = x + (Math.pow(-1,k) * Math.pow(angulo, 2 * k))/(factorial(2 * k));
            k += 1;
            contador += 1;

            //calculo del error
            error_aproximado = Math.abs((x-y)/x) * 100;
            System.out.println("----------------------------------------------------------");
            System.out.println("La iteracion actual es: " + contador);
            System.out.println("El valor de la iteracion #" + contador+ " es: " + x);
            System.out.println("Su error aproximado es: " + error_aproximado);
            System.out.println("----------------------------------------------------------");
            System.out.println("\n\n");

        } while (error_aproximado > error_esperado);
        
        System.out.println("----------------------------------------------------------");
        System.out.println("La iteracion final es: " + contador);
        System.out.println("El valor de la iteracion #" + contador+ " es: " + x);
        System.out.println("Su error aproximado final es: " + error_aproximado);
        System.out.println("----------------------------------------------------------");
        System.out.println("\n\n");

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