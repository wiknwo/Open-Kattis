/* EsejSolution.cpp
 * Created on: 5 Jan 2018
 * Author: SK
 *    Medium
 * 1. It contains at least A, and at most B words;
 * 2. Every word contains at least one, and at most 15 letters;
 * 3. the used vocabulary is large enough, in other words, the essay contains at least B/2B different words.
 *
 *  The essay should be output in a single line, using only lowercase letters of the English alphabet and spaces.
 *  The words used can, but need not be, words from the English (or any) language.
 *
 *  Input: The first and only line of input contains the integers A and B (A <= B <= 100000) from the task.
 *  Output: The first and only line of output must contain any essay that meets the rules from the task.
 * */
#include<iostream>
#include<cstdlib>
#include<math.h>
#include<map>
using namespace std;

//string create_A_Word(int minStringLength = 1, int maxStringLength = 15);
string create_A_Word(void);

int main()
{
	int A, B;
	string tmp;
	map<string, int> essay;

	cin >> A >> B;

	while(essay.size() < (unsigned int)max(A, B / 2))
	{
		tmp = create_A_Word();

		if(essay.count(tmp) != 1) //if word is not in essay.
			essay.insert({tmp, 1});
	}

	for(map<string, int>::iterator mapIt = essay.begin(); mapIt != essay.end();mapIt++)
		cout << mapIt->first << ' ';

}

string create_A_Word(void)
{
	string word = "";
	int wordLength = (rand() % 15) + 1; //Every word contains at least one, and at most 15 letters;

	for(int i = 0;i < wordLength;i++)
		word += (char)(rand() % 26 + 97);

	return word;
}




