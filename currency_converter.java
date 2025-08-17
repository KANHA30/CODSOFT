import java.util.Scanner;

public class currency_converter{
    public static void main(String[] args) {

       
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("-: Welcome to Currency Converter :-");
        System.out.println("1. USD to Rupee");
        System.out.println("2. Rupee to USD");
        System.out.println("3. Rupee to Ruble");
        System.out.println("4. Ruble to Rupee");
        System.out.println("5. Euro to Rupee");
        System.out.println("6. Rupee to Euro");
        System.out.print("Enter your choice (1 or 2 or 3 or 4 or 5 or 6): ");
        int choice = scanner.nextInt();

       
        if (choice == 1) {
            System.out.print("Enter the amount in USD: ");
            double USD = scanner.nextDouble();
            double Rupee = usdToRupee(USD);
            System.out.println("Converted amount in Rupee: " + Rupee);
        } 
        
        else if (choice == 2) {
            System.out.print("Enter the amount in Rupee: ");
            double Rupee = scanner.nextDouble();
            double USD = RupeeToUsd(Rupee);
            System.out.println("Converted amount in USD: " +USD);
        }


         if (choice == 3) {
            System.out.print("Enter the amount in Rupee: ");
            double Rupee = scanner.nextDouble();
            double Ruble = RupeeToRuble(Rupee);
            System.out.println("Converted amount in Ruble: " + Ruble);
        } 
        
        
        else if (choice == 4) {
            System.out.print("Enter the amount in Ruble: ");
            double Ruble = scanner.nextDouble();
            double Rupee = rubleToRupee(Ruble);
            System.out.println("Converted amount in Rupee: " +Rupee);
        }


            else if (choice == 5) {
                System.out.print("Enter the amount in EURO: ");
                double EURO= scanner.nextDouble();
                double Rupee = euroToRupee(EURO);
                System.out.println("Converted amount in USD: " +Rupee);
        } 


        else if (choice == 6) {
            System.out.print("Enter the amount in Rupee: ");
            double Rupee = scanner.nextDouble();
            double EURO = RupeeToEuro(Rupee);
            System.out.println("Converted amount in USD: " +EURO);
        }
       
        
        else {
            System.out.println("Invalid choice. Please select 1 or 2 or 3 or 4 or 5 or 6.");
        }

        scanner.close();
    }


    public static double usdToRupee(double USD) {
        return USD * 87.65;  // Date: 31/07/2025
    }
    public static double RupeeToUsd(double Rupee) {
        return Rupee * 0.0119804;  // Date 31/07/2025 
    }



    public static double RupeeToRuble(double Rupee) {
        return Rupee * 0.93;  // Date: 31/07/2025
    }
    public static double rubleToRupee(double ruble) {
        return ruble * 1.08;  // Date 31/07/2025 
    }




    public static double euroToRupee(double EURO) {
        return EURO *100.20;   //Date: 31/07/2025
    }
    public static double RupeeToEuro(double Rupee) {
        return Rupee *0.010;   //Date: 31/07/2025
    }

   
}
