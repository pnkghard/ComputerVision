/*
Mr.Natwarlal :


Mr. Natwarlal is a businessman and is famous as he has never gone in loss on any deal. This has made people suspicious of him for his backdoor 
illegal information gathering. The complaint has been lodged and legal team has started keeping track of him. The past history of all deals made by
Mr. Natwarlal is studied by the legal team and they are sure that there is something illegal. Mr. Natwarlal has been sent notice and has to appear 
before the legal team after D+1 days.

Mr. Natwarlal is very smart and he knows that legal team will ask how he has never incurred loss in any of the deal. He knows that there is a 
commercial ship for sale and he plans for a fraud to get out of sight of the legal team. The sale prices of commercial ship will change on each day 
upto D(inclusive) days. Mr. Natwarlal wants to buy and sell the commercial ship within these D(inclusive) days for a loss so that he has a proof for 
a loss deal when he appears before the legal team.

The sale prices for each day till D days is known by Mr. Natwarlal as he has friends who give him inside information before every deal. 
He Knows someone everywhere. Mr. Natwarlal wants to make a loss at deal but also wants to make sure that the loss he incurs is the minimum.

Mr. Natwarlal wants to know the amount of minimum loss he would incur in this deal. He can do it on own but since the number of days are large, 
he needs a programmer to do the task and for this he has hired you. He has provided a sample task so that you understand what needs to be done clearly.

Example:
For the given set of sale prices of ship for 4 consecutive days, the best option would be to buy the ship on the first day at a price of 8 crore and 
sell it on day 4 at a price of 5 crore. The amount of money lost in this deal would be 3 crore which is the least minimum possible.

You will be paid a lot of money if you could provide him the correct amount of money loss.  Can you find the minimum loss of money?

Input Format
The first line of input consist of number of days, D
The second line of input consists of sale prices(in crores) of commercial ship for D consecutive days space separately.

Constraints :
2<= D <=2*10^5 (1e5)
1<= Day[d] <=10^16 (1e16)

Output Format : Print the required output in a separate line.

Sample TestCase 1:
Input:
5
6 8 10 4 9

Output:
1

Explanation: 
The minimum loss of money would be incurred if the ship is bought at third day at 10 Crores and sold at fifth day at a price of 9 croces.

Buying Price = 10 Crore
Selling Price = 9 Crore
Loss = Buying Price - Selling Price = 10 - 9 = 1 Crore
The loss of money would be 1 Crore which is the minimum amount of loss possible.
*/


#include <bits/stdc++.h>
using namespace std;

int main() {
	long long d;
	cin >> d;

	long long p[d];

	for(int i=0; i<d; i++) {
		cin >> p[i];
	}
    
    for(int i=0; i<d; i++) {
        cout << p[i] << " ";
    }

    int netLoss = INT_MAX;

    for(int i=0; i<d; i++) {
        for(int j=i+1; j<d; j++) {
            if(p[i] < p[j]) {
                int m = p[j] - p[i];
                if (m < netLoss) {
                    netLoss = m;
                }
            }
        }
    }

    cout << netLoss;


    return 0;
}