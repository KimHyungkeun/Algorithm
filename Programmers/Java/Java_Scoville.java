import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> scoville_list = new PriorityQueue<>();
        int count = 0;
        int real_scovile = 0;
        boolean flag;
               
        for (int i = 0 ; i < scoville.length ; i ++) {
            scoville_list.add(scoville[i]);
        }
        
        // for (int str : scoville_list) {
        //     System.out.println(str);
        // }
        
        while (true) {
            count ++;
            flag = true;
            
            if (scoville_list.size() == 1 && scoville_list.peek() < K ) {
                count = -1;
                break;
            }
           
            real_scovile = scoville_list.poll();
            real_scovile += (scoville_list.poll() * 2);
            scoville_list.add(real_scovile);
           
            // for (int str : scoville_list) {
            //     System.out.println(str);
            // }
    
            for (int value : scoville_list) {
                if (value < K) {
                    flag = false;
                    break;
                }
            }
            if (flag == true)
                break;         
        }
              
        return count;
    }
}