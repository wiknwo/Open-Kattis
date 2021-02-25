/*
 * UnBearAbleZooSolution.cpp
 *
 *  Created on: 3 Jan 2018
 *      Author: SK
 *
 *      Easy
 */
#include<iostream>
#include<sstream> //stringstream
#include<map>
#include<vector>
#include<algorithm> //transform

using namespace std;

string parseStringSpace(string str);

int main()
{
	int testCase = -1;
	string lineOfInput, animalDescription;
	vector<map<string, int>> lists; //5 elements max
	vector<map<string, int>>::iterator vectorIt;
	map<string, int>::iterator mapIt;

	//Getting number of animal descriptions(test case no.)
	getline(cin, lineOfInput);
	testCase = atoi(lineOfInput.c_str());

	//Getting input from user.
	while(testCase != 0)
	{
		//Make map of animal descriptions
		map<string, int> animalList;

		//Read -testCase- animal descriptions
		for(int i = 0;i < testCase;i++)
		{
			getline(cin, lineOfInput); //Read animal description.
			animalDescription = parseStringSpace(lineOfInput); //Parse the description and return the last word.
			transform(animalDescription.begin(), animalDescription.end(), animalDescription.begin(), ::tolower); //Converting description to lower case.

			if(animalList.count(animalDescription) != 1) //If animal is not in list.
				animalList.insert({animalDescription, 1});

			else //if animal is in list, increment its value.
				animalList[animalDescription] = animalList.at(animalDescription) + 1;
		}

		lists.push_back(animalList); //Add the list to the lists vector.

		//Getting number of animal descriptions(test case no.)
		getline(cin, lineOfInput);
		testCase = atoi(lineOfInput.c_str());
	}

	//Printing results
	for(vectorIt = lists.begin();vectorIt != lists.end();vectorIt++)
	{
		cout << "List " << distance(lists.begin(), vectorIt) + 1 << ":\n"; //Get index of vector element

		for(mapIt = vectorIt->begin(); mapIt != vectorIt->end();mapIt++)
			cout << mapIt->first << " | " << mapIt->second << "\n"; //Key | value
	}

	//Memory clean up.
	lists.clear(); //erase removes elements from the front of the vector.
}

//Function to parse a string about whitespace characters.
string parseStringSpace(string str)
{
	vector<string> tokens;
	istringstream iss(str);

	for(string s; iss >> s;)
	    tokens.push_back(s);

	return tokens.back();
}
