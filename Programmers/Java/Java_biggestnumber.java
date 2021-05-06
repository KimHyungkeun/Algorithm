import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";   
        String[] str_numbers = new String[numbers.length];
        
        for(int i=0; i<str_numbers.length; i++) {
		    str_numbers[i] = String.valueOf(numbers[i]);
	    }
	

        // 정렬(람다식)
        // Arrays.sort(result, (o1, o2) -> (o2 + o1).compareTo(o1 + o2));

        // 정렬
        Arrays.sort(str_numbers, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return (o2+o1).compareTo(o1+o2);
            }
        });

        // for(int i=0; i<str_numbers.length; i++) {
        //     System.out.println(str_numbers[i]);
        // }
        
        if (str_numbers[0].equals("0"))
            return "0";
        
        for(int i=0; i<str_numbers.length; i++) {
            answer += str_numbers[i];
        }
            
        return answer;
    }
}