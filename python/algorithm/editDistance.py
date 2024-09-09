import math
keyboard_cartesian = {'q': {'x':0, 'y':0}, 'w': {'x':1, 'y':0}, 'e': {'x':2, 'y':0},
                      'r': {'x':3, 'y':0}, 't': {'x':4, 'y':0}, 'y': {'x':5, 'y':0},
                      'u': {'x':6, 'y':0}, 'i': {'x':7, 'y':0}, 'o': {'x':8, 'y':0},
                      'p': {'x':9, 'y':0}, 'a': {'x':0, 'y':1}, 'z': {'x':0, 'y':2},
                      's': {'x':1, 'y':1}, 'x': {'x':1, 'y':2}, 'd': {'x':2, 'y':1},
                      'c': {'x':2, 'y':2}, 'f': {'x':3, 'y':1}, 'b': {'x':4, 'y':2},
                      'm': {'x':5, 'y':2}, 'j': {'x':6, 'y':1}, 'g': {'x':4, 'y':1},
                      'h': {'x':5, 'y':1}, 'j': {'x':6, 'y':1}, 'k': {'x':7, 'y':1},
                      'l': {'x':8, 'y':1}, 'v': {'x':3, 'y':2}, 'n': {'x':5, 'y':2}, }

def euclidean_distance(a,b):
    X = (keyboard_cartesian[a]['x'] - keyboard_cartesian[b]['x'])**2
    Y = (keyboard_cartesian[a]['y'] - keyboard_cartesian[b]['y'])**2
    return math.sqrt(X+Y)
     
     
for i in keyboard_cartesian.keys():
    for j in keyboard_cartesian.keys():
        distance_from_i_to_j = [(i, j, euclidean_distance(i, j))]
        

def editDistance(str1, str2, m, n):
    if m == 0: return n
    if n == 0: return m
    
    if str1[m-1] == str2[n-1]:
        return editDistance(str1, str2, m-1, n-1)
    
    return 1 + min(editDistance(str1, str2, m, n-1),
                   editDistance(str1, str2, m-1, n),
                   editDistance(str1, str2, m-1, n-1))
    
str1 = 'sunday'
str2 = 'saturday'
m = len(str1)
n = len(str2)
print(editDistance(str1, str2, m, n))
    
# print(euclidean_distance('a', 'w'))
