import textio.TextIO;

public class threeNPlus1Problem {
    public static void main(String[] args) {

        int userInt;        // user start point
        int counter = 0;

        System.out.println("This program takes an integer and uses it in the 3n + 1 algorithm.");
        System.out.print("What number greater than 1 did you want to start with? > ");
        userInt = TextIO.getInt();
        System.out.println();

        /*
        Start the loop
         */


        if (userInt < 2) {
            System.out.println("This is an unacceptable entry.");
        } else {
            System.out.println("You have chosen " + userInt + " so here we go!");
            while (userInt != 1) {

                if (userInt % 2 == 0) {
                    userInt /= 2;
                } else {
                    userInt = userInt * 3 + 1;
                }
                System.out.print(userInt + " ");
                counter++;
            }
            System.out.println("\nWe've reached the number 1 in " + counter + " tries!");
        }
    }

}
