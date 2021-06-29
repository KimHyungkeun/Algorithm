import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine(); 
        StringBuffer sb = new StringBuffer(str); 
        
        String str_rev = sb.reverse().toString(); 
        
        if (str.equals(str_rev)) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }


    }
}