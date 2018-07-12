# to arrange into functions

def get_drive():
    '''
    this is to automate switching between home PC and laptop
    it returns J:\\AFL\\ or D:\\AFL\\ depending if D:\ is available
    
    No parameters required
    '''
    
    import win32api
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    if 'D:\\' in drives:
        drive = 'D:\\AFL\\'
    else:
        drive = 'J:\\AFL\\'
    return drive


def get_proxy(proxy):
        if proxy:
            from os import environ
            pwd = input('Please enter your LAN Pwd')
            environ["http_proxy"]="http://c819325:"+pwd+"@http-gw.tcif.telstra.com.au:8080"
            environ["https_proxy"]=environ.get("http_proxy")
        return None


def fix_round(round_in):
    '''
    this function convert Round values into sequential integers
    '''
    if round_in=='QF':
        rnd='25'
    elif round_in=='EF':
        rnd='26'
    elif round_in=='SF':
        rnd='27'
    elif round_in=='PF':
        rnd='28'
    elif round_in=='GF':
        rnd='29'
    elif round_in[0]=='R':
        rnd=round_in[1:]
    else:
        rnd=round_in
    return int(rnd)

def fix_team_name(name):
    '''
    this function converts any team name to a consistent
    set of  names which are usable for joins
    '''
    if 'Crows' in name:
        team_name='Adelaide'
    elif name.strip()=='Adelaide Crows':
        team_name='Adelaide'
    elif name=='AD':
        team_name='Adelaide'
    elif name=='Crows':
        team_name='Adelaide'
    elif name=='BL':
        team_name='Brisbane Lions'
    elif name=='Lions':
        team_name='Brisbane Lions'
    elif name=='CA':
        team_name='Carlton'
    elif name=='Blues':
        team_name='Carlton'
    elif name=='CW':
        team_name='Collingwood'
    elif name=='Magpies':
        team_name='Collingwood'
    elif name=='ES':
        team_name='Essendon'
    elif name=='Bombers':
        team_name='Essendon'
    elif name=='FR':
        team_name='Fremantle'
    elif name=='Dockers':
        team_name='Fremantle'
    elif name=='GE':
        team_name='Geelong'
    elif name=='Cats':
        team_name='Geelong'
    elif name=='Geelong Cats':
        team_name='Geelong'
    elif name=='GC':
        team_name='Gold Coast'
    elif name=='Suns':
        team_name='Gold Coast'
    elif name=='Gold Coast Suns':
        team_name='Gold Coast'
    elif name=='GWS Giants':
        team_name='Greater Western Sydney'
    elif name=='GWS':
        team_name='Greater Western Sydney'
    elif name=='GW':
        team_name='Greater Western Sydney'
    elif name=='Giants':
        team_name='Greater Western Sydney'
    elif name=='GW Sydney':
        team_name='Greater Western Sydney'
    elif name=='HW':
        team_name='Hawthorn'
    elif name=='Hawks':
        team_name='Hawthorn'
    elif name=='ME':
        team_name='Melbourne'
    elif name=='Demons':
        team_name='Melbourne'
    elif name=='Deamons':
        team_name='Melbourne'
    elif name=='KA':
        team_name='North Melbourne'
    elif name=='NM':
        team_name='North Melbourne'
    elif name=='Kangaroos':
        team_name='North Melbourne'
    elif name=='PA':
        team_name='Port Adelaide'
    elif name=='Power':
        team_name='Port Adelaide'
    elif name=='RI':
        team_name='Richmond'
    elif name=='Tigers':
        team_name='Richmond'
    elif name=='SK':
        team_name='St Kilda'
    elif name=='Saints':
        team_name='St Kilda'
    elif name=='SY':
        team_name='Sydney'
    elif 'Swans' in name:
        team_name='Sydney'
    elif name=='WC':
        team_name='West Coast'
    elif name=='West Coast Eagles':
        team_name='West Coast'
    elif name=='Eagles':
        team_name='West Coast'
    elif name=='WB':
        team_name='Western Bulldogs'
    elif name=='Bulldogs':
        team_name='Western Bulldogs'
    else:
        team_name=name
    return team_name

def fix_venue(name):
    if name=='AAMI':
        ground = 'Olympic Park'
    elif name=='ANZ':
        ground = 'Stadium Australia'
    elif name=='Adelaide':
        ground='Adelaide Oval'
    elif name=='Aurora':
        ground = 'York Park'
    elif name=='Blacktown':
        ground='Blacktown'
    elif name=='Blundstone Arena':
        ground = 'Bellerive Oval'
    elif name=='Blundstone':
        ground = 'Bellerive Oval'
    elif name=="Cazaly's":
        ground= "Cazaly's Stadium"
    elif name=='Domain':
        ground='Subiaco'
    elif name=='Etihad Stadium':
        ground = 'Docklands'
    elif name=='Etihad':
        ground = 'Docklands'
    elif name=='GMHBA Stadium':
        ground='Kardinia Park'
    elif name=='GMHBA':
        ground='Kardinia Park'
    elif name=='Gabba':
        ground = 'Gabba'
    elif name=='Jiangwan':
        ground = 'Jiangwan Stadium'
    elif name=='Jiangwan Stadium, China':
        ground = 'Jiangwan Stadium'
    elif name=='M.C.G':
        ground = 'M.C.G.'
    elif name=='MCG':
        ground = 'M.C.G.'
    elif name=='Mars Stadium, Ballarat':
        ground = 'Eureka Stadium'
    elif name=='Mars':
        ground = 'Eureka Stadium'
    elif name=='Metricon Stadium':
        ground = 'Carrara'
    elif name=='Metricon':
        ground = 'Carrara'
    elif name=='Perth':
        ground='Perth Stadium'
    elif name=='SCG':
        ground='S.C.G.'
    elif name=='Spotless Stadium':
        ground='Sydney Showground'
    elif name=='Spotless':
        ground='Sydney Showground'
    elif name=='UNSW Canberra Oval':
        ground='Manuka Oval'
    elif name=='StarTrack':
        ground='Manuka Oval'
    elif name=='Treager Park, Alice Springs':
        ground='Traeger Park'
    elif name=='TIO Stadium, Darwin':
        ground='Marrara Oval'
    elif name=='TIO':
        ground='Marrara Oval'
    elif name=='University of Tasmania Stadium':
        ground='York Park'
    elif name=='UTAS':
        ground='York Park'
    elif name=='Westpac':
        ground='Wellington'
    else:
        ground=name
    return ground

def get_ladder(seas_from,seas_to,proxy=False):
    '''
    this is just to get the ladder history

    Input required - update season from and to in the function call at the bottom
    this function returns a dataframe for AFL ladder position history
    seas_from - season to start from
    seas_to - season end - inclusive
    '''
    import bs4 as bs
    import urllib.request
    import pandas as pd
    from dateutil import parser
    
    a =get_proxy(proxy)
    
    ladder = pd.DataFrame(columns=['Team','Games','Points','Percentage','Round','Position','Season'])
    for season in range(seas_from-1,seas_to+1): 
        cur_url = 'http://afltables.com/afl/seas/'+str(season)+'.html'
        dfs = pd.read_html(cur_url)

        for df in dfs:
            if df.columns.nlevels>1:
                break
            if len(df)>1 and 'Ladder' in df[0][0] and 'Rd' in df[0][0]:
                rnd = df[0][0][3:5]
                ldr = df.copy() 
                ldr = ldr.drop(0,0)
                ldr.columns = ['Team','Games','Points','Percentage']
                ldr['Round']=rnd
                ldr['Position']=ldr.index
                ldr['Season']=season
                ladder = pd.concat([ladder,ldr])
    ladder['Team'] = [fix_team_name(x) for x in ladder['Team']]
    
    # repeat last round for last and until 29
    ladder_f = ladder.copy()
    ladder_f.drop_duplicates(subset=['Team','Season'], keep='last', inplace=True)

    # get last round for each season
    ladder_y = ladder_f.copy()
    ladder_y.drop_duplicates(subset=['Season'], keep='last', inplace=True)
    ladder_y=ladder_y.drop(['Team','Games','Points','Percentage','Position'],1)
    rnd=[]
    seas=[]
    for index, row in ladder_y.iterrows():
        st = int(row.Round)
        #print(type(st))
        for i in range(st+1,30):
            rnd.append(i)
            seas.append(row.Season)
    ldr = pd.DataFrame()
    ldr['Season'] = seas
    ldr['Round'] = rnd
    ldr = pd.merge(ladder_f.drop(['Round'],1),ldr,how='inner',on=['Season'])
    ladder = pd.concat([ladder,ldr])
    ladder = ladder.sort_values(by=['Team','Season'],axis=0)
    ladder['PosOld']=ladder.Position.shift(1)  #previous ladder position taken
    ladder = ladder.drop(['Position'],1)
    ladder['Round']= [int(x) for x in ladder['Round']]
    ladder=ladder.dropna(axis=0)
    ladder['PosOld']= [int(x) for x in ladder['PosOld']]  
    return ladder

def get_fixture(proxy=False):
    '''
    this is to get AFL fixture from theroar.com.au
    set proxy=True if you are on LAN
    '''
    import bs4 as bs
    import urllib.request
    import pandas as pd
    from dateutil import parser

    a =get_proxy(proxy)
 
    url='https://www.theroar.com.au/afl-draw/'
    sauce = urllib.request.urlopen(url)
    soup = bs.BeautifulSoup(sauce,'lxml')

    fixture = pd.DataFrame(columns=['Round','Date','HomeTeam','AwayTeam','Venue'])

    for x in soup.find_all('tbody'):
        rnd_counter = 0

        for y in x.find_all('tr'):

            if y.find_all('strong'):
                rnd_counter +=1

            else:
                if not y.find_all('h3') and 'Byes' not in y.text and 'TBC' not in y.text:
                    dt,teams,venue,tm = y.text.strip().split('\n')
                    if dt == 'Sar Apr 21':
                        dt = 'Sat Apr 21'

                    dt = parser.parse(dt)
                    if teams == 'North Melbourne Carlton':
                            hm_team = 'North Melbourne'
                            aw_team = 'Carlton'
                    else:
                        hm_team, aw_team = teams.split(' vs ')

                    #print(rnd_counter,dt,fix_team_name(hm_team),fix_team_name(aw_team),fix_venue(venue))
                    df = pd.DataFrame(columns=['Round','Date','HomeTeam','AwayTeam','Venue'])
                    df.loc[0]=[rnd_counter,dt,fix_team_name(hm_team),fix_team_name(aw_team),fix_venue(venue)]
                    fixture = pd.concat([fixture,df])
    return fixture

def get_odds_history(season_from,season_to,proxy=False):
    '''
    this function gets odds history from footywire.com
    min season from is 2010- so it will make the min date 2010 if less than that
    set proxy=True if on LAN
    '''
    import bs4 as bs
    import urllib.request
    import pandas as pd
    from string import ascii_uppercase
    from dateutil import parser
    import datetime
    a =get_proxy(proxy)
 
    if season_from<2010:
        season_from=2010
    odds_history=pd.DataFrame()
    for season in range(season_from,season_to+1):
        print('Getting odds for season',season,'...')
        sauce = urllib.request.urlopen('https://www.footywire.com/afl/footy/afl_betting?year='+str(season))
        soup = bs.BeautifulSoup(sauce,'lxml')


        for x in soup.find_all('div',class_ ='datadiv'):
            date=[]
            venue=[]
            team_HM=[]
            odds_HM=[]
            team_AW=[]
            odds_AW=[]
            counter =0

            home_team_cursor = True
            for y in x.find_all('tr'):

                for z in y.find_all('td',class_='data'):
                    counter = counter+1
                    if z.has_attr('height'):
                        counter = 0
                        #print('new game ',z.text)
                        date.append(z.text)
                    elif z.has_attr('rowspan'):
                        #print('venue ', z.text)
                        venue.append(z.text)
                    elif not z.has_attr('align'):
                        if counter == 2:
                            #print('Home team: ', z.text)
                            team_HM.append(z.text)
                            home_team_cursor=True    
                        else:
                            #print('Away team: ', z.text)
                            counter = 0
                            team_AW.append(z.text)
                            home_team_cursor=False
                    elif counter ==3 and not home_team_cursor:
                        #print('away team odds: ',z.text)
                        odds_AW.append(z.text)
                    elif counter==5 and home_team_cursor:
                        #print('home team odds: ',z.text)
                        odds_HM.append(z.text)
        odds = pd.DataFrame()
        odds['Date']=[parser.parse(x,dayfirst=True) for x in date]
        odds['Venue']=[fix_venue(x) for x in venue]
        odds['HomeTeam']=[fix_team_name(x) for x in team_HM]
        odds['OddsHome']=[x for x in odds_HM]
        odds['AwayTeam']=[fix_team_name(x) for x in team_AW]
        odds['OddsAway']=[x for x in odds_AW]
        odds_history = pd.concat([odds_history,odds])  
    odds = odds.drop_duplicates(subset=['Date','HomeTeam','AwayTeam'],keep='last')
    return odds_history

def get_games(proxy=False):
    
    '''
    this function gets past games history
    and gets attendance where it is available
    '''
    import pandas as pd
    
    a =get_proxy(proxy)
        
    col_specification =[(7, 15), (16, 33), (51, 68), (87, 116),(117,128)]
    attend = pd.read_fwf('https://afltables.com/afl/stats/biglists/bg7.txt', 
                         colspecs=col_specification, skiprows=[0],parse_dates=[1])
    attend.columns = ['Attendance', 'HomeTeam', 'AwayTeam', 'Venue','Date']
    attend['Date']  = pd.to_datetime(attend['Date'],dayfirst=True)
    attend['Attendance'] = attend.Attendance.str.replace(r"[\*]",'')
    col_specification =[(0, 5), (7, 18), (24, 27), (29, 46),(47,63), (64,81),(82,99),(100,117)]
    games= pd.read_fwf('http://afltables.com/afl/stats/biglists/bg3.txt', 
                       colspecs=col_specification, skiprows=[0],parse_dates=[1])
    games.columns = ['GameID', 'Date', 'Round', 'HomeTeam', 'ScoreHm','AwayTeam','ScoreAw','Venue']
    games = pd.merge(games,attend,how='left',on=['Venue','Date','HomeTeam','AwayTeam'])

    #fix rounds in games
    games['Round'] = [fix_round(x) for x in games['Round']]
    
    games['Year']=games['Date'].map(lambda x: x.year)

    #fix North Melb in games
    games['HomeTeam'] = [fix_team_name(x) for x in games['HomeTeam']]
    games['AwayTeam'] = [fix_team_name(x) for x in games['AwayTeam']]

    # get result
    games['H'] = [int(x.split('.')[2]) for x in games['ScoreHm']]
    games['A'] = [int(x.split('.')[2]) for x in games['ScoreAw']]
    games = games.drop(['ScoreHm','ScoreAw'],1)
    games['Result'] = [round((x[0] /(x[0] +x[1])),3) for x in zip(games['H'],games['A'])]
    games = games.drop(['H','A'],1)
    games['ResultWL'] = [1 if x>=0.5 else 0 for x in games.Result]
    return games


def get_team_performance_hist(season_from,season_to,proxy=False):
    '''
    this is to get the team performance history
    '''

    import pandas as pd
    import numpy as np
    from datetime import datetime
    from dateutil import parser
    import bs4 as bs
    import urllib.request

    a =get_proxy(proxy)


    games = get_games()
    games_H = games.copy()
    games_H['Team']=games_H['HomeTeam']
    games_H['HomeFlag']=1
    games_H = games_H.drop(['HomeTeam','AwayTeam'], 1)

    games_A = games.copy()
    games_A['Team']=games_A['AwayTeam']
    games_A['HomeFlag']=0
    games_A = games_A.drop(['HomeTeam','AwayTeam'], 1)
    games_for_join = pd.concat([games_H,games_A])

    team_performace = pd.DataFrame()
    for season in range(season_from-4,season_to+1):
        sauce = urllib.request.urlopen('https://afltables.com/afl/stats/'+str(season)+'t.html')
        soup = bs.BeautifulSoup(sauce,'lxml')

        tms=[]
        i=0
        for x in soup.find_all('th'):
            if 'Team Statistics [Players]' in x.text:
                tms.append(x.text[0:-26])
                i+=1
        cur_url = 'https://afltables.com/afl/stats/'+str(season)+'t.html'
        dfs = pd.read_html(cur_url,header=1)
        all_dfs = pd.DataFrame()

        for i in range(len(dfs)):
            if i % 2==0:
                x= pd.concat([dfs[i],dfs[i+1].drop(['#','Opponent'],1)],1)
                x['Team']=tms[i]
                all_dfs = pd.concat([all_dfs, x])
        all_dfs=all_dfs[all_dfs['#'] != 'W-D-L']
        all_dfs['Year']=season
        team_performace = pd.concat([team_performace,all_dfs])
    team_performace = team_performace.rename(columns={'#': 'Round'})
    team_performace['Round'] = [fix_round(x) for x in team_performace['Round']]
    team_performace['Team'] = [fix_team_name(x) for x in team_performace['Team']]
    team_performace['Opponent'] = [fix_team_name(x) for x in team_performace['Opponent']]

    team_performace = pd.merge(team_performace,games_for_join.drop(['GameID','Attendance','Result'],1),how='left',on=

['Year','Round','Team'])

    team_performace['KI'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['KI']]
    team_performace['MK'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['MK']]
    team_performace['HB'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['HB']]
    team_performace['DI'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['DI']]
    team_performace['GL'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['GL']]
    team_performace['BH'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['BH']]
    team_performace['HO'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['HO']]
    team_performace['TK'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['TK']]
    team_performace['RB'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['RB']]
    team_performace['IF'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['IF']]
    team_performace['CL'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['CL']]
    team_performace['CG'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['CG']]
    team_performace['FF'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['FF']]
    team_performace['FA'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['FA']]
    team_performace['BR'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['BR']]
    team_performace['CP'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['CP']]
    team_performace['UP'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['UP']]
    team_performace['CM'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['CM']]
    team_performace['MI'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['MI']]
    team_performace['1%'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['1%']]
    team_performace['BO'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['BO']]
    team_performace['GA'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['GA']]
    return team_performace


def get_lineup(year,rnd,proxy=False):
    '''
    returns all available line-up for given year
    year - current year you need to specify
    rnd - current round where line-up has been released (could be improved into auto later)
    proxy = True if on LAN
    Pre-requisites: 
     1.TeamRef.csv - file which maps team names to AFL line-up abbreviated names
     2.Fixture function is used

    '''    
    import bs4 as bs
    import urllib.request
    import pandas as pd
    from dateutil import parser


    from string import ascii_uppercase
    from dateutil import parser
    import datetime

    fixture = get_fixture(proxy)
    fixture = fixture[fixture.Round==rnd]  #this limits to current round only
    teams = pd.read_csv(get_drive()+'TeamRef.csv')

    this_1 = pd.merge(fixture,teams,how="inner",left_on=['HomeTeam'],right_on=['Team'])
    this_2 = pd.merge(this_1,teams,how="inner",left_on=['AwayTeam'],right_on=['Team'])
    rounds = this_2.drop(['Team_x','Team_y'],1)
    rounds['Game'] = [x + '-v-' +y for x,y in zip(rounds.AFL_Team_Nm_x,rounds.AFL_Team_Nm_y)]
    rounds = rounds.drop(['AFL_Team_Nm_x','AFL_Team_Nm_y'],1)


    # now get available line-up for player ref working

    #rounds = rounds[rounds.Round<=max_round]    # needs updating, just available

    lineup=pd.DataFrame()
    for gm,rnd in zip(rounds['Game'],rounds['Round']):
        url='http://www.afl.com.au/match-centre/'+str(year)+'/'+str(rnd)+'/'+gm
        
        sauce = urllib.request.urlopen(url)
        soup = bs.BeautifulSoup(sauce,'lxml')

        tms=[]
        plrs=[]
        for x in soup.find_all('div',class_ ='lineup'):
            for t in x.find_all('div',class_ ='text-inouts'):
                team=''
                for tm in t.find_all('h4'):
                    team=tm.text

                for p in t.find_all('div',class_ ='posGroup'):
                    position=''
                    for pos in p.find_all('p',class_ ='pos'):
                        position =pos.text.strip()
                    for player in p.find_all('li'):
                        if position in ['B','HB','C','HF','F','Fol','I/C']:
                            tms.append(team)
                            plrs.append(player.text.strip().strip(','))

        d = pd.DataFrame()
        d['Team'] = tms
        d['Player'] = plrs
        lineup=pd.concat([lineup,d])
    lineup['Team']=[fix_team_name(x) for x in lineup['Team']]
    return lineup

def get_player_base(proxy):
    '''
    !!! run only when need to update for new players !!!
    returns a dataframe of player base table to enable to skip older players
    e.g. players[players.DoB>'1975-01-01']  this gives 2.5k player subset
    
    typical use - to create Players.csv file in AFL directory - !!! pre-requisite for getting player performance

    '''
    import bs4 as bs
    import urllib.request
    import pandas as pd
    from string import ascii_uppercase
    from dateutil import parser
    import datetime
    a =get_proxy(proxy)
    
    players = pd.DataFrame(columns=['Name','DoB','Url','Debut_Age','Age_Last_Played_Days'])

    # get player urls
    links = []
    for c in ascii_uppercase :
        sauce = urllib.request.urlopen('https://afltables.com/afl/stats/players'+c+'_idx.html')
        soup = bs.BeautifulSoup(sauce,'lxml')
        for url in soup.find_all('a',href=True):
            links.append('https://afltables.com/afl/stats/'+url['href'])
    # now remove non-player links - ones that contain 'idx'
    links = [item for item in links if 'players' in item and 'idx' not in item and 'afl_index' not in item]        

    for cur_url in links:
        sauce = urllib.request.urlopen(cur_url)
        soup = bs.BeautifulSoup(sauce,'lxml')

        #Name
        x = soup.find_all('h1')
        name = x[0].text

        #DoB
        found_dob=False

        for x in soup.find_all('b'):
            if x.text == 'Born:':
                dob = x.next_sibling
                found_dob=True
                break
        if found_dob:
            dob=parser.parse(dob[0:11],dayfirst=True)
        else:
            dob = datetime.datetime(1900, 1, 1, 0, 0)

        #Debut
        found_debut = False
        for x in soup.find_all('b'):
            if x.text == 'Debut:':
                debut = x.next_sibling
                found_debut=True
                break
        if found_debut:
            debut =debut.split()
            debut1 = ''.join(c for c in debut[0] if c.isdigit())
            if len(debut)>1:
                debut2 = ''.join(c for c in debut[1] if c.isdigit())
                debut = int(debut1)+int(debut2)/365
            else:
                debut = int(debut1)
        else:
            debut = 100
        #age last played
        found_last = False
        for x in soup.find_all('b'):
            if x.text == 'Last:':
                age_last = x.next_sibling
                found_last=True
                break
        if found_last:
            age_last =age_last.split()
            a1 = ''.join(c for c in age_last[0] if c.isdigit())
            if len(age_last)>1:
                a2 = ''.join(c for c in age_last[1] if c.isdigit())
                age_last = int(a1)*365.25+int(a2) #in days
            else:
                age_last = int(a1)*365.25
        else:
            age_last = 40*365.25
        today = datetime.datetime.today()
        last_played_date = dob + datetime.timedelta(days=age_last)
        since_last_game=today-last_played_date
        df = pd.DataFrame(columns=['Name','DoB','Url','Debut_Age','Age_Last_Played_Days','Last_Played_Date'])
        df.loc[0]=[name,dob,cur_url,debut,age_last,last_played_date]
        players = pd.concat([players,df])
        print(name)
    return players



def get_player_perf(DoB_min='1975-01-01',proxy=False):
    '''
    Use this only once per complete round and save into CSV as it takes a while to run
    this function returns a dataframe of player performance history
    Entire player history is returned
    DoB_min is limiting factor to get only player born after the date - for performance reasons
    change the default if you need to go more back into older players or in reverse
    Pre-requisite: Players.csv file exists in the AFL directory
    set proxy=True when on office LAN
    
    '''
    import bs4 as bs
    import urllib.request
    import pandas as pd

    a =get_proxy(proxy)

    players = pd.read_csv(get_drive()+'Players.csv')
    players =players[players['DoB']>DoB_min]

    player_stats = pd.DataFrame(columns=['Url','Team','Year'])

    for cur_url in players.Url:
        print(cur_url)
        sauce = urllib.request.urlopen(cur_url)
        soup = bs.BeautifulSoup(sauce,'lxml')

        found=False
        dfs=[]
        for table in soup.find_all('table'):
            #t1=tables[7]
            t=table.find('tbody')
            res = []
            row = []
            rows = t.find_all('tr')
            for tr in rows:
                for td in tr.find_all('td'):
                    row.append(td.text)
                res.append(row)
                row = []
            df=pd.DataFrame(data=res)

            if len(df.columns)==28: # found first game
                    found = True
            if found:
                h=table.find('thead')
                h1 = h.find('tr')
                h2 = h1.find('th')
                header =h2.text
                team_year = header.split('-')
                team = team_year[0].strip()
                year = team_year[1].strip()
                df['Url']=cur_url
                df['Team']=team
                df['Year']=year
                player_stats = pd.concat([player_stats,df])
    player_stats = player_stats.rename(columns={0:'GameNo',1:'Opponent',2:'Round',3:'Result',4:'Jersey',5:'KI',6:'MK',7:'HB',8:'DI',9:'GL',10:'BH',11:'HO',12:'TK',13:'RB',14:'IF',15:'CL',16:'CG',17:'FF',18:'FA',19:'BR',20:'CP',21:'UP',22:'CM',23:'MI',24:'1%',25:'BO',26:'GA',27:'%P'})
    player_stats['Round']=[fix_round(x) for x in player_stats['Round']]


    games_set = get_games(proxy=False)



    #create one game row for each team
    gamesH = games_set.drop(['AwayTeam','Venue','Attendance','Result','ResultWL'],1)
    gamesA = games_set.drop(['HomeTeam','Venue','Attendance','Result','ResultWL'],1)
    gamesH=gamesH.rename(columns={'HomeTeam':'Team'})
    gamesA=gamesA.rename(columns={'AwayTeam':'Team'})
    gamesAH=pd.concat([gamesH,gamesA])
    gamesAH['Year'] = [str(x) for x in gamesAH['Year']]
    # get date and game id for each player record
    player_stats=pd.merge(player_stats,gamesAH,how='inner',on=['Team','Year','Round'])
    player_stats=player_stats.drop_duplicates(subset=['Url','Year','Round'],keep='first')
    
    return player_stats

def get_pastXthis_opponent(x,team,opponent,dt,team_performaceDF):
    '''
    this function gets previous team performance coming to this game
    takes x(how many games of history), team, opponent, date of current game, team stats dataframe to get games prior to this
    
    '''
    #last 3 against this team
    tp = team_performaceDF[(team_performaceDF['Team']==team) & (team_performaceDF['Date'] <dt) & (team_performaceDF['Opponent']==opponent) ]  # later row.Team
    tp = tp.sort_values(by=['Date'],ascending=False)
    tp = tp.head(x)
    tp = tp.drop(['Round','Date', 'HomeFlag','Year'],1)
    tp_avg = tp.groupby(by='Team').aggregate('mean')
    tp_avg.columns = [str(col) + '_lstXopp' for col in tp_avg.columns]
    if tp_avg.shape[0]==0:
        print('empty row generated for ', dt,' team:',team, ' vs.', opponent)
    return tp_avg

def get_pastXground(x,team,dt,venue,team_performaceDF):
    '''
    this function gets previous team performance coming to this game
    takes x(how many games of history), team, date and venue of current game, team stats dataframe to get games prior to this
    
    '''
    tp2 = team_performaceDF[(team_performaceDF['Team']==team) & (team_performaceDF['Date'] <dt) & (team_performaceDF['Venue'] == venue)] 
    tp2 = tp2.sort_values(by=['Date'],ascending=False)
    tp2 = tp2.head(x)
    tp2 = tp2.drop(['Round','Date', 'HomeFlag','Year'],1)
    tp2_avg = tp2.groupby(by='Team').aggregate('mean')
    tp2_avg.columns = [str(col) + '_lstXgrd' for col in tp2_avg.columns]
    if tp2_avg.shape[0]==0:
        print('empty row generated for ',dt,' at ', venue,' team:',team)
    return tp2_avg

def get_pastX(x,team,dt,team_performaceDF,print_missing=False):
    '''
    this function gets previous team performance coming to this game
    takes x(how many games of history), team, date of current game, team stats dataframe to get games prior to this
    
    '''

    tp1 = team_performaceDF[(team_performaceDF['Team']==team) & (team_performaceDF['Date'] <dt)] 
    tp1 = tp1.sort_values(by=['Date'],ascending=False)
    tp1 = tp1.head(x)
    tp1 = tp1.drop(['Round','Date', 'HomeFlag','Year'],1)
    tp1_avg = tp1.groupby(by='Team').aggregate('mean')
    tp1_avg.columns = [str(col) + '_lstX' for col in tp1_avg.columns]
    if tp1_avg.shape[0]==0 and print_missing:
        print('empty row generated for ', dt,' team:',team)
    return tp1_avg
