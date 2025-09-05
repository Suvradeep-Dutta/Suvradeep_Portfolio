import java.util.Scanner;

public class Array_Sum_Avg 
{
    @SuppressWarnings("resource")
    public static void main()
    {
        Scanner sc= new Scanner(System.in);
        
        int n, i, ar[], sum=0;
        double avg=0;

        System.out.println("Enter size of the array:");
        n= sc.nextInt();

        ar= new int[n];

        System.out.println("Enter elements in the array:");
        for(i=0; i<n; i++)
        {
            ar[i]= sc.nextInt();
        }


        for(i=0;i<n; i++)
        {
            sum= sum+ ar[i];
        }

        avg= sum/ n;

        System.out.println("SUM of the elements of the array= " + sum);
        System.out.println("Average= " + avg);

        sc.close();
    }

}
