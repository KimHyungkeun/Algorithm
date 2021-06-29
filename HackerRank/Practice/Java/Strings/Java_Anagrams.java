import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine().toLowerCase();
        String b = sc.nextLine().toLowerCase();
        
        if (a.length() != b.length()) {
            System.out.println("Not Anagrams");
        } else {
            ArrayList<Character> list1 = new ArrayList<>();
            ArrayList<Character> list2 = new ArrayList<>();
            
            for (int i = 0 ; i < a.length() ; i ++) {
                list1.add(a.charAt(i));
                list2.add(b.charAt(i));
            }
            
            Collections.sort(list1);
            Collections.sort(list2);

            boolean flag = true;
            for (int i = 0 ; i < list1.size() ; i ++) {
                if (list1.get(i) != list2.get(i)) {
                    flag = false;
                    break;
                }
            }
            
            if (!flag) 
                System.out.println("Not Anagrams");
            else 
                System.out.println("Anagrams");
            
            
        }
        
        
    }
}