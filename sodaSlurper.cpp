/**
 * Soda Slurper
 * 
 * William Ikenna-Nwosu (wiknwo)
 * 
 * Tim is an absolutely obsessive soda drinker, he simply 
 * cannot get enough. Most annoyingly though, he almost 
 * never has any money, so his only obvious legal way to 
 * obtain more soda is to take the money he gets when he 
 * recycles empty soda bottles to buy new ones. In addition 
 * to the empty bottles resulting from his own consumption 
 * he sometimes find empty bottles in the street. One day 
 * he was extra thirsty, so he actually drank sodas until 
 * he couldn’t afford a new one.
 * 
 * Input 
 * Three non-negative integers e,f,c, where e<1000 equals 
 * the number of empty soda bottles in Tim’s possession at
 *  the start of the day, f<1000 the number of empty soda 
 * bottles found during the day, and 2≤c<2000 the number 
 * of empty bottles required to buy a new soda.
 * 
 * Output
 * How many sodas did Tim drink on his extra thirsty day?
 */
#include <iostream>
using namespace std;

int main(){
    int e = 0, f = 0, c = 0;
    cin >> e >> f >> c;
    // cout << e << " " << f << " " << c;
    int numberOfEmptyBottles = e + f;
    int numberOfSodasDrank = 0;

    while(numberOfEmptyBottles > 0){
        numberOfEmptyBottles -= c;
        if(numberOfEmptyBottles >= 0){
            numberOfEmptyBottles += 1;
            numberOfSodasDrank += 1;
        }
    }

    cout << numberOfSodasDrank;
}