import java.util. Scanner;

public class LinearSearch
{
    public static void main()
    {
        Scanner sc= new Scanner(System.in);
        int n, ar[], e, i, index= -1;

        System .out.println("Enter size of the array:");
        n= sc.nextInt();

        ar= new int[n];

        System.out.println("Enter elements in the array:");
        for(i=0; i<n; i++)
        {
            ar[i]= sc.nextInt();
        }

        System.out.println("Enter elemnt to search:");
        e= sc.nextInt();

        for(i=0; i<n; i++)
        {
            if(ar[i]== e)
            {
                index= i;
                break;
            }
        }

        if (index != -1)
        {
            if(index== 1)
            System.out.println("The element was found in the array at " + i + "st index.");
            else if(index== 2)
            System.out.println("The element was found in the array at " + i + "nd index.");
            else if(index== 3)
            System.out.println("The element was found in the array at " + i + "rd index.");
            else
            System.out.println("The element was found in the array at " + i + "th index.");
        }
        
        else
        System.out.println("Element is not present in the array.");

        sc.close();
    }
}
