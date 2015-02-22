import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

public class ArtistPairs {

    public static void main(String[] args){
 
        Scanner input = new Scanner(System.in);
        String fileName = "";
        List<String> fullList = new ArrayList<String>();
        HashMap<String, Integer> counter = new HashMap<String, Integer>();
        List<String> popularArtists = new ArrayList<String>();
 
        System.out.println("Enter file name for lists of artists: ");
        fileName = input.nextLine();
        try {
            File f = new File(fileName);
            }
        catch (Exception ex) {
            ex.printStackTrace();
            }
 
        System.out.println("Enter new file name for popular pairs of artists: ");
        String newName = keyboard.nextLine();
        
        System.out.println(popularArtists);
        
        input.close();
    }
 
    public void readFile(){
        ArrayList<String>tmpList = new ArrayList<String>();
        try {
            Scanner fileInput = new Scanner(new FileReader(f));
        }
        catch (Exception ex) {
            ex.printStackTrace();
        }
        while(fileInput.hasNextLine()) {
            String tmpLine = fileInput.nextLine();
            tmpList.add(tmpLine);
        }
        fullList.add(tmpList);
    }
 
    public void countArtists(){
        for(int i = 0; i < 1000; i++){
            String line = input.nextLine();
            List<String> favoriteArtists = Arrays.asList(line.split(","));
            for (int j = 0; j < favoriteArtists.size(); j++){
                if (counter.containsKey(favoriteArtists.get(j))){
                    int current = counter.get(favoriteArtists.get(j));
                    counter.put(favoriteArtists.get(j), current + 1);
                    if (current + 1 == 50){
                        popularArtists.add(favoriteArtists.get(j));
                    }
                }
                else {
                    counter.put(favoriteArtists.get(j), 1);
                }
            }
        }
    }
}