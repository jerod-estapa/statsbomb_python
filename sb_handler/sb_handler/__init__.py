
print("Get help at any time by running sb_help()")
def sb_help():
    print("Version 0.1\n\nFUNCTIONS:\ndata = open_sb(<FILENAME>)\ndf = clean_sb(data)\nStartingXI = Lineups(data)\n")

def open_sb(file):
        file = file
        import json

        with open(file) as f:
            data_load = json.load(f)
        f.close()
        return data_load

def clean_sb(data):
    import pandas as pd
    data = data
    i = 0
    ind = []
    per = []
    dur = []
    ty = []
    pl = []
    m = []
    s = []
    x = []
    y = []
    end_x = []
    end_y = []
    out = []
    rec = []
    tm = []
    ptm = []
    h = []
    bp = []

    pat = []

    for i in range(0,len(data)):
        if ("index" in data[i]):
            ind.append(data[i]['index'])
        else:
            ind.append(0)
        if ("period" in data[i]):
            per.append(data[i]['period'])
        else:
            per.append(None)

        if ("duration" in data[i]):
            dur.append(data[i]['duration'])
        else:
            dur.append(0)

        if ("type" in data[i]):
            ty.append(data[i]['type']['name'])
        else:
            ty.append(None)

        if ("player" in data[i]):
            pl.append(data[i]['player']['name'])
        else:
            pl.append(None)

        if ("minute" in data[i]):
            m.append(data[i]['minute'])
        else:
            m.append(None)

        if ("second" in data[i]):
            s.append(data[i]['second'])
        else:
            s.append(None)

        if ("location" in data[i]):
            x.append(data[i]['location'][0])
            y.append(data[i]['location'][1])
        else:
            x.append(None)
            y.append(None)

        if ("pass" in data[i]):
            if("end_location" in data[i]['pass']):
                end_x.append(data[i]['pass']['end_location'][0])
                end_y.append(data[i]['pass']['end_location'][1])
            else:
                end_x.append(None)
                end_y.append(None)
        elif("shot" in data[i]):
            if("end_location" in data[i]['shot']):
                end_x.append(data[i]['shot']['end_location'][0])
                end_y.append(data[i]['shot']['end_location'][1])
            else:
                end_x.append(None)
                end_y.append(None)
        else:
            end_x.append(None)
            end_y.append(None)


        if ("play_pattern" in data[i]):
            pat.append(data[i]['play_pattern']['name'])
        else:
            pat.append(None)

        if ("pass" in data[i]):
            if ("recipient" in data[i]['pass']):
                rec.append(data[i]['pass']['recipient']['name'])
            else:
                rec.append(None)  
        else:
            rec.append(None)

        if ("pass" in data[i]):
            if("outcome" in data[i]['pass']):
                out.append(data[i]['pass']['outcome']['name'])
            elif("outcome" not in data[i]['pass']):
                out.append("Complete")
        else:
            out.append(None)

        if ("team" in data[i]):
            tm.append(data[i]['team']['name'])
        else:
            tm.append(None)

        if ("possession_team" in data[i]):
            ptm.append(data[i]['possession_team']['name'])
        else:
            ptm.append(None)
        if ("pass" in data[i]):
            if('height' in data[i]['pass']):
                h.append(data[i]['pass']['height']['name'])
            else:
                h.append(None)
        else:
            h.append(None)




    match_events = pd.DataFrame()
    match_events['m_index'] = ind
    match_events['period'] = per
    match_events['duration'] = dur
    match_events['minute'] = m
    match_events['second'] = s
    match_events['type'] = ty
    match_events['player'] = pl
    match_events['team'] = tm
    match_events['pos_team'] = ptm
    match_events['x'] = x
    match_events['y'] = y
    match_events['end_x'] = end_x 
    match_events['end_y'] = end_y
    match_events['height'] = h
    match_events['outcome'] = out
    match_events['recipient'] = rec



    match_events['play_pattern'] = pat
    return match_events


def Lineups(data):
    import pandas as pd
    import numpy as np
    homeTeam = pd.DataFrame()
    
    i = 0
    for i in range(0,11):
    
        jno = (data[0]['tactics']['lineup'][i]['jersey_number'])
        pID = (data[0]['tactics']['lineup'][i]['player']['id'])
        pName = (data[0]['tactics']['lineup'][i]['player']['name'])
        pPos = (data[0]['tactics']['lineup'][i]['position']['name'])
        tName = (data[0]['team']['name'])
        tempDF = pd.DataFrame([jno,pID,pName,pPos,tName]).T
        homeTeam = homeTeam.append(tempDF,ignore_index=True)
        
    homeTeam.columns=['Jersey','pID','Player','Position','Team']
    
    awayTeam = pd.DataFrame()
    
    ii =  0
    for ii in range(0,11):

        jno = (data[1]['tactics']['lineup'][ii]['jersey_number'])
        pID = (data[1]['tactics']['lineup'][ii]['player']['id'])
        pName = (data[1]['tactics']['lineup'][ii]['player']['name'])
        pPos = (data[1]['tactics']['lineup'][ii]['position']['name'])
        tName = (data[1]['team']['name'])
        tempDF = pd.DataFrame([jno,pID,pName,pPos,tName]).T
        awayTeam = awayTeam.append(tempDF,ignore_index=True)
        
    awayTeam.columns=['Jersey','pID','Player','Position','Team']
    
    
    LineUps = homeTeam.append(awayTeam,ignore_index=True)
    return LineUps


def players_played(data):
    df = clean_sb(data)
    
    import pandas as pd
    import numpy as np
    sub_in_p = []
    sub_in_pID = []
    sub_out_pID = []
    sub_in_m = []
    sub_in_s = []
    sub_in_t = []
    sub_out_p = []
    sub_out_m = []
    sub_out_s = []
    sub_out_t = []
    i = 0
    for i in range(0,len(data)):
        if ("Substitution" in data[i]['type']['name']):
            sub_out_p.append(data[i]['player']['name'])
            sub_in_p.append(data[i]['substitution']['replacement']['name'])
            sub_out_m.append(data[i]['minute'])
            sub_in_m.append(data[i]['minute'])
            sub_out_s.append(data[i]['second'])
            sub_in_s.append(data[i]['second'])
            sub_out_t.append(data[i]['team']['name'])
            sub_in_t.append(data[i]['team']['name'])
            sub_in_pID.append(data[i]['substitution']['replacement']['id'])
            sub_out_pID.append(data[i]['player']['id'])
        else:
            pass
    sub_list = pd.DataFrame([sub_out_p,sub_out_pID,sub_in_p,sub_in_pID,sub_in_t,sub_in_m,sub_in_s]).T
    sub_list.columns=['Off','Off_pID','On','On_pID','Team','Minute','Second']
    jn = ['-'] * len(sub_list)
    jn = np.array(jn)

    # Get Sub Positions
    sppos = []
    j = 0
    for j in range(0,len(sub_list)):
        p = sub_list.On.iloc[j]
        ppos = []
        i = 0
        for i in range(0,len(data)):
            try:
                if (p in data[i]['player']['name']):
                    ppos.append(data[i]['position']['name'])
                else:
                    pass
            except KeyError:
                pass
        try:
            ppos = ppos[0]
        except Exception:
            ppos = ['-']
        sppos.append(ppos)

    # Create a sub df that can be added to LineUps
    sub_list_n = pd.DataFrame([jn,sub_list.On_pID.values,sub_list.On.values,sppos,sub_list.Team.values,sub_list.Minute.values,sub_list.Second.values]).T
    sub_list_n.columns=['Jersey','pID','Player','Position','Team','Start_Minute','Start_Second']
    sub_list_n

    sub_list_n
    
    LineUps = Lineups(data)
    
    LineUps['Start_Minute'] = 0
    LineUps['Start_Second'] = 0
    LineUps = LineUps.append(sub_list_n,ignore_index=True)
    LineUps.reset_index(inplace=True)
    del LineUps['index']

    off_p = sub_list.Off_pID.values
    off_p

    i = 0
    End_Minute = []
    End_Second = []

    for i in range(0,len(LineUps)):
        if(LineUps.pID.iloc[i] in off_p):
            End_Minute.append(sub_list[sub_list['Off_pID'] == LineUps.pID.iloc[i]].Minute.values.item())
            End_Second.append(sub_list[sub_list['Off_pID'] == LineUps.pID.iloc[i]].Second.values.item())
        else:
            End_Minute.append(df.minute.iloc[-1])
            End_Second.append(df.second.iloc[-1]) 
    LineUps['End_Minute'] = End_Minute
    LineUps['End_Second'] = End_Second
    LineUps['Mins_Played'] = LineUps.End_Minute - LineUps.Start_Minute
    LineUps = LineUps[['Jersey','pID','Player','Position','Team','Start_Minute','Start_Second','End_Minute','End_Second','Mins_Played']]
    players_played = LineUps

    return players_played


def get_shots(data):
    import pandas as pd
    import numpy as np
    shot_data = []

    i = 0
    for i in range(0,len(data)):
        if("shot" in data[i]):
            shot_data.append(data[i])
        else:
            pass
   
    i = 0
    ind = []
    dur = []
    ty = []
    pl = []
    m = []
    s = []
    x = []
    y = []
    end_x = []
    end_y = []
    ous = []
    rec = []
    tm = []
    ptm = []
    bp = []
    sbxg = [] 
    pat = []

    for i in range(0,len(shot_data)):
        if ("index" in shot_data[i]):
            ind.append(shot_data[i]['index'])
        else:
            ind.append(0)

        if ("duration" in shot_data[i]):
            dur.append(shot_data[i]['duration'])
        else:
            dur.append(0)

        if ("type" in shot_data[i]):
            ty.append(shot_data[i]['type']['name'])
        else:
            ty.append(None)

        if ("player" in shot_data[i]):
            pl.append(shot_data[i]['player']['name'])
        else:
            pl.append(None)

        if ("minute" in shot_data[i]):
            m.append(shot_data[i]['minute'])
        else:
            m.append(None)

        if ("second" in shot_data[i]):
            s.append(shot_data[i]['second'])
        else:
            s.append(None)

        if ("location" in shot_data[i]):
            x.append(shot_data[i]['location'][0])
            y.append(shot_data[i]['location'][1])
        else:
            x.append(None)
            y.append(None)

        if ("pass" in shot_data[i]):
            if("end_location" in shot_data[i]['pass']):
                end_x.append(shot_data[i]['pass']['end_location'][0])
                end_y.append(shot_data[i]['pass']['end_location'][1])
            else:
                end_x.append(None)
                end_y.append(None)
        elif("shot" in shot_data[i]):
            if("end_location" in shot_data[i]['shot']):
                end_x.append(shot_data[i]['shot']['end_location'][0])
                end_y.append(shot_data[i]['shot']['end_location'][1])
            else:
                end_x.append(None)
                end_y.append(None)
        else:
            end_x.append(None)
            end_y.append(None)


        
       
         
        if ("shot" in shot_data[i]):
            ous.append(shot_data[i]['shot']['outcome']['name'])
        else:
            pass
        
        if ("play_pattern" in shot_data[i]):
            pat.append(shot_data[i]['play_pattern']['name'])
        else:
            pat.append(None)

        if ("pass" in shot_data[i]):
            if ("recipient" in shot_data[i]['pass']):
                rec.append(shot_data[i]['pass']['recipient']['name'])
            else:
                rec.append(None)  
        else:
            rec.append(None)

        if ("team" in shot_data[i]):
            tm.append(shot_data[i]['team']['name'])
        else:
            tm.append(None)

        if ("possession_team" in shot_data[i]):
            ptm.append(shot_data[i]['possession_team']['name'])
        else:
            ptm.append(None)

        bp.append(shot_data[i]['shot']['body_part']['name'])
        try:
            sbxg.append(shot_data[i]['shot']['statsbomb_xg'])
        except KeyError:
            sbxg.append(0.01)
    shots = pd.DataFrame()
    shots['m_index'] = ind
    shots['duration'] = dur
    shots['minute'] = m
    shots['second'] = s
    shots['type'] = ty
    shots['player'] = pl
    shots['body_part'] = bp
    shots['sb_xg'] = sbxg
    shots['team'] = tm
    shots['pos_team'] = ptm
    shots['x'] = x
    shots['y'] = y
    shots['end_x'] = end_x 
    shots['end_y'] = end_y
    shots['outcome'] = ous
    shots['recipient'] = rec



    shots['play_pattern'] = pat
    return shots



### SHOT MAP ###

def shot_map(data, team):
    import pandas as pd
    import numpy as np
    import seaborn as sns; sns.set()
    from tqdm import tqdm
    import matplotlib.pyplot as plt
    import pylab
    from matplotlib.collections import LineCollection
    import matplotlib as mpl

    shots = get_shots(data)
    
    team = team
    teams = shots.team.unique()

    if team == teams[0]:
        opposition = teams[1]
    else:
        opposition = teams[0]
        
    

    


    fig,ax2 = plt.subplots(figsize=(12.4,6.8))
    #ax2 = plt.axes([0, 0, 1.5, 0.5])
    #fig.figsize(6.8,10.4)
    ax2.axis('off')

    


                ### TOP ###
    vcx1 = [0,0,68,68,0]            # sidelines
    vcy1 = [0,104,104,0,0]

    vcx2 = [13.84,13.84,54.16,54.16] # outer box
    vcy2 = [104,87.5,87.5,104]

    vcx3 = [30.34,30.34,37.66,37.66] # goal
    vcy3 = [104,104.2,104.2,104]

    vcx4 = [24.84,24.84,43.16,43.16] # 6-y box
    vcy4 = [104,99.5,99.5,104]

    vcx5 = [0,68] # Half-way-line
    vcy5 = [52,52]


                ### BOTTOM ###

    vcx6 = [13.84,13.84,54.16,54.16] # outer box
    vcy6 = [0,16.5,16.5,0]

    vcx7 = [30.34,30.34,37.66,37.66] # goal
    vcy7 = [0,-0.2,-0.2,0]

    vcx8 = [24.84,24.84,43.16,43.16] # 6-y box
    vcy8 = [0,4.5,4.5,0]


    #CENTRE CIRCLE

    circle3 = plt.Circle((34, 52), 9.15,ls='solid',lw=1.5,color='black', fill=False, zorder=1,alpha=1)


    ###### BOX #######
    plt.plot(vcx1,vcy1,c='black',zorder=5)
    plt.plot(vcx2,vcy2,c='black',zorder=5)
    plt.plot(vcx3,vcy3,c='black',zorder=5)
    plt.plot(vcx4,vcy4,c='black',zorder=5)
    plt.plot(vcx5,vcy5,c='black',zorder=5)
    plt.plot(vcx6,vcy6,c='black',zorder=5)
    plt.plot(vcx7,vcy7,c='black',zorder=5)
    plt.plot(vcx8,vcy8,c='black',zorder=5)

    plt.scatter(34,93,c='black',zorder=5)
    plt.scatter(34,11,c='black',zorder=5)
    plt.scatter(34,52,c='black',zorder=5)

    circle1 = plt.Circle((34, 93.5), 9.15,ls='solid',lw=1.5,color='black', fill=False, zorder=1,alpha=1)
    circle2 = plt.Circle((34, 10.5), 9.15,ls='solid',lw=1.5,color='black', fill=False, zorder=1,alpha=1)
    ax2.add_artist(circle1)
    ax2.add_artist(circle2)
    ax2.add_artist(circle3)
    rec1 = plt.Rectangle((20, 87.5), 30,16,ls='-',color='white', zorder=1,alpha=1)
    rec2 = plt.Rectangle((0,0),68,104,color='grey',zorder=2,alpha=0.2)  
    rec3 = plt.Rectangle((20, 0), 30,16.5,ls='-',color='white', zorder=1,alpha=1)

    ax2.add_artist(rec1)
    ax2.add_artist(rec2)
    ax2.add_artist(rec3)

    nshots = shots[shots['team'] == team]
    nshots_h = nshots[nshots['body_part'] == 'Head']
    nshots_f = nshots[(nshots['body_part'] == 'Left Foot')|(nshots['body_part'] == 'Right Foot')]

    x = nshots['x']/120 * 104
    y = nshots['y']/80 * 68
    y = 68 - y

    xh = nshots_h['x']/120 * 104
    yh = nshots_h['y']/80 * 68
    yh = 68 - yh

    xf = nshots_f['x']/120 * 104
    yf = nshots_f['y']/80 * 68
    yf = 68 - yf

    x_size = np.array(nshots.sb_xg.values)
    xf_size = np.array(nshots_f.sb_xg.values)
    xh_size = np.array(nshots_h.sb_xg.values)

    plt.ylim(52,105)
    plt.xlim(0,68)

    ax2.scatter(-100,-100,marker='o',c='grey',edgecolors='black',s=200,label='Head',alpha=0.6)
    ax2.scatter(-100,-100,marker='H',c='grey',edgecolors='black',s=200,label='Foot',alpha=0.6)
    ax2.legend(bbox_to_anchor=(0.70, 0.001),ncol=3,fontsize=14)



    if max(x_size) > 0.50:
        vmx = max(x_size)
    else:
        vmx = 0.50

    plt.scatter(y,x,cmap='RdBu_r',c=x_size,edgecolors='black',alpha=0.9,marker='H',linewidths=1.25,zorder=5000,s=0,vmin=0.00,vmax=vmx)
    plt.colorbar(ax=ax2)


    plt.scatter(yf,xf,cmap='RdBu_r',c=xf_size,edgecolors='black',alpha=0.9,marker='H',linewidths=1.25,zorder=5000,s=xf_size*1000,vmin=0.00,vmax=vmx)

    plt.scatter(yh,xh,cmap='RdBu_r',c=xh_size,edgecolors='black',alpha=0.9,marker='o',linewidths=1.25,zorder=5000,s=xh_size*1000,vmin=0.00,vmax=vmx)

    plt.title(str(team)+" vs "+str(opposition), fontsize=18)

    img = plt.imread("statsbomb-logo.jpg")
    ax2.imshow(img, extent=[50,67,53.0275,58.275],zorder=10000)


        

    plt.savefig("shot_map_"+str(team)+"_vs_"+str(opposition),bbox_inches='tight',dpi=300)
    print("this viz is saved as 'shot_map_"+str(team)+"_vs_"+str(opposition)+".png'")
    plt.show()
    

def player_pass(df,player_name):
    import pandas as pd
    import numpy as np
    import seaborn as sns; sns.set()
    from tqdm import tqdm
    import matplotlib.pyplot as plt
    


    p_pass = df[(df['player'] == player_name)&(df['type'] == 'Pass')]

    p_pass = p_pass[['player','x','y','end_x','end_y','height']]

    p_passg = p_pass[p_pass['height'] == 'Ground Pass']
    p_passg.reset_index(inplace=True)
    p_passl = p_pass[p_pass['height'] == 'Low Pass']
    p_passl.reset_index(inplace=True)
    p_passh = p_pass[p_pass['height'] == 'High Pass']
    p_passh.reset_index(inplace=True)


    #inc_p_pass = p_pass[p_pass['outcome'] == 'Incomplete']

    #teams = shots.team.unique()

    #if team == teams[0]:
    #    opposition = teams[1]
    #else:
    #    opposition = teams[0]






    fig,ax2 = plt.subplots(figsize=(9.8,12.4))
    #ax2 = plt.axes([0, 0, 1.5, 0.5])
    #fig.figsize(6.8,10.4)
    ax2.axis('off')




                ### TOP ###
    vcx1 = [0,0,68,68,0]            # sidelines
    vcy1 = [0,104,104,0,0]

    vcx2 = [13.84,13.84,54.16,54.16] # outer box
    vcy2 = [104,87.5,87.5,104]

    vcx3 = [30.34,30.34,37.66,37.66] # goal
    vcy3 = [104,104.2,104.2,104]

    vcx4 = [24.84,24.84,43.16,43.16] # 6-y box
    vcy4 = [104,99.5,99.5,104]

    vcx5 = [0,68] # Half-way-line
    vcy5 = [52,52]


                ### BOTTOM ###

    vcx6 = [13.84,13.84,54.16,54.16] # outer box
    vcy6 = [0,16.5,16.5,0]

    vcx7 = [30.34,30.34,37.66,37.66] # goal
    vcy7 = [0,-0.2,-0.2,0]

    vcx8 = [24.84,24.84,43.16,43.16] # 6-y box
    vcy8 = [0,4.5,4.5,0]


    #CENTRE CIRCLE

    circle3 = plt.Circle((34, 52), 9.15,ls='solid',lw=1.5,color='black', fill=False, zorder=1,alpha=1)


    ###### BOX #######
    plt.plot(vcx1,vcy1,c='black',zorder=5)
    plt.plot(vcx2,vcy2,c='black',zorder=5)
    plt.plot(vcx3,vcy3,c='black',zorder=5)
    plt.plot(vcx4,vcy4,c='black',zorder=5)
    plt.plot(vcx5,vcy5,c='black',zorder=5)
    plt.plot(vcx6,vcy6,c='black',zorder=5)
    plt.plot(vcx7,vcy7,c='black',zorder=5)
    plt.plot(vcx8,vcy8,c='black',zorder=5)

    plt.scatter(34,93,c='black',zorder=5)
    plt.scatter(34,11,c='black',zorder=5)
    plt.scatter(34,52,c='black',zorder=5)

    circle1 = plt.Circle((34, 93.5), 9.15,ls='solid',lw=1.5,color='black', fill=False, zorder=1,alpha=1)
    circle2 = plt.Circle((34, 10.5), 9.15,ls='solid',lw=1.5,color='black', fill=False, zorder=1,alpha=1)
    ax2.add_artist(circle1)
    ax2.add_artist(circle2)
    ax2.add_artist(circle3)
    rec1 = plt.Rectangle((20, 87.5), 30,16,ls='-',color='white', zorder=1,alpha=1)
    rec2 = plt.Rectangle((0,0),68,104,color='grey',zorder=2,alpha=0.2)  
    rec3 = plt.Rectangle((20, 0), 30,16.5,ls='-',color='white', zorder=1,alpha=1)

    ax2.add_artist(rec1)
    ax2.add_artist(rec2)
    ax2.add_artist(rec3)


    xgp = p_passg['x']/120 * 104
    ygp = p_passg['y']/80 * 68
    end_xgp = p_passg['end_x']/120 * 104
    end_ygp = p_passg['end_y']/80 * 68

    xlp = p_passl['x']/120 * 104
    ylp = p_passl['y']/80 * 68
    end_xlp = p_passl['end_x']/120 * 104
    end_ylp = p_passl['end_y']/80 * 68

    xhp = p_passh['x']/120 * 104
    yhp = p_passh['y']/80 * 68
    end_xhp = p_passh['end_x']/120 * 104
    end_yhp = p_passh['end_y']/80 * 68



    x = p_pass.x/120 * 104
    y = p_pass.y/80 * 68

    y = 68 - y

    ygp = 68 - ygp
    end_ygp = 68 - end_ygp

    ylp = 68 - ylp
    end_ylp = 68 - end_ylp

    yhp = 68 - yhp
    end_yhp = 68 - end_yhp



    #x_size = np.array(nshots.sb_xg.values)

    plt.ylim(-1,105)
    plt.xlim(-1,69)

    i = 0

    for i in range(0,len(p_passg)):
        plt.plot([ygp[i],end_ygp[i]],
                [xgp[i],end_xgp[i]],c='red',alpha=0.7,zorder=500)
    i = 0
    for i in range(0,len(p_passl)):
        plt.plot([ylp[i],end_ylp[i]],
                [xlp[i],end_xlp[i]],c='blue',alpha=0.7,zorder=500)
    i = 0
    for i in range(0,len(p_passh)):
        plt.plot([yhp[i],end_yhp[i]],
                [xhp[i],end_xhp[i]],c='green',alpha=0.7,zorder=500)
        

    plt.scatter(y,x,color='white',edgecolors='black',linewidths=1.25,zorder=501,s=110)
    plt.title(str(p_pass['player'].iloc[0])+" Passes", fontsize=18)


    ## PLOT LINES FOR LEGEND ##


    plt.plot([-100,-100],
            [-100,-100],c='red',alpha=0.7,zorder=500,label='Ground Pass')
    plt.plot([-100,-100],
            [-100,-100],c='blue',alpha=0.7,zorder=500,label='Low Pass')
    plt.plot([-100,-100],
            [-100,-100],c='green',alpha=0.7,zorder=500,label='High Pass')



    img = plt.imread("statsbomb-logo.jpg")
    ax2.imshow(img, extent=[50,67,1.0275,5.275],zorder=10000)
    plt.legend(fontsize=12)
    plt.savefig(str(p_pass['player'].iloc[0])+"_passes",bbox_inches='tight',dpi=300)
    print("viz saved as "+str(p_pass['player'].iloc[0])+"_passes")

    plt.show()

    



