import java.io.*;
import java.util.*;
import java.math.BigInteger; // BigInteger 클래스를 통해 무한대의 값을 다룰 수 있다.

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        BigInteger a = new BigInteger(sc.nextLine());
        BigInteger b = new BigInteger(sc.nextLine());
        
        System.out.println(a.add(b)); // 두 수의 합
        System.out.println(a.multiply(b)); // 두 수의 곱
    }
}