```python
from funzione import crosscount
import math

def test_crosscount_1():
    v = [10, 20, 30, 40]  # Define the list of coordinates
    assert crosscount(v) == 0

def test_crosscount_2():
    v = [10, 20, 30, 40]
    people = ['A', 'B', 'C', 'D']
    links = [('A', 'B'), ('C', 'D')]
    loc = {p:(v[2*i],v[2*i+1]) for i, p in enumerate(people)}
    assert crosscount(v) == 0

def test_crosscount_3():
    v = [10, 20, 30, 40]
    people = ['A', 'B', 'C', 'D']
    links = [('A', 'B'), ('C', 'D')]
    loc = {p:(v[2*i],v[2*i+1]) for i, p in enumerate(people)}
    total = 0
    for i in range(len(links)):
        for j in range(i+1, len(links)):
            (x1,y1),(x2,y2) = loc[links[i][0]],loc[links[i][1]]
            (x3,y3),(x4,y4) = loc[links[j][0]],loc[links[j][1]]
            den = (y4-y3)*(x2-x1)-(x4-x3)*(y2-y1)
            if den == 0: continue
            ua=((x4-x3)*(y1-y3)-(y4-y3)*(x1-x3))/den
            ub=((x2-x1)*(y1-y3)-(y2-y1)*(x1-x3))/den
            if ua>0 and ua<1 and ub>0 and ub<1: total +=1
        for i in range(len(people)):
            for j in range(i+1, len(people)):
                (x1,y1), (x2,y2) = loc[people[i]], loc[people[j]]
                dist = math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
                if dist < 50: total += (1.0-(dist/50))
    assert crosscount(v) == total

def test_crosscount_4():
    v = [10, 20, 30, 40]
    people = ['A', 'B', 'C', 'D']
    links = [('A', 'B'), ('C', 'D')]
    loc = {p:(v[2*i],v[2*i+1]) for i, p in enumerate(people)}
    total = 0
    for i in range(len(links)):
        for j in range(i+1, len(links)):
            (x1,y1),(x2,y2) = loc[links[i][0]],loc[links[i][1]]
            (x3,y3),(x4,y4) = loc[links[j][0]],loc[links[j][1]]
            den = (y4-y3)*(x2-x1)-(x4-x3)*(y2-y1)
            if den == 0: continue
            ua=((x4-x3)*(y1-y3)-(y4-y3)*(x1-x3))/den
            ub=((x2-x1)*(y1-y3)-(y2-y1)*(x1-x3))/den
            if ua>0 and ua<1 and ub>0 and ub<1: total +=1
    assert crosscount(v) == 0

def test_crosscount_5():
    v = [10, 20, 30, 40]
    people = ['A', 'B', 'C', 'D']
    links = [('A', 'B'), ('C', 'D')]
    loc = {p:(v[2*i],v[2*i+1]) for i, p in enumerate(people)}
    total = 0
    for i in range(len(people)):
        for j in range(i+1, len(people)):
            (x1,y1), (x2,y2) = loc[people[i]], loc[people[j]]
            dist = math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
            if dist < 50: total += (1.0-(dist/50))
    assert crosscount(v) == total

def test_crosscount_6():
    v = [10, 20, 30, 40]
    people = ['A', 'B', 'C', 'D']
    links = [('A', 'B'), ('C', 'D')]
    loc = {p:(v[2*i],v[2*i
