import java.util.Random;

//***********************************
//Deck.java
//Jackie Luo (jhl2182)
//November 2014
//***********************************

//=================================================
//Objects of this class handle the deck in the game
//of BlackJack, instantiating the full deck of cards,
//drawing cards from the deck, and shuffling the
//deck randomly.
//=================================================

public class Deck {

    private Card[] cards;
    private int cardsDrawn;
    private int top;

    // This constructor initializes the array cards (by
    // assigning 52 combinations of values and suits)
    // and the instance variables cardsDrawn and top
    public Deck(){
        cards = new Card[52];
        int x = 0;
        int[] values = {1,2,3,4,5,6,7,8,9,10,11,12,13};
        String[] suits = {"Clubs","Diamonds","Hearts","Spades"};
        for (int v = 0; v < 13; v++){
            for (int s = 0; s < 4; s++){
                cards[x] = new Card(values[v],suits[s]);
                x++;
            }
        }
        cardsDrawn = 0;
        top = 0;
    }

    // This method returns myCard of type Card, drawing the top
    // of the deck and then keeping track of which card is on top
    // within the array cards and how many cards have been drawn
    public Card draw(){
        Card myCard = cards[top++];
        cardsDrawn++;
        return myCard;
    }

    // This method shuffles the deck by using the Fisher-Yates
    // algorithm to randomize the order of the cards in the array
    // and then resets cardsDrawn to zero
    public void shuffle(){
        Random randomNumber = new Random();
        for (int i = cards.length - 1; i > 0; i--){
            int index = randomNumber.nextInt(i+1);
            Card x = cards[index];
            cards[index] = cards[i];
            cards[i] = x;
        }
        cardsDrawn = 0;
    }

    // This method returns the variable cardsDrawn
    public int getCardsDrawn(){
        return cardsDrawn;
    }

    // This method returns a string consisting of 52 lines, where
    // each line contains a description of the card in the deck at
    // the corresponding position (top-to-bottom)
    public String toString(){
        String deckOrder = "";
        for (int i = 0; i < 52; i++){
            deckOrder += this.cards[i].toString() + "\n";
        }
        return deckOrder;
    }

}
