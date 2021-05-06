import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        List<String> phone_book_list = new ArrayList<>(Arrays.asList(phone_book));
        
        int i = 0;
        int j = 0;
        int k = 0;
        // System.out.println(phone_book[0].charAt(0));
        for (String str : phone_book_list) {
            // System.out.println(str.charAt(0));
            for (j=0;j<phone_book.length;j++) {
                
                if (i == j)
                    continue;
                
                if (str.length() > phone_book[j].length())
                    continue;
                
                for (k=0;k<str.length();k++) {
                    if (str.charAt(k) == phone_book[j].charAt(k)) {
                        answer = false;
                    }
                    
                    else {
                        answer = true;
                        break;
                    }
                }
                
                if (answer == false)
                    return answer;     
            }
            i++;
        }     
        return answer;
    }
}

