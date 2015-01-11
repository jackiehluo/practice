import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int testCases = in.nextInt();
        
        double min;
        double max;
        double minRoot;
        double maxRoot;
        int count = 0;
        
        for (int i = 0; i < testCases; i++) {
            min = in.nextDouble();
            max = in.nextDouble();
            minRoot = Math.sqrt(min);
            maxRoot = Math.sqrt(max);
            if ((int)minRoot != (int)maxRoot || minRoot == (int)minRoot
                || maxRoot == (int)maxRoot) {
                    for (int j = (int)(Math.ceil(minRoot)); j <= maxRoot; j++) {
                        count++;
                    }
            }
            else {
                count = 0;
            }
            System.out.println(count);
            count = 0;
        }
    }
}