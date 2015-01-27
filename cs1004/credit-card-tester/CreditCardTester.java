import java.util.Scanner;

/**
 * A tester for the CreditCard class.
 * 
 * @author Cannon 
 */
public class CreditCardTester {
    public static void main(String[] args) {
        System.out.println("Please enter an 12-digit number.");
	Scanner scanner = new Scanner(System.in);
	String creditCardNumber = scanner.next();
	if (creditCardNumber.length() != 12) {
	    System.out.println("That was not an 12-digit number!");
	    return;
	}
	CreditCard card = new CreditCard(creditCardNumber);
	card.check();
	if (card.isValid()) {
	    System.out.println("Valid");
	} 
	else {
	    int code = card.getErrorCode();
	    System.out.println("Oops! That's an invalid number.");
	    System.out.println("The error code was: " + code); 
	}

    }
}
