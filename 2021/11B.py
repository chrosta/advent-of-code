#!/usr/bin/python
###
# 11B
###
data = "6744638455 3135745418 4754123271 4224257161 8167186546 2268577674 7177768175 2662255275 4655343376 7852526168".split(" ")
data = [list(r) for r in data]
rows = len(data)
cols = len(data[0])
data = [[int(data[r][c]) for c in range(cols)] for r in range(rows)]
def show(t, d): print("---["+t+"]---"); print(str(d).replace('[[',"[").replace(']]', "]").replace(' ', "").replace('],[', "]\n["))
#--
show("DATA, 0", data)
#--
steps = 0
flashes = 0
while True:
    # Increasing energy levels of octopuses...
    for r in range(0, rows):
        for c in range(0, cols):
            data[r][c] += 1
    # Octopuses flashing after energy level was updated...
    temp = []
    while True:
        f = 0
        for r in range(0, rows):
            for c in range(0, cols):
                a = "["+str(r)+","+str(c)+"]"
                if data[r][c] > 9 and a not in str(temp).replace(', ', ","):
                    f += 1
                    flashes += 1
                    if (r-1) >= 0: data[r-1][c] += 1
                    if (r-1) >= 0 and (c+1) < cols: data[r-1][c+1] += 1
                    if (c+1) < cols: data[r][c+1] += 1
                    if (r+1) < rows and (c+1) < cols: data[r+1][c+1] += 1
                    if (r+1) < rows: data[r+1][c] += 1
                    if (r+1) < rows and (c-1) >= 0: data[r+1][c-1] += 1
                    if (c-1) >= 0: data[r][c-1] += 1
                    if (r-1) >= 0 and (c-1) >= 0: data[r-1][c-1] += 1
                    temp.append(a)
        if f == 0: break
    # Flashed octopuses are settings to 0...
    s = 0
    for r in range(0, rows):
        for c in range(0, cols):
            if data[r][c] > 9:
                data[r][c] = 0
                s += 1
    #--
    show("DATA, "+str(steps+1), data)
    if s == (rows*cols): break
    steps += 1
#==
214
