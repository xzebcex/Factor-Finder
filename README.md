# Factor Finder
This script determines the factors of a positive whole integer.

## How to Use
1.	Launch the application.
2.	When prompted, provide a positive whole number to factor.
3.	The application will display the factors of the number you supplied.
4.	At the prompt, type 'Q' to exit the application.

## Definition of Factors
The factors of a number are two numbers that, when multiplied together, give the number. 2 x 13 = 26, for example, therefore 2 and 13 are factors of 26. Since 1 x 26 = 26, 1 and 26 are both factors of 26. 26 is said to have four factors: 1, 2, 13, and 26.

## How the Program Works
The script use a while loop to repeatedly request the user for input until the user presses the 'Q' key to exit. If the user provides a valid positive whole integer, the program uses a for loop and the math module to discover its factors. The script then eliminates and organizes the duplicate factors before showing them to the user.
Note:Please keep in mind that the script only works with positive full numbers. If the user submits an invalid input, the program will prompt them again until they enter an acceptable input.
