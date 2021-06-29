import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        int n = sc.nextInt();
        
        int limit = str.length() - n;
        ArrayList<String> list = new ArrayList<>();
        
        for (int i = 0 ; i <= limit ; i ++) {
            list.add(str.substring(i, i+n));
        }
        Collections.sort(list);
        // System.out.println(list.get(0));
        System.out.println(list.get(0) + "\n" + list.get(list.size()-1));
        


    }
}