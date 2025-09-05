import java.util.Scanner;

public class Array_Even_Odd 
{
    public static void main()
    {
        int ar[],n, i, e=0, o=0;
        Scanner sc= new Scanner(System.in);

        System .out.println("Enter the size of the array:");
        n= sc.nextInt();

        ar= new int[n];

        System.out.println("Enter elements in the array:");
        for(i=0; i<n;i++)
        {
            ar[i]= sc.nextInt();
        }

        for(i=0; i<n; i++)
        {
            if(ar[i]% 2== 0)
            e++;
            else
            o++;
        }

        System.out.println("Total number of Even elements in the array: " + e);
        System.out.println("Total number of Odd elements in the array: " + o);

        sc.close();
    }

}
