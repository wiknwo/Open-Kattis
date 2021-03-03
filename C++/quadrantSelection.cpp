/**
 * Quadrant Selection
 * 
 * William Ikenna-Nwosu
 * 
 * A common problem in mathematics is to determine which 
 * quadrant a given point lies in. There are four 
 * quadrants, numbered from 1 to 4, as shown in the 
 * diagram below:
 * 
 * For example, the point A, which is at coordinates 
 * (12,5) lies in quadrant 1 since both its x and y 
 * values are positive, and point B lies in quadrant 2 
 * since its x value is negative and its y value is 
 * positive.
 *
 * Your job is to take a point and determine the quadrant 
 * it is in. You can assume that neither of the two 
 * coordinates will be 0.
 **/
#include<iostream>

int main(){
    int x = 0, y = 0;

    // Getting user input
    std::cin >> x;
    std::cin >> y;

    // Writing logic
    if(x > 0 && y > 0){
        std::cout << 1;
    } else if(x < 0 && y > 0) {
        std::cout << 2;
    } else if(x < 0 && y < 0) {
        std::cout << 3;
    } else if(x > 0 && y < 0) {
        std::cout << 4;
    }
}