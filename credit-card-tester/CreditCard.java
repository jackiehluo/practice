//***************************
// CreditCard.java
// Jackie Luo (jhl2182)
// October 2014
//***************************

//====================================================
// Objects of this class determine whether a credit
// card number is valid, based on a series of
// check-sums.
//====================================================

public class CreditCard {

	private String number;
	private boolean valid;
	private int errorCode;
	
	// This constructor accepts the string for the credit
	// card number as input and initializes the instance
	// variables: number, valid, and errorCode
	public CreditCard(String creditCardNumber){
		this.number = creditCardNumber;
		this.valid = true;
		this.errorCode = 0;
	}	
	
	// This method is the first of six checks to see if the
	// credit card number is valid by determining whether
	// the first digit is 4
	public void checkOne() {
		int firstDigit = Integer.parseInt(number.substring(0, 1));
		if (firstDigit == 4) {
			this.valid = true;
			checkTwo();
		}
		else {
			this.valid = false;
			this.errorCode = 1;
		}
	}
	
	// This method is the second of six checks to see if
	// the credit card number is valid by determining
	// whether the fourth digit of the number is 1 greater
	// than the fifth digit
	public void checkTwo() {
		int fourthDigit = Integer.parseInt(number.substring(3, 4));
		int fifthDigit = Integer.parseInt(number.substring(4, 5));
		if (fourthDigit == fifthDigit + 1) {
			this.valid = true;
			checkThree();
		}
		else {
			this.valid = false;
			this.errorCode = 2;
		}
	}
	
	// This method is the third of six checks to see if
	// the credit card number if valid by determining
	// whether the product of the first, fifth, and ninth
	// digits is 24
	public void checkThree() {
		int firstDigit = Integer.parseInt(number.substring(0, 1));
		int fifthDigit = Integer.parseInt(number.substring(4, 5));
		int ninthDigit = Integer.parseInt(number.substring(8, 9));
		if (firstDigit * fifthDigit * ninthDigit == 24) {
			this.valid = true;
			checkFour();
		}
		else {
			this.valid = false;
			this.errorCode = 3;
		}
	}
	
	// This method is the fourth of six checks to see if
	// the credit card number is valid by determining
	// whether the sum of all twelve digits is evenly
	// divisible by 4
	public void checkFour() {
		int sum = 0;
		// This for loop converts each of the digits in the string
		// to an integer and adds it to sumFirst
		for (int x = 0; x < number.length(); x++) {
			int nthDigit = Integer.parseInt(number.substring(x, x+1));
			sum += nthDigit;
		}
		
		if (sum % 4 == 0) {
			this.valid = true;
			checkFive();
		}
		else {
			this.valid = false;
			this.errorCode = 4;
		}
	}
	
	// This method is the fifth of six checks to see if
	// the credit card number is valid by determining
	// whether the sum of the first four digits is 1 less
	// than the sum of the last four digits
	public void checkFive() {
		int sumFirst = 0;
		int sumLast = 0;
		// This for loop converts each of the first four digits in
		// the string to an integer and adds it to sumFirst
		for (int x = 0; x < 4; x++) {
			int nthFirstDigit = Integer.parseInt(number.substring(x, x+1));
			sumFirst += nthFirstDigit;
		}
		// This for loop converts each of the last four digits in
		// the string to an integer and adds it to sumLast
		for (int y = number.length() - 4; y < number.length(); y++) {
			int nthLastDigit = Integer.parseInt(number.substring(y, y+1));
			sumLast += nthLastDigit;
		}
		
		if (sumFirst == sumLast - 1) {
			this.valid = true;
			checkSix();
		}
		else {
			this.valid = false;
			this.errorCode = 5;
		}
	}
	
	// This method is the last of six checks to see if
	// the credit card number is valid by determining
	// whether the sum of the two-digit number created by
	// combining the first and second digits  and the
	// two-digit number created by combining the seventh
	// and eighth digits is 100
	public void checkSix() {
		int firstSecondDigit = Integer.parseInt(number.substring(0, 2));
		int seventhEighthDigit = Integer.parseInt(number.substring(6, 8));
		if (firstSecondDigit + seventhEighthDigit == 100) {
			this.valid = true;
		}
		else {
			this.valid = false;
			this.errorCode = 6;
		}
	}
	
	// This method is a mutator
	public void check() {
		checkOne();
	}
	
	// This method is an accessor
	public boolean isValid() {
		return this.valid;
	}
	
	// This method is an accessor
	public int getErrorCode() {
		return this.errorCode;
	}
	
}
