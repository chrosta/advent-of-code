#!/usr/bin/python
###
# 14A
###
# template = "NNCB"
# pairs = "CH,B HH,N CB,H NH,C HB,C HC,B HN,C NN,C BH,H NC,B NB,B BN,B BB,N BC,B CC,N CN,C".split(" ")
template = "KBKPHKHHNBCVCHPSPNHF"
pairs = "OP,H CF,C BB,V KH,O CV,S FV,O FS,K KO,C PP,S SH,K FH,O NF,H PN,P BO,H OK,K PO,P SF,K BF,P HH,S KP,H HB,N NP,V KK,P PF,P BK,V OF,H FO,S VC,P FK,B NK,S CB,B PV,C CO,N BN,C HV,H OC,N NB,O CS,S HK,C VS,F BH,C PC,S KC,O VO,P FB,K BV,V VN,N ON,F VH,H CN,O HO,O SV,O SS,H KF,N SP,C NS,V SO,F BC,P HC,C FP,H OH,S OB,S HF,V SC,B SN,N VK,C NC,V VV,S SK,K PK,K PS,N KB,S KS,C NN,C OO,C BS,B NV,H FF,P FC,N OS,H KN,N VP,B PH,N NH,S OV,O FN,V CP,B NO,V CK,C VF,B HS,B KV,K VB,H SB,S BP,S CC,F HP,B PB,P HN,P CH,O".split(" ")
pairs = [p.split(",") for p in pairs]
#pairs = [[p[0], "".join([p[0][:1],p[1],p[0][1:]])] for p in pairs]
#--
print(template)
print(pairs)
#--
for i in range(10):
    print(i)
    print(len(template))
    t = 0
    while True:
        s = template[t:t+2]
        for p in pairs:
            if s == p[0]:
                template = list(template)
                template.insert(t+1, p[1])
                template = "".join(template)
                t += 1
        t += 1
        if t+2 > len(template):
            break
    # print("---")
    # print(template)
print("===")
print(template)
t = list(set(template))
t.sort()
c = [template.count(c) for c in t]
c.sort()
print(c[len(c)-1] - c[0])
#==
# 2435

#--
exit(0)
for x in range(1):
    print("---")
    new = {}
    for p in pairs:
        if old.find(p[0]) > -1:
            # new[old.find(p[0])] = old.replace(p[0], p[1])
            new[old.find(p[0])] = p[1]
    text = old
    for k, v in sorted(new.items()):
        print(k, v)
        #text = old[0:k]+
        # text = text.paste(k+1, v[k:k+3])
        # print(text)
    print("===")
    print(text)
    old = str(text)
