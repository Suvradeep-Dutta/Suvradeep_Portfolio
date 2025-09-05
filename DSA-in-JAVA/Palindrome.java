import java.util.Scanner;
public class Palindrome 
{
    public static void main()
    {
        Scanner sc= new Scanner(System.in);
        int n, num=0, rev=0, r=0;

        System.out.println("Enter a number: ");
        n= sc.nextInt();

        num= n;

        while(n> 0)
        {
            r= n% 10;
            rev= rev* 10+ r;
            n= n/ 10;
        }

        if(num== rev)
        System.out.println("The number is Palindrome.");

        else
        System.out.println("The number is not Palindrome.");

        sc.close();
    }

}
