alu-scripting
Regular Expression - README
This repository contains a collection of Ruby scripts that use regular expressions to match specific patterns. Each script corresponds to a task with its own requirements and examples.

Getting Started
To get started, make sure you have Ruby installed on your system. These scripts are designed to work with the Oniguruma regular expression library, which is the default library used by Ruby.

Installation
Clone the repository to your local machine:
git clone https://github.com/davyleroy/alu-scripting.git
Change into the regular_expressions directory:
cd alu-scripting/regular_expressions
Usage
Each task has its own Ruby script file. You can run the scripts by providing command-line arguments to match against the regular expressions.

For example, to run the 0-simply_match_school.rb script and match the string "School," use the following command:

ruby 0-simply_match_school.rb School
This will execute the script and display the output based on whether the regular expression matches the input string.

Make sure to replace the script name and argument value according to the specific task you want to run.

Tasks Overview
Task 0: Simply Matching School
In this task, the regular expression should match the string "School." The provided Ruby script accepts one argument and passes it to a regular expression matching method.

Task 1: Repetition Token #0
The regular expression should match cases containing repetitive sequences of "01" followed by a "0." The provided Ruby script accepts one argument and passes it to a regular expression matching method.

Task 2: Repetition Token #1
The regular expression should match cases containing repetitive sequences of "0" followed by a "1" and "1" followed by a "0." The provided Ruby script accepts one argument and passes it to a regular expression matching method.

Task 3: Repetition Token #2
The regular expression should match cases containing repetitive sequences of "b" followed by any number of "a." The provided Ruby script accepts one argument and passes it to a regular expression matching method.

Task 4: Repetition Token #3
The regular expression should match cases containing repetitive sequences of "t" followed by any number of "n." The regular expression should not use square brackets. The provided Ruby script accepts one argument and passes it to a regular expression matching method.

Task 5: Not Quite HBTN Yet
The regular expression should match strings that start with "h," end with "n," and can have any single character in between. The provided Ruby script accepts one argument and passes it to a regular expression matching method.

Task 6: Call Me Maybe
The regular expression should match 10-digit phone numbers. The provided Ruby script accepts one argument and passes it to a regular expression matching method.

Task 7: OMG WHY ARE YOU SHOUTING?
The regular expression should match strings consisting only of capital letters. The provided Ruby script accepts one argument and passes it to a regular expression matching method.

Task 8: TextMe
The script processes a log file containing text message transactions and extracts specific information (sender, receiver, and flags). The provided Ruby script accepts the log file path as an argument and outputs the required information.

Task 9: Pass LinkedIn Technical Interview Level 0
This task requires solving LinkedIn's regex puzzle. Instructions are provided in the script file. Take a screenshot of the "Congratulations" screen with the date and time of completion and provide it as an answer file.

Resources
For further understanding of regular expressions and how to use them effectively, you can refer to

the following resources:

Regular expressions - basics
Regular expressions - advanced
Rubular - a helpful tool for testing and visualizing regular expressions
Use a regular expression against a problem: now you have 2 problems
Learn Regular Expressions with simple, interactive exercises
Repository Structure
0-simply_match_school.rb: Ruby script for Task 0.
1-repetition_token_0.rb: Ruby script for Task 1.
2-repetition_token_1.rb: Ruby script for Task 2.
3-repetition_token_2.rb: Ruby script for Task 3.
4-repetition_token_3.rb: Ruby script for Task 4.
5-beginning_and_end.rb: Ruby script for Task 5.
6-phone_number.rb: Ruby script for Task 6.
7-OMG_WHY_ARE_YOU_SHOUTING.rb: Ruby script for Task 7.
8-textme.rb: Ruby script for Task 8.
9-passed_linkedin_regex_challenge.jpg: Screenshot of completion for Task 9.
Contributing
Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or a pull request in the repository.

License
This project is licensed under the MIT License.
