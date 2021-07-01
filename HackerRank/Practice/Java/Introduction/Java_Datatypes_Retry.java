import java.io.*;
import java.util.*;
import java.math.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        for (int i = 0 ; i < n ; i ++) {
            
            // sc.nextLine();
            
            try {
                long num = sc.nextLong();

                System.out.println(num + " can be fitted in: ");
                if (-128 <= num && num <= 127) {
                    System.out.println("* byte");
                } 
                if (-Math.pow(2,15) <= num && num <= Math.pow(2,15)-1) {
                    System.out.println("* short");
                }
                if (-Math.pow(2,31) <= num && num <= Math.pow(2,31)-1) {
                    System.out.println("* int");
                }
                if (-Math.pow(2,63) <= num && num <= Math.pow(2,63)-1) {
                    System.out.println("* long");
                }

            } catch(Exception e) {
                System.out.println(sc.next() + " can't be fitted anywhere.");
            }
            
            
        }
    }
}

// https://www.hackerrank.com/challenges/java-datatypes/forum