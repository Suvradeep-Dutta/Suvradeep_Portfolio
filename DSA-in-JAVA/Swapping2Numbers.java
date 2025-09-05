import java.util.Scanner;

public class Swapping2Numbers 
{
    public static void main()
    {
        int a, b;
        Scanner sc= new Scanner(System.in);

        System.out.println("Enter first numbers:");
        a= sc.nextInt();
        System.out.println("Enter second numbers:");
        b= sc.nextInt();

        a= a+ b;
        b= a- b;
        a= a- b;

        System.out.println("First numbers is: " + a);
        System.out.println("Second numbers is: " + b);

        sc.close();
    }

}
