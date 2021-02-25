/*
 * BattleSimulationSolution.cpp
 *
 *  Created on: 11 Jan 2018
 *      Author: SK
 *
 *      Medium
 *      Solved
 */
#include<iostream>
#include<set>
using namespace std;

int main()
{
	string monsterMoveSequence = "";
	set<string> comboPermutations = {"RBL", "RLB", "LBR", "LRB", "BLR", "BRL"};

	getline(cin, monsterMoveSequence);

	for(size_t i = 0;i < monsterMoveSequence.length();i++)
	{
		if(comboPermutations.count(monsterMoveSequence.substr(i, 3)))
		{
			cout << 'C';
			i = i + 2;
		}

		else
		{
			switch(monsterMoveSequence[i])
			{
				case 'R': cout << 'S';
								break;

				case 'B': cout << 'K';
								break;

				case 'L': cout << 'H';
								break;
			}
		}
	}

}




