import java.util.Scanner;
public class Factorial 
{
    public static void main()
    {
        Scanner sc= new Scanner(System.in);
        int n, fact= 1, i= 1;

        System.out.println("Enter a number: ");
        n= sc.nextInt();
        do
        {
            fact= fact* i;
            i++;
        }
        while( i<= n);

        System.out.println("The factorial of the number is: " + fact);
        
        sc.close();



    }

}
