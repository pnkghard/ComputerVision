/*
Sports Tournament :
The company XYZ is hosting a cricket tournament for its employees. The teams are to be built by different departments and the 
format of the tournament will be knockout. The HR lead is busy with preparations and has done all the promotions. The sponsors are 
very keen for the tournament and have raised queries about it. The sponsors have asked about the number of matches that needs to be 
played. It is where the HR executive is unable to help as he made all the preparations but forgot about the basic questions. He badly 
needs your help to find the number of matches they have to organize. 

The HR has provided you with the total number of teams(N) that registered for the tournament. 
If there is any team left out to be paired then it automatically gets promoted to the next round. Now, only you who can save the
HR from embarrassment by solving the problem.



Input Format:   The first line of input consist of the number of test cases T.
                Next T lines each consist of the number of teams participating in the tournament, N.

Constraints:    1<= T <=100
                2<= N <=100000

Output Format :For each test case, print the number of matches that have to be played.

Sample TestCase 1:
Input:  2
        4
        7
Output: 3
        6

Explanation:    Test Case 1: N = 4 = 2 + 1 = 3
                Test Case 2: N = 7 = 3 + 2 + 1 = 6
*/

#include <bits/stdc++.h>
using namespace std;

int matches(int t, int m) {
        if(t == 1) {
                return m;
        }
        if((t%2) != 0) {
                m = m + 1;
                t--;
        }
        m = m + (t/2);
        matches((t/2), m);
}

int main() {

        int t;
        cin >> t;
        for(int i=0; i<t; i++) {
                int team;
                cin >> team;

                cout << matches(team, 0) << endl;
        }

        return 0;
}