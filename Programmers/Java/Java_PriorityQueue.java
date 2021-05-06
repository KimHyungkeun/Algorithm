import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        PriorityQueue<Integer> answer_min_list = new PriorityQueue<>();
        PriorityQueue<Integer> answer_max_list = new PriorityQueue<>(Collections.reverseOrder());
        String s;
        int num;
        
        for (int i = 0 ; i <operations.length; i++) {
            
            
            if (operations[i].contains("I")) {
                // System.out.println(operations[i]);
                s = operations[i].substring(2);
                num = Integer.parseInt(s);
                // System.out.println(num);
                answer_max_list.offer(num);
                answer_min_list.offer(num);
            }
            
            else if (operations[i].equals("D 1")) {
                if (answer_min_list.size() == 0 || answer_max_list.size() == 0)
                    continue;
                int max = answer_max_list.poll();
                answer_min_list.remove(max);
            }
            
            else {
                if (answer_min_list.size() == 0 || answer_max_list.size() == 0)
                    continue;
                int min = answer_min_list.poll();
                answer_max_list.remove(min);
            }
            
            // for (int j = 0 ; j < answer_max_list.size() ; j++) {
            //     System.out.print(answer_max_list.peek());
            // }
            // System.out.println(operations[i]);
        }
                   
        int[] answer = new int[2];
        if (answer_max_list.size() == 0 || answer_min_list.size() == 0)
            return answer;
        answer[0] = answer_max_list.peek();
        answer[1] = answer_min_list.peek();
        return answer;
    }
}