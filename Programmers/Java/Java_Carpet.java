import java.util.*;

class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        int total = brown + yellow;
        int weight = 0;
        int height = 0;
        List<Integer> lists = new ArrayList<>();
        
        for(int i = 1; i <= yellow; i++){
            if((yellow % i)==0){
                // System.out.println(i);
                lists.add(i);
            }               
        }
        
        if (lists.size() % 2 == 0) {
            for (int i = 0 ; i < (lists.size() / 2) ; i++) {
                height = lists.get(i);
                weight = lists.get((lists.size()-1) - i);
                // System.out.println(height + " " + weight);
                
                if ((height+2) * (weight+2) == total) {
                    answer[0] = weight + 2;
                    answer[1] = height + 2;
                }
            }
            // answer[0] = lists.get(lists.size() / 2);
            // answer[1] = lists.get((lists.size() / 2) - 1);
        }
        
        else {
            for (int i = 0 ; i <= (lists.size() / 2) ; i++) {
                height = lists.get(i);
                weight = lists.get((lists.size()-1) - i);
                // System.out.println(height + " " + weight);
                
                if ((height+2) * (weight+2) == total) {
                    answer[0] = weight + 2;
                    answer[1] = height + 2;
                }
            }
             // answer[0] = lists.get(lists.size() / 2);
             // answer[1] = lists.get(lists.size() / 2);
        }

        return answer;
    }
}