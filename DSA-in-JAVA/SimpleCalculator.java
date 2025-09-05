import java.util.Scanner;

public class SimpleCalculator 
{
    public static void main(String[] args)
    {
        Scanner sc= new Scanner(System.in);
        double a, b;

        System.out.println("Enter 2 numbers");
        a= sc.nextDouble();
        b= sc.nextDouble();

        System.out.println("SUM= " + (a+b));
        
        if(a>b)
        System.out.println("Substraction= " + (a-b));
        else
        System.out.println("Substraction= " + (b-a));

        System.out.println("Product= " + (a*b));

        if(b != 0)
        System.out.println("Division= " + (a/b));

        sc.close();

    }


}
