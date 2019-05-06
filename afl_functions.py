def get_drive():
    '''
    this is to automate switching between home PC and laptop
    it returns J:\\AFL\\ or D:\\AFL\\ depending if D:\ is available
    
    No parameters required
    '''
    
    import win32api
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    if 'J:\\' in drives:
        drive = 'J:\\AFL\\'
    else:
        drive = 'C:\\Users\\shumi\\Git\\AFL\\'
    return drive


def get_proxy(proxy):
        if proxy:
            from os import environ
            #pwd = input('Please enter your LAN Pwd')
            environ["http_proxy"]="http://vshumilov:lAptop78-@http://kpmgproxy.com/kpmgproxy.pac:8080"
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
    elif name=='Football Park':
        ground='Adelaide Oval'
    elif name=='Adelaide':
        ground='Adelaide Oval'
    elif name=='AO':
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
    elif name=='MS':
        ground = 'Docklands'
    elif name=='MRVL':
        ground = 'Docklands'
    elif name=='Etihad':
        ground = 'Docklands'
    elif name=='GMHBA Stadium':
        ground='Kardinia Park'
    elif name=='GMHBA':
        ground='Kardinia Park'
    elif name=='Gabba':
        ground = 'Gabba'
    elif name=='G':
        ground = 'Gabba'
    elif name=='Jiangwan':
        ground = 'Jiangwan Stadium'
    elif name=='Jiangwan Stadium, China':
        ground = 'Jiangwan Stadium'
    elif name=='M.C.G':
        ground = 'M.C.G.'
    elif name=='MCG':
        ground = 'M.C.G.'
    elif name=='MARS':
        ground = 'Eureka Stadium'
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
    elif name=='Subiaco':
        ground='Perth Stadium'
    elif name=='OS':
        ground='Perth Stadium'
    elif name=='SCG':
        ground='S.C.G.'
    elif name=='Spotless Stadium':
        ground='Sydney Showground'
    elif name=='SSGS':
        ground='Sydney Showground'
    elif name=='Spotless':
        ground='Sydney Showground'
    elif name=='UNSW Canberra Oval':
        ground='Manuka Oval'
    elif name=='MO':
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
            if len(df)>1 and 'Ladder' in df[0][0] and 'Rd' in df[0][0] and len(df.columns)>2:
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
    #ldr = pd.merge(ladder_f.drop(['Round'],1),ldr,how='inner',on=['Season'])
    ladder = pd.concat([ladder,ldr],sort=False)
    ladder = ladder.sort_values(by=['Team','Season'],axis=0)
    ladder['PosOld']=ladder.Position.shift(1)  #previous ladder position taken
    ladder = ladder.drop(['Position'],1)
    ladder['Round']= [int(x) for x in ladder['Round']]
    ladder=ladder.dropna(axis=0)
    ladder['PosOld']= [int(x) for x in ladder['PosOld']]  
    return ladder


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
    #games = games.drop(['H','A'],1)
    games['ResultWL'] = [1 if x>=0.5 else 0 for x in games.Result]
    games['Venue']=[fix_venue(x) for x in games['Venue']]
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
                cols = [c for c in x.columns if c.lower()[:4] != 'unna']
                x=x[cols]
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

    team_performace['KIt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['KI']]
    team_performace['MKt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['MK']]
    team_performace['HBt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['HB']]
    team_performace['DIt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['DI']]
    team_performace['GLt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['GL']]
    team_performace['BHt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['BH']]
    team_performace['HOt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['HO']]
    team_performace['TKt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['TK']]
    team_performace['RBt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['RB']]
    team_performace['IFt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['IF']]
    team_performace['CLt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['CL']]
    team_performace['CGt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['CG']]
    team_performace['FFt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['FF']]
    team_performace['FAt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['FA']]
    team_performace['BRt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['BR']]
    team_performace['CPt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['CP']]
    team_performace['UPt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['UP']]
    team_performace['CMt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['CM']]
    team_performace['MIt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['MI']]
    team_performace['1%t'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['1%']]
    team_performace['BOt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['BO']]
    team_performace['GAt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['GA']]
    #added Score metric SC
    team_performace['SCt'] = [g*6+b for g,b in zip(team_performace['GLt'],team_performace['BHt'])]
    # this version change - getting opponent's stats "o" in column name is for "opposition"
    team_performace['KIo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['KI']]
    team_performace['MKo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['MK']]
    team_performace['HBo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['HB']]
    team_performace['DIo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['DI']]
    team_performace['GLo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['GL']]
    team_performace['BHo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['BH']]
    team_performace['HOo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['HO']]
    team_performace['TKo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['TK']]
    team_performace['RBo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['RB']]
    team_performace['IFo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['IF']]
    team_performace['CLo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['CL']]
    team_performace['CGo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['CG']]
    team_performace['FFo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['FF']]
    team_performace['FAo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['FA']]
    team_performace['BRo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['BR']]
    team_performace['CPo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['CP']]
    team_performace['UPo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['UP']]
    team_performace['CMo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['CM']]
    team_performace['MIo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['MI']]
    team_performace['1%o'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['1%']]
    team_performace['BOo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['BO']]
    team_performace['GAo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['GA']]
    team_performace['SCo'] = [g*6+b for g,b in zip(team_performace['GLo'],team_performace['BHo'])]
    #added Score metric SC
    
    #difference metric
    team_performace['KI'] = [t-o for t,o in zip(team_performace['KIt'],team_performace['KIo'])]
    team_performace['MK'] = [t-o for t,o in zip(team_performace['MKt'],team_performace['MKo'])]
    team_performace['HB'] = [t-o for t,o in zip(team_performace['HBt'],team_performace['HBo'])]
    team_performace['DI'] = [t-o for t,o in zip(team_performace['DIt'],team_performace['DIo'])]
    team_performace['GL'] = [t-o for t,o in zip(team_performace['GLt'],team_performace['GLo'])]
    team_performace['BH'] = [t-o for t,o in zip(team_performace['BHt'],team_performace['BHo'])]
    team_performace['HO'] = [t-o for t,o in zip(team_performace['HOt'],team_performace['HOo'])]
    team_performace['TK'] = [t-o for t,o in zip(team_performace['TKt'],team_performace['TKo'])]
    team_performace['RB'] = [t-o for t,o in zip(team_performace['RBt'],team_performace['RBo'])]
    team_performace['IF'] = [t-o for t,o in zip(team_performace['IFt'],team_performace['IFo'])]
    team_performace['CL'] = [t-o for t,o in zip(team_performace['CLt'],team_performace['CLo'])]
    team_performace['CG'] = [t-o for t,o in zip(team_performace['CGt'],team_performace['CGo'])]
    team_performace['FF'] = [t-o for t,o in zip(team_performace['FFt'],team_performace['FFo'])]
    team_performace['FA'] = [t-o for t,o in zip(team_performace['FAt'],team_performace['FAo'])]
    team_performace['BR'] = [t-o for t,o in zip(team_performace['BRt'],team_performace['BRo'])]
    team_performace['CP'] = [t-o for t,o in zip(team_performace['CPt'],team_performace['CPo'])]
    team_performace['UP'] = [t-o for t,o in zip(team_performace['UPt'],team_performace['UPo'])]
    team_performace['CM'] = [t-o for t,o in zip(team_performace['CMt'],team_performace['CMo'])]
    team_performace['MI'] = [t-o for t,o in zip(team_performace['MIt'],team_performace['MIo'])]
    team_performace['1%'] = [t-o for t,o in zip(team_performace['1%t'],team_performace['1%o'])]
    team_performace['BO'] = [t-o for t,o in zip(team_performace['BOt'],team_performace['BOo'])]
    team_performace['GA'] = [t-o for t,o in zip(team_performace['GAt'],team_performace['GAo'])]
    team_performace['SC'] = [t-o for t,o in zip(team_performace['SCt'],team_performace['SCo'])]
    return team_performace

def get_team_performance_hist_rel(season_from,season_to,proxy=False):
    '''
    this relative version of team performance history
    main metric is expressed as team's relative advantage over the opponent
    e.g. if team goals is 12 and opponent goals is 6
    the main GL metric shows (12-6)/(12+6) = 0.333
    if both team and opponent metrics are zero then combined one =0
    so values range from -1 to +1
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
                cols = [c for c in x.columns if c.lower()[:4] != 'unna']
                x=x[cols]
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

    team_performace['KIt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['KI']]
    team_performace['MKt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['MK']]
    team_performace['HBt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['HB']]
    team_performace['DIt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['DI']]
    team_performace['GLt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['GL']]
    team_performace['BHt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['BH']]
    team_performace['HOt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['HO']]
    team_performace['TKt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['TK']]
    team_performace['RBt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['RB']]
    team_performace['IFt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['IF']]
    team_performace['CLt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['CL']]
    team_performace['CGt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['CG']]
    team_performace['FFt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['FF']]
    team_performace['FAt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['FA']]
    team_performace['BRt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['BR']]
    team_performace['CPt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['CP']]
    team_performace['UPt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['UP']]
    team_performace['CMt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['CM']]
    team_performace['MIt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['MI']]
    team_performace['1%t'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['1%']]
    team_performace['BOt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['BO']]
    team_performace['GAt'] = [0 if len(x.split('-')[0])==0 else int(x.split('-')[0]) for x in team_performace['GA']]
    #added Score metric SC
    team_performace['SCt'] = [g*6+b for g,b in zip(team_performace['GLt'],team_performace['BHt'])]
    # this version change - getting opponent's stats "o" in column name is for "opposition"
    team_performace['KIo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['KI']]
    team_performace['MKo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['MK']]
    team_performace['HBo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['HB']]
    team_performace['DIo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['DI']]
    team_performace['GLo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['GL']]
    team_performace['BHo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['BH']]
    team_performace['HOo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['HO']]
    team_performace['TKo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['TK']]
    team_performace['RBo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['RB']]
    team_performace['IFo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['IF']]
    team_performace['CLo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['CL']]
    team_performace['CGo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['CG']]
    team_performace['FFo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['FF']]
    team_performace['FAo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['FA']]
    team_performace['BRo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['BR']]
    team_performace['CPo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['CP']]
    team_performace['UPo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['UP']]
    team_performace['CMo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['CM']]
    team_performace['MIo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['MI']]
    team_performace['1%o'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['1%']]
    team_performace['BOo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['BO']]
    team_performace['GAo'] = [0 if len(x.split('-')[1])==0 else int(x.split('-')[1]) for x in team_performace['GA']]
    team_performace['SCo'] = [g*6+b for g,b in zip(team_performace['GLo'],team_performace['BHo'])]
    #added Score metric SC
    
    #difference metric - now relative version ranging from -1 to +1 where 0 is even performance
    team_performace['KI'] = [(t-o)/(t+o) if (t+o)>0 else 0 for t,o in zip(team_performace['KIt'],team_performace['KIo'])]
    team_performace['MK'] = [(t-o)/(t+o) if (t+o)>0 else 0 for t,o in zip(team_performace['MKt'],team_performace['MKo'])]
    team_performace['HB'] = [(t-o)/(t+o) if (t+o)>0 else 0 for t,o in zip(team_performace['HBt'],team_performace['HBo'])]
    team_performace['DI'] = [(t-o)/(t+o) if (t+o)>0 else 0 for t,o in zip(team_performace['DIt'],team_performace['DIo'])]
    team_performace['GL'] = [(t-o)/(t+o) if (t+o)>0 else 0 for t,o in zip(team_performace['GLt'],team_performace['GLo'])]
    team_performace['BH'] = [(t-o)/(t+o) if (t+o)>0 else 0 for t,o in zip(team_performace['BHt'],team_performace['BHo'])]
    team_performace['HO'] = [(t-o)/(t+o) if (t+o)>0 else 0 for t,o in zip(team_performace['HOt'],team_performace['HOo'])]
    team_performace['TK'] = [(t-o)/(t+o) if (t+o)>0 else 0 for t,o in zip(team_performace['TKt'],team_performace['TKo'])]
    team_performace['RB'] = [(t-o)/(t+o) if (t+o)>0 else 0 for t,o in zip(team_performace['RBt'],team_performace['RBo'])]
    team_performace['IF'] = [(t-o)/(t+o) if (t+o)>0 else 0 for t,o in zip(team_performace['IFt'],team_performace['IFo'])]
    team_performace['CL'] = [(t-o)/(t+o) if (t+o)>0 else 0 for t,o in zip(team_performace['CLt'],team_performace['CLo'])]
    team_performace['CG'] = [(t-o)/(t+o) if (t+o)>0 else 0 for t,o in zip(team_performace['CGt'],team_performace['CGo'])]
    team_performace['FF'] = [(t-o)/(t+o) if (t+o)>0 else 0 for t,o in zip(team_performace['FFt'],team_performace['FFo'])]
    team_performace['FA'] = [(t-o)/(t+o) if (t+o)>0 else 0 for t,o in zip(team_performace['FAt'],team_performace['FAo'])]
    team_performace['BR'] = [(t-o)/(t+o) if (t+o)>0 else 0 for t,o in zip(team_performace['BRt'],team_performace['BRo'])]
    team_performace['CP'] = [(t-o)/(t+o) if (t+o)>0 else 0 for t,o in zip(team_performace['CPt'],team_performace['CPo'])]
    team_performace['UP'] = [(t-o)/(t+o) if (t+o)>0 else 0 for t,o in zip(team_performace['UPt'],team_performace['UPo'])]
    team_performace['CM'] = [(t-o)/(t+o) if (t+o)>0 else 0 for t,o in zip(team_performace['CMt'],team_performace['CMo'])]
    team_performace['MI'] = [(t-o)/(t+o) if (t+o)>0 else 0 for t,o in zip(team_performace['MIt'],team_performace['MIo'])]
    team_performace['1%'] = [(t-o)/(t+o) if (t+o)>0 else 0 for t,o in zip(team_performace['1%t'],team_performace['1%o'])]
    team_performace['BO'] = [(t-o)/(t+o) if (t+o)>0 else 0 for t,o in zip(team_performace['BOt'],team_performace['BOo'])]
    team_performace['GA'] = [(t-o)/(t+o) if (t+o)>0 else 0 for t,o in zip(team_performace['GAt'],team_performace['GAo'])]
    team_performace['SC'] = [(t-o)/(t+o) if (t+o)>0 else 0 for t,o in zip(team_performace['SCt'],team_performace['SCo'])]
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



#create functions to calculate adj.ladder points 
def adj_points_home(lst):
    w1=5.0 # for winning against top4 team as of end of last season
    w2=4.0 # for winning against top5-8 team as of end of last season
    w3=3.0 # for winning against 9-13 team as of end of last season
    w4=2.5 # for winning against 14-18 team as of end of last season
    l1=0.5 # for a bottom team (>=12) losing against to top 4 team as of end of last season with close margin
    l2=0.5 # for a bottom team (>=12) losing against to top 5-8 team as of end of last season with close margin

    if lst['ResultWL'] >0.5:
        if lst['PreseasonRankA']<=4:
            return w1
        elif lst['PreseasonRankA']<=8:
            return w2
        elif lst['PreseasonRankA']<=13:
            return w3
        else:
            return w4   
    else:
        if lst['PreseasonRankH']>=12 and lst['PreseasonRankA']<=4 and lst['Result']>=0.42:
            return l1
        elif lst['PreseasonRankH']>=12 and lst['PreseasonRankA']<=8 and lst['Result']>=0.42:
            return l2
        else:
            return 0
def adj_points_away(lst):
    w1=5.0 # for winning against top4 team as of end of last season
    w2=4.0 # for winning against top5-8 team as of end of last season
    w3=3.0 # for winning against 9-13 team as of end of last season
    w4=2.5 # for winning against 14-18 team as of end of last season
    l1=0.5 # for a bottom team (>=12) losing against to top 4 team as of end of last season with close margin
    l2=0.5 # for a bottom team (>=12) losing against to top 5-8 team as of end of last season with close margin
    if lst['ResultWL'] <0.5:
        if lst['PreseasonRankH']<=4:
            return w1
        elif lst['PreseasonRankH']<=8:
            return w2
        elif lst['PreseasonRankH']<=13:
            return w3
        else:
            return w4   
    else:
        if lst['PreseasonRankA']>=12 and lst['PreseasonRankH']<=4 and lst['Result']<=0.58:
            return l1
        elif lst['PreseasonRankA']>=12 and lst['PreseasonRankH']<=8 and lst['Result']<=0.58:
            return l2
        else:
            return 0


# function to create a column with points for this team from either home or away column
def adj_points_combo(lst):
    if lst['HomeFlag'] ==1:
        return lst['PointsHome']
    else:
        return lst['PointsAway']

def get_pastXgames(x,team,dt,DF):
    '''
    this function gets previous team performance coming to this game
    takes x(how many games of history), team, date of current game, team stats dataframe to get games prior to this

    '''
    newDF = DF[(DF['Team']==team) & (DF['Date'] <dt)] 
    newDF = newDF.sort_values(by=['Date'],ascending=False)
    newDF = newDF.head(x)
    newDF = newDF.drop(['Round','GameID','Result','Date','Venue','H','A','ResultWL','PointsHome','PointsAway','PreseasonRankA','PreseasonRankH', 'HomeFlag','Year'],1)
    newDF = newDF.groupby(by='Team',as_index=False).aggregate('sum')
    if len(newDF)>0:
        return newDF.iloc[0]['TeamPoints']
    else:
        return 0

def get_game_base(season_from,season_to,proxy=False):
    '''
    This function returns does the following:
    1. Applies adjusted ladder points
    2. Create separate reacord for each team - home and away teams
    
    Output - 2 dataframes:
    1. games_for_join - one team -sided version and  has more history beyond the train period (+ 3 seasons)
    2. train_data - exact train period limited data
    '''
    import pandas as pd
    ladder = get_ladder(seas_from=season_from-3,seas_to=season_to,proxy=False)

    # get latest ladder for each team for each season
    ladder = ladder.sort_values(by=['Season','Team','Round'])
    season_end = ladder.groupby(by=['Season','Team'],as_index=False).last()
    season_end['Season']=[x+1 for x in season_end['Season']]  # enable a join from next seson
    
    games = get_games(proxy=False)
    
    
    train_data = games[(games['Year']>=season_from-2) & (games['Year']<=season_to)]

    # bring last year ladder at season end - Not including finals
    games = pd.merge(games,season_end.drop(['Games','Percentage','Points','Round'],1),left_on=['HomeTeam','Year'], right_on=['Team','Season'],how='inner')
    games = games.drop(['Season','Team'],1)
    games = pd.merge(games,season_end.drop(['Games','Percentage','Points','Round'],1),left_on=['AwayTeam','Year'], right_on=['Team','Season'],how='inner')
    games = games.drop(['Season','Team'],1)
    games = games.rename(columns={"PosOld_x": "PreseasonRankH", "PosOld_y": "PreseasonRankA"})


    #Final code to assign adjusted ladder points - best parameters are 5,4,3,2.5,0.5,0.5

    #apply ladder points by rows of games dataframe
    games['PointsHome'] = games.apply(adj_points_home, axis=1)
    games['PointsAway'] = games.apply(adj_points_away, axis=1)

    # create a table which makes 2 records out of 1 game for home and away team - this allows sequencing by team and look in the past
    gm_H = games.copy()
    gm_H['Team']=gm_H['HomeTeam']
    gm_H['HomeFlag']=1
    gm_H = gm_H.drop(['HomeTeam','AwayTeam'], 1)

    gm_A = games.copy()
    gm_A['Team']=gm_A['AwayTeam']
    gm_A['HomeFlag']=0
    gm_A['ResultWL']=1-gm_A['ResultWL'] # reverse outcome
    gm_A = gm_A.drop(['HomeTeam','AwayTeam'], 1)

    games_for_join = pd.concat([gm_H,gm_A])
    del gm_H
    del gm_A

    games_for_join['TeamPoints'] = games_for_join.apply(adj_points_combo, axis=1)
    return games_for_join,train_data

def adj_ladder(train_data,games_for_join):
    '''
    This function iterates over train_data and 
    applies/calculates adjusted ladder
    Second dataframe used is longer history version of
    training_data
    
    '''
    import pandas as pd 
    # iterate over training data
    ladder_span = 21  # 21 proven to be the best performance
    adj_ladder = pd.DataFrame()
    for i,row in train_data.iterrows():
        #gm=row['GameID']
        tm = row['HomeTeam']
        dt = row['Date']

        new_row = pd.DataFrame(columns=['Date','HomeTeam','AdLadderHm','AdLadderAw'])
        h= get_pastXgames(ladder_span,row.HomeTeam,row.Date,games_for_join)
        a= get_pastXgames(ladder_span,row.AwayTeam,row.Date,games_for_join)
        new_row.loc[0]=[dt,tm,h,a]
        adj_ladder = pd.concat([ adj_ladder,new_row])    
    return adj_ladder


def rescale_stats(perf_data):
    '''
    This function rescales performance metrics
    according to team sterangth difference
    Scoring Metrics (Goals and behinds) are not adjusted
    '''
    # list of columns to scale is determined by subtraction of ones where no scaling is needed from total list of columns
    # this allows new metrics to be added (unlikely)
    column_list = perf_data.columns
    column_list=column_list.drop(['Round', 'Opponent', 'Team', 'Year', 'Date', 'Venue', 'H', 'A', 'ResultWL',
           'HomeFlag', 'AdjLadderDiff','GL','BH'])   #Goals and behinds are excluded as they make up the result
    # scale factors
    s1=1.3 #for more than 40 points
    s2=1.1 #for 20-40 points
    s3=1.05 #for 10-20 points

    # no scale version: comment out when not in use !!!!!!!
    #s1=1 #for more than 40 points
    #s2=1 #for 20-40 points
    #s3=1 #for 10-20 points

    perf_data=perf_data.reset_index(drop=True)

    for index, row in perf_data.iterrows():
        row=row.copy()
        ldr = row.AdjLadderDiff
        if ldr <-40:
            for column in column_list:
                perf_data.loc[index, column] = row[column]*s1
        elif ldr <-20:
            for column in column_list:
                perf_data.loc[index, column] = row[column]*s2
        elif ldr <-10:
            for column in column_list:
                perf_data.loc[index, column] = row[column]*s3
        elif ldr>40:
            for column in column_list:
                perf_data.loc[index, column] = row[column]/s1
        elif ldr>20:
            for column in column_list:
                perf_data.loc[index, column] = row[column]/s2
        elif ldr>10:
            for column in column_list:
                perf_data.loc[index, column] = row[column]/s3
        else: # away team bump
            if row.HomeFlag==0:
                for column in column_list:
                    perf_data.loc[index, column] = row[column]*s3
        return perf_data


def get_data(season_from,season_to,proxy=False,train_mode=True):
    '''
    This function creates a dataset with all necessary adjustments
    the resulting set can be used for training or scoring
    leave train_mode=True when creating training set
    set train_mode=False when scoring/predicting
    When scoring, you need to have a csv file in the folder
    When scoring set season_from and season_to to the same season
    containing Date,HomeTeam,AwayTeam,Venue (assuming Round is not used as variable !!!!!!!)
    
    '''
    import pandas as pd

    if not train_mode:
        # use CSV
        score_data = pd.read_csv('C:\\Users\\shumi\\Git\\AFL\\ToScore.csv')

        #clean names
        score_data['HomeTeam'] = [fix_team_name(x) for x in score_data.HomeTeam]
        score_data['AwayTeam'] = [fix_team_name(x) for x in score_data.AwayTeam]
        score_data['Venue'] = [fix_venue(x) for x in score_data.Venue]
        score_data['Year']=season_to
        score_data['Date'] = pd.to_datetime(score_data['Date'])

    games_for_join, train_data = get_game_base(season_from=season_from,season_to=season_to,proxy=False)
    # at this point games_for_join has everything, and it is time to bring history - aka adjusted ladder

    
    
    # bring adjusted ladder to main dataset
    train_data=pd.merge(train_data,adj_ladder(train_data,games_for_join),how='inner',on=['Date','HomeTeam'])
    train_data['AdjLadderDiff'] = train_data['AdLadderHm'] - train_data['AdLadderAw']

    # get team performance to make adjustments on team strength
    # relative version
    team_perf = get_team_performance_hist_rel(season_from=season_from-2,season_to=season_to,proxy=False)
    print('Max date in performance data: ',team_perf['Date'].max())
    # absolute version:
    #team_perf = get_team_performance_hist(season_from=season_from-2,season_to=season_to,proxy=False)


    #bring adjusted ladder difference to use with metrics
    #idea: if a team is playing gainst a weaker team their metrics should be scaled down


    team_perfH = pd.merge(team_perf,train_data[['Date', 'HomeTeam','AdjLadderDiff']],
                         left_on=['Date', 'Team'],right_on=['Date', 'HomeTeam'])
    team_perfA = pd.merge(team_perf,train_data[['Date', 'AwayTeam','AdjLadderDiff']],
                         left_on=['Date', 'Team'],right_on=['Date', 'AwayTeam'])

    team_perfA['AdjLadderDiff'] = [-x for x in team_perfA['AdjLadderDiff']] #reverse for away team
    team_perf1 = pd.concat([team_perfH,team_perfA],sort=False)
    team_perf1 = team_perf1.drop(['HomeTeam','AwayTeam'],1)    

    # now need to re-scale metrics according to team strength difference (except scoring ones)
    team_perf1=rescale_stats(team_perf1)

    #limit dataset to training period (was allowed earlier to grab adj ladder)
    train_data = train_data[train_data['Year']>=season_from]

    #switch starting point depending on mode
    if train_mode:
        data_to_use=train_data.copy()
    else:
        score_data1 = adj_ladder(train_data=score_data,games_for_join=games_for_join)
        score_data1['AdjLadderDiff'] = score_data1['AdLadderHm'] - score_data1['AdLadderAw']
        score_data1 = score_data1.drop(['AdLadderHm','AdLadderAw'],1)
        score_data = score_data.merge(score_data1, how='inner', on = ['Date', 'HomeTeam'])
        data_to_use=score_data.copy()
    
    # this gets 2 df's for home and away team each for last X games against any oppponent
    length=15 # how many past games to look at - 15 was obtained as the best option
    hist_df_hm=pd.DataFrame()
    hist_df_aw=pd.DataFrame()
    for i, row in data_to_use.iterrows():
            hist = get_pastX(dt=row.Date,x=length,team=row.HomeTeam,team_performaceDF=team_perf1)
            hist['Team']=row.HomeTeam
            hist['Date']=row.Date
            hist['Opponent']=row.AwayTeam
            hist_df_hm=pd.concat([hist_df_hm,hist])
            hist = get_pastX(dt=row.Date,x=length,team=row.AwayTeam,team_performaceDF=team_perf1)
            hist['Team']=row.AwayTeam
            hist['Date']=row.Date
            #hist['GameID']=row.GameID
            hist_df_aw=pd.concat([hist_df_aw,hist])

    hist_df_hm=hist_df_hm.reset_index(drop=True)
    hist_df_aw=hist_df_aw.reset_index(drop=True)

    #columns ignored from get_team_performance function - the absolute ones in this case - keep only differences
    remove_list=['KIt', 'MKt', 'HBt', 'DIt', 'GLt','BHt', 'HOt', 'TKt', 'RBt', 'IFt','CLt',
                 'CGt', 'FFt', 'FAt', 'BRt','CPt', 'UPt','CMt', 'MIt', '1%t',
                 'BOt', 'GAt','SCt','KIo', 'MKo', 'HBo', 'DIo', 'GLo','BHo',
                 'HOo', 'TKo', 'RBo', 'IFo','CLo', 'CGo', 'FFo', 'FAo', 'BRo',
                 'CPo', 'UPo', 'CMo', 'MIo', '1%o','BOo', 'GAo','SCo']

    #remove opposition metrics
    hist_df_hm = hist_df_hm.drop([x+'_lstX' for x in remove_list],1)
    hist_df_aw = hist_df_aw.drop([x+'_lstX' for x in remove_list],1)

    # tweak to resolve a mistery of AdjLadderDiff disapperiang somethimes
    if 'AdjLadderDiff_lstX' in hist_df_hm.columns:
        hist_df_hm=hist_df_hm.drop(['AdjLadderDiff_lstX'],1)
    if 'AdjLadderDiff_lstX' in hist_df_aw.columns:
        hist_df_aw=hist_df_aw.drop(['AdjLadderDiff_lstX'],1)
    
    # now past metrics averages need to be brought together for each geame to calculate a difference
    hist_df = pd.merge(hist_df_hm.drop(['H_lstX', 'A_lstX','ResultWL_lstX'],1),
                       hist_df_aw.drop(['H_lstX', 'A_lstX','ResultWL_lstX'],1),
                       how='inner',left_on=['Opponent','Date'], right_on=['Team','Date'])

    hist_df = hist_df.drop(['Opponent','Team_y'],1)
    hist_df = hist_df.rename(columns={'Team_x':'Team'})

    #prepare to calculate differences
    column_list =['KI_lstX', 'MK_lstX', 'HB_lstX', 'DI_lstX', 'GL_lstX',
           'BH_lstX', 'HO_lstX', 'TK_lstX', 'RB_lstX', 'IF_lstX',
           'CL_lstX', 'CG_lstX', 'FF_lstX', 'FA_lstX', 'BR_lstX',
           'CP_lstX', 'UP_lstX', 'CM_lstX', 'MI_lstX', '1%_lstX',
           'BO_lstX', 'GA_lstX','SC_lstX']
    #calculate differences and drop original columns
    for col in column_list:
        hist_df[col] = [a-b for a,b in zip(hist_df[col+'_x'],hist_df[col+'_y'])]
        hist_df = hist_df.drop(col+'_x',1)
        hist_df = hist_df.drop(col+'_y',1)

    # add to training set - strength adjusted past stats
    train_data1= pd.merge(data_to_use,hist_df,left_on=['HomeTeam','Date'],right_on=['Team','Date'])
    train_data1 = train_data1.drop(['Team'],1)
    # this gets 2 df's for home and away team each for last X games at this GROUND
    length=10 # how many past games to look at 
    hist_df_hm=pd.DataFrame()
    hist_df_aw=pd.DataFrame()
    for i, row in data_to_use.iterrows():
            hist = get_pastXground(dt=row.Date,x=length,team=row.HomeTeam,venue=row.Venue,team_performaceDF=team_perf1)
            hist['Team']=row.HomeTeam
            hist['Date']=row.Date
            hist['Opponent']=row.AwayTeam
            #hist['GameID']=row.GameID
            hist_df_hm=pd.concat([hist_df_hm,hist])
            hist = get_pastXground(dt=row.Date,x=length,team=row.AwayTeam,venue=row.Venue,team_performaceDF=team_perf1)
            hist['Team']=row.AwayTeam
            hist['Date']=row.Date
            #hist['GameID']=row.GameID
            hist_df_aw=pd.concat([hist_df_aw,hist])

    hist_df_hm=hist_df_hm.reset_index(drop=True)
    hist_df_aw=hist_df_aw.reset_index(drop=True)

    #remove opposition metrics
    hist_df_hm = hist_df_hm.drop([x+'_lstXgrd' for x in remove_list],1)
    hist_df_aw = hist_df_aw.drop([x+'_lstXgrd' for x in remove_list],1)

    # tweak to resolve a mistery of AdjLadderDiff disapperiang somethimes
    if 'AdjLadderDiff_lstXgrd' in hist_df_hm.columns:
        hist_df_hm=hist_df_hm.drop(['AdjLadderDiff_lstXgrd'],1)
    if 'AdjLadderDiff_lstXgrd' in hist_df_aw.columns:
        hist_df_aw=hist_df_aw.drop(['AdjLadderDiff_lstXgrd'],1)
   
    
    # now past metrics averages need to be brought together for each geame to calculate a difference
    hist_df = pd.merge(hist_df_hm.drop(['H_lstXgrd', 'A_lstXgrd','ResultWL_lstXgrd'],1),
                       hist_df_aw.drop(['H_lstXgrd', 'A_lstXgrd','ResultWL_lstXgrd'],1),
                       how='inner',left_on=['Opponent','Date'], right_on=['Team','Date'])
    hist_df = hist_df.drop(['Opponent','Team_y'],1)
    hist_df = hist_df.rename(columns={'Team_x':'Team'})

    #prepare to calculate differences
    column_list =['KI_lstXgrd', 'MK_lstXgrd', 'HB_lstXgrd', 'DI_lstXgrd', 'GL_lstXgrd',
           'BH_lstXgrd', 'HO_lstXgrd', 'TK_lstXgrd', 'RB_lstXgrd', 'IF_lstXgrd',
           'CL_lstXgrd', 'CG_lstXgrd', 'FF_lstXgrd', 'FA_lstXgrd', 'BR_lstXgrd',
           'CP_lstXgrd', 'UP_lstXgrd', 'CM_lstXgrd', 'MI_lstXgrd', '1%_lstXgrd',
           'BO_lstXgrd', 'GA_lstXgrd','SC_lstXgrd']
    #calculate differences and drop original columns
    for col in column_list:
        hist_df[col] = [a-b for a,b in zip(hist_df[col+'_x'],hist_df[col+'_y'])]
        hist_df = hist_df.drop(col+'_x',1)
        hist_df = hist_df.drop(col+'_y',1)

    # add to training set - strength adjusted past stats
    train_data2= pd.merge(train_data1,hist_df,how='left',left_on=['HomeTeam','Date'],right_on=['Team','Date'])
    train_data2 = train_data2.drop(['Team'],1)
    # This opponent
    # this gets 2 df's for home and away team each for last X games with this opponent
    length=5 # how many past games to look at hist_df_hm=pd.DataFrame()
    hist_df_hm=pd.DataFrame()
    hist_df_aw=pd.DataFrame()
    for i, row in data_to_use.iterrows():
            hist = get_pastXthis_opponent(dt=row.Date,x=length,team=row.HomeTeam,opponent=row.AwayTeam,team_performaceDF=team_perf1)
            hist['Team']=row.HomeTeam
            hist['Date']=row.Date
            hist['Opponent']=row.AwayTeam
            #hist['GameID']=row.GameID
            hist_df_hm=pd.concat([hist_df_hm,hist])
            hist = get_pastXthis_opponent(dt=row.Date,x=length,team=row.AwayTeam,opponent=row.HomeTeam,team_performaceDF=team_perf1)
            hist['Team']=row.AwayTeam
            hist['Date']=row.Date
            #hist['GameID']=row.GameID
            hist_df_aw=pd.concat([hist_df_aw,hist])

    hist_df_hm=hist_df_hm.reset_index(drop=True)
    hist_df_aw=hist_df_aw.reset_index(drop=True)

    #remove opposition metrics
    hist_df_hm = hist_df_hm.drop([x+'_lstXopp' for x in remove_list],1)
    hist_df_aw = hist_df_aw.drop([x+'_lstXopp' for x in remove_list],1)

    # tweak to resolve a mistery of AdjLadderDiff disapperiang somethimes
    if 'AdjLadderDiff_lstXopp' in hist_df_hm.columns:
        hist_df_hm=hist_df_hm.drop(['AdjLadderDiff_lstXopp'],1)
    if 'AdjLadderDiff_lstXopp' in hist_df_aw.columns:
        hist_df_aw=hist_df_aw.drop(['AdjLadderDiff_lstXopp'],1)
   
    
    # now past metrics averages need to be brought together for each geame to calculate a difference
    hist_df = pd.merge(hist_df_hm.drop(['H_lstXopp', 'A_lstXopp', 'ResultWL_lstXopp'],1),
                       hist_df_aw.drop(['H_lstXopp', 'A_lstXopp', 'ResultWL_lstXopp'],1),
                       how='inner',left_on=['Opponent','Date'], right_on=['Team','Date'])
    hist_df = hist_df.drop(['Opponent','Team_y'],1)
    hist_df = hist_df.rename(columns={'Team_x':'Team'})
    #prepare to calculate differences
    column_list =['KI_lstXopp', 'MK_lstXopp', 'HB_lstXopp', 'DI_lstXopp', 'GL_lstXopp',
           'BH_lstXopp', 'HO_lstXopp', 'TK_lstXopp', 'RB_lstXopp', 'IF_lstXopp',
           'CL_lstXopp', 'CG_lstXopp', 'FF_lstXopp', 'FA_lstXopp', 'BR_lstXopp',
           'CP_lstXopp', 'UP_lstXopp', 'CM_lstXopp', 'MI_lstXopp', '1%_lstXopp',
           'BO_lstXopp', 'GA_lstXopp','SC_lstXopp']
    #calculate differences and drop original columns
    for col in column_list:
        hist_df[col] = [a-b for a,b in zip(hist_df[col+'_x'],hist_df[col+'_y'])]
        hist_df = hist_df.drop(col+'_x',1)
        hist_df = hist_df.drop(col+'_y',1)

    # add to training set - strength adjusted past stats
    train_data3= train_data2.merge(hist_df,how='left',left_on=['HomeTeam','Date'],right_on=['Team','Date'])
    train_data3 = train_data3.drop(['Team'],1)
    # now change na to 0.0
    train_data3 = train_data3.fillna(0)
    
    # home away factor - maintained in the csv
    hm_aw = pd.read_csv('C:\\Users\\shumi\\Git\\AFL\\HmAwDisadvantage.csv')
    train_data3 = pd.merge(train_data3,hm_aw,how='inner',left_on=['HomeTeam','Venue'],right_on=['Team','Venue'])
    train_data3=train_data3.rename(columns={'HA_Disadvantage':'H_Disadv'})
    train_data3 = pd.merge(train_data3,hm_aw,how='inner',left_on=['AwayTeam','Venue'],right_on=['Team','Venue'])
    train_data3=train_data3.rename(columns={'HA_Disadvantage':'A_Disadv'})
    train_data3['HmAwDisadvantage']=[x-y for (x,y) in zip(train_data3['H_Disadv'],train_data3['A_Disadv'])]
    train_data3 = train_data3.drop(['H_Disadv','A_Disadv','Team_x', 'Team_y'],1)

    return train_data3

def get_fixtureAFL():
    '''
    this function grabs Fixture from AFL.com.au website
    note, it should be tested during a season to see what comes back 
    i.e. current round only or more
    
    '''
    import requests
    from bs4 import BeautifulSoup
    import json
    import pandas as pd


    fixture = pd.DataFrame()

    # Usual code to get the website - Use requests, it's much easier
    url = 'http://www.afl.com.au/fixture'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    # lets get the div that containts the script
    fixtures_container = soup.find("div", {"class": "o-main-container__fixture"})

    # Lets get the script in the div and just output the text
    script = fixtures_container.find('script2').text

    # Lets get hacky and remove the first bit of crap data
    clean_data = script.replace("\n    window.byClubData = ","")

    # Here is your JSON data. Happy days
    json_data = json.loads(clean_data)

    i=1
    for data in json_data['fixtures']:
        aw =data.get('awayTeam','')
        aw_team=aw.get('teamName','')

        hm =data.get('homeTeam','')
        hm_team=hm.get('teamName','')

        mtch = data.get('match','')

        rnd= mtch.get('roundNumber','')
        venue = mtch.get('venueAbbr','')
        dts= mtch.get('startDateTimes','')

        date = dts[0].get("date")


        new_row = pd.DataFrame(columns=['Round','GameNo','HomeTeam','AwayTeam','Venue','Date'])
        new_row.loc[0]=[rnd,i,fix_team_name(hm_team),fix_team_name(aw_team),fix_venue(venue),date]
        fixture = pd.concat([fixture,new_row])        
        i+=1
    return fixture

#function to get last X player performance metrics 
def player_last_X(url,x,season,rnd,df):
    import numpy as np
    '''
    this function produces latest x performances for a given player 
    prior to this round - e.g. last 20 for player P before this round
    Returns df of metrics in ORDER of latest game first (DESC)
    url - player url on afltables.com
    x - how many games of past performance you need
    season & rnd - what is the season & round the current game is
    (prior to which you need the stats)
    df - performance dataframe to get the stats from
    '''
    df_player = df[(df['Url']==url)]   # extract player
    df_player = df_player[(df_player['Year']<season) | ((df_player['Year']==season) & (df_player['Round']<rnd))] # extract prior games
    df_player = df_player.sort_values(by=['Date'],ascending=False)
    df_player = df_player.head(x)
    # one-hot encoding venues could be done later
    '''
    df_player['Adelaide Oval']= np.where(df_player['Venue']=='Adelaide Oval', 1, 0)
    df_player['Bellerive Oval']= np.where(df_player['Venue']=='Bellerive Oval', 1, 0)
    df_player['Bruce Stadium']= np.where(df_player['Venue']=='Bruce Stadium', 1, 0)
    df_player['Carrara']= np.where(df_player['Venue']=='Carrara', 1, 0)
    df_player["Cazaly's Stadium"]= np.where(df_player['Venue']=="Cazaly's Stadium", 1, 0)
    df_player['Docklands']= np.where(df_player['Venue']=='Docklands', 1, 0)
    df_player['Eureka Stadium']= np.where(df_player['Venue']=='Eureka Stadium', 1, 0)
    df_player['Gabba']= np.where(df_player['Venue']=='Gabba', 1, 0)
    df_player['Jiangwan Stadium']= np.where(df_player['Venue']=='Jiangwan Stadium', 1, 0)
    df_player['Kardinia Park']= np.where(df_player['Venue']=='Kardinia Park', 1, 0)
    df_player['M.C.G.']= np.where(df_player['Venue']=='M.C.G.', 1, 0)
    df_player['Manuka Oval']= np.where(df_player['Venue']=='Manuka Oval', 1, 0)
    df_player['Marrara Oval']= np.where(df_player['Venue']=='Marrara Oval', 1, 0)
    df_player['North Hobart']= np.where(df_player['Venue']=='North Hobart', 1, 0)
    df_player['Perth Stadium']= np.where(df_player['Venue']=='Perth Stadium', 1, 0)
    df_player['S.C.G.']= np.where(df_player['Venue']=='S.C.G.', 1, 0)
    df_player['Stadium Australia']= np.where(df_player['Venue']=='Stadium Australia', 1, 0)
    df_player['Sydney Showground']= np.where(df_player['Venue']=='Sydney Showground', 1, 0)
    df_player['Traeger Park']= np.where(df_player['Venue']=='Traeger Park', 1, 0)
    df_player['Wellington']= np.where(df_player['Venue']=='Wellington', 1, 0)
    df_player['York Park']= np.where(df_player['Venue']=='York Park', 1, 0)
    df_player['Blacktown']= np.where(df_player['Venue']=='Blacktown', 1, 0)
    df_player=df_player.drop(['Venue'],1)    
    '''
    # opponent encoding
    df_player['Adelaide']= np.where(df_player['Opponent']=='Adelaide', 1, 0)
    df_player['Brisbane Lions']= np.where(df_player['Opponent']=='Brisbane Lions', 1, 0)
    df_player['Carlton']= np.where(df_player['Opponent']=='Carlton', 1, 0)
    df_player['Collingwood']= np.where(df_player['Opponent']=='Collingwood', 1, 0)
    df_player['Essendon']= np.where(df_player['Opponent']=='Essendon', 1, 0)
    df_player['Fremantle']= np.where(df_player['Opponent']=='Fremantle', 1, 0)
    df_player['Geelong']= np.where(df_player['Opponent']=='Geelong', 1, 0)
    df_player['Gold Coast']= np.where(df_player['Opponent']=='Gold Coast', 1, 0)
    df_player['Greater Western Sydney']= np.where(df_player['Opponent']=='Greater Western Sydney', 1, 0)
    df_player['Hawthorn']= np.where(df_player['Opponent']=='Hawthorn', 1, 0)
    df_player['Melbourne']= np.where(df_player['Opponent']=='Melbourne', 1, 0)
    df_player['North Melbourne']= np.where(df_player['Opponent']=='North Melbourne', 1, 0)
    df_player['Port Adelaide']= np.where(df_player['Opponent']=='Port Adelaide', 1, 0)
    df_player['Richmond']= np.where(df_player['Opponent']=='Richmond', 1, 0)
    df_player['St Kilda']= np.where(df_player['Opponent']=='St Kilda', 1, 0)
    df_player['Sydney']= np.where(df_player['Opponent']=='Sydney', 1, 0)
    df_player['West Coast']= np.where(df_player['Opponent']=='West Coast', 1, 0)
    df_player['Western Bulldogs']= np.where(df_player['Opponent']=='Western Bulldogs', 1, 0)
    
    df_player=df_player.drop(['Opponent'],1) 
    #drop other columns
    df_player=df_player.drop(['GameID','Result','H','A','GameNo','Jersey'],1)
    df_player = df_player.rename(columns={'Year': 'Year_hist', 'Round': 'Round_hist', 'Date': 'Date_hist','Team':'Team_hist'})
    return df_player
