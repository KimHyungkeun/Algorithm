import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine();
        String b = sc.nextLine();
        
        System.out.println(a.length() + b.length());
        
        if (a.compareTo(b) > 0) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
        
        String a_first = a.substring(0,1).toUpperCase() + a.substring(1);
        String b_first = b.substring(0,1).toUpperCase() + b.substring(1);
        
        System.out.println(a_first + " " + b_first);
    }
}