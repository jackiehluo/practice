import java.util.ArrayList;

//***********************************
//Dealer.java
//Jackie Luo (jhl2182)
//November 2014
//***********************************

//=================================================
//Objects of this class handle the dealer's hand
//throughout each game of BlackJack by adding cards,
//showing one card to the player, and then showing
//the full hand after each hand.
//=================================================

public class Dealer {

    private ArrayList<Card> hand; // The dealer's cards
    private int handTotal; // The total value of the hand

    // This constructor initializes the ArrayList hand for
    // the dealer and the instance variable handTotal
    public Dealer(){
        hand = new ArrayList<Card>();
        handTotal = 0;
    }

    // This method returns the variable handTotal for the
    // dealer's hand
    public int getTotal(){
        return handTotal;
    }

    // This method adds a card to the dealer's hand and
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
    
    // This method returns String dealerCard, which
    // shows the player the dealer's first drawn
    // card
    public String showCard(){
        String dealerCard = hand.get(0).toString();
        return dealerCard;
    }
    
    // This method returns String dealerHand, which
    // shows all of the cards that the dealer is
    // holding in a list
    public String showHand(){
        String dealerHand = "";
        for (int i = 0; i <= (hand.size() - 1); i++){
            dealerHand += hand.get(i).toString() + "\n";
        }
        return dealerHand;
    }
    
}
