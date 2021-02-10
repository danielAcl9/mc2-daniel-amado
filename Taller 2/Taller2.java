package discretas;

import java.util.Collection;
import java.util.Collections;
import java.util.HashSet;
import java.util.Set;

import jdk.javadoc.internal.doclets.toolkit.taglets.SystemPropertyTaglet;

public class Taller1 {
	public static void main(String [] args) {
		HashSet<Integer> A = new HashSet<>();
		for (int i = 6; i < 25; i++){
			A.add(i);
		}
		System.out.println("A = " + A);
		
		HashSet<Integer> B = new HashSet<>();
		for (int i = 1; i < 30; i +=2){
			B.add(i);
		}
		System.out.println("B = " + B);

		HashSet<Integer> C = new HashSet<>();
		C.add(0);
		C.add(3);
		C.add(6);
		C.add(9);
		C.add(11);
		C.add(15);
		C.add(18);
		C.add(20);
		System.out.println("C = " + C);
		
		boolean primo;
		HashSet<Integer> D = new HashSet<>();
		for (int i = 2; i <= 40; i++){	
			primo = true;
			for (int j = 2; j <= i/2; j++) {
				if(i%j==0) {
					primo = false;
				}
			}
			if (primo) {
				D.add(i);
			}
		}
		System.out.println("D = " + D);
//--------------------------------------------------------------Operaciónes --------------------------------------------------------


		HashSet<Integer> R1 = intersec(SymDif(A, B), C);
		HashSet<Integer> R2 = union(dif(A, C), B);
		HashSet<Integer> R3 = SymDif(A, (union(C, D)));
		HashSet<Integer> R4 = SymDif(dif(C, A), intersec(B, D));
		
		
		System.out.println("Operación 1: " +R1);
		System.out.println("Operación 2: " +R2);
		System.out.println("Operación 3: " +R3);
		System.out.println("Operación 4: " +R4);
		
	}	
	
	private static HashSet<Integer> union(HashSet<Integer> X, HashSet<Integer> Y) {
		HashSet<Integer> R = new HashSet<>();
		for (int elemento : X) {
			R.add(elemento);
		}
		for (int elemento :Y) {
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
		HashSet<Integer> R = dif(union(X,Y), intersec(X,Y));
		return R;
		//(A U B) - (A N B)
	}
}	

