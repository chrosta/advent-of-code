#!/usr/bin/python
###
# 14B
###
import re
from collections import Counter
from copy import deepcopy as dc
# template = "NNCB"
# pairs = "CH,B HH,N CB,H NH,C HB,C HC,B HN,C NN,C BH,H NC,B NB,B BN,B BB,N BC,B CC,N CN,C"
template = "KBKPHKHHNBCVCHPSPNHF"
pairs = "OP,H CF,C BB,V KH,O CV,S FV,O FS,K KO,C PP,S SH,K FH,O NF,H PN,P BO,H OK,K PO,P SF,K BF,P HH,S KP,H HB,N NP,V KK,P PF,P BK,V OF,H FO,S VC,P FK,B NK,S CB,B PV,C CO,N BN,C HV,H OC,N NB,O CS,S HK,C VS,F BH,C PC,S KC,O VO,P FB,K BV,V VN,N ON,F VH,H CN,O HO,O SV,O SS,H KF,N SP,C NS,V SO,F BC,P HC,C FP,H OH,S OB,S HF,V SC,B SN,N VK,C NC,V VV,S SK,K PK,K PS,N KB,S KS,C NN,C OO,C BS,B NV,H FF,P FC,N OS,H KN,N VP,B PH,N NH,S OV,O FN,V CP,B NO,V CK,C VF,B HS,B KV,K VB,H SB,S BP,S CC,F HP,B PB,P HN,P CH,O"
last = template[-1:]

print(template)
pairs = {x[:2]:x[3] for x in pairs.split(' ')}
print(pairs)
chars = Counter(template)
print(chars)
template = Counter(a+b for a, b in zip(template, template[1:]))
print(template)
print("---")

old = template
for i in range(40):
    new = Counter()
    for (a,b), v in old.items():
        i = pairs[a+b]
        new[a+i] += v
        new[i+b] += v
        chars[i] += v
        old = new
    print(old)
print("===")
print(max(chars.values()) - min(chars.values()))
#==
# 2587447599164
