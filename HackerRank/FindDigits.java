import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);
        int testCases = input.nextInt();
        while (testCases < 1 || testCases > 10) {
            System.out.println("Please input a number from 1 to 10.");
            testCases = input.nextInt();
        }
        
        for (int i = 0; i < testCases; i++) {
            int number = input.nextInt();
            int temp = number;
            int digits = 0;
            for (int j = 0; j < String.valueOf(number).length(); j++) {
                int currentDigit = temp % 10;
                if (currentDigit != 0 && number % currentDigit == 0) {
                    digits++;
                }
                temp = temp / 10;
            }
            System.out.println(digits);
        }
    }
}