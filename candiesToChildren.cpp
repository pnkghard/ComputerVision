/*

Candies To Children (100 Marks)
There are N children standing in a line. Each child is assigned a rating value. You are giving candies to these children subjected to the 
following requirements:
-> Each child must have at least one candy.
-> Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?


Input Format
You will be given a function with integer array with rating of the children as integer element.


Constraints
1 < N < 10^5
1 < ai < 10^5


Output Format
You will return the minimum candies you must give to the children.


Sample TestCase 1
Input
6
1
3
4
3
2
1
Output
13

*/

#include <bits/stdc++.h>
using namespace std;

int32_t main() {

    int n;
    cin >> n;
    int ratings[n];
    int candies[n];
    int ans = n+2;
    for(int i=0; i<n; i++) {
        cin >> ratings[i];
        candies[i] = 1;
    }

    for(int i=0; i<n; i++) {

        if(ratings[i] > ratings[i-1]) {
            ans++;
        }
        if(ratings[i] > ratings[i+1]) {
            ans++;
        }
        
    }

    cout << ans;

    return 0;
}