import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'findDay' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts following parameters:
     *  1. INTEGER month
     *  2. INTEGER day
     *  3. INTEGER year
     */

    public static String findDay(int month, int day, int year) {
         String day_name = "" ;
        String date = String.valueOf(year) + String.format("%02d", month) +  String.format("%02d", day);
        System.out.println(date);
        String dateType = "yyyyMMdd";
     
        SimpleDateFormat dateFormat = new SimpleDateFormat(dateType) ;
        
        try {
            Date nDate = dateFormat.parse(date) ;
            Calendar cal = Calendar.getInstance() ;
            cal.setTime(nDate);
            
            int dayNum = cal.get(Calendar.DAY_OF_WEEK) ;
           
            
            switch(dayNum){
                case 1:
                    day_name = "SUNDAY";
                    break ;
                case 2:
                    day_name = "MONDAY";
                    break ;
                case 3:
                    day_name = "TUESDAY";
                    break ;
                case 4:
                    day_name = "WEDNESDAY";
                    break ;
                case 5:
                    day_name = "THURSDAY";
                    break ;
                case 6:
                    day_name = "FRIDAY";
                    break ;
                case 7:
                    day_name = "SATURDAY";
                    break ;
                
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        
        return day_name ;


    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int month = Integer.parseInt(firstMultipleInput[0]);

        int day = Integer.parseInt(firstMultipleInput[1]);

        int year = Integer.parseInt(firstMultipleInput[2]);

        String res = Result.findDay(month, day, year);

        bufferedWriter.write(res);
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
