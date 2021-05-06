import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {      
        List<Integer> progress_list = new ArrayList<>();
        List<Integer> speeds_list = new ArrayList<>();
        List<Integer> answer_list = new ArrayList<>();
       
        int len = progresses.length;
        int i = 0;
        
        for (i = 0 ; i < len ; i++) {
            progress_list.add(progresses[i]);
            speeds_list.add(speeds[i]);
        } 
        
         // for (int str : speeds_list) {
         //    System.out.println(str);
         // }
        
        while (progress_list.size() != 0) {
            i = 0;
            for (int str : progress_list) {
                progress_list.set(i, str+speeds_list.get(i));
                i++;
            }
            
            int j = 0;
            int count = 0;
            while (progress_list.size() != 0) {
                if (progress_list.get(0) >= 100) {
                    count++;
                    progress_list.remove(0);
                    speeds_list.remove(0);
                }
                
                else
                    break;             
            } 
            
            if (count >= 1)
                answer_list.add(count);
            
        }
       
              
         int[] answer = new int[answer_list.size()];
         int size = 0;
        
         for (int str : answer_list) {
            answer[size] = str;
            size++;
         }
         
         return answer;
    }
}