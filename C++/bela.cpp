/*
 * BelaSolution.cpp
 *
 *  Created on: 30 Dec 2017
 *      Author: SK
 *
 *      Trivial
 */
#include<iostream>
#include<map>
using namespace std;

int main(void)
{
	int numHands = 0; // Hand: set of 4 cards.
	char domSuit_B = '0'; //Hold char value of dominant suit.
	string card = ""; //(number, value)
	map<char, int> Scores = {{'A', 11}, {'K', 4}, {'Q', 3}, {'J', 20}, {'T', 10}, {'9', 14}, {'8', 0}, {'7', 0}}; // Hash table holding all scores.
	int totalPoints = 0;

	//user input
	cin >> numHands >> domSuit_B;

	for(int i = 1;i <= 4 * numHands;i++)
	{
		//Read a card(number, suit)
		cin >> card;

		//If the suit of the card is 'Not dominant'
		if(card[1] != domSuit_B)
		{
			if(card[0] == 'J') totalPoints += 2;

			else if(card[0] == '9') totalPoints += 0;

			else totalPoints += Scores[card[0]];
		}

		else
		{
			totalPoints += Scores[card[0]];
		}
	}

	cout << totalPoints;
}

/* To use c++ static map initialization, do the following;
 * select project -> Properties -> C/C++ Build -> Setings ->
 * Cygwin C++ compiler -> Miscellaneous -> Other flags ->
 * add -std=c++11 to the end.*/



