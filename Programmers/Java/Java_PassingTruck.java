import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int count = 0;
        int max = 0;
        int tmp = 0;
        
        Queue<Integer> queue = new LinkedList<>();
        List<Integer> queue_count = new ArrayList<>();
        Queue<Integer> weights_queue = new LinkedList<>();
        
        for (int val : truck_weights) {
            weights_queue.offer(val);
        }
        
        // System.out.println(weights_queue);
        // System.out.println(queue.isEmpty());
        
        int j = 0;
        while (true) {           
            count ++;
            j++;
            // System.out.println(queue);
            // System.out.println(weights_queue);
            // System.out.println(queue_count);
            
            if(queue.isEmpty() && weights_queue.isEmpty()) {
                break;
            }
            
            if ((!queue_count.isEmpty()) && (queue_count.get(0) == bridge_length)) {
                queue_count.remove(0);
                max -= queue.peek();
                queue.poll();
            }
                        
            if (!weights_queue.isEmpty()) {
                tmp = weights_queue.peek();
                max += tmp;
            }
            
            if ((max <= weight) && (!weights_queue.isEmpty())) {
                int i = 0;
                for (int val : queue_count) {
                    queue_count.set(i, val+1);
                    i++;
                }
                queue.offer(weights_queue.poll());
                // System.out.println("OK");
                queue_count.add(1);
            }
            
            else {
                max -= tmp;
                int i = 0;
                for (int val : queue_count) {
                    queue_count.set(i, val+1);
                    i++;
                }
            }
            
        }
        
        count --;
        return count;
    }
}