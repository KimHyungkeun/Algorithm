import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double money = sc.nextDouble();
        
        
        try {
            NumberFormat us = NumberFormat.getCurrencyInstance(Locale.US);
            
            Locale indiaLocale = new Locale("en", "in");
            NumberFormat india = NumberFormat.getCurrencyInstance(indiaLocale);
            NumberFormat ch = NumberFormat.getCurrencyInstance(Locale.CHINA);
            NumberFormat fr = NumberFormat.getCurrencyInstance(Locale.FRANCE);
            
            System.out.println("US: " + us.format(money));
            
            // String str = india.format(money);
            // String new_str = "Rs." + str.substring(1,str.length());
            System.out.println("India: " + india.format(money));
            
            System.out.println("China: " + ch.format(money));
            
            System.out.println("France: " + fr.format(money));
            
        } catch(Exception e) {
            e.printStackTrace();
        }
    }
}
