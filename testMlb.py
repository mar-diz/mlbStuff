import statsapi

#this makes calls directly to MLB StatsAPI endpoints returns raw data
#print(statsapi.get())
#looks up player name and general inf
print("Look up player name: " + str(statsapi.lookup_player("Giancarlo Stanton")))
#gets standings of which league and which division you input
print(statsapi.standings_data(103)[201]['teams'])

#print # of winning games for which team
print('The A\'s won %s games in 2018.' % sum(1 for x in statsapi.schedule(team=133,start_date='01/01/2018',end_date='12/31/2018') if x.get('winning_team','')=='Oakland Athletics'))

#print the linescore for all games that the Phillies won in July 2008
#for x in [y for y in statsapi.schedule(team=143,start_date='07/01/2015',end_date='07/31/2019') if y.get('winning_team','')=='Philadelphia Phillies']:
#    print('%s\nWinner: %s, Loser: %s\n%s\n\n' % (x['game_date'], x['winning_team'], x['losing_team'], statsapi.linescore(x['game_id'])))
