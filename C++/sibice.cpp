/*
 * SibiceSolution.cpp

 *
 *  Created on: 30 Dec 2017
 *      Author: SK
 *
 *      Trivial
 */
#include<iostream>
#include<math.h>
using namespace std;

int main(void)
{
	int numMatches = 0, width = 0, height = 0, matchLength = 0;

	//Reading 3 numbers on one line.
	cin >> numMatches >> width >> height;
	double hypoteneuse = sqrt((width * width) + (height * height));

	//Check if the match fits.
	for(int i = 1;i <= numMatches;i++)
	{
		cin >> matchLength;

		if(matchLength > hypoteneuse) cout << "NE \n";

		else cout << "DA \n";
	}
}




