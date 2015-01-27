//***********************************
// Oracle.java
// Jackie Luo (jhl2182)
// October 2014
//***********************************

//===============================================
// Objects of this class determine the number of
// bulls and cows, based on a computer-generated
// four-digit number and the user's input number.
//===============================================

public class Oracle{
    
    private String pattern;
    private String randomNumber;

    // This constructor accepts the string for the user's
    // four-digit guess as input and initializes the
    // instance variable randomNumber
    public Oracle(String guess){
        this.randomNumber = "1234";
    }

    // This method is a mutator used to test the code
    public void setPattern(String solution){
        pattern = solution;
    }

    // This method is an accessor used to test the code
    public String getPattern(){
        return pattern;
    }

    // This method returns the number of bulls that the
    // String guess should earn, based on the number of
    // digits guessed correctly in the right positions
    public int howManyBulls(String guess){
        int bulls = 0;
        for (int i = 0; i < 4; i++){
            if (guess.charAt(i) == randomNumber.charAt(i)){
                bulls++;
            }
        }
        return bulls;
    }

    // This method returns the number of cows that the
    // String guess should earn, based on the number of
    // digits guessed correctly in the wrong positions
    // (with up to one cow for each digit from 0 and 9
    // and none if there is a bull for that digit)
    public int howManyCows(String guess){
        int cows = 0;
        for (int i = 0; i < 4; i++){
            if (guess.contains(randomNumber.substring(i, i+1))
                    && (guess.charAt(i) !=
                    randomNumber.charAt(i))){
                cows++;
            }
        }
        return cows;
    }

    // This method generates a string of four random
    // non-repeating digits as the computer's chosen
    // number for the game
    public void chooseNumber(){
        int digitOne = (int)(Math.random() * 10);
        int digitTwo = (int)(Math.random() * 10);
        while (digitTwo == digitOne) {
            digitTwo = (int)(Math.random() * 10);
        }
        int digitThree = (int)(Math.random() * 10);
        while (digitThree == digitOne || digitThree == digitTwo) {
            digitThree = (int)(Math.random() * 10);
        }
        int digitFour = (int)(Math.random() * 10);
        while (digitFour == digitOne || digitFour == digitTwo
                || digitFour == digitThree) {
            digitFour = (int)(Math.random() * 10);
        }
        String newNumber = Integer.toString(digitOne) +
            Integer.toString(digitTwo) + Integer.toString(digitThree) +
            Integer.toString(digitFour);
        this.randomNumber = newNumber;
    }
    
}
