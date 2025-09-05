import java.util.Scanner;

public class Array_MaxMin 
{
    @SuppressWarnings("resource")
    public static void main()
    {
        Scanner sc= new Scanner(System.in);
        int n, ar[], i, max=0, min=0;

        System.out.println("Enter size of the array:");
        n= sc.nextInt();

        ar= new int[n];

        System.out.println("Enter elements in the array:");
        for(i=0; i<n; i++)
        {
            ar[i]= sc.nextInt();
        }

        max= ar[0];
        min= ar[0];
        for(i=1; i<n; i++)
        {
            if(ar[i]> max)
            max= ar[i];
            if(ar[i]< min)
            min= ar[i];
        }

        System.out.println("Greatest element:" + max);
        System.out.println("Smallest element:" + min);

        sc.close();
    }

}
