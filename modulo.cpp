/**
 * Modulo
 * 
 * William Ikenna-Nwosu (wiknwo)
 * 
 * Given two integers A and B, A modulo B is the remainder 
 * when dividing A by B. For example, the numbers 7, 14, 27 
 * and 38 become 1, 2, 0 and 2, modulo 3. Write a program 
 * that accepts 10 numbers as input and outputs the number 
 * of distinct numbers in the input, if the numbers are 
 * considered modulo 42.
 * 
 * Input
 * The input will contain 10 non-negative integers, 
 * each smaller than 1000, one per line.
 * 
 * Output
 * Output the number of distinct values when considered 
 * modulo 42 on a single line.
 * 
 **/
#include<iostream>
#include<unordered_set>
using namespace std;

int main(){
    int number = -1; // Array to hold numbers
    unordered_set<int> distinctValues = {};

    for(int i = 0;i < 10;i++) {
        cin >> number;
        const bool is_in = distinctValues.find(number % 42) != distinctValues.end();
        if(!is_in) distinctValues.insert(number % 42);
    }
    cout << distinctValues.size();


    
}