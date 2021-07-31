import sys, os
from ROOT import *

f = TFile("/home/tkimmel/Research/root/charmmfrecon.root")
#ts = f.Get("dsprecontree")
#tl = f.Get("dsplrecontree")
tp = f.Get("bcspi0tree")

#nEntriess = ts.GetEntries()
#nEntriesl = tl.GetEntries()
nEntriesp = tp.GetEntries()

"""
maxnpizs = int(ts.GetMaximum("npiz"))
maxnpizl = int(tl.GetMaximum("npiz"))
ntrus = [0]*maxnpizs
nfals = [0]*maxnpizs
ntrul = [0]*maxnpizl
nfall = [0]*maxnpizl
"""

maxnpizp = int(tp.GetMaximum("npiz"))
ntrus = [0]*maxnpizp
nfals = [0]*maxnpizp
ntrul = [0]*maxnpizp
nfall = [0]*maxnpizp
ntrup = [0]*maxnpizp
nfalp = [0]*maxnpizp

"""
for i in range(0, nEntriess):
    ts.GetEntry(i)
    piflag = ts.piflag
    npiz = ts.npiz
    if piflag == 2:
        nfals[npiz]+=1
    if piflag ==3:
        ntrus[npiz]+=1


for i in range(0, nEntriesl):
    tl.GetEntry(i)
    piflag = tl.piflag
    npiz = tl.npiz
    if piflag == 2:
        nfall[npiz]+=1
    if piflag ==3:
        ntrul[npiz]+=1
"""
"""
for i in range(0, nEntriess):
    ts.GetEntry(i)
    piflag = ts.piflag
    npiz = ts.npiz
    if piflag == 2:
        nfals[npiz]+=1
    if piflag ==3:
        ntrus[npiz]+=1

for i in range(1, maxnpizs):
    ntru = float(ntrus[i])
    total = float(ntrus[i]+nfals[i])
    if total != 0:
        chance = ntru/total
        print("The selection chance for multiplicity %i is: %f"%(i,chance))
    else:
        print("There were no events for multiplicity %i"%(i))
"""

for i in range(0, nEntriesp):
    tp.GetEntry(i)
    piflag = tp.piflag
    npiz = tp.npiz
    realdecayflag = tp.realdecayflag
    if piflag == 2:
        nfalp[npiz]+=1
        if realdecayflag == 1:
            nfall[npiz]+=1
        if realdecayflag ==2 :
            nfals[npiz]+=1
    if piflag == 3:
        ntrup[npiz]+=1
        if realdecayflag == 1:
            ntrul[npiz]+=1
        if realdecayflag == 2:
            ntrus[npiz]+=1

for i in range(1, maxnpizp):
    tntru = float(ntrup[i])
    tnfal = float(nfalp[i])
    total = float(ntrup[i]+nfalp[i])

    tntrul = float(ntrul[i])
    tnfall = float(nfall[i])
    totall = float(ntrul[i]+nfall[i])

    tntrus = float(ntrus[i])
    tnfals = float(nfals[i])
    totals = float(ntrus[i]+nfals[i])

    print("MULTIPLICITY %i"%(i))
    print("================")
    if total != 0:
        chance = tntru/total
        var = (chance*(1-chance))/total# Variance of a binomial distribution
        print("Signal/Total: %f/%f"%(tntru,total))
        print("The selection chance for all pi0s with multiplicity %i is: %f +- %f"%(i,chance,var))
        print("\n")
    else:
        print("There were no events for all pi0s with multiplicity %i"%(i))
        print("\n")
    if totall != 0:
        chancel = tntrul/totall
        varl = (chancel*(1-chancel))/totall
        print("Signal/Total: %f/%f"%(tntrul,totall))
        print("The selection chance for KL pi0s multiplicity %i is: %f +- %f"%(i,chancel,varl))
        print("\n")
    else:
        print("There were no events for KL pi0s with multiplicity %i"%(i))
        print("\n")
    if totals != 0:
        chances = tntrus/totals
        varss = (chances*(1-chances))/totals
        print("Signal/Total: %f/%f"%(tntrus,totals))
        print("The selection chance for KS pi0s multiplicity %i is: %f +- %f"%(i,chances,varss))
        print("\n")
    else:
        print("There were no events for KS pi0s with multiplicity %i"%(i))
        print("\n")
    print("\n")
