/**
 * Easy
 *
 *
 * # = building
 * X = parked car
 * . = free space
 * monster truck is 2 * 2
 */
#include<iostream>
using namespace std;

void getSquashCount(char monsterTruckSpace[], int carsSquashed[]);

int main()
{
	int R = 0; //Number of rows.
	int C = 0; //Number of columns.
	int rowNumber, columnNumber;
	static int squashCount[5] = {}; //initialized with 0.
	static char twoByTwo[4]; //Monster truck parking space.

	cin >> R >> C;

	//Filling map of city.
	string mapOfCity[R];

	for(rowNumber = 0;rowNumber < R;rowNumber++)
	{
		cin >> mapOfCity[rowNumber];
	}

	//Iterating over map of city and determining number of parking spaces for monster truck.
	for(rowNumber = 0;rowNumber < R - 1;rowNumber++)
	{
		for(columnNumber = 0;columnNumber < C - 1;columnNumber++)
		{
			//Monster truck parking space.
			twoByTwo[0] = mapOfCity[rowNumber][columnNumber];
			twoByTwo[1] = mapOfCity[rowNumber + 1][columnNumber];
			twoByTwo[2] = mapOfCity[rowNumber][columnNumber + 1];
			twoByTwo[3] = mapOfCity[rowNumber + 1][columnNumber + 1];
			getSquashCount(twoByTwo, squashCount);
		}
	}

	//Print required output.
	for(int i = 0;i < 5;i++)
		cout << squashCount[i] << "\n";
}

void getSquashCount(char monsterTruckSpace[], int carsSquashed[])
{
	int numFreeSpaces = 0, numParkedCars = 0;

	for(int i = 0;i < 4;i++)
	{
		if(monsterTruckSpace[i] == '.')
			numFreeSpaces++;

		else if(monsterTruckSpace[i] == 'X')
			numParkedCars++;
	}

	if(numFreeSpaces == 4)
		carsSquashed[0] += 1;

	else if((numParkedCars == 1) && (numFreeSpaces == 3))
		carsSquashed[1] += 1;

	else if((numParkedCars == 2) && (numFreeSpaces == 2))
		carsSquashed[2] += 1;

	else if((numParkedCars == 3) && (numFreeSpaces == 1))
		carsSquashed[3] += 1;

	else if(numParkedCars == 4)
		carsSquashed[4] += 1;
}
