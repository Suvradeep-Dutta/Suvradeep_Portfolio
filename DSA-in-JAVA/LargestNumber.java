import java.util.Scanner;

public class LargestNumber 
{
    public static void main()
    {
        Scanner sc= new Scanner(System.in);
        int a, b;

        System.out.println("Enter two n numbers:");
        a= sc.nextInt();
        b= sc.nextInt();

        if (a>b)
        System.out.println("First number is the largest number.");

        else if (b>a)
        System.out.println("Second number is the largest number.");

        else
        System.out.println("Both numners are equal.");

        sc.close();
    }

}
