START_STATE = {'player': 'alice', 'alice_room': 'west room', 'bob_room': 'east room', 'red_key': 'east room',
               'blue_key': 'west room', 'green_key': 'east room'}

statedict = {}

myarr = []

def swperson(state):
    a = state.get('player')
    if(a == 'alice'):
        state['player']= 'bob'
    else:
        state['player']= 'alice'
    return state

def go(state):
    ch = False
    r = state.get('red_key')
    b = state.get('blue_key')
    g = state.get('green_key')
    a = state.get('player')
    croom = state.get(a + '_room')
    str = ""
    st = getstate(state)
    count = statedict.get(st)
    if(count == None):
        statedict.setdefault(st)
        statedict[st] = ""
        count = ""


    if (croom == 'red room'):
        if(r == croom) and count.find("r") == -1:
            state[a + '_room'] = 'west room'
            state['red_key']= 'west room'
            str= a + 'to w'
            ch = True
            statedict[st] += "r"
    if (croom == 'west room'):
        if r == croom and count.find("r") == -1:
            state[a + '_room'] = 'red room'
            state['red_key'] = 'red room'
            str = a + 'to r'
            ch = True
            statedict[st] += "r"
        if g == croom and count.find("g") == -1:
            state[a + '_room'] = 'east room'
            state['green_key'] = 'east room'
            str = a + 'to e'
            ch = True
            statedict[st] += "g"
    if (croom == 'east room'):
        if(g == croom) and count.find("g") == -1:
            state[a + '_room'] = 'west room'
            state['green_key'] = 'west room'
            str = a + 'to w'
            ch = True
            statedict[st] += "g"
        if(b == croom) and count.find("b") == -1:
            state[a + '_room'] = 'blue room'
            state['blue_key'] = 'blue room'
            str = a + 'to b'
            ch = True
            statedict[st] += "b"
    if (croom == 'blue room'):
        if(b == croom) and count.find("b") == -1:
            state[a + '_room'] = 'east room'
            state['blue_key'] = 'east room'
            str = a + 'to e'
            ch = True
            statedict[st] += "b"
    if(ch):
        return [state, str]
    state = swperson(state)
    return [state, str]

def getstate(state):
    str = state.get('player')[0] + state.get('alice_room')[0] + state.get('bob_room')[0] + state.get('red_key')[0] + state.get('blue_key')[0] + state.get('green_key')[0]
    return str


def rec(state):
    modstate = state.copy()
    ret = go(modstate)
    if(ret == None):
        return None
    modstate = ret[0]
    str = ret[1]
    graphstr = getstate(state) + "->" + getstate(modstate) + ";"
    if(myarr.count(graphstr) !=0):
        return None
    myarr.append(graphstr)
    return rec(modstate)

rec(START_STATE)
print(myarr)
