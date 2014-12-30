import java.io.File;
import java.util.Scanner;
import java.util.ArrayList;

//***********************************
//EffectsTest.java
//Jackie Luo (jhl2182)
//November 2014
//***********************************

//=================================================
//Objects of this class receive the number of PPM
//files and their names, add the files to an
//ArrayList, and receive the name for the new file,
//then calling the method filter() from the Effects
//class to filter out the unwanted images.
//=================================================
 
public class EffectsTest {
 
    public static void main(String[] args){ 
 
        Effects e = new Effects();
        ArrayList<File> fileList = new ArrayList<File>(); // The ArrayList holds the File objects
        int inputFiles = 0;
        String fileName = "";
        Scanner keyboard = new Scanner(System.in);
 
    // The user is asked to give the number of files so that
    // the correct number of files are requested, and then the
    // program gets the names for each file to add to the
    // ArrayList fileList
        System.out.println("Enter the number of input files: ");
        inputFiles = keyboard.nextInt();
        keyboard.nextLine();
        for(int n = 0; n < inputFiles; n++) {
            System.out.println("Enter file name: ");
            fileName = keyboard.nextLine();
            try {
                File f = new File(fileName);
                fileList.add(f);
                }
            catch (Exception ex) {
                ex.printStackTrace();
                }
            }
    
    // The user has the option to name the new file created
    // before the program calls the method filter() from
    // the Effects class
        System.out.println("Enter new file name: ");
        String newName = keyboard.nextLine();
        e.filter(fileList, newName);
    }
}