import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner myScan = new Scanner(System.in);
        String inputString = myScan.nextLine();
        
        char[] chars = inputString.toCharArray();
        Arrays.sort(chars);
        String newString = new String(chars);
        
        int odds = 0;
        int count = 1;
        char previous = newString.charAt(0);
        
        for (int i = 1; i < newString.length(); i++) {
            char current = newString.charAt(i);
            if (current == previous) {
                 count++;
            }
            else {
                if (count % 2 != 0) {
                    odds++;
                }
                count = 1;
            }
            previous = current;
        }
       
        String ans = "";
        
        if (odds <= 1) {
            ans = "YES";
        }
        else {
            ans = "NO";
        }

        System.out.println(ans);
        myScan.close();
    }
}