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
            int height = 1;
            int growthCycles = 0;
            int totalCycles = input.nextInt();
            while (totalCycles < 0 || totalCycles > 60) {
                System.out.println("Please input a number from 0 to 60.");
                totalCycles = input.nextInt();
            }
            while (growthCycles < totalCycles) {
                if (growthCycles < totalCycles) {
                    height = height * 2;
                    growthCycles++;
                }
                if (growthCycles < totalCycles) {
                    height = height + 1;
                    growthCycles++;
                }
            }
            System.out.println(height);
        }
    }
}