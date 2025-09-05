import java.util.Scanner;

public class BasicDetailsInput 
{
    public static void main(String[] args)
    {
        String name;
    int age;
    Scanner sc= new Scanner(System.in);

    System.out.println("Enter your name: ");
    name= sc.nextLine();

    System.out.println("Enter your age: ");
    age= sc.nextInt();


    System.out.println(" Hello " + name + ". You are " + age + " years old.");

    sc.close();

    }
    
}
