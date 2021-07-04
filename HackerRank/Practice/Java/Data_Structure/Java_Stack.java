import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        try {
            String str = "";
            while ((str = br.readLine()) != null) {
                ArrayList<Character> list = new ArrayList<>();
                for (int i = 0 ; i < str.length() ; i ++) {
                    if (list.isEmpty()) {
                        list.add(str.charAt(i));
                    }       
                    else if (list.get(list.size()-1).equals('(') && str.charAt(i) == ')') {
                        list.remove(list.size()-1);
                    }
                    else if (list.get(list.size()-1).equals('{') && str.charAt(i) == '}') {
                        list.remove(list.size()-1);
                    }
                    else if (list.get(list.size()-1).equals('[') && str.charAt(i) == ']') {
                        list.remove(list.size()-1);
                    }
                    
                    else {
                        list.add(str.charAt(i));
                    }
                    // System.out.println(list);
                }    
                
                if (list.isEmpty()) {
                    System.out.println("true");
                }else{
                    System.out.println("false");
                }
            }
            
            
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
