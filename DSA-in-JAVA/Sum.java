import java.util.Scanner;

public class Sum 
{
    public static void main(String[] args)
    {
        Scanner sc= new Scanner(System.in);
        int a, b, sum=0;
        System.out.println("Enter first Number:");
        a= sc.nextInt();
        System.out.println("Enter second number:");
        b=sc.nextInt();

        sum= a+b;
        System.out.println("SUM="+ sum);
        sc.close();


    }
    
    

}
