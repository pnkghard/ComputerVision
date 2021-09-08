/*

Varun has got a date after a long time and wants to look his best for his partner. He decides to go shopping to buy a new t-shirt 
and a pair of jeans but since it is the month’s end, he has a budget of only B rupees. He wants to spend the maximum money on jeans 
and t-shirt combo within the given budget. The problem is that he is good with his cloth choices but not with the calculations and 
asks for your help. 

Varun has selected T t-shirts and J jeans. He provides you the prices of each of them and you have to determine the maximum 
money he can spend shopping. If it is not possible to buy the jeans and t-shirt with the given budget, you can tell him -1.


Example:    1. 
            Budget, B = 20
            Jeans, Ji = [ 10, 5, 8 ]
            T-shirts, Ti = [ 11, 7, 4 ]
            The maximum money he can spend is 19 by buying the J3 jeans along with the T1 t-shirt.

            2.
            Budget, B = 10
            Jeans, Ji = [ 8 , 9 , 10 ]
            T-shirt, Ti = [ 4, 6, 3 ]
            With the given budget, it is not possible for Varun to buy the jeans and t-shirt both. Thus, the maximum money he can spend is -1.


Can you help him shop and get ready for his date?



Input Format :  The first line of input consists of the Budget, B
                The second line of input consists of the number of jeans (J) and number of t-shirts (T) space-separately.
                The third line of input consists of the J space-separated jeans prices, Ji
                The fourth line of input consists of the T space-separated t-shirt prices, Ti

Constraints:    1<= B <=10^6
                1<= J, T <=1000
                1<= Ji, Ti =10^6

Output Format:  Print the maximum money Varun can spend shopping.

Sample TestCase 1:
Input:  10
        3 3
        5 7 9
        6 2 7
Output: 9

Explanation :   The maximum money can be spent by selecting J2 jeans and T2 t-shirt.
                Maximum money  = 7 + 2 = 9

*/


import java.io.*;
import java.util.*;

public class DateShopping {

    

    static int maxBudget(int j[], int t[], int l, int k, int max, int B) {

        

        for(int m=0; m<l; m++) {
            int avg = 0;
            for(int n=0; n<k; n++) {
                avg = j[m] + t[n];
                if (avg > max && avg <= B) {
                    max = avg;
                }
            }
            
        }
        return max;

    }

    public static void main(String args[] ) throws Exception {

    	Scanner sc = new Scanner(System.in);

        int B = sc.nextInt();
        int J, T;
        J = sc.nextInt();
        T = sc.nextInt();

        int Jeans[] = new int[J];
        int TShirt[] = new int[T];

        for(int i=0; i<J; i++) {
            Jeans[i] = sc.nextInt();
        }

        for(int i=0; i<T; i++) {
            TShirt[i] = sc.nextInt();
        }

        int max = -1;

        

        System.out.println(maxBudget(Jeans, TShirt, J, T, max, B));

   }
   
    
}




/*
20
3 3
10 5 8
11 7 4
19

10
3 3
8 9 10
4 6 3
-1

10
3 3
5 7 9
6 2 7
9
*/