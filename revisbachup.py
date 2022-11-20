from random import randint
board = [[' ',' ',' '],[' ',' ','T'],[' ',' ',' ']]
entities = []
players = [[['physics','computer science'],[],[],[],[]]]

physicsquestions1=[
['question 1','a',1,[
'/-\\',
'| |',
'\\_\\_']],

['question 2','b',2,['']],

['question 3','c',3,[
' | | ',
' | | ',
'\\   /',
' \\_/ ']]
]

global enemies
noot=0
squirtle=10
charizard=5

for i in range(0,charizard):
    board.append([' ',' ',' '])

for i in range(0,len(board)):
    for i2 in range(0,squirtle):
        board[i].append(' ')
        
def questioner(physicsquestions):
    picker=randint(0,len(physicsquestions)-1)
    print(physicsquestions[picker][0])
    for i in range(0,len(physicsquestions[picker][3])):
        print(physicsquestions[picker][3][i])
    answer=input('Input:')
    if answer==physicsquestions[picker][1]:
        return True
    print('answer:',physicsquestions[picker][1])

def idea(entities):
    for i2 in range(0,len(entities)):
        print('-----')
        print('ID=',i2+1,': type-',entities[i2][0],', x=',entities[i2][1]+1,', y=',len(board)-entities[i2][2],', hp=',entities[i2][3],', intent=',entities[i2][4],',', entities[i2][5])
    print('-----')
        
def target(attackposx, hitposx, attackposy, hitposy, rangee):
    if (attackposx-rangee<=hitposx<=attackposx+rangee):
        if (attackposy-rangee<=hitposy<=attackposy+rangee):
            return True
        
def AItargeting(players,entities,entity,team):
    pliof=False
    targeter=255
    if team==1:
        for i in range(0,len(players)-1):
            targeteer=abs(players[i][2][1]-entities[entity][1])+abs(players[i][2][2]-entities[entity][2])
            if targeteer<targeter:
                targeter=targeteer
                ploof=i
        for i in range(0,len(entities)):
            if entities[i][6]==2:
                targeteer=abs(entities[i][1]-entities[entity][1])+abs(entities[i][2]-entities[entity][2])
                if targeteer<targeter:
                    targeter=targeteer
                    pliof=True
                    ploof=i
    elif team==2:
        for i in range(0,len(entities)):
            if entities[i][6]==1:
                targeteer=abs(entities[i][1]-entities[entity][1])+abs(entities[i][2]-entities[entity][2])
                if targeteer<targeter:
                    targeter=targeteer
                    pliof=True
                    ploof=i
    return ploof, pliof

def deaths(entities):
    global enemies
    ploosh = []
    for i2 in range(0,len(entities)):
        if entities[i2][3]<1:
            print('blehhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
            ploosh.append(i2)
            if entities[i2][6]==1:
                enemies=enemies-1
    pliish=-1
    for i2 in range(0,len(ploosh)):
        pliish=pliish+1
        entities.pop(ploosh[i2-pliish])

def boardbake(board, entities, players):
    print('')
    grob=-1
    for i in range(0,len(board[0])+1):
        grob=grob+1
        if grob==10:
            grob=0
        print(grob,end = '')
    print('+')
    for i in range(0,len(board[0])):
        print('+',end = '')
    print('+')
    for i in range(0,len(board)):
        print('+',end = '')
        for i2 in range(0,len(board[i])):
            there=False
            for i3 in range(0,len(players)-1):
                if players[i3][2][1]==i2:
                    if players[i3][2][2]==i:
                        print(i3+1,end = '')
                        there=True
            for i3 in range(0,len(entities)):
                if entities[i3][1]==i2:
                    if entities[i3][2]==i:
                        if entities[i3][0]=='goblin':
                            if there==False:
                                print('g',end = '')
                        elif entities[i3][0]=='goblin archer':
                            if there==False:
                                print('a',end = '')
                        elif entities[i3][0]=='turret':
                            if there==False:
                                print('*',end = '')
                        there=True
            if there==False:
                print(board[i][i2],end = '')
        print('+',end='')
        print(len(board)-i)
    for i in range(0,len(board[0])+1):
        print('+',end = '')
    print('+')


def boardmake(board, entities, players):
    for i in range(0,len(board[0])+1):
        print('+',end = '')
    print('+')
    for i in range(0,len(board)):
        print('+',end = '')
        for i2 in range(0,len(board[i])):
            there=False
            for i3 in range(0,len(players)-1):
                if players[i3][2][1]==i2:
                    if players[i3][2][2]==i:
                        print(i3+1,end = '')
                        there=True
            for i3 in range(0,len(entities)):
                if entities[i3][1]==i2:
                    if entities[i3][2]==i:
                        if entities[i3][0]=='goblin':
                            if there==False:
                                print('g',end = '')
                        elif entities[i3][0]=='goblin archer':
                            if there==False:
                                print('a',end = '')
                        elif entities[i3][0]=='turret':
                            if there==False:
                                print('*',end = '')
                        there=True
            if there==False:
                print(board[i][i2],end = '')
        print('+')
    for i in range(0,len(board[0])+1):
        print('+',end = '')
    print('+')
wave=0

#print('')
#print('//////////////////////////////////////////////////////////')
#print('Hi! This is my temporary guide to this game!')
#print('In this game the subjects you choose influence your abilities')
#print('notes: ranges are square, for testing purposes you cannot take damage, players are numbers on the board.')
#print('A.I notes: they gain intents the turn after spawning. Blocking reduces damage by half, rounded down.')
#print('A.I intents: move/attack:twice-attack if in range, move if not. block: move once and block next turn.')
#print('Important: there will be an entity list that will show info and Ids. this is important for targeting')
#print('sword: range 1, 2-3 damage. movement: 3 turns of movement each players turn. Inspect: useful for checking entity IDs')
#print('physics: static shock: range 3, 2-3 dmg, inflict shock on self resticting movement by 2 next turn.')
#print('physics: quantum jump: warp to anywhere on the board')
#print('computer science: works but in development, place down turrets with a range of 3 and 4 hp that deal 1 dmg.')
#print('    this is currently infinate, this will be refined in the final product')
#print('maths: mage shield: after your next turn, absorb up to 3 hits')
#print('maths: magic missile: range 2, fires a 1-2 dmg missile for each entity in range which hit random targets')
#print('    damage against block is rounded up instead')
#print('Further Maths: you can switch between 2 different warp weapons, the spear and the bow')
#print('Further Maths: warp spear: base 1 damage,+1 damage for each movement used in the same direction this turn')
#print('    this does not take the largest value that turn, if you end by going in a different direction that will reset it.')
#print('    otherwise functions like a sword.')
#print('Further Maths: warp bow: you can fire this twice each wave, 2-3 dmg, range 6')
#print('have fun with this wall of text!')
#print('//////////////////////////////////////////////////////////')
#print('')
#print('')
#print('')

if questioner(physicsquestions1)==True:
    print('meese')

check=False
while check==False:
    check=True
    ploop=input('How many players are there: ')
    try:
        int(ploop)
    except:
        print('make sure you write a number')
        check=False

plonk=int(ploop)
for i in range(0,plonk):
    players.append([[],[],[],[],[]])
    print('-------------------------')
    check=False
    while check==False:
        check=True 
        ploop=input('How many subjects do you do: ')
        try:
            int(ploop)
        except:
            print('make sure you write a number')
            check=False
    
    plink=int(ploop)
    for i2 in range(0,plink):
        check=False
        while check==False:
            check=True 
            print('physics(1), computer science(2), maths(3), further maths(4)')
            ploop=input('Name a subject that you do (type the number from the key above): ')
            try:
                int(ploop)
            except:
                print('make sure you write a number')
                check=False
        plank=ploop
        players[i][0].append(plank)
        
for i in range(0,len(players)):
    players[i][2].append(i)
    players[i][2].append(2*i)
    players[i][2].append(len(board)-1)
    players[i][2].append(20)
    players[i].append([])

for i in range(0,len(players)):
    players[i][1].append(0)
    for i2 in range(0,len(players[i][0])):
        if players[i][0][i2]=='1':
            players[i][1].append(1)
            players[i][1].append(2)
        elif players[i][0][i2]=='2':
            players[i][1].append(3)
            players[i][1].append(4)
        elif players[i][0][i2]=='3':
            players[i][1].append(7)
            players[i][1].append(8)
        elif players[i][0][i2]=='4':
            players[i][1].append(9)
            players[i][1].append(10)
    players[i][1].append(5)
    players[i][1].append(6)
    players[i][4].append(0)
    players[i][4].append('none')
    players[i][4].append(0)
    players[i][4].append([])
    players[i][4][3].append(['solar',4])

while wave < 10:
    wave=wave+1
    spawner=wave+3
    enemies=0
    for i in range(0,len(players)-1):
        players[i][4][2]=2
    while spawner>2:
        spawn=randint(0, 0)
        if spawn==0:
            print('goblin')
            spawner=spawner-1
            enemies=enemies+1
            entities.append(['goblin',randint(0, len(board[0])-1),0,4,'none', 'not blocking',1])
        elif spawn==1:
            print('goblin archer')
            spawner=spawner-2
            enemies=enemies+1
            entities.append(['goblin archer',randint(0, len(board[0])-1),0,5,'none', 'not blocking',1])
    while enemies>0:
        for i in range(0,len(players)-1):
            charger=0
            charger1='none'
            idea(entities)
            boardmake(board, entities, players)
            movement=3
            players[i][4][0]=0
            players[i][3].append('status effects')
            for i2 in range(0,len(players[i][3])):
                pliish=0
                if players[i][3][i2-pliish-1]=='status effects':
                    pliish=pliish+1
                    players[i][3].pop(i2-pliish)
                elif players[i][3][i2-pliish-1]=='shocked':
                    pliish=pliish+1
                    print('shocked')
                    movement=movement-2
                    players[i][3].pop(i2-pliish)
                elif players[i][3][i2-pliish-1]=='shielding':
                    pliish=pliish+1
                    players[i][4][0]=3
                    players[i][3].pop(i2-pliish)
            while movement>0:
                print('current movement:',movement)
                movie=input('Choose a movement direction(w,a,s,d,(x to skip)): ')
                valid=False
                if movie=='w':
                    if (players[i][2][2])-1<0:
                        print('noooooo')
                    elif board[players[i][2][2]-1][players[i][2][1]]=='T':
                        print('Thats a tree')
                    else:
                        print('w')
                        players[i][2][2]=players[i][2][2]-1
                        movement=movement-1
                        valid=True
                elif movie=='a':
                    if players[i][2][1]-1<0:
                        print('noooooo')
                    elif board[players[i][2][2]][players[i][2][1]-1]=='T':
                        print('Thats a tree')
                    else:
                        print('a')
                        players[i][2][1]=players[i][2][1]-1
                        movement=movement-1
                        valid=True
                elif movie=='s':
                    if players[i][2][2]+1>len(board)-1:
                        print('noooooo')
                    elif board[players[i][2][2]+1][players[i][2][1]]=='T':
                        print('Thats a tree')
                    else:
                        print('s')
                        players[i][2][2]=players[i][2][2]+1
                        movement=movement-1
                        valid=True
                elif movie=='d':
                    if players[i][2][1]+1>len(board[0])-1:
                        print('noooooo')
                    elif board[players[i][2][2]][players[i][2][1]+1]=='T':
                        print('Thats a tree')
                    else:
                        print('d')
                        players[i][2][1]=players[i][2][1]+1
                        movement=movement-1
                        valid=True
                elif movie=='x':
                    print('x')
                    movement=movement-1
                    charger=0
                if valid==True:
                    if charger1==movie:
                        charger=charger+1
                    else:
                        charger=1
                    charger1=movie
                print(charger,'charge',charger1)
            idea(entities)
            boardmake(board, entities, players)
            print('----------------------------------')
            for i2 in range(0,len(players[i][1])):
                if players[i][1][i2]==0:
                    print(i2, ': hit with sword')
                elif players[i][1][i2]==1:
                    print(i2, ': static shock')
                elif players[i][1][i2]==2:
                    print(i2, ': quantum jump')
                elif players[i][1][i2]==3:
                    print(i2, ': repair turret')
                elif players[i][1][i2]==4:
                    print(i2, ': place turret')
                elif players[i][1][i2]==6:
                    print(i2, ': inspect an entity')
                elif players[i][1][i2]==5:
                    print(i2, ': skip')
                elif players[i][1][i2]==7:
                    print(i2, ': magic missile')
                elif players[i][1][i2]==8:
                    print(i2, ': mage shield')
                elif players[i][1][i2]==9:
                    print(i2, ': create warp weapon')
                elif players[i][1][i2]==10:
                    if players[i][4][1]=='none':
                        print(i2, ': warp weapon unavailable, create new warp weapon')
                    else:
                        print(i2, ': use warp weapon-', players[i][4][1])
            print('----------------------------------')
            floof=True
            while floof==True:
                check=False
                while check==False:
                    check=True
                    action=input('Choose your action: ')
                    try:
                        int(action)
                    except:
                        print('make sure you write a number')
                        check=False
                if players[i][1][int(action)]==0:
                    check=False
                    while check==False:
                        check=True
                        sights=input('Enter the ID of the target:')
                        try:
                            entities[int(sights)-1]
                        except:
                            print('make sure you write a number and that the entity exists')
                            check=False
                    if (target(players[i][2][1],entities[int(sights)-1][1],players[i][2][2],entities[int(sights)-1][2],1))==True:
                        damage=randint(2,3)
                        if entities[int(sights)-1][5]=='blocking':
                            damage=damage//2
                        print(damage,'dmg')
                        entities[int(sights)-1][3]=entities[int(sights)-1][3]-damage
                        floof=False
                elif players[i][1][int(action)]==1:
                    check=False
                    while check==False:
                        check=True
                        sights=input('Enter the ID of the target:')
                        try:
                            entities[int(sights)-1]
                        except:
                            print('make sure you write a number and that the entity exists')
                            check=False
                    if (target(players[i][2][1],entities[int(sights)-1][1],players[i][2][2],entities[int(sights)-1][2],3))==True:
                        #questioner(physicsquestions1)
                        damage=randint(2,3)
                        players[i][3].append('shocked')
                        floof=False
                        if entities[int(sights)-1][5]=='blocking':
                            damage=damage//2
                        print(damage,'dmg')
                        entities[int(sights)-1][3]=entities[int(sights)-1][3]-damage
                elif players[i][1][int(action)]==2:
                    check2=False
                    while check2==False:
                        check2=True
                        check1=False
                        boardbake(board, entities, players)
                        while check1==False:
                            check1=True
                            check=False
                            while check==False:
                                check=True
                                xticket=input('state x coordinate: ')
                                try:
                                    int(xticket)
                                except:
                                    print('make sure you write a number')
                                    check=False
                            check=False
                            while check==False:
                                check=True
                                yticket=input('state y coordinate: ')
                                try:
                                    int(yticket)
                                except:
                                    print('make sure you write a number')
                                    check=False
                            if int(yticket)>=len(board) or int(yticket)<=0:
                                check1=False
                                print('Off the board')
                            if int(xticket)>=len(board[0]) or int(xticket)<=0:
                                check1=False
                                print('Off the board')
                        if board[len(board)-int(yticket)][int(xticket)-1]=='T':
                            check2=False
                            print('theres a tree there')
                    print('boing')
                    players[i][2][1]=int(xticket)-1
                    players[i][2][2]=len(board)-int(yticket)
                    floof=False
                elif players[i][1][int(action)]==3:
                    check=False
                    while check==False:
                        check=True
                        sights=input('Enter the ID of the target:')
                        try:
                            if entities[int(sights)-1][0]!='turret':
                                print('this is not a turret')
                        except:
                            print('make sure you write a number and that the entity exists')
                            check=False
                    if (target(players[i][2][1],entities[int(sights)-1][1],players[i][2][2],entities[int(sights)-1][2],1))==True:
                        entities[int(sights)-1][3]=4
                        floof=False
                elif players[i][1][int(action)]==4:
                    pliish=0
                    for i2 in range(0,len(entities)):
                        print('fllo')
                        if entities[i2-pliish][0]=='turret':
                            entities.pop(i2-pliish)
                            pliish=pliish+1
                    entities.append(['turret', players[i][2][1],players[i][2][2],4,'target sighted', 'operational',2])
                    floof=False
                elif players[i][1][int(action)]==5:
                    print('skipped action')
                    floof=False
                elif players[i][1][int(action)]==6:
                    boardbake(board, entities, players)
                    check=False
                    while check==False:
                        check=True
                        xticket=input('state x coordinate: ')
                        try:
                            int(xticket)
                        except:
                            print('make sure you write a number')
                            check=False
                    check=False
                    while check==False:
                        check=True
                        yticket=input('state y coordinate: ')
                        try:
                            int(yticket)
                        except:
                            print('make sure you write a number')
                            check=False
                    for i2 in range(0,len(entities)):
                        if (entities[i2][1]+1)==int(xticket):
                            if (len(board)-entities[i2][2])==int(yticket):
                                print('ID=',i2+1,entities[i2][0])
                                print(entities[i2][3],'hp')
                                print('intent=',entities[i2][4])

                elif players[i][1][int(action)]==7:
                    print('Pwoosh')
                    hum=[]
                    for i2 in range(0, len(entities)):
                        if target(players[i][2][1], entities[i2][1], players[i][2][2], entities[i2][2], 2)==True:
                            hum.append(i2)
                    for i2 in range(0, len(hum)):
                        hom=randint(0, len(hum)-1)
                        damage=randint(1,2)
                        if entities[hum[hom]][5]=='blocking':
                            damage=(damage+1)//2
                        print('magic missile:',damage,'dmg against entity',hum[hom]+1)
                        entities[hum[hom]][3]=entities[hum[hom]][3]-damage
                    if len(hum)>0:
                        floof=False
                    else:
                        print('no targets')
                elif players[i][1][int(action)]==8:
                    print('hummumum')
                    players[i][3].append('shielding')
                    floof=False
                elif players[i][1][int(action)]==9:
                    print('====')
                    print('1 : warp spear')
                    print('2 : warp bow')
                    print('====')
                    check=False
                    check1=False
                    while check1==False:
                        check1=True
                        while check==False:
                            check=True
                            yticket=input('state weapon id: ')
                            try:
                                int(yticket)
                            except:
                                print('make sure you write a number')
                                check=False
                        if int(yticket)>2 or int(yticket)<1:
                            check1=False
                            print('that warp cannot be created')
                    if int(yticket)==1:
                        players[i][4][1]='spear'
                    elif int(yticket)==2:
                        players[i][4][1]='bow'
                elif players[i][1][int(action)]==10:
                    print(players[i][4][1])
                    if players[i][4][1]=='spear':
                        check=False
                        while check==False:
                            check=True
                            sights=input('Enter the ID of the target:')
                            try:
                                entities[int(sights)-1]
                            except:
                                print('make sure you write a number and that the entity exists')
                                check=False
                        if (target(players[i][2][1],entities[int(sights)-1][1],players[i][2][2],entities[int(sights)-1][2],1))==True:
                            damage=1+charger
                            if entities[int(sights)-1][5]=='blocking':
                                damage=damage//2
                            print(damage,'dmg')
                            entities[int(sights)-1][3]=entities[int(sights)-1][3]-damage
                            floof=False
                    elif players[i][4][1]=='bow':
                        
                        check=False
                        while check==False:
                            check=True
                            sights=input('Enter the ID of the target:')
                            try:
                                entities[int(sights)-1]
                            except:
                                print('make sure you write a number and that the entity exists')
                                check=False
                        if players[i][4][2]>0:
                            if (target(players[i][2][1],entities[int(sights)-1][1],players[i][2][2],entities[int(sights)-1][2],6))==True:
                                damage=randint(2,3)
                                if entities[int(sights)-1][5]=='blocking':
                                    damage=damage//2
                                print(damage,'dmg')
                                entities[int(sights)-1][3]=entities[int(sights)-1][3]-damage
                                players[i][4][2]=players[i][4][2]-1
                                floof=False
                            else:
                                print('out of range')
                        else:
                            print('no ammo left')
                
            deaths(entities)
        print('///////////////////////////')
        print('AIs turn')
        print()
        for i in range(0,len(entities)):
            if entities[i][0]=='turret':
                try:
                    k=AItargeting(players,entities,i,2)[0]
                    if target(entities[i][1], entities[k][1], entities[i][2], entities[k][2], 3)==True:
                        print('Turret: Firing on entity ID',k)
                        damage=1
                        if entities[int(sights)-1][5]=='blocking':
                            damage=damage//2
                        print(damage,'dmg')
                        entities[int(sights)-1][3]=entities[int(sights)-1][3]-damage
                except:
                    print('Turret: No target found')
            elif entities[i][0]=='goblin':
                k=AItargeting(players,entities,i,1)[0]
                entities[i][5]='not blocking'
                if AItargeting(players,entities,i,1)[1]==True:
                    if entities[i][4]=='move/attack':
                        for i2 in range(0,2):
                            randoom=(randint(1,2))
                            if (entities[i][2]+2>entities[k][2]>entities[i][2]-2)and(entities[i][1]+2>entities[k][1]>entities[i][1]-2):
                                print('entity',i,'Attacks entity',k)
                                entities[k][3]=entities[k][3]-2
                            elif randoom==1:
                                if entities[k][2]>entities[i][2]:
                                    entities[i][2]=entities[i][2]+1
                                elif entities[k][2]<entities[i][2]:
                                    entities[i][2]=entities[i][2]-1
                                elif entities[k][1]<entities[i][1]:
                                    entities[i][1]=entities[i][1]-1
                                elif entities[k][1]>entities[i][1]:
                                    entities[i][1]=entities[i][1]+1
                            elif randoom==2:
                                if entities[k][1]<entities[i][1]:
                                    entities[i][1]=entities[i][1]-1
                                elif entities[k][1]>entities[i][1]:
                                    entities[i][1]=entities[i][1]+1
                                elif entities[k][2]>entities[i][2]:
                                    entities[i][2]=entities[i][2]+1
                                elif entities[k][2]<entities[i][2]:
                                    entities[i][2]=entities[i][2]-1
                    elif entities[i][4]=='block':
                        entities[i][5]='blocking'
                        randoom=(randint(1,2))
                        if randoom==1:
                            if entities[k][2]>entities[i][2]:
                                entities[i][2]=entities[i][2]+1
                            elif entities[k][2]<entities[i][2]:
                                entities[i][2]=entities[i][2]-1
                            elif entities[k][1]<entities[i][1]:
                                entities[i][1]=entities[i][1]-1
                            elif entities[k][1]>entities[i][1]:
                                entities[i][1]=entities[i][1]+1
                        elif randoom==2:
                            if entities[k][1]<entities[i][1]:
                                entities[i][1]=entities[i][1]-1
                            elif entities[k][1]>entities[i][1]:
                                entities[i][1]=entities[i][1]+1
                            elif entities[k][2]>entities[i][2]:
                                entities[i][2]=entities[i][2]+1
                            elif entities[k][2]<entities[i][2]:
                                entities[i][2]=entities[i][2]-1
                else:
                    if entities[i][4]=='move/attack':
                        for i2 in range(0,2):
                            randoom=(randint(1,2))
                            if (entities[i][2]+2>players[k][2][2]>entities[i][2]-2)and(entities[i][1]+2>players[k][2][1]>entities[i][1]-2):
                                if players[k][4][0]>0:
                                    print('Attack by entity',i+1,'against',k+1,'blocked. remaining shield:',players[k][4][0])
                                    players[k][4][0]=players[k][4][0]-1
                                else:
                                    print(i+1,'Attacks player',k+1)
                            elif randoom==1:
                                if players[k][2][2]>entities[i][2]:
                                    entities[i][2]=entities[i][2]+1
                                elif players[k][2][2]<entities[i][2]:
                                    entities[i][2]=entities[i][2]-1
                                elif players[k][2][1]<entities[i][1]:
                                    entities[i][1]=entities[i][1]-1
                                elif players[k][2][1]>entities[i][1]:
                                    entities[i][1]=entities[i][1]+1
                            elif randoom==2:
                                if players[k][2][1]<entities[i][1]:
                                    entities[i][1]=entities[i][1]-1
                                elif players[k][2][1]>entities[i][1]:
                                    entities[i][1]=entities[i][1]+1
                                elif players[k][2][2]>entities[i][2]:
                                    entities[i][2]=entities[i][2]+1
                                elif players[k][2][2]<entities[i][2]:
                                    entities[i][2]=entities[i][2]-1
                    elif entities[i][4]=='block':
                        entities[i][5]='blocking'
                        randoom=(randint(1,2))
                        if randoom==1:
                            if players[0][2][2]>entities[i][2]:
                                entities[i][2]=entities[i][2]+1
                            elif players[0][2][2]<entities[i][2]:
                                entities[i][2]=entities[i][2]-1
                            elif players[0][2][1]<entities[i][1]:
                                entities[i][1]=entities[i][1]-1
                            elif players[0][2][1]>entities[i][1]:
                                entities[i][1]=entities[i][1]+1
                        elif randoom==2:
                            if players[0][2][1]<entities[i][1]:
                                entities[i][1]=entities[i][1]-1
                            elif players[0][2][1]>entities[i][1]:
                                entities[i][1]=entities[i][1]+1
                            elif players[0][2][2]>entities[i][2]:
                                entities[i][2]=entities[i][2]+1
                            elif players[0][2][2]<entities[i][2]:
                                entities[i][2]=entities[i][2]-1
                randoom=(randint(1,2))
                if randoom==1:
                    entities[i][4]='move/attack'
                elif randoom==2:
                    entities[i][4]='block'
            elif entities[i][0]=='goblin archer':
                print('Im a goblin archer')
        deaths(entities)
                