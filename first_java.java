import java.util.Scanner;


public class first_java {
  @SuppressWarnings("resource")
  public static void main(String[] args) {

    Scanner myObj = new Scanner(System.in);
    String userName;
    System.out.println("Enter username: ");
    userName = myObj.nextLine();
    userName = userName.toLowerCase();

    if ("henry".equals(userName)) {
      System.out.println("Welcome Henry!");
    } else {
      System.out.println("Your not henry!");
    }

    System.out.println();

    Scanner myO = new Scanner(System.in);
    int age;
    System.out.println("Enter your age:");
    age = myO.nextInt();

    if (age >= 18){
      System.out.println("You can vote!");
    } else{
      System.out.println("You cannot vote!");
    }

    System.out.println();

    Scanner myOb = new Scanner(System.in);
    String password;
    System.out.println("Enter your password: ");
    password = myOb.nextLine();
    password = password.toLowerCase();

    if ("jugs".equals(password)){
      System.out.println("Good password!");
    } else{
      System.out.println("Bad password");
    }

    System.err.println();

    Scanner myN = new Scanner(System.in);
    String LastName;
    System.out.println("What is your last name? ");
    LastName = myN.nextLine();
    LastName = LastName.toLowerCase();

    if ("beachum".equals(LastName)){
      System.out.println("We are related!");
    }  else {
      System.out.println("We are not related!");
    }

    System.err.println();

    System.out.println("Age is: " + age + "," + " Username is: " + userName + "," + " Password is: " + password + ", " + "Last name is: " + LastName);
  }
}

 