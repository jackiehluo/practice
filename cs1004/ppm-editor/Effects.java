import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

//***********************************
//Effects.java
//Jackie Luo (jhl2182)
//November 2014
//***********************************

//=================================================
//Objects of this class receive the inputs from the
//EffectsTest class and compares the files line by
//line to filter the unwanted images using majority
//rules.
//=================================================
 
public class Effects {

    private ArrayList<File> fileList; // The File objects received from user
    private ArrayList<ArrayList<String>> listList; // List of contents of files

    // This constructor initializes the ArrayList fileList, which contains
    // the File objects that the user indicated in the EffectsTest class,
    // and the ArrayList listList, an ArrayList that contains ArrayLists
    // with the contents of each file
    public Effects() {
        fileList = new ArrayList<File>();
        listList = new ArrayList<ArrayList<String>>();
    }

    // This method adds the contents of the files to ArrayList listList,
    // using the ArrayList tmpList to store lines before adding them to
    // to listList
    public void addInputs() {
        Scanner fileInput = null;
        for(int n = 0; n < fileList.size(); n++) {
            ArrayList<String>tmpList = new ArrayList<String>();
            try {
                fileInput = new Scanner(new FileReader(fileList.get(n)));
            }
            catch (Exception ex) {
                ex.printStackTrace();
            }
            while(fileInput.hasNextLine()) {
                String tmpLine = fileInput.nextLine();
                tmpList.add(tmpLine);
            }
        listList.add(tmpList);
        }
    }

    // This method filters the unwanted images out of the photo and
    // writes the new file with the given file name
    public void filter(ArrayList<File> fileList, String newName) {
        FileWriter fw = null;
        try {
            fw = new FileWriter(newName);
        }
        catch (Exception ex) {
            ex.printStackTrace();
        }
        ArrayList<String>tmpList = new ArrayList<String>();
        this.fileList = fileList;
        this.addInputs();
        ArrayList<String> lineList = new ArrayList<String>();
        for(int i = 0; i < listList.get(0).size(); i++) {
            lineList = new ArrayList<String>();
            for(int j = 0; j < listList.size(); j++) {
                tmpList = listList.get(j);
                String line = tmpList.get(i);
                System.out.println(line);
                lineList.add(line);
            }
            Collections.sort(lineList);
            int max = 0;
            String current = "";
            String correctLine = "";
            int count = 0;
            for(int n = 0; n < lineList.size() - 1; n++) {
                current = lineList.get(n);
 
                if (lineList.get(n) == lineList.get(n + 1)) {
                    count++;
                }
                else {
                    count = 1;
                }
 
                if (count > max) {
                    max = count;
                    correctLine = current;
                }
            }
 
            try {
                fw.write(correctLine + "\n");
            }
            catch (Exception ex) {
                ex.printStackTrace();
            }
        }
        try {
            fw.close();
        }
        catch (Exception ex) {
            ex.printStackTrace();
        }
    }
}