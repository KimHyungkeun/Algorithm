import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        HashMap<String, Integer> map = new HashMap<>();
        int answer = 1;
        
        for (int i = 0 ; i < clothes.length ; i++) {
            if (map.containsKey(clothes[i][1])) {
                map.put(clothes[i][1], map.get(clothes[i][1]) + 1);
            }
            
            else {
                map.put(clothes[i][1], 1);
            }
        }
        
          map.forEach((key, value)->{
              map.put(key, map.get(key) + 1);
          });
        
         Iterator<String> keys = map.keySet().iterator();
          while( keys.hasNext() ){
              String key = keys.next();
              answer *= map.get(key);
          }
        
        answer--;
                
        // System.out.println(map);
        return answer;
    }
}