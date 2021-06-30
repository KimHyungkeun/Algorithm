// import java.io.*;
// import java.util.*;

// public class Solution {

//     public static void main(String[] args) {
//         /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
//         ArrayList<String> list = new ArrayList<>();
         
//         Scanner sc = new Scanner(System.in);
//         String str = sc.nextLine();
//         String[] tokens = str.split(" ");
//         String[] except = {"!", ",", "?", ".", "_", "'", "@"};
        
        
//         for (int i = 0 ; i < tokens.length ; i++) {
//             boolean flag = true;
//             String[] tmp = null;
//             for (int j = 0 ; j < except.length; j ++) {
//                 if (tokens[i].contains(except[j])) {
//                     if (except[j].equals("?"))
//                         tmp = tokens[i].split("\\?");
//                     else
//                         tmp = tokens[i].split(except[j]);
//                     flag = false;
//                     break;
//                 }
//             }
            
            
//             if (flag) {
//                 list.add(tokens[i]);
//             }
//             else {
//                 for (int k = 0 ; k < tmp.length ; k ++) {
//                     list.add(tmp[k]);
//                 }
//             }
                 
//         }

//         System.out.println(list.size());
//         int length = list.size();
//         for (int i = 0 ; i < length ; i++) {
//             System.out.println(list.get(i));
//         }
    

//     }
// }

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        ArrayList<String> list = new ArrayList<>();
         
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();

        str = str.trim(); // 공백을 제거하는 메소드
        if (str.length() == 0) {
            System.out.println(0);
        }
        else {
            String[] tokens = str.split("['!?,._@ ]+");
            System.out.println(tokens.length);
            int len = tokens.length;
            for (int i = 0 ; i < len ; i ++) {
                System.out.println(tokens[i]);
            }

        }       
        
    }
}

// https://www.thepoorcoder.com/hackerrank-java-string-tokens-solution/