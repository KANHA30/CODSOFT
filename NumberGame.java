import java.util.Random;
import java.util.Scanner;

public class NumberGame {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
    
        String playAgain = "yes";
        int roundsWon = 0;
        int totalRounds = 0;
        
        System.out.println("\n----- Welcome to \"Number Game\" -----");
        
        while(playAgain.equalsIgnoreCase("yes")) {
            System.out.println("\nNew round started! Try to guess the number between 1 and 100.");

            Random rand = new Random();
            int generatedNumber = rand.nextInt(100) + 1;    // Generates a random number between 1 and 100

            int maxAttempts = 10;
            boolean guessedCorrectly = false;
            totalRounds++;

            for(int attempts = 1; attempts <= maxAttempts; attempts++) {
            System.out.print("Attempt " + attempts + ":-" + " Enter your guess: ");
            int userGuess = sc.nextInt();
            sc.nextLine();

            if(userGuess == generatedNumber) {
                System.out.println("\nCongrats! You guessed the correct number in " + attempts + "th attempt.");
                guessedCorrectly = true;
                roundsWon++;    // User won the round 
                break;
            } else if(userGuess > generatedNumber) {
                    System.out.println("Your guess is too HIGH.");
            } else if(userGuess < generatedNumber) {
                    System.out.println("Your guess is too LOW.");
            } 

            if(attempts == maxAttempts) {
                System.out.println("\nYou have used all your attempts. The generated number was " + generatedNumber);
            }
        }

        // Asking user if he want to play again
        System.out.println("\nDo you want to play again? (yes/no): ");
        playAgain = sc.nextLine();
    }

        // Displaying score after exiting the game
        System.out.println("\n----- Game Over -----");
        System.out.println("Total Rounds Played: " + totalRounds);
        System.out.println("Rounds Won: " + roundsWon);
        System.out.println("\nThanks for playing!");

        sc.close();
    }
}
