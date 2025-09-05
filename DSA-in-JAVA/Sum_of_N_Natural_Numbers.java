import java.util.Scanner;

public class Sum_of_N_Natural_Numbers 
{
    public static void main()
    {
        int n, sum =0, i=1;

        Scanner sc= new Scanner(System.in);

        System.out.println("Enter upper limit:");
        n= sc.nextInt();

        while(i<=n)
        {
            sum= sum+ i;
            i++;
        }

        System.out.println("SUM= " + sum);

        sc.close();
    }

}
