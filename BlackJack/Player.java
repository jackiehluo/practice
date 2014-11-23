import java.util.ArrayList;

//***********************************
//Player.java
//Jackie Luo (jhl2182)
//November 2014
//***********************************

//=================================================
//Objects of this class handle the player's hand
//throughout each game of BlackJack by adding cards
//and showing the player her hand.
//=================================================

public class Player {

    private ArrayList<Card> hand; // The player's cards
    private int handTotal; // The total value of the hand

    // This constructor initializes the ArrayList hand for
    // the player and the instance variable handTotal
    public Player(){
        hand = new ArrayList<Card>();
        handTotal = 0;
    }

    // This method returns the variable handTotal for the
    // player's hand
    public int getTotal(){
        return handTotal;
    }

    // This method adds a card to the player's hand and
    // adjusts handTotal to account for the value of each
    // new card, with face cards equaling 10 and aces
    // equaling 1 or 11, depending on which brings the
    // total closest to 21 without going bust
    public void addCard(Card myCard){
        hand.add(myCard);
        if (myCard.getValue() > 10){
            handTotal += 10;
        }
        else if (myCard.getValue() == 1 && (handTotal + 11 <= 21)){
            handTotal += 11;
        }
        else {
            handTotal += myCard.getValue();
        }
    }
    
    // This method returns String playerHand, which
    // shows all of the cards that the player is
    // holding in a list
    public String showHand(){
        String playerHand = "";
        for (int i = 0; i <= (hand.size() - 1); i++){
            playerHand += hand.get(i).toString() + "\n";
        }
        return playerHand;
    }
    
}