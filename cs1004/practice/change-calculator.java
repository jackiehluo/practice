import java.util.Scanner;

//**************
// P225.java
// Jackie Luo
//**************

public class P225{

    public static void main(String[] args){

    // Read amount due and received for transaction

    Scanner in = new Scanner(System.in);

    final int PENNIES_PER_DOLLAR = 100;
    final int PENNIES_PER_QUARTER = 25;
    final int PENNIES_PER_DIME = 10;
    final int PENNIES_PER_NICKEL = 5;

    System.out.print("Please enter the amount due in pennies: ");
    int amountDue = in.nextInt();
    System.out.print("Please enter the amount received in pennies: ");
    int amountReceived = in.nextInt();

    // Compute change owed to customer

    int changeOwed = amountReceived - amountDue;
    int dollars = changeOwed / PENNIES_PER_DOLLAR;
    changeOwed = changeOwed % PENNIES_PER_DOLLAR;
    int quarters = changeOwed / PENNIES_PER_QUARTER;
    changeOwed = changeOwed % PENNIES_PER_QUARTER;
    int dimes = changeOwed / PENNIES_PER_DIME;
    changeOwed = changeOwed % PENNIES_PER_DIME;
    int nickels = changeOwed / PENNIES_PER_NICKEL;
    changeOwed = changeOwed % PENNIES_PER_NICKEL;
    
    // Print change owed

    System.out.printf("Dollars:  %6d\n", dollars);
    System.out.printf("Quarters: %6d\n", quarters);
    System.out.printf("Dimes:    %6d\n", dimes);
    System.out.printf("Nickels:  %6d\n", nickels);
    System.out.printf("Pennies:  %6d\n", changeOwed);
    
    }
}
    
