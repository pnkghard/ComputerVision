/*
Corona Fine :
The government has asked to organise social functions with a limited capacity of 100 people because of the COVID. 
People have not taken the guidelines seriously and as a result, various states are seeing an increase in the number of corona cases. 
The government has decided to impose fines now on the defaulters and new guidelines have been proposed.

Guidelines for the fine:
The number of people is less than or equal to 100. No fine will be imposed on anyone.

The number of people is between 101 to 200. The fine will be collected and a warning will be given. The fine will be collected as 
follows:
    Fine = (Number of people - 100) * 500

The number of people is greater than 200. The fine will be imposed and the case will be registered. 
The fine will be collected as follows:
    Fine = (Number of people - 100) * 1000


Example:    1.
            Number of people, N = 70
            Fine = 0
            Action = No Fine

            2. 
            Number of people, N = 150
            Fine = (150 - 100) * 500 = 25000
            Action = Warning

            3.
            Number of people, N = 300
            Fine = (300 - 100) * 1000 = 200000
            Action = Register Case


The government is asking for a program which can calculate the fine and the action required for the given number of people attending 
the function. Can you do it?

Input Format: The only line of input consists of the number of people in the function, N

Constraints:    1<= N <=1000

Output Format: Print the fine and the action required space-separately.

Sample TestCase 1:
    Input : 70
    Output: 0 No Fine
Sample TestCase 2:
    Input:  150
    Output: 25000 Warning
Sample TestCase 3:
    Input:300
    Output: 200000 Register Case
*/

import java.io.*;
import java.util.*;

public class CoronaFine {
    public static void main(String args[] ) throws Exception {

        Scanner sc = new Scanner(System.in);

        int people = sc.nextInt();

        int fine = 0;

        if( people <= 100) {
            System.out.println(fine + " No Fine");
        } else if (people > 100 && people <= 200) {
            fine = (people - 100) * 500;
            System.out.println(fine + " Warning");
        } else if (people > 200) {
            fine = (people - 100) * 1000;
            System.out.println(fine + " Register Case");
        }

    }
    
}