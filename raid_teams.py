'''Raid Teams

    William Ikenna-Nwosu (wiknwo)

    There is an upcoming raid event in an online game. You 
    are the leader of a guild with N adventurers. In this 
    game, every adventurer has a rating S for each of the 3 
    skills that every adventurer must learn. A high S value 
    indicates mastery at that skill. You wish to group the 
    adventurers into raid teams using the following steps:

    - Amongst all currently available adventurers, the 
    adventurer with the highest S value for the first 
    skill is selected. In cases of ties, the adventurer 
    with the lexicographically smallest name is selected. 
    That adventurer is no longer available from now on.

    - The same selection criteria is applied for the 
    second and third skill in order.

    - These three adventurers will form a raid team.

    - The process repeats starting from the first skill 
    until no more teams of three can be formed. There 
    could be situations where some players are not part 
    of any raid teams. They will stay behind and guard the 
    guild hall during the event.

    Report the members of every newly-created raid team, 
    in the order which the teams were formed. All N 
    adventurers are available initially.

    Input
    The first line of the input contains an integer 
    N (3≤N≤100000). N lines follow, each line beginning 
    with the name of the adventurer followed by three 
    integers S1 S2 S3 (0≤S1,S2,S3≤2000000000) describing the 
    level of proficiency of the adventurer in the three 
    skills in order. All names are non-empty alphanumeric 
    string of at most 10 characters, and all names are 
    unique.

    Output
    Whenever a raid team is formed, on a new line, output 
    the three names of the adventurers of the new team 
    from the lexicographically smallest name to the 
    lexicographically largest name, with a single space 
    between consecutive names.

    Subtasks
    (40 Points): 1≤N≤10000, all adventurers have the same 
    skill values for all three skills.

    (30 Points): 1≤N≤10000

    (30 Points): No additional constraint.

    Warning
    The I/O files are large. Please use fast I/O methods.
'''
class Player:
    playercount = 0 # Common base class for all players

    def __init__(self, player_name, s1, s2, s3):
        self._player_name = player_name
        self._s1 = s1
        self._s2 = s2
        self._s3 = s3
        Player.playercount += 1

    def getS1(self):
        return self._s1

    def getS2(self):
        return self._s2

    def getS3(self):
        return self._s3

    def to_s(self):
        return self._player_name
    
def main():
    n = int(input(""))
    players = []
    for i in range(n):
        data = input("").split(" ")
        data[1] = int(data[1]) # S1
        data[2] = int(data[2]) # S2
        data[3] = int(data[3]) # S3
        player = Player(data[0], data[1], data[2], data[3])
        players.append(player)

    # Form teams by selecting player with highest S1 value
    # then if ties form, select player with lexicographically
    # smalleest name first. This player cannot be chosen
    # again now. Repeat for S2, S3, second and third team
    # member respectively
    teams = []
    # Sorting players by S1, S2, S3
    while players and len(players) >= 3:
        team = []
        sorted_players_s1 = sorted(players, key=lambda x: (x.getS1(), x.to_s()), reverse=True)
        team.append(sorted_players_s1[0].to_s())
        players.remove(sorted_players_s1[0])
        sorted_players_s2 = sorted(players, key=lambda x: (x.getS2(), x.to_s()), reverse=True)
        team.append(sorted_players_s2[0].to_s())
        players.remove(sorted_players_s2[0])
        sorted_players_s3 = sorted(players, key=lambda x: (x.getS3(), x.to_s()), reverse=True)
        team.append(sorted_players_s3[0].to_s())
        players.remove(sorted_players_s3[0])
        teams.append(team)
    # Printing results
    for team in teams:
        print("{}".format(' '.join(team)))
    
if __name__ == '__main__':
    main()