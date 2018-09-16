# statsbomb_python
Python Package for using Statsbomb IQ dataset

This is a work in progress package to allow Python users to work with Statsbomb IQ's free public datasets. The code so far looks only at a match by match json.


after install, run with <b> from sb_handler import * </b>

## TO DO SHORT TERM ##
- pull goal keeper data from json
- write code for pass maps
- write code for player level data (shots,tackles,interceptions etc..)
- ~~create player location shot maps (using SB's freeze frame, plot where players, GK etc.. are when shot is taken)~~
- add expanded event information to dataframe


## TO DO LONG TERM ##
- combine matches to look at player/team data over longer time period
- clean up for loops with list comprehension

## some quick functions to get started: ##

data = open_sb(INSERT_FILENAME) 
    # reads json file

df = clean_sb(data)

    # cleans data and puts it into a dataframe - more cols to be added

StartingXI = Lineups(data)

    #returns starting players

played = players_played(data)

    # returns all players who entered pitch with mins --> to do: add goals for/against 

shots = get_shots(data)

    # returns a dataframe of shots --> to do: add shot outcomes

shot_map(data,team) 

    # plots a shot map for selected team with size and shade representing xG value --> to do: add further shot information      (body part, outcome)

player_pass(df,player_name,orientation) 

    # plots passes made by player - names can be found by running df.player.unique() - orientation set as either 'vertical' or    'horizontal' --> to do: seperate successful and unsuccessful passes

get_individual_shot(data,number) 

    # plots individual shot freeze frame with positions of other players. number refers to shot number with 1 being first shot of match, 2 being second etc..) -> to do: add GK context, creat Abbreviation dictionary to shorten code

## NOTES ##

I'm not sure what each unit in SB's x and y coordinates refers to, and I prefer working in metres, so all xy values are converted to plot on a 104 x 68 metre pitch
