import java.util.Scanner;

//**************************
// P221.java
// Jackie Luo
//**************************

public class P221{

    public static void main(String[] args){

    // Read year

    Scanner in = new Scanner(System.in);

    System.out.print("Please enter a year: ");
    int year = in.nextInt();
    
    // Compute month and day of Easter Sunday

    int a = year % 19;
    int b = year / 100;
    int c = year % 100;
    int d = b / 4;
    int e = b % 4;
    int g = (8 * b + 13) / 25;
    int h = (19 * a + b - d - g + 15) % 30;
    int j = c / 4;
    int k = c % 4;
    int m = (a + 11 * h) / 319;
    int r = (2 * e + 2 * j - k - h + m + 32) % 7;
    int n = (h - m + r + 90) / 25;
    int p = (h - m + r + n + 19) % 32;

    System.out.print("That year, Easter Sunday falls on " + n + "/"
        + p + ".\n");
    }
}
