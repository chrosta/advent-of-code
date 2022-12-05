#!/usr/bin/python
###
# 12B
###
# caves = "A-start start-b A-c A-b b-d A-end end-b".replace('-', ",").split(" ")
caves = "pg-CH pg-yd yd-start fe-hv bi-CH CH-yd end-bi fe-RY ng-CH fe-CH ng-pg hv-FL FL-fe hv-pg bi-hv CH-end hv-ng yd-ng pg-fe start-ng end-FL fe-bi FL-ks pg-start".replace('-', ",").split(" ")
caves = [c.split(",") for c in caves]
paths = []
for c in caves:
    if c[1] == "start":
        c.insert(0, c[1])
        c.pop(2)
    if c[0] == "end":
        c.append(c[0])
        c.pop(0)
for i in range(len(caves)):
    c = caves[i]
    if c[0] != "start" and c[1] != "end":
        caves.append([c[1], c[0]])
#--
class Cave(object):
    def __init__(self, n, u=None):
        self.__up = u
        self.__name = n
        self.__downs = []

    def __str__(self):
        return self.__name

    def name(self):
        return str(self)

    def path(self, p=None):
        if p == None:
            p = [self.__name]
        if self.__up != None:
            p.insert(0, str(self.__up))
            p = self.__up.path(p)
        return p

    def down(self):
        global caves
        for cave in caves:
            if self.__name == cave[0]:
                down = Cave(cave[1], self)
                # print("CHECK="+str([self.__name, str(down)])+"?")
                # print("CHECK="+str(down.path())+"!")
                if self.__name == "start":
                    self.__downs.append(down)
                else:
                    a = str([self.__name, down.name()]).replace('[', "").replace(']', "")
                    b = str(down.path()[:-1]).replace('[', "").replace(']', "")
                    p = down.path()
                    #--
                    s = []
                    for c in p:
                        if len(c) < 3 and c.islower():
                            s.append(c)
                    s.sort()
                    # print(s)
                    # print(len([i for i in range(len(s)-1) if s[i] == s[i+1]]))
                    if len([i for i in range(len(s)-1) if s[i] == s[i+1]]) < 2:
                        print("CHECK=["+a+"]?")
                        print("CHECK="+str(down.path())+"!")
                        self.__downs.append(down)
                    #--
        if len(self.__downs) > 0:
            for d in self.__downs:
                d.down()
#--
print("CAVES="+str(caves))
start = Cave("start")
start.down()
#--
# And finish output in BASH.
#--
# ./12B.py | grep "'end']!" | sort | uniq -c | wc -l
#==
150426
