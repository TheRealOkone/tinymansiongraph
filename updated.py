import random
import sys

START_STATE = {'player': 'alice', 'alice_room': 'west room', 'bob_room': 'east room', 'red_key': 'east room',
               'blue_key': 'west room', 'green_key': 'east room'}

statedict = {}

myarr = []


def swperson(state):
    a = state.get('player')
    if (a == 'alice'):
        state['player'] = 'bob'
    else:
        state['player'] = 'alice'
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
    if (count == None):
        statedict.setdefault(st)
        statedict[st] = ""
        count = ""

    if (croom == 'red room'):
        if (r == croom) and count.find("r") == -1:
            state[a + '_room'] = 'west room'
            state['red_key'] = 'west room'
            statedict[st] += "r"
            return [state, str]
        if (r == croom) and (g == croom) and count.find("t") == -1:
            state[a + '_room'] = 'west room'
            state['red_key'] = 'west room'
            state['green_key'] = 'west room'
            statedict[st] += "t"
            return [state, str]
        if (r == croom) and (b == croom) and count.find("y") == -1:
            state[a + '_room'] = 'west room'
            state['red_key'] = 'west room'
            state['blue_key'] = 'west room'
            statedict[st] += "y"
            return [state, str]
        if (r == croom) and (g == croom) and (b == croom) and count.find("u") == -1:
            state[a + '_room'] = 'west room'
            state['red_key'] = 'west room'
            state['green_key'] = 'west room'
            state['blue_key'] = 'west room'
            statedict[st] += "u"
            return [state, str]
    if (croom == 'west room'):
        if r == croom and count.find("r") == -1:
            state[a + '_room'] = 'red room'
            state['red_key'] = 'red room'
            statedict[st] += "r"
            return [state, str]
        if (r == croom) and (g == croom) and count.find("t") == -1:
            state[a + '_room'] = 'red room'
            state['red_key'] = 'red room'
            state['green_key'] = 'red room'
            statedict[st] += "t"
            return [state, str]
        if (r == croom) and (b == croom) and count.find("y") == -1:
            state[a + '_room'] = 'red room'
            state['red_key'] = 'red room'
            state['blue_key'] = 'red room'
            statedict[st] += "y"
            return [state, str]
        if (r == croom) and (g == croom) and (b == croom) and count.find("u") == -1:
            state[a + '_room'] = 'red room'
            state['red_key'] = 'red room'
            state['green_key'] = 'red room'
            state['blue_key'] = 'red room'
            statedict[st] += "u"
            return [state, str]

        if g == croom and count.find("g") == -1:
            state[a + '_room'] = 'east room'
            state['green_key'] = 'east room'
            statedict[st] += "g"
            return [state, str]
        if (r == croom) and (g == croom) and count.find("h") == -1:
            state[a + '_room'] = 'east room'
            state['red_key'] = 'east room'
            state['green_key'] = 'east room'
            statedict[st] += "h"
            return [state, str]
        if (g == croom) and (b == croom) and count.find("j") == -1:
            state[a + '_room'] = 'east room'
            state['blue_key'] = 'east room'
            state['green_key'] = 'east room'
            statedict[st] += "j"
            return [state, str]
        if (r == croom) and (g == croom) and (b == croom) and count.find("k") == -1:
            state[a + '_room'] = 'east room'
            state['red_key'] = 'east room'
            state['green_key'] = 'east room'
            state['blue_key'] = 'east room'
            statedict[st] += "k"
            return [state, str]
    if (croom == 'east room'):
        if (g == croom) and count.find("g") == -1:
            state[a + '_room'] = 'west room'
            state['green_key'] = 'west room'
            statedict[st] += "g"
            return [state, str]
        if (r == croom) and (g == croom) and count.find("h") == -1:
            state[a + '_room'] = 'west room'
            state['red_key'] = 'west room'
            state['green_key'] = 'west room'
            statedict[st] += "h"
            return [state, str]
        if (g == croom) and (b == croom) and count.find("j") == -1:
            state[a + '_room'] = 'west room'
            state['blue_key'] = 'west room'
            state['green_key'] = 'west room'
            statedict[st] += "j"
            return [state, str]
        if (r == croom) and (g == croom) and (b == croom) and count.find("k") == -1:
            state[a + '_room'] = 'west room'
            state['red_key'] = 'west room'
            state['green_key'] = 'west room'
            state['blue_key'] = 'west room'
            statedict[st] += "k"
            return [state, str]

        if (b == croom) and count.find("b") == -1:
            state[a + '_room'] = 'blue room'
            state['blue_key'] = 'blue room'
            statedict[st] += "b"
            return [state, str]
        if (r == croom) and (b == croom) and count.find("n") == -1:
            state[a + '_room'] = 'blue room'
            state['red_key'] = 'blue room'
            state['blue_key'] = 'blue room'
            statedict[st] += "n"
            return [state, str]
        if (g == croom) and (b == croom) and count.find("m") == -1:
            state[a + '_room'] = 'blue room'
            state['blue_key'] = 'blue room'
            state['green_key'] = 'blue room'
            statedict[st] += "m"
            return [state, str]
        if (r == croom) and (g == croom) and (b == croom) and count.find(",") == -1:
            state[a + '_room'] = 'blue room'
            state['red_key'] = 'blue room'
            state['green_key'] = 'blue room'
            state['blue_key'] = 'blue room'
            statedict[st] += ","
            return [state, str]

    if (croom == 'blue room'):
        if (b == croom) and count.find("b") == -1:
            state[a + '_room'] = 'east room'
            state['blue_key'] = 'east room'
            statedict[st] += "b"
            return [state, str]
        if (r == croom) and (b == croom) and count.find("n") == -1:
            state[a + '_room'] = 'east room'
            state['red_key'] = 'east room'
            state['blue_key'] = 'east room'
            statedict[st] += "n"
            return [state, str]
        if (g == croom) and (b == croom) and count.find("m") == -1:
            state[a + '_room'] = 'east room'
            state['blue_key'] = 'east room'
            state['green_key'] = 'east room'
            statedict[st] += "m"
            return [state, str]
        if (r == croom) and (g == croom) and (b == croom) and count.find(",") == -1:
            state[a + '_room'] = 'east room'
            state['red_key'] = 'east room'
            state['green_key'] = 'east room'
            state['blue_key'] = 'east room'
            statedict[st] += ","
            return [state, str]
    return [state, str]


def getstate(state):
    str = state.get('player')[0] + state.get('alice_room')[0] + state.get('bob_room')[0] + state.get('red_key')[0] + \
          state.get('blue_key')[0] + state.get('green_key')[0]
    return str


def rec(state, recu):
    modstate = state.copy()
    recu += 1
    modstate2 = swperson(modstate)
    graphstralt = getstate(modstate) + "->" + getstate(modstate2) + ";"
    if recu > 20:
        return None

    ret = go(modstate)
    ret2 = go(modstate2)
    if (ret == None) and (ret2 == None):
        return None
    modstate = ret[0]
    modstate2 = ret2[0]
    str = ret[1]
    graphstr = getstate(state) + "->" + getstate(modstate) + ";"
    graphstr2 = getstate(state) + "->" + getstate(modstate2) + ";"
    if myarr.count(graphstr) == 0:
        myarr.append(graphstr)
        rec(modstate, recu)
        rec(modstate, recu)
        rec(modstate, recu)
        rec(modstate, recu)
        rec(modstate, recu)
    if myarr.count(graphstr2) == 0:
        myarr.append(graphstr2)
        rec(modstate2, recu)
        rec(modstate2, recu)
        rec(modstate2, recu)
        rec(modstate2, recu)
        rec(modstate2, recu)

    if myarr.count(graphstralt) == 0:
        myarr.append(graphstralt)
    rec(modstate, recu)
    rec(modstate2, recu)

    return None


sys.setrecursionlimit(150000)
random.seed()
rec(START_STATE, 0)
print(myarr)
print(len(myarr))
