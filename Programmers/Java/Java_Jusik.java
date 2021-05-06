import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        int len = prices.length;
        int[] answer = new int[len];
        int time = 0;
        int i, j;
        
        // for (int i = 0 ; i < len ; i++) {
        //     answer[i] = 0;
        //     // System.out.println(answer[i]);
        // }
        
          for (i = 0 ; i < len ; i++) {    
                time = 0;
                for (j = i+1 ; j < len ; j ++) {
                    if (prices[i] <= prices[j]){
                        time++ ;
                    }
                    
                    else {
                        time++;
                        break;
                    }
                }
                               
                answer[i] = time;               
         }
        
        
        
        return answer;
    }
}