import java. util.Scanner;
public class ArrayBasics 
{
    public static void main()
    {
        Scanner sc = new Scanner(System.in);

        int n, i, ar[];

        System.out.println("Enter size of the array:");
        n= sc.nextInt();

        ar= new int[n];

        System.out.println("Enter elements in the array: ");
        for(i=0; i<n; i++)
        {
            ar[i]= sc.nextInt();
        }

        System.out.println("The elements of the array are:");

        for(i=0; i< n; i++)
        {
            System.out.println(ar[i]);
        }

        sc.close();
    }

}
