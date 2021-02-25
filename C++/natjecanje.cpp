/*
 * Main.cpp
 *
 *  Created on: 3 Oct 2018
 *      Author: SK
 *
 *      Medium Solved
 */
#include<iostream>
#include<sstream>
using namespace std;

int main (void){
	int N; // 2 <= N <= 10 total number of teams
	int S; // 2 <= S <= N number of teams with damaged kayaks
	int R; // 1 <= R <= N number of teams with reserve kayaks
	int team_with_damaged_kayak, cannot_start = 0;
	string line = "";

	getline(cin, line);
	istringstream iss(line);
	iss >> N;
	iss >> S;
	iss >> R;
	iss.clear();

	int competitors[N] = {0}; //All teams in competition 0 = 1, 1 = 2

	//Read teams with damaged kayaks
	getline(cin, line);
	iss.str(line);

	for(int i = 0;i < S;i++){
		iss >> team_with_damaged_kayak;
		competitors[team_with_damaged_kayak - 1] -= 1;
	}

	//Read teams with reserved kayaks
	getline(cin, line);
	iss.clear();
	iss.str(line);

	for(int i = 0;i < R;i++){
		iss >> team_with_damaged_kayak;
		competitors[team_with_damaged_kayak - 1] += 1;
	}

	//
	for(int i = 0;i < N;i++){
		//if kayak is damaged
		if(competitors[i] == -1){
			if(competitors[i - 1] == 1){
				competitors[i] += competitors[i - 1];
				competitors[i - 1]--;
			}

			else if(competitors[i + 1] == 1){
				competitors[i] += competitors[i + 1];
				competitors[i + 1]--;
			}

			else {
				cannot_start++;
			}
		}
	}

	cout << cannot_start;
}




