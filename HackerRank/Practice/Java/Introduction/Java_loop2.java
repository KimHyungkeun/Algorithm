import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        for (int i = 0 ; i < n ; i++) {
            String nums = sc.nextLine();
            String[] cmd = nums.split(" ");
            
            int start = Integer.parseInt(cmd[0]);
            int end = Integer.parseInt(cmd[1]);
            int round = Integer.parseInt(cmd[2]);
            
            int total = 0;
            for (int j = 1 ; j <= round ; j++) {
                if (j == 1) 
                    total += (start + end);
                else 
                    total += (Math.pow(2,(j-1)) * end);  
                
                System.out.print(total + " ");
            }
            System.out.println();
        }
    }
}