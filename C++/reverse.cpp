/**
 * Reverse
 * 
 * William Ikenna-Nwosu (wiknwo)
 * 
 * Little Jóna needs a program. The program should read 
 * integers and print them in reverse order. Jóna asks 
 * for your help.
 * 
 * Input
 * The first line of input contains the integer n. 
 * Then comes a list of n integers, each on its own line.
 * 
 * Output
 * The list should be printed in reverse order of input.
 **/
#include<iostream>

int main(){
    int n = 0; // Number of integers in list
    std::cin >> n;
    int integers[n] = {0}; // Array of integers

    for(int i = 0;i < n;i++){
        std::cin >> integers[i];
    }

    for(int i = n - 1;i > -1;i--){
        std::cout << integers[i] << "\n";
    }
}