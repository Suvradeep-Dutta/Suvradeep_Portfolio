import java.util.Scanner;
public class Print_N_Natural_Numbers 
{
    public static void main(String[] args)
    {
        Scanner sc= new Scanner(System.in);
        int n, i; 

        System.out.println("Enter upper limit: ");
        n= sc.nextInt();

        for(i= 1; i<= n; i++)
        {
            System.out.println(i);
        }

        sc.close();
    }

}
