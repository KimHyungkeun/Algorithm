import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ArrayList<Integer> list = new ArrayList<>();

        for (int i = 0 ; i < n ; i++) {
            int val = sc.nextInt();
            list.add(val);
        }

        // String ele_str = sc.nextLine();
        
        // String[] ele_arr = ele_str.split(" ");
        // for (int i = 0 ; i < ele_arr.length ; i++) {
        //     list.add(Integer.parseInt(ele_arr[i]));
        // }

        int cmd_n = sc.nextInt();
        sc.nextLine();
        
        for (int i = 0 ; i < cmd_n ; i++) {
            String cmd = sc.next();
            if (cmd.equals("Insert")) {
                int idx = sc.nextInt();
                int num = sc.nextInt();
                list.add(idx, num);

                // String pos_ele = sc.nextLine();
                // String[] pos_ele_arr = pos_ele.split(" ");
                // list.add(Integer.parseInt(pos_ele_arr[0]), Integer.parseInt(pos_ele_arr[1])); 
            }
            
            else {
                int idx = sc.nextInt();
                list.remove(idx);
            }
        }
        
        sc.close();
        int size = list.size();
        for (int i = 0 ; i < size ; i ++) {
            System.out.print(list.get(i) + " ");
        }
    }
}

// https://www.hackerrank.com/challenges/java-list/forum

