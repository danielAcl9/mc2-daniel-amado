import java.util.HashSet;
import java.util.Scanner;

public class Taller1 {
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese el tamaño de los conjuntos");
        int size = sc.nextInt();

        // Conjunto 1 ---------------------------------------------------------------------------------------------
        System.out.println("Ingrese los " + size + " elementos del conjunto 1");
        HashSet<Float> C1 = new HashSet<>();
        for (int i = 0; i < size; i++){
            C1.add(sc.nextFloat());
        }

        // Conjunto 2 ---------------------------------------------------------------------------------------------
        System.out.println("Ingrese los " + size + " elementos del conjunto 2");
        HashSet<Float> C2 = new HashSet<>();
        for (int i = 0; i < size; i++){
            C2.add(sc.nextFloat());
        }
        
        // Operaciones ---------------------------------------------------------------------------------------------
        System.out.println("¿Que operación desea hacer?\n 1. Unión\n 2. Intersección\n 3. Diferencia \n 4. Diferencia Simétrica");
        int operacion = sc.nextInt();
        switch(operacion){

            case 1:
                HashSet<Float> rta = union(C1,C2);
                System.out.println(rta);
            break;

            case 2:
                HashSet<Float> rta2 = intersec(C1,C2);
                System.out.println(rta2);
            break;

            case 3:
                HashSet<Float> rta3 = dif(C1,C2);
                System.out.println(rta3);
            break;

            case 4:
                HashSet<Float> rta4 = SymDif(C1,C2);
                System.out.println(rta4);
            break;

        }
    }

        // ---------------------------------------------------------------------------------
        private static HashSet<Float> union(HashSet<Float> X, HashSet<Float> Y) {
            HashSet<Float> R = new HashSet<>();
            for (float elemento : X) {
                R.add(elemento);
            }
            for (float elemento :Y) {
                R.add(elemento);
            }
            return R;
        }
        
        private static HashSet<Float> intersec(HashSet<Float> X, HashSet<Float> Y) {
            HashSet<Float> R = new HashSet<>();
            R = X;
            R.retainAll(Y);

            return R;
        }
        
        private static HashSet<Float> dif(HashSet<Float> X, HashSet<Float> Y) {
            HashSet<Integer> R = new HashSet<>();
            R = Y;
            Y.remove(X);
            
            return R;
        }
        
        private static HashSet<Float> SymDif(HashSet<Float> X, HashSet<Float> Y) {
            HashSet<Integer> R = dif(intersec(X,Y), union(X,Y));
    
            return R;
            //(A U B) - (A N B)
        }
    
}