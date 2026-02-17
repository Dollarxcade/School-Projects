# School-Projects
These are projects that are worth sharing that I did in School.
## Number Guessing Game
> [!IMPORTANT]
> This project works only on console based IDE's that support alert.

A simple console-based number guessing game written in **JavaScript**, where the player tries to guess a randomly generated number between 1 and 100.

This was my first-ever coding project, made back in Grade 6 during the COVID-19 lockdowns. Even though it’s under school projects, I didn’t actually learn this in class but this was something I taught myself while online school was going on. While a lot of people were skipping classes to watch YouTube or play games, I ended up spending that time learning how to code instead.

It’s a very basic project, but it’s also the one that got me into programming in the first place, so it has a lot of sentimental value.

## Tic Tac Toe
> [!NOTE]
> Not functional right now.

A console-based Tic Tac Toe game written in **Python**, created during a Grade 8 coding club.

This was my first real attempt at using Python. The code isn’t fully functional — mostly due to the quality of instruction at the time but it still represents an important step in my learning process. You can see me experimenting with game logic, turns, and basic program structure for the first time.

This project is kept as a snapshot of where I was skill-wise at that point, not as a finished product.

## Grade 11 Computer Science Portal

This project is a console-based portal I built during **Grade 11 Computer Science** to make doing worksheets less annoying.

Instead of writing answers on paper and then checking them online, this portal lets everything be done directly through the console. Teachers can access the answers digitally, making the process faster and more organized. This wasn’t an official class assignment it used concepts well beyond what we were learning at the time but I built it because it solved a real problem I had.

The system is also easy to extend. If you want to add your own worksheet questions, you can do so by following the comments in the code.

## Volunteer Scheduler Documentation

This script was developed to assist school club executives (including me) in managing volunteer assignments effectively. It automates the process of organizing student volunteers into groups for workshops or events, ensuring that logistical constraints are met while maintaining fairness across the volunteer pool.

The script utilizes a scarcity optimization algorithm that prioritizes students with limited availability to ensure they have an opportunity to volunteer before flexible spots are filled. It maintains strict training date validation, grouping volunteers only if they share a common rehearsal or training date, and automatically excludes those who cannot attend any training sessions. To ensure fairness, a "max sessions" cap prevents individual volunteers from being over-scheduled, while grade-level pairing logic groups students of similar ages together to improve the social experience. Additionally, the script handles data integrity by automatically identifying the most recent response from students who may have submitted the form multiple times.

## Installation and Setup
1. **Install VS Code**: Download and install the application from the official website.
2. **Install Python Extension**: Open VS Code, click on the Extensions icon in the left sidebar, search for "Python," and click install.
3. **Install Pandas**: Open your terminal (or the terminal window in VS Code) and type the following command:
   `pip install pandas`

## Preparation
1. **Format the CSV**: Ensure your volunteer interest form results are saved as a `.csv` file with these specific columns:
   * Column A: Timestamp
   * Column B: Email Address
   * Column C: Full Name
   * Column E: Volunteer Availability (Dates separated by commas like Friday, November 16 in that exact format, no year, only one comma between day and month)
   * Column F: Training Availability (Dates separated by commas same format as above)
   * Column G: Grade Level
2. **Organize Files**: Create a new empty folder. Place the Python script and your formatted CSV file into this folder.

## How to Run
1. Open the folder containing the script and CSV in VS Code.
2. Open the script file.
3. Click the **triangle icon** (Play button) located in the top-right corner of the editor.
4. Follow the prompts in the console at the bottom of the screen:
   * Enter the number of groups per day.
   * Enter the number of people per group.
   * Enter the maximum number of sessions allowed per person.
5. Once completed, a new file named `final_volunteer_schedule.csv` will be generated in the same folder. This file contains the finalized schedule and reasons for any unassigned volunteers.

*Last updated 2026-02-17*
