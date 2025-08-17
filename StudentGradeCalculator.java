import java.util.Scanner;

public class StudentGradeCalculator {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("\n-: Welcome to \"Student Grade Calculator\" :-");  

        int totalMarks = 0;
        float avgPercentage;

        System.out.print("\nEnter the total number of Subjects: ");
        int subjects = sc.nextInt();

        if(subjects <= 0) {
            System.out.println("Subjects must be greater than 0.");
            return;
        }
        
        for(int i = 1; i <= subjects; i++) {
            System.out.printf("Enter marks of Subject %d (Out of 100): ", i);
            int marks = sc.nextInt();

            if(marks < 0 || marks > 100) {
                System.out.println("\nInvalid Input! Please enter correct marks.");
                i--;    // Ask for the current subject again
                continue;
            }
            totalMarks += marks;
        }
        System.out.println("\n----------------------------------");
        System.out.println("\nThe total marks obtained in all subjects is: " + totalMarks);

        avgPercentage = (float) totalMarks / subjects;
        System.out.println("Average Percentage: " + avgPercentage + "%");

        // Assign Grade 
        if(avgPercentage >= 90) {
            System.out.println("Grade 'O' (OUTSTANDING)");
        } else if(avgPercentage >= 80) {
            System.out.println("Grade 'E' (EXCELLENT)");
        } else if(avgPercentage >= 70) {
            System.out.println("Grade 'A' (AVERAGE)");
        } else if(avgPercentage >= 60) {
            System.out.println("Grade 'B' (BELOW AVERAGE)");
        } else if (avgPercentage >= 50) {
            System.out.println("Grade 'C' (GOOD)");
        } else {
            System.out.println("Grade 'D'! (Oops! Please improve yourself)");
        }

        sc.close();
        System.out.println("\n----------------------------------");
    }
    
}
