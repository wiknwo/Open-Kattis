/*
 * FilipSolution.cpp
 *
 *  Created on: 2 Jan 2018
 *      Author: SK
 *
 *      Trivial
 *      Solved.
 */
#include<bits/stdc++.h> //reverse
#include<iostream> //cout
#include<algorithm> //max
#include<string.h>
using namespace std;

/*int main()
{
	string A, B;
	int A_int, B_int;

	cin >> A >> B;

	reverse(A.begin(), A.end());
	reverse(B.begin(), B.end());

	stringstream Astream(A), Bstream(B);
	Astream >> A_int;
	Bstream >> B_int;

	cout << max(A_int, B_int);
}*/

int main()
{
	string lineOfInput;
	int A, B;

	getline(cin, lineOfInput);
	reverse(lineOfInput.begin(), lineOfInput.end());

	stringstream inputStream(lineOfInput);
	inputStream >> A;
	inputStream >> B;

	cout << max(A, B);
}

/*
#include<iostream>
#include<algorithm>
using namespace std;

int reverseDigits(int num);

int main()
{
	int A, B;
	cin >> A >> B;

	cout << max(reverseDigits(A), reverseDigits(B));
}

//https://www.geeksforgeeks.org/write-a-c-program-to-reverse-digits-of-a-number/
int reverseDigits(int num)
{
    int rev_num = 0;

    while(num > 0)
    {
        rev_num = rev_num*10 + num%10;
        num = num/10;
    }

    return rev_num;
}
*/



