import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        
        int integer = sc.nextInt(); 
        double doubles = sc.nextDouble();
        sc.nextLine(); // 쓸데 없는 개행문자 제거
        String str = sc.nextLine();       
        
       
        
        
        System.out.println("String: " + str);
        System.out.println("Double: " + doubles);
        System.out.println("Int: " + integer);
        
    }
}