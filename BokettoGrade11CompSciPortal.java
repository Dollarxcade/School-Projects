import java.util.*;

public class WorksheetPortal extends ConsoleProgram {

    private Map<String, Runnable> questions = new HashMap<>();

    public void run() {
        setupQuestions();
        
        while (true) {
            printMenu();
            String choice = readLine("Enter Day Number (or 'q' to quit): ");
            if (choice.equalsIgnoreCase("q")) {
                println("Exiting program. Goodbye!");
                break;
            }
            String qnum = readLine("Enter Question Number: ");
            for (int i = 0; i < 8; i++) {
            println();
            }
            String key = choice + "-" + qnum;
            
            clearConsole();
            
            if (questions.containsKey(key)) {
                questions.get(key).run();
                String again = readLine("\nRun again (r), go to menu (m), or quit (q)? ");
                if (again.equalsIgnoreCase("q")) {
                    break;
                } else if (again.equalsIgnoreCase("r")) {
                    clearConsole();
                    questions.get(key).run();
                }
            } else {
                println("That question is not available yet.");
            }
        }
    }

    private void setupQuestions() {
        questions.put("0-0", () -> {
            System.out.print("Hello world!");
        });
        
        questions.put("19-13", () -> {
            String school = "Glenforest";
            String address = "3575 Fieldgate Dr.";
            String name = readLine("Name: ");
            int age = readInt("Age: ");
            int grade = readInt("Grade: ");
            System.out.print("Student " + name + ", age " + age + ", in grade ");
            System.out.print(grade + ", has been registered at " + school);
            System.out.print(". The school address is " + address);
        });
        
        questions.put("20-4", () -> {
            System.out.println("Only answer with true/false all lower case");
            println();
            boolean choresDone = readBoolean("Chores done? ");
            boolean wantGame = readBoolean("Want game? ");
            boolean playGame = choresDone && wantGame;
            System.out.print("Play game? " + playGame);
        });
        
        questions.put("20-12", () -> {
            System.out.println("Only answer with true/false all lower case");
            System.out.println();
            boolean homeworkDone = readBoolean("Home work done? ");
            boolean cleanedRoom = readBoolean("Cleaned room? ");
            boolean friendHome = readBoolean("Is friend home? ");
            boolean permission = readBoolean("Did you ask mom for permission and did she say yes? ");
            boolean goToFriend = homeworkDone && cleanedRoom && friendHome && permission;
            if(goToFriend == true)
            {
                System.out.print("You can go to your friend's house");
            }
            else
            {
                System.out.print("No, you can't go to your friend's house");
            }
        });
        
        questions.put("21-9", () -> {
            System.out.print("Valid weight?"+ !true);
        });
    }

    private void printMenu() {
        clearConsole();
        println("=== Worksheet Portal ==========================");
        println();
        println("Made with <3 by Shafan 'Boketto' Khaja");
        println("https://github.com/Dollarxcade");
        println();
        println("Type a Day Number and a Question Number to run.");
        println("Or type 'q' to quit.");
    }

    private void clearConsole() {
        for (int i = 0; i < 26; i++) {
            println();
        }
        println("===============================================");
    }
}

//Last updated 2025-10-05
