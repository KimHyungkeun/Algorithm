import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        int i = 0 ;
        
        Arrays.sort(participant);
        Arrays.sort(completion);
        
        for (i = 0 ; i < completion.length ; i ++){
            if (participant[i].equals(completion[i]) == false) {
                return participant[i];
            }      
        }
    
      answer = participant[participant.length-1];
      return answer;
    }
}

// 아래는 다른 사람의 정답

// import java.util.*;

// class Solution {
//     public String solution(String[] participant, String[] completion) {
//         String answer = "";
        
//         Arrays.sort(participant);
//         Arrays.sort(completion);
//         System.out.println(participant);
//         System.out.println(completion);

        
//         for (int i=0;i<participant.length;i++) {
//             if (i == participant.length - 1){
//                 answer = participant[i];
//                 break;
//             }
                
//             if (completion[i].equals(participant[i]))
//                 continue;
//             else {
//                 answer = participant[i];
//                 break;
//             }
                
//         }
        
        
        
//         return answer;
//     }
// }