import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        
        try {
            int n = Integer.parseInt(br.readLine());
            String pattern = "^[a-zA-Z0-9_]*$";   
            String initiate = "^[a-zA-Z]*$";  
            String username = "";
            

            for (int i = 0 ; i < n ; i++) {
                username = br.readLine();
                // System.out.println("Username : " + username);
                
                if (!username.matches(pattern)) {
                    System.out.println("Invalid");
                }
                           
                else if (!username.substring(0,1).matches(initiate)) {
                    System.out.println("Invalid");
                }

         
                else if (username.length() < 8 || username.length() > 30) {
                    System.out.println("Invalid");
                } 
                

                else {
                    System.out.println("Valid");
                }
                
                
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}