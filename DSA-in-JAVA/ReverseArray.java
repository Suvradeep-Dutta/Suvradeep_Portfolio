import java.util.Scanner;

public class ReverseArray 
{
    public static void main()
    {
        Scanner sc= new  Scanner(System.in);
        int n, ar[],i;

        System.out.println("Enter the size of the array:");
        n= sc.nextInt();

        ar= new int[n];

        System.out.println("Enter elements in the array:");
        for(i=0; i<n; i++)
        {
            ar[i]= sc.nextInt();
        }

        System.out.println("The array in reverse order:");
        for(i=n-1; i>=0; i--)
        {
            System.out.println(ar[i]);
        }

        sc.close();
    }
    
}
