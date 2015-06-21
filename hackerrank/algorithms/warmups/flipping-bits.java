import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);
        int testCases = input.nextInt();
        long number;
        long unsignedNumber;
        
        for (int i = 0; i < testCases; i++) {
            number = input.nextLong();
            number = ~number;
            unsignedNumber = number & 0xffffffffL;
            System.out.println(unsignedNumber);
        }
        
    }
}