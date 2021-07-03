import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // Scanner sc = new Scanner(System.in);
        try {
            int n = Integer.parseInt(br.readLine());
           
            Map<String, String> hashMap = new HashMap<String, String>();
            for (int i = 0 ; i < n ; i++) {
                String name = br.readLine();
                String phone_num = br.readLine();
                // System.out.println(name + " " + phone_num);
                hashMap.put(name, phone_num);
            }
            
            String name = "";
            while ((name = br.readLine()) != null) {
                
                // String name = sc.nextLine();
                if (!hashMap.containsKey(name)) {
                    System.out.println("Not found");
                } else {
                    System.out.println(name + "=" + hashMap.get(name));
                }
            }

        }catch(Exception e) {
            e.printStackTrace();
        }
    }
}