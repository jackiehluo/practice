import java.util.Scanner;

//***********************************
//Game.java
//Jackie Luo (jhl2182)
//November 2014
//***********************************

//=================================================
//Objects of this class start the game of BlackJack,
//accept the user input (choosing to hit or stand),
//and print the results of the game after each hand
//between the player and the dealer.
//=================================================

public class Game {

    private Deck deck;
    private Player player;
    private Dealer dealer;
    private Scanner input;

    // This constructor initializes the instances of
    // Deck, Player, and Dealer classes
    public Game(){
        deck = new Deck();
        player = new Player();
        dealer = new Dealer();
        }

    // This method begins the game by welcoming the user and
    // calling the method playHand(), and after each hand, the
    // user is given the option to play again
    public void play(){
        System.out.println("Welcome to BlackJack! Let's begin.");
        playHand();
        System.out.println("Would you like to play again?");
        input = new Scanner(System.in);
        String replay = input.next();
        if (replay.equals("yes")){
            play();
        }
    }
    
    // This method plays one hand by calling shuffle() from the
    // class Deck, drawing cards for the player and dealer
    // and adding them to their respective hands, showing the player
    // her hand and one card from the dealer's hand, and then
    // calling methods askPlayer(), playDealer(), and getResult();
    // at the end of the method, new instances of Player() and
    // Dealer() allow the game to start as new
    public void playHand(){
        deck.shuffle();
        player.addCard(deck.draw());
        player.addCard(deck.draw());
        System.out.println("Here's your hand:\n" + player.showHand());
        dealer.addCard(deck.draw());
        dealer.addCard(deck.draw());
        System.out.println("Here's one of the dealer's cards:\n" +
                dealer.showCard());
        askPlayer();
        playDealer();
        getResult();
        player = new Player();
        dealer = new Dealer();
    }
    
    // This method asks the player whether they want to hit or
    // stand, and the player is allowed to hit as long as her
    // hand total is under 21
    public void askPlayer(){
        if (player.getTotal() < 21){
            System.out.println("Would you like to hit or stand?");
            input = new Scanner(System.in);
            String choice = input.next();
            if (choice.equals("hit")){
                player.addCard(deck.draw());
                System.out.println("Here's your hand:\n" + player.showHand());
                askPlayer();
            }
            else if (choice.equals("stand")){
                System.out.println("Your hand total: " + player.getTotal());
            }
            else {
                System.out.println("Please choose to either hit or stand!");
                askPlayer();
            }
        }
    }
    
    // This method plays the dealer by hitting (adding cards to
    // the dealer's hand while its total is equal to or less than
    // 16) or standing (while the hand total is 17 or greater)
    public void playDealer(){
        while (dealer.getTotal() <= 16){
            dealer.addCard(deck.draw());
        }
    }
    
    // This method shows the result of the game by printing the
    // dealer's hand and total and whether the player wins, loses,
    // or ties with the dealer, depending on the final totals
    public void getResult(){
        System.out.println("The dealer's total:\n" + dealer.getTotal());
        System.out.println("The dealer's hand:\n" + dealer.showHand());
        if (player.getTotal() <= 21 && player.getTotal() > dealer.getTotal()){
            System.out.println("You win!");
        }
        else if (player.getTotal() <= 21 && dealer.getTotal() > 21){
        	System.out.println("The dealer went bust. You win!");
        }
        else if (player.getTotal() <= 21 && player.getTotal() ==
                dealer.getTotal()){
            System.out.println("The game is a tie.");
        }
        else if (dealer.getTotal() <= 21 && player.getTotal() <
                dealer.getTotal()){
            System.out.println("The dealer wins!");
        }
        else {
            System.out.println("You went bust. The dealer wins!");
        }
    }
    
}