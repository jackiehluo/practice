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
        
        String newString = "";
        for (int i = 0; i < testCases; i++) {
            newString = input.nextLine();
            char previous = newString.charAt(0);
            int deletions = 0;
            for (int j = 1; j < newString.length(); j++) {
                char current = newString.charAt(j);
                if (current == previous) {
                    deletions++;
                }
                previous = current;
            }
            System.out.println(deletions); 
        }
    }
}