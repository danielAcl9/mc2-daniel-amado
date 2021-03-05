import java.util.Collection;
import java.util.Collections;
import java.util.HashSet;
import java.util.Set;

//import jdk.javadoc.internal.doclets.toolkit.taglets.SystemPropertyTaglet;

public class Punto1 {
    public static void main(String[] args) {

        HashSet<Integer> A = new HashSet<>();
        A.add(1);
        A.add(2);
        A.add(4);
        A.add(8);
        A.add(15);
        A.add(31);
        A.add(46);
        System.out.println("A = " + A);

        HashSet<Integer> B = new HashSet<>();
        for (int i = 6; i <= 25; i++) {
            B.add(i);
        }
        System.out.println("B = " + B);

        HashSet<Integer> C = new HashSet<>();
        for (int i = -5; i <= 30; i++) {
            if (i % 3 == 0) {
                C.add(i);
            }
        }
        System.out.println("C = " + C);

        boolean primo;
        HashSet<Integer> D = new HashSet<>();
        for (int i = 6; i < 50; i++) {
            primo = true;
            for (int j = 2; j <= i / 2; j++) {
                if (i % j == 0) {
                    primo = false;
                }
            }
            if (primo) {
                D.add(i);
            }
        }
        System.out.println("D = " + D);
        // --------------------------------------------------------------Operaciones
        // --------------------------------------------------------

        HashSet<Integer> R1 = union(intersec(B, C), SymDif(A, D));
        HashSet<Integer> R2 = SymDif(SymDif(B, C), union(A, dif(B, C)));
        HashSet<Integer> R3 = intersec(SymDif(dif(C, B), intersec(A, D)), union(A, union(B, C)));

        System.out.println("Operación 1: " + R1);
        System.out.println("Operación 2: " + R2);
        System.out.println("Operación 3: " + R3);
        // System.out.println("Operación 4: " + R4);

    }

    private static HashSet<Integer> union(HashSet<Integer> X, HashSet<Integer> Y) {
        HashSet<Integer> R = new HashSet<>();
        for (int elemento : X) {
            R.add(elemento);
        }
        for (int elemento : Y) {
            R.add(elemento);
        }
        return R;
    }

    private static HashSet<Integer> intersec(HashSet<Integer> X, HashSet<Integer> Y) {

        HashSet<Integer> R = new HashSet<>(X);
        R.retainAll(Y);

        return R;
    }

    private static HashSet<Integer> dif(HashSet<Integer> X, HashSet<Integer> Y) {
        HashSet<Integer> R = new HashSet<>(X);

        for (int elemento : Y) {
            R.remove(elemento);
        }

        return R;
    }

    private static HashSet<Integer> SymDif(HashSet<Integer> X, HashSet<Integer> Y) {
        HashSet<Integer> R = dif(union(X, Y), intersec(X, Y));
        return R;
        // (A U B) - (A N B)
    }
}
