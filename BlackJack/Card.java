// To help get you started we have completed this class for you 
// Leave this class as it is.

public class Card {

    private String suit;
    private int value;

    public Card(int aValue, String aSuit){
    value=aValue;
    suit=aSuit;
    }

    public String toString(){
    String myCard;

    if(value==1)//if the card is an Ace
        myCard="Ace of ";
    else if(value==11)//Jack
        myCard="Jack of ";
    else if(value==12)//Queen
        myCard="Queen of ";
    else if(value==13)//King
        myCard="King of ";
    else //any number/suit between 2-10
            myCard=value +" of ";

        //Adds the suit type to the card value
    myCard+=suit;

    return myCard;
    }

    public int getValue(){
    return value;
    }
}
