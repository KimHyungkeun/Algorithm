import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int val = sc.nextInt();
        int val2 = sc.nextInt();
        
        if (val <= 0 || val2 <= 0) {
            System.out.println("java.lang.Exception: Breadth and height must be positive");
        }
        else {
            System.out.println(val*val2);
        }
    }
}