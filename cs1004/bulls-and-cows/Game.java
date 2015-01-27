import java.util.Scanner;

//***********************************
// Game.java
// Jackie Luo (jhl2182)
// October 2014
//***********************************

//===============================================
// Objects of this class start the game of Bulls
// and Cows, accept the user input, and print the
// number of bulls and cows from the Oracle class.
//===============================================

public class Game{

    private int turns;
    private Oracle computer;
    private Scanner input;
    private String guess;

    // This constructor initializes the instance variable
    // turns and an instance of the Oracle class
    public Game(){
    // your code for the Game constructor goes here
        this.turns = 0;
        this.computer = new Oracle(guess);
    }

    // This method begins the game by calling chooseNumber()
    // in the Oracle class to generate the computer's choice
    // and calling playOneTurn() until the user guesses the
    // right number, then printing the number of turns taken
    public void playGame(){
        computer.chooseNumber();
        System.out.println("Welcome to Bulls and Cows! Please enter a"
            + " four-digit number.");
        do {
            turns++;
            playOneTurn();
        } while (computer.howManyBulls(guess) < 4);
        if (computer.howManyBulls(guess) == 4){
            System.out.println("Congratulations, you guessed the number in " +
                turns + " turns!");  
        }
    }

    // This method plays one turn by accepting the user's
    // input for the four-digit guess, then printing the
    // number of bulls and cows for that guess
    public void playOneTurn(){
        input = new Scanner(System.in);
        guess = input.next();
        if (guess.length() != 4){
            System.out.println("That was not a four-digit number!");
            playOneTurn();
        }
        System.out.println(computer.howManyBulls(guess) + " bulls and "
            + computer.howManyCows(guess) + " cows");
    }

    // This method is a mutator used to test the code
    public void setPattern(String solution){
        computer.setPattern(solution);
    }

    // This method is an accessor used to test the code
    public String getPattern(){
        return computer.getPattern();
    }

}