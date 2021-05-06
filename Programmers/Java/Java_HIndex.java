import java.util.*;

class Solution {
    public int solution(int[] citations) {
        int h = 0;
        int count;
        Arrays.sort(citations);
        
        int max = citations[citations.length-1];
        
        for (int i = 0 ; i <= max; i++) {
            // System.out.println(citations[i]);
            count = 0;
            for (int j = 0 ; j < citations.length ; j ++) {
                if (citations[j] >= i)
                    count++;
            }
            
            if (count >= i && i >= h)
                h = i;
        }
        
        return h;
    }
}