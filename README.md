# pareto_watch
Pareto Watch old TV shows. Takes a TV show and returns the top 20% of episodes from IMDB sorted by episode number.

Uses python, pandas, and IMDbPY (https://imdbpy.github.io/) -- install guide and docs here: https://imdbpy.readthedocs.io/en/latest/

### Example output (using Star Wars: The Clone Wars):

(base) C:\Users\stone\source\repos\pythonParetoWatch>python paretowatch.py

Please enter the show name: star wars clone

Found show with title Star Wars: Clone Wars from 2003

Is this correct [Y]/n: n

These were the top 5 returns from IMDB:

id - title - year

0 - Star Wars: Clone Wars - 2003

1 - Star Wars: Clone Wars - FINAL Season (My Thoughts) - 2020

2 - Star Wars: The Clone Wars - 2008

3 - Star Wars: The Clone Wars - 2008

4 - Star Wars: Episode II - Attack of the Clones - 2002

Enter the show id, or 'n' to quit:2

Fetching episode ratings. . .

There are 133 episodes of Star Wars: The Clone Wars

You should Pareto watch these 27 episodes:

			 episode_title 	episode_rating  season  season_ep_number  abs_ep_number

	24                Nightsisters        8.701235       3                12             56
	21                     Monster        8.801235       3                13             57
	14         Witches of the Mist        9.001235       3                14             58
	13                   Overlords        9.001235       3                15             59
	20             Altar of Mortis        8.801235       3                16             60
	12            Ghosts of Mortis        9.001235       3                17             61
	26          Darkness on Umbara        8.701235       4                 7             73
	25                 The General        8.701235       4                 8             74
	19             Plan of Dissent        8.801235       4                 9             75
	6             Carnage of Krell        9.401235       4                10             76
	18                     The Box        8.801235       4                17             83
	9                      Revenge        9.101235       4                22             88
	17                     Revival        8.901235       5                 1             89
	15                    Eminence        8.901235       5                14            102
	8             Shades of Reason        9.201235       5                15            103
	4                  The Lawless        9.701235       5                16            104
	10  The Jedi Who Knew Too Much        9.101235       5                18            106
	11             To Catch a Jedi        9.101235       5                19            107
	5               The Wrong Jedi        9.701235       5                20            108
	22                      Orders        8.801235       6                 4            112
	16                      Voices        8.901235       6                11            119
	23                     Destiny        8.801235       6                12            120
	7                    Sacrifice        9.201235       6                13            121
	3    Old Friends Not Forgotten        9.801235       7                 9            130
	1       The Phantom Apprentice        9.901235       7                10            131
	2                    Shattered        9.901235       7                11            132
	0            Victory and Death        9.901235       7                12            133
