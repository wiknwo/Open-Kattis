/**
 * William Ikenna-Nwosu (16303711)
 **/
#include <iostream>
#include <map>
#include <string>
#include <sstream>
using namespace std;

int main(){
    map<int, int> numberOfParkingSpaces = {{0, 0}, {1, 0}, {2, 0}, {3, 0}, {4, 0}};
    string monstertruck[2][2];
    int r = 0;
    int c = 0;

    cout << "Enter number of rows and columns separated by space: ";
    cin >> r >> c;
    string parkinglot[r][c];
    string lineofinput = "";

    for(int i = 0;i < r;i++){
        cout << "Enter parking line: ";
        cin >> lineofinput;
        stringstream(lineofinput);
        cout << lineofinput << endl;
    }

    for(int i = 0;i < r;i++){
        cout << parkinglot[i] << endl;
    }
}