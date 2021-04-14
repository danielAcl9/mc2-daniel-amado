import java.util.Scanner;

public class taller15_1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese la dimensión de la matriz");
        int n = sc.nextInt();
        double matriz[][] = new double[n][n];
        System.out.println("Ingrese los elementos de la matriz");
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                matriz[i][j] = sc.nextDouble();

        double mInversa[][] = invertir(matriz);

        System.out.println("La matriz inversa es: ");
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                System.out.print(mInversa[i][j] + "  ");
            }
            System.out.println();
        }
        sc.close();
    }

    public static double[][] invertir(double a[][]) {
        int n = a.length;
        double x[][] = new double[n][n];
        double b[][] = new double[n][n];
        int indice[] = new int[n];
        for (int i = 0; i < n; ++i)
            b[i][i] = 1;

        gaussiano(a, indice);

        for (int i = 0; i < n - 1; ++i)
            for (int j = i + 1; j < n; ++j)
                for (int k = 0; k < n; ++k)
                    b[indice[j]][k] -= a[indice[j]][i] * b[indice[i]][k];

        // Sustitución
        for (int i = 0; i < n; ++i) {
            x[n - 1][i] = b[indice[n - 1]][i] / a[indice[n - 1]][n - 1];
            for (int j = n - 2; j >= 0; --j) {
                x[j][i] = b[indice[j]][i];
                for (int k = j + 1; k < n; ++k) {
                    x[j][i] -= a[indice[j]][k] * x[k][i];
                }
                x[j][i] /= a[indice[j]][j];
            }
        }
        return x;
    }

    // Método para llevar el pitove en Gauss, indice lo almacena.

    public static void gaussiano(double a[][], int indice[]) {
        int n = indice.length;
        double c[] = new double[n];

        // Inicia el indice
        for (int i = 0; i < n; ++i)
            indice[i] = i;

        for (int i = 0; i < n; ++i) {
            double c1 = 0;
            for (int j = 0; j < n; ++j) {
                double c0 = Math.abs(a[i][j]);
                if (c0 > c1)
                    c1 = c0;
            }
            c[i] = c1;
        }

        // Busca el elemento pivote
        int k = 0;
        for (int j = 0; j < n - 1; ++j) {
            double pi1 = 0;
            for (int i = j; i < n; ++i) {
                double pi0 = Math.abs(a[indice[i]][j]);
                pi0 /= c[indice[i]];
                if (pi0 > pi1) {
                    pi1 = pi0;
                    k = i;
                }
            }

            // Cambio de filas por el cambio de pivote

            int itmp = indice[j];
            indice[j] = indice[k];
            indice[k] = itmp;
            for (int i = j + 1; i < n; ++i) {
                double pj = a[indice[i]][j] / a[indice[j]][j];
                
                a[indice[i]][j] = pj;

                for (int l = j + 1; l < n; ++l)
                    a[indice[i]][l] -= pj * a[indice[j]][l];
            }
        }
    }
}