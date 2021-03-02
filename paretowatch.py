# -*- coding: utf-8 -*-
"""
From:
https://www.reddit.com/r/slatestarcodex/comments/fzuk1v/pareto_watch_of_old_tv_shows/

Look up show on IMDB. Find title code - should be something similar to tt0103359 in the url, format typically www.imdb.com/title/tt0103359/
Goto show sort: https://www.imdb.com/search/title/?series=tt0103359&sort=user_rating,desc&count=250&view=simple and replace series=ttxxxxxx& with the series code. 
Calculate the 20% episode number, and find the rating.Ex: Batman TAS has 85 episodes, episode 17 is 20% of the way thru, and the 17th episode down in ratings is rated at 8.5.
Use ratinggraph.com and watch all episodes 8.5+ in chronological order.
Watch finale no matter what to get conclusion.

Test with:
Star Wars: The Clone Wars


imdb library docs:
https://imdbpy.readthedocs.io/en/latest/search.html?q=episodes&check_keywords=yes&area=default
"""

from imdb import IMDb
import pandas as pd
import datetime

today = datetime.datetime.now()

ia = IMDb()

# Look up show
show_name = input('Please enter the show name: ')

shows = ia.search_movie(show_name)

# ok set up our object
showobj = shows[0]
#double check
print('Found show with title {}'.format(showobj['title']))
check = input('Is this correct [Y]/n: ')
if check == 'n':
    print('quitting')
else:
    #update to relfect its a tv show
    print('Fetching episode ratings. . .')
    ia.update(showobj,'episodes')
    # calculate number of episodes
    num_episodes = showobj['episodes number']
    eps_to_watch = int(round(num_episodes / 5,0))-1
    
    print('There are {} episodes of {}'.format(num_episodes,showobj['title']))
    print('You should Pareto watch these {} episodes:'.format(eps_to_watch+1))    
    
    episode = showobj['episodes'][1][1]
    episode['rating']
    
    episodes = showobj['episodes']
    # ok so need to construct a df with episode title, episode rating, season #, ep #
    #empty dictionary 
    data = {'episode_title':[],
            'episode_rating':[],
            'season':[],
            'season_ep_number':[],
            'abs_ep_number':[]}
    episode_number = 1
    #iter through season
    for season_number in episodes:
        #iter through eps in season
        for ep_num in episodes[season_number]:
            # have to check to make sure episode has already aired!!
            ep_date = episodes[season_number][ep_num]['original air date'].replace('.','')
            if (len(ep_date) <= 4): # future episode with unformatted date
                ep_date = datetime.datetime.strptime('9999','%Y')
            else:
                ep_date = datetime.datetime.strptime(ep_date,'%d %b %Y')
            # update data dict
            # episode title
            data['episode_title'].append(episodes[season_number][ep_num]['title'])
            # episode rating
            # if unaired, set rating to 0.0
            if ep_date > today:
                data['episode_rating'].append(0.0)
            else:
                data['episode_rating'].append(episodes[season_number][ep_num]['rating'])
            # season number
            data['season'].append(season_number)
            # season ep number
            data['season_ep_number'].append(ep_num)
            # abs ep number
            data['abs_ep_number'].append(episode_number)
            episode_number += 1
            
    # put into a dataframe
    df = pd.DataFrame(data)
    
    # sort by rating number
    df.sort_values(by='episode_rating',ascending=False,inplace=True)
    
    # reset index
    df.reset_index(inplace=True)
    
    # drop the old index column
    df.drop(labels='index',axis=1,inplace=True)
    
    # truncate the df in place
    df = df.truncate(after=eps_to_watch)
    
    # and sort by the abs_ep_number
    df.sort_values(by='abs_ep_number',inplace=True)

    # print the results
    print(df.to_string())