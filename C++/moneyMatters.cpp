/**
 * Money Matters
 * 
 * William Ikenna-Nwosu (wiknwo)
 * 
 * Our sad tale begins with a tight clique of friends. 
 * Together they went on a trip to the picturesque country 
 * of Molvania. During their stay, various events which are 
 * too horrible to mention occurred. The net result was that 
 * the last evening of the trip ended with a momentous 
 * exchange of “I never want to see you again!”s. A quick 
 * calculation tells you it may have been said almost 50 
 * million times!
 *
 * Back home in Scandinavia, our group of ex-friends realize 
 * that they haven’t split the costs incurred during the 
 * trip evenly. Some people may be out several thousand 
 * crowns. Settling the debts turns out to be a bit more 
 * problematic than it ought to be, as many in the group no 
 * longer wish to speak to one another, and even less to 
 * give each other money.
 *
 * Naturally, you want to help out, so you ask each person 
 * to tell you how much money she owes or is owed, and whom 
 * she is still friends with. Given this information, you’re 
 * sure you can figure out if it’s possible for everyone to 
 * get even, and with money only being given between persons 
 * who are still friends.
 * 
 * Input
 * The first line contains two integers, n (2≤n≤10000), and 
 * m (0≤m≤50000), the number of friends and the number of 
 * remaining friendships. The friends are named 0,1,…,n−1. 
 * Then n lines follow, each containing an integer o 
 * (−10000≤o≤10000) indicating how much each person owes 
 * (or is owed if o<0). The first of those lines gives the 
 * balance of person 0, the second line the balance of 
 * person 1, and so on. The sum of these values is zero.
 * 
 * Output
 * After this comes m lines giving the remaining 
 * friendships, each line containing two integers x, y 
 * (0≤x<y≤n−1) indicating that persons x and y are still 
 * friends.
 * 
 * Output
 * Your output should consist of a single line saying 
 * “POSSIBLE” or “IMPOSSIBLE”.
 **/
#include <iostream>
using namespace std;

int main(){
    int n = 0, m = 0; // n = number of friends, m = number of remaining friendships
    cin >> n >> m;
    int friends[n] = {0};
    int remainingFriendships[m][2] = {0};
    int x = -1, y = -1; // x and y are still friends
    bool flag = true;

    // Getting money owed by or owed to friends
    for(int i = 0;i < n;i++){
        cin >> friends[i];
        // o indicating how much each person owes 
        // (or is owed o < 0). Money only being 
        // given between persons who are still
        // friends
    }

    // Getting remaining friendships
    for(int i = 0;i < m;i++){
        cin >> x >> y;
        remainingFriendships[i][0] = x;
        remainingFriendships[i][1] = y;
    }

    // Calculating if it's possible for everyone to get money back
    for(int i = 0;i < m;i++){
        if(friends[remainingFriendships[i][0]] < 0){
            friends[remainingFriendships[i][0]] = friends[remainingFriendships[i][0]] + friends[remainingFriendships[i][1]];
            friends[remainingFriendships[i][1]] = 0;
        } else if(friends[remainingFriendships[i][1]] < 0){
            friends[remainingFriendships[i][1]] = friends[remainingFriendships[i][0]] + friends[remainingFriendships[i][1]];
            friends[remainingFriendships[i][0]] = 0;
        }
    }

    for(int i = 0;i < n;i++){
        if(friends[i] != 0) {
            flag = false;
            break;
        }
    }

    if(flag) cout << "POSSIBLE";
    if(!flag) cout << "IMPOSSIBLE";

}