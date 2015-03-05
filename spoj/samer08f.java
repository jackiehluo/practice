import java.util.Scanner;

class Squares {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        boolean run = true;

        while(run == true) {
            int n = input.nextInt();
            if(n == 0) {
                run = false;
            }
            else {
                int squares = 0;
                for(int i = 0; i < n + 1; i++) {
                    squares += i * i;
                }
                System.out.println(squares);
            }

        }

        input.close();

    }

}