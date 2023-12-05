

import pandas as pd
import numpy as np
import nfl_data_py as nfl



## takes a list of years and returns a dataframe grouped into games

def get_data(years):
   
    pbp_data = nfl.import_pbp_data(years)  ## Takes a list of years as input
    

    pass_df = pbp_data[pbp_data['play_type'] == 'pass']  ## since we are looking at quarterback performance, we only need pass plays

    ## These are stats relevant to quarterback performance
    columns = ['passer_player_name', 'posteam', 'defteam', 'season', 'week', 'play_type',
            'complete_pass', 'incomplete_pass', 'interception', 'qb_hit', 'sack', 'pass_touchdown',
           'passing_yards']

    pass_df=pass_df[columns]


    pass_df = pass_df.groupby(['passer_player_name', 'week', 'season'], as_index=False).agg(
    {'posteam' : 'first',
     'defteam' : 'first',
     'complete_pass' : 'sum',
     'incomplete_pass' : 'sum',
     'interception' : 'sum',
     'qb_hit' : 'sum',
     'sack' : 'sum',
     'pass_touchdown' : 'sum',
     'passing_yards' : 'sum',
     }
    )## changes data from play by play to per-game
    return pass_df
