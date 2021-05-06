import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int idx = 0;
        int[] student_1 = new int[10000];
        int[] student_2 = new int[10000];
        int[] student_2_support = {2,1,2,3,2,4,2,5}; // 길이 8
        int[] student_3 = new int[10000];
        int[] student_3_support = {3,3,1,1,2,2,4,4,5,5}; // 길이 10
        
        int stu1 = 0; //학생1이 맞은 정답 수
        int stu2 = 0; //학생2이 맞은 정답 수
        int stu3 = 0; //학생3이 맞은 정답 수
        
        for (int i = 0 ; i < student_1.length ; i++)       
            student_1[i] = (i % 5) + 1;
        
//         for (int i = 0 ; i < 10 ; i++) {
//             System.out.println(student_1[i]);
//         }
        
        for (int i = 0 ; i < student_2.length ; i ++) {            
            idx = i % 8;
            student_2[i] = student_2_support[idx]; 
        }
        
        for (int i = 0 ; i < student_3.length ; i ++) {            
            idx = i % 10;
            student_3[i] = student_3_support[idx]; 
        }
        
        for (int i = 0 ; i < answers.length ; i++) {
            if (answers[i] == student_1[i])
                stu1++;
            
            if (answers[i] == student_2[i])
                stu2++;
            
            if (answers[i] == student_3[i])
                stu3++;
        }
        
        HashMap<Integer, Integer> map = new HashMap<>();
        map.put(1, stu1);
        map.put(2, stu2);
        map.put(3, stu3);
                
        List<Integer> keySetList = new ArrayList<>(map.keySet());      
        Collections.sort(keySetList, (o1, o2) -> (map.get(o2).compareTo(map.get(o1)))); //내림차순 정렬
		
        int max = 0; //최댓값을 저장하는 변수
        ArrayList<Integer> arrayList = new ArrayList<>();       
        for(Integer key : keySetList) {
			max = map.get(key);
            break;
		}
        
        for(Integer key : keySetList) {
              
			if (max == (map.get(key))) 
                arrayList.add(key);
		}
        
        // System.out.println(arrayList);
        int[] answer = new int[arrayList.size()];
        int size=0;

        for(Integer tmp : arrayList){
             answer[size++] = tmp;
        }
        return answer;
    }
}