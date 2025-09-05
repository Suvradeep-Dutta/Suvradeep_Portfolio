import java.util.Scanner;

public class DayOfTheWeek 
{
    public static void main()
    {
        Scanner sc= new Scanner(System.in);
        int ch;
        System.out.println("Enter 1 for Monday");
        System.out.println("Enter 2 for Tuesday");
        System.out.println("Enter 3 for Wednesday");
        System.out.println("Enter 4 for Thursday");
        System.out.println("Enter 5 for Friday");
        System.out.println("Enter 6 for Saturday");
        System.out.println("Enter 7 for Sunday");

        System.out.println("\n");

        System.out.println("Enter your choice: ");
        ch= sc.nextInt();

        switch(ch)
        {
            case 1:
                System.out.println("Monday");
                break;
            case 2:
                System.out.println("Tuesday");
                break;
            case 3:
                System.out.println("Wednesday");
                break;
            case 4:
                System.out.println("Thursday");
                break;
            case 5:
                System.out.println("Friday");
                break;
            case 6:
                System.out.println("Saturday");
                break;
            case 7:
                System.out.println("Sunday");
                break;
            default:
                System.out.println("Invalid choice!");

        }
        sc.close();

    }

}
