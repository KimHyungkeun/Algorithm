import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        
        List<String> participant_list = new ArrayList<>(Arrays.asList(participant));
        List<String> completion_list = new ArrayList<>(Arrays.asList(completion));
        
        int i = 0 ;
        while (completion_list.size() != 0) {

            if (completion_list.contains(participant_list.get(i)) == true) {            
                completion_list.remove(participant_list.get(i));
                participant_list.remove(i);
                i = 0;
            }
            
            else
                i++;
        }
        
        answer = participant_list.get(0);
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