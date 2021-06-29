import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        String range = sc.nextLine();
        String[] idx = range.split(" ");
        
        int start = Integer.valueOf(idx[0]);
        int end = Integer.valueOf(idx[1]);
        
        String answer = str.substring(start, end);
        System.out.println(answer);
    }
}