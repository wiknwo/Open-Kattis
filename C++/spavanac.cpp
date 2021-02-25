/*
 * SpavanacSolution.cpp
 *
 *  Created on: 1 Jan 2018
 *      Author: SK
 *
 *  Trivial
 *
 */
#include<iostream>
using namespace std;


int main()
{
	int H = 0; //Hours: 0 <= H <= 23
	int M = 0; //Minutes: 0 <= M <= 59

	cin >> H >> M; //Reading hours and minutes.

	//Output time 45 minutes before input time.
	M -= 45;

	if(M < 0)
	{
		H = H - 1;

		while(M < 0)
		{
			M = M + 60;
		}
	}

	if(H < 0)
	{
		while(H < 0)
		{
			H = H + 24;
		}
	}

	cout << H << " " << M;
}

