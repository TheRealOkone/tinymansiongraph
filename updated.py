import random
import sys

START_STATE = {'player': 'alice', 'alice_room': 'west room', 'bob_room': 'east room', 'red_key': 'east room',
               'blue_key': 'west room', 'green_key': 'east room'}

statedict = {}

myarr = []


alicelock = 0

boblock = 0

def swperson(state):
    a = state.get('player')
    if (alicelock == 0) and (boblock == 0):
        if (a == 'alice'):
            state['player'] = 'bob'
        if (a == 'bob'):
            state['player'] = 'alice'
    if (alicelock == 1):
        state['player'] = 'bob'
    if (boblock == 1):
            state['player'] = 'alice'
    if (boblock == 1) and (alicelock == 1):
            state['player'] = 'win'
    return state


def go(state):
    if state == None:
        return None
    ch = False
    str = ""
    r = state.get('red_key')
    b = state.get('blue_key')
    g = state.get('green_key')
    a = state.get('player')
    if a == 'alice' and state.get('alice_room') == "red room" and state.get('bob_room') == "blue room":
        state["player"] = "win"
        return [state,str]
    if a == 'alice' and state.get('alice_room') == "red room":
        return None
    if a == 'bob' and state.get('bob_room') == "blue room":
        return None

    croom = state.get(a + '_room')

    st = getstate(state)
    count = statedict.get(st)
    if (count == None):
        statedict.setdefault(st)
        statedict[st] = ""
        count = ""

    if (croom == 'red room'):
        if (r == croom) and (g == croom) and (b == croom) and count.find("u") == -1:
            state[a + '_room'] = 'west room'
            state['red_key'] = 'west room'
            state['green_key'] = 'west room'
            state['blue_key'] = 'west room'
            statedict[st] += "u"
            return [state, str]
        if (r == croom) and (g == croom) and (b == croom) and count.find("q") == -1:
            state[a + '_room'] = 'west room'
            state['red_key'] = 'west room'
            state['green_key'] = 'west room'
            statedict[st] += "q"
            return [state, str]
        if (r == croom) and (g == croom) and (b != croom) and count.find("t") == -1:
            state[a + '_room'] = 'west room'
            state['red_key'] = 'west room'
            state['green_key'] = 'west room'
            statedict[st] += "t"
            return [state, str]
        if (r == croom) and (b == croom) and (g == croom) and count.find("w") == -1:
            state[a + '_room'] = 'west room'
            state['red_key'] = 'west room'
            state['blue_key'] = 'west room'
            statedict[st] += "w"
            return [state, str]
        if (r == croom) and (b == croom) and (g != croom) and count.find("e") == -1:
            state[a + '_room'] = 'west room'
            state['red_key'] = 'west room'
            state['blue_key'] = 'west room'
            statedict[st] += "e"
            return [state, str]
        if (r == croom) and (g == croom) and (b == croom) and count.find("i") == -1:
            state[a + '_room'] = 'west room'
            state['red_key'] = 'west room'
            statedict[st] += "i"
            return [state, str]
        if (r == croom) and (g != croom) and (b == croom) and count.find("o") == -1:
            state[a + '_room'] = 'west room'
            state['red_key'] = 'west room'
            statedict[st] += "o"
            return [state, str]
        if (r == croom) and (g == croom) and (b != croom) and count.find("r") == -1:
            state[a + '_room'] = 'west room'
            state['red_key'] = 'west room'
            statedict[st] += "r"
            return [state, str]
        if (r == croom) and (g != croom) and (b != croom) and count.find("r") == -1:
            state[a + '_room'] = 'west room'
            state['red_key'] = 'west room'
            statedict[st] += "r"
            return [state, str]

    if croom == 'west room':
        if (r == croom) and (g == croom) and (b == croom) and count.find("u") == -1:
            state[a + '_room'] = 'red room'
            state['red_key'] = 'red room'
            state['green_key'] = 'red room'
            state['blue_key'] = 'red room'
            statedict[st] += "u"
            return [state, str]
        if (r == croom) and (g == croom) and (b == croom) and count.find("h") == -1:
            state[a + '_room'] = 'east room'
            state['red_key'] = 'east room'
            state['green_key'] = 'east room'
            statedict[st] += "h"
            return [state, str]
        if (r == croom) and (g == croom) and (b != croom) and count.find("k") == -1:
            state[a + '_room'] = 'east room'
            state['red_key'] = 'east room'
            state['green_key'] = 'east room'
            statedict[st] += "k"
            return [state, str]
        if (g == croom) and (b == croom) and (g == croom) and count.find("l") == -1:
            state[a + '_room'] = 'east room'
            state['blue_key'] = 'east room'
            state['green_key'] = 'east room'
            statedict[st] += "l"
            return [state, str]
        if (g == croom) and (b == croom) and (g != croom) and count.find("j") == -1:
            state[a + '_room'] = 'east room'
            state['blue_key'] = 'east room'
            state['green_key'] = 'east room'
            statedict[st] += "j"
            return [state, str]

        if (r == croom) and (g == croom) and (b == croom) and count.find("t") == -1:
            state[a + '_room'] = 'red room'
            state['red_key'] = 'red room'
            state['green_key'] = 'red room'
            statedict[st] += "t"
            return [state, str]
        if (r == croom) and (g == croom) and (b != croom) and count.find(";") == -1:
            state[a + '_room'] = 'red room'
            state['red_key'] = 'red room'
            state['green_key'] = 'red room'
            statedict[st] += ";"
            return [state, str]
        if (r == croom) and (b == croom) and (g == croom) and count.find("y") == -1:
            state[a + '_room'] = 'red room'
            state['red_key'] = 'red room'
            state['blue_key'] = 'red room'
            statedict[st] += "y"
            return [state, str]
        if (r == croom) and (b == croom) and (g != croom) and count.find("p") == -1:
            state[a + '_room'] = 'red room'
            state['red_key'] = 'red room'
            state['blue_key'] = 'red room'
            statedict[st] += "p"
            return [state, str]

        if r == croom and (g == croom) and (b == croom) and count.find("r") == -1:
            state[a + '_room'] = 'red room'
            state['red_key'] = 'red room'
            statedict[st] += "r"
            return [state, str]
        if r == croom and (g != croom) and (b == croom) and count.find("z") == -1:
            state[a + '_room'] = 'red room'
            state['red_key'] = 'red room'
            statedict[st] += "z"
            return [state, str]
        if r == croom and (g == croom) and (b != croom) and count.find("x") == -1:
            state[a + '_room'] = 'red room'
            state['red_key'] = 'red room'
            statedict[st] += "x"
            return [state, str]
        if r == croom and (g != croom) and (b != croom) and count.find("c") == -1:
            state[a + '_room'] = 'red room'
            state['red_key'] = 'red room'
            statedict[st] += "c"
            return [state, str]


        if g == croom and (r == croom) and (b == croom) and count.find("g") == -1:
            state[a + '_room'] = 'east room'
            state['green_key'] = 'east room'
            statedict[st] += "g"
            return [state, str]
        if g == croom and (r != croom) and (b == croom) and count.find("m") == -1:
            state[a + '_room'] = 'east room'
            state['green_key'] = 'east room'
            statedict[st] += "m"
            return [state, str]
        if g == croom and (r == croom) and (b != croom) and count.find("n") == -1:
            state[a + '_room'] = 'east room'
            state['green_key'] = 'east room'
            statedict[st] += "n"
            return [state, str]
        if g == croom and (r != croom) and (b != croom) and count.find("b") == -1:
            state[a + '_room'] = 'east room'
            state['green_key'] = 'east room'
            statedict[st] += "b"
            return [state, str]


    if (croom == 'east room'):
        if (r == croom) and (g == croom) and (b == croom) and count.find("k") == -1:
            state[a + '_room'] = 'west room'
            state['red_key'] = 'west room'
            state['green_key'] = 'west room'
            state['blue_key'] = 'west room'
            statedict[st] += "k"
            return [state, str]
        if (r == croom) and (g == croom) and (b == croom) and count.find(",") == -1:
            state[a + '_room'] = 'blue room'
            state['red_key'] = 'blue room'
            state['green_key'] = 'blue room'
            state['blue_key'] = 'blue room'
            statedict[st] += ","
            return [state, str]
        if (r == croom) and (b == croom) and (g == croom) and count.find("n") == -1:
            state[a + '_room'] = 'blue room'
            state['red_key'] = 'blue room'
            state['blue_key'] = 'blue room'
            statedict[st] += "n"
            return [state, str]
        if (r == croom) and (b == croom) and (g != croom) and count.find("1") == -1:
            state[a + '_room'] = 'blue room'
            state['red_key'] = 'blue room'
            state['blue_key'] = 'blue room'
            statedict[st] += "1"
            return [state, str]
        if (g == croom) and (b == croom) and (r == croom) and count.find("m") == -1:
            state[a + '_room'] = 'blue room'
            state['blue_key'] = 'blue room'
            state['green_key'] = 'blue room'
            statedict[st] += "m"
            return [state, str]
        if (r == croom) and (g == croom) and (r != croom) and count.find("h") == -1:
            state[a + '_room'] = 'west room'
            state['red_key'] = 'west room'
            state['green_key'] = 'west room'
            statedict[st] += "h"
            return [state, str]
        if (r == croom) and (g == croom) and (r == croom) and count.find("2") == -1:
            state[a + '_room'] = 'west room'
            state['red_key'] = 'west room'
            state['green_key'] = 'west room'
            statedict[st] += "2"
            return [state, str]
        if (g == croom) and (b == croom) and (r == croom) and count.find("j") == -1:
            state[a + '_room'] = 'west room'
            state['blue_key'] = 'west room'
            state['green_key'] = 'west room'
            statedict[st] += "j"
            return [state, str]
        if (g == croom) and (b == croom) and (r != croom) and count.find("3") == -1:
            state[a + '_room'] = 'west room'
            state['blue_key'] = 'west room'
            state['green_key'] = 'west room'
            statedict[st] += "3"
            return [state, str]

        if (g == croom) and (r == croom) and (b == croom) and count.find("g") == -1:
            state[a + '_room'] = 'west room'
            state['green_key'] = 'west room'
            statedict[st] += "g"
            return [state, str]
        if (g == croom) and (r != croom) and (b == croom) and count.find("4") == -1:
            state[a + '_room'] = 'west room'
            state['green_key'] = 'west room'
            statedict[st] += "4"
            return [state, str]
        if (g == croom) and (r == croom) and (b != croom) and count.find("5") == -1:
            state[a + '_room'] = 'west room'
            state['green_key'] = 'west room'
            statedict[st] += "5"
            return [state, str]
        if (g == croom) and (r != croom) and (b != croom) and count.find("6") == -1:
            state[a + '_room'] = 'west room'
            state['green_key'] = 'west room'
            statedict[st] += "6"
            return [state, str]

        if (b == croom) and (g == croom) and (r == croom) and count.find("b") == -1:
            state[a + '_room'] = 'blue room'
            state['blue_key'] = 'blue room'
            statedict[st] += "b"
            return [state, str]
        if (b == croom) and (g != croom) and (r == croom) and count.find("7") == -1:
            state[a + '_room'] = 'blue room'
            state['blue_key'] = 'blue room'
            statedict[st] += "7"
            return [state, str]
        if (b == croom) and (g == croom) and (r != croom) and count.find("8") == -1:
            state[a + '_room'] = 'blue room'
            state['blue_key'] = 'blue room'
            statedict[st] += "8"
            return [state, str]
        if (b == croom) and (g != croom) and (r != croom) and count.find("9") == -1:
            state[a + '_room'] = 'blue room'
            state['blue_key'] = 'blue room'
            statedict[st] += "9"
            return [state, str]



    if (croom == 'blue room'):
        if (r == croom) and (g == croom) and (b == croom) and count.find(",") == -1:
            state[a + '_room'] = 'east room'
            state['red_key'] = 'east room'
            state['green_key'] = 'east room'
            state['blue_key'] = 'east room'
            statedict[st] += ","
            return [state, str]
        if (r == croom) and (b == croom) and (g == croom) and count.find("n") == -1:
            state[a + '_room'] = 'east room'
            state['red_key'] = 'east room'
            state['blue_key'] = 'east room'
            statedict[st] += "n"
            return [state, str]
        if (r == croom) and (b == croom) and (g != croom) and count.find("a") == -1:
            state[a + '_room'] = 'east room'
            state['red_key'] = 'east room'
            state['blue_key'] = 'east room'
            statedict[st] += "a"
            return [state, str]
        if (g == croom) and (b == croom) and (r == croom) and count.find("m") == -1:
            state[a + '_room'] = 'east room'
            state['blue_key'] = 'east room'
            state['green_key'] = 'east room'
            statedict[st] += "m"
            return [state, str]
        if (g == croom) and (b == croom) and (r != croom) and count.find("s") == -1:
            state[a + '_room'] = 'east room'
            state['blue_key'] = 'east room'
            state['green_key'] = 'east room'
            statedict[st] += "s"
            return [state, str]

        if (b == croom) and (r == croom) and (g == croom) and count.find("b") == -1:
            state[a + '_room'] = 'east room'
            state['blue_key'] = 'east room'
            statedict[st] += "b"
            return [state, str]
        if (b == croom) and (r != croom) and (g == croom) and count.find("1") == -1:
            state[a + '_room'] = 'east room'
            state['blue_key'] = 'east room'
            statedict[st] += "1"
            return [state, str]
        if (b == croom) and (r == croom) and (g != croom) and count.find("2") == -1:
            state[a + '_room'] = 'east room'
            state['blue_key'] = 'east room'
            statedict[st] += "2"
            return [state, str]
        if (b == croom) and (r != croom) and (g != croom) and count.find("3") == -1:
            state[a + '_room'] = 'east room'
            state['blue_key'] = 'east room'
            statedict[st] += "3"
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
    if(modstate != modstate2):
        graphstralt = getstate(modstate) + "->" + getstate(modstate2) + ";"
        if myarr.count(graphstralt) == 0:
            myarr.append(graphstralt)
    if recu > 900:
        return None

    ret = go(modstate)
    ret2 = go(modstate2)
    if (ret == None) and (ret2 == None):
        return None
    if state.get('player') == "win":
        graphstrwin = getstate(state) + ' [style="filled",fillcolor="green"];'
        if myarr.count(graphstrwin) == 0:
            myarr.append(graphstrwin)
        return None
    if(ret != None):
        modstate = ret[0]
        graphstr = getstate(state) + "->" + getstate(modstate) + ";"
        if myarr.count(graphstr) == 0:
            myarr.append(graphstr)
            rec(modstate, recu)
            rec(modstate, recu)
            rec(modstate, recu)
            rec(modstate, recu)
            rec(modstate, recu)
            rec(modstate, recu)
            rec(modstate, recu)
            rec(modstate, recu)
            rec(modstate, recu)
            rec(modstate, recu)
            rec(modstate, recu)
            rec(modstate, recu)
            rec(modstate, recu)
            rec(modstate, recu)
            rec(modstate, recu)
            rec(modstate, recu)
            rec(modstate, recu)
            rec(modstate, recu)
            rec(modstate, recu)
            rec(modstate, recu)
            rec(modstate, recu)
            rec(modstate, recu)
            rec(modstate, recu)
            rec(modstate, recu)
            rec(modstate, recu)
            rec(modstate, recu)
            rec(modstate, recu)
    if(ret2 != None):
        modstate2 = ret2[0]
        graphstr2 = getstate(state) + "->" + getstate(modstate2) + ";"
        if myarr.count(graphstr2) == 0:
            myarr.append(graphstr2)
            rec(modstate2, recu)
            rec(modstate2, recu)
            rec(modstate2, recu)
            rec(modstate2, recu)
            rec(modstate2, recu)
            rec(modstate2, recu)
            rec(modstate2, recu)
            rec(modstate2, recu)
            rec(modstate2, recu)
            rec(modstate2, recu)
            rec(modstate2, recu)
            rec(modstate2, recu)
            rec(modstate2, recu)
            rec(modstate2, recu)
            rec(modstate2, recu)
            rec(modstate2, recu)
            rec(modstate2, recu)
            rec(modstate2, recu)
            rec(modstate2, recu)
            rec(modstate2, recu)
            rec(modstate2, recu)
            rec(modstate2, recu)
            rec(modstate2, recu)
            rec(modstate2, recu)
            rec(modstate2, recu)
            rec(modstate2, recu)
            rec(modstate2, recu)
            rec(modstate2, recu)
            rec(modstate2, recu)
            rec(modstate2, recu)
    return None

def out(myarr):
    for i in myarr:
        print(i)

sys.setrecursionlimit(150000)
random.seed()
rec(START_STATE, 0)
print(myarr)
print(len(myarr))
print(statedict)
print(len(statedict))
out(myarr)
