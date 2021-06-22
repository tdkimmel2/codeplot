from ROOT import *
import sys
import math
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

#f = TFile("/home/tkimmel/Research/root/partialMC.root","READ")
#f2 = TFile("/home/tkimmel/Research/root/partialData.root","READ")
#f = TFile("/home/tkimmel/Research/root/systematics/dsSystematics.root","READ")
#f2 = TFile("/home/tkimmel/Research/root/systematics/dsSystematicsData.root","READ")
f = TFile("/home/tkimmel/Research/root/allmfrecon.root","READ")
t11 = f.Get("dsrecontree")
t12 = f.Get("dslrecontree")
#t21 = f2.Get("dsrecontree")
#t22 = f2.Get("dslrecontree")

pip = "kspipP"
pim = "kspimP"
mc = "mcflag"
truth = "abs(dsflag)==1"

bins=[0.05,0.075,0.1,0.125,0.15,0.175,0.2]
Effs = [0.832,0.930,0.967,0.984,1.009,1.008,1]
Errs = [0.0706,0.0288,0.0233,0.0197,0.0194,0.02109,0.0032]

print("Pi Plus")
num=float(0)
err=float(0)
for i in range(len(bins)):
    if i == len(bins)-1:
        continue
        rightbin = bins[i]
        kRangeL = t11.Draw(pip,pip+">= %f"%(rightbin),"goff")
        num += kRangeL*Effs[i]
        err += kRangeL*Errs[i]
    else:
        leftbin = bins[i]
        rightbin = bins[i+1]
        kRangeL = t11.Draw(pip,pip+">= %f && "%(leftbin)+pip+"< %f"%(rightbin),"goff")
        #num += kRangeL*Effs[i]
        #err += kRangeL*Errs[i]
        num += kRangeL
        err += kRangeL*Errs[i]
        #err += kRangeL
        print("%f >= "%(leftbin)+pip+" < %f: %i"%(rightbin,kRangeL))
total = t11.Draw(pip,"","goff")
totalerr = t11.Draw(pip,pip+"<0.2","goff")
frac = num/total
fracerr = err/totalerr
print frac
print fracerr
print("Total Systematic: %.4f"%(frac*fracerr + Errs[-1]*(1-frac)))

print("\nPi Minus")
num=float(0)
err=float(0)
for i in range(len(bins)):
    if i == len(bins)-1:
        continue
        rightbin = bins[i]
        kRangeL = t11.Draw(pim,pim+">= %f"%(rightbin),"goff")
        num += kRangeL*Effs[i]
        err += kRangeL*Errs[i]
    else:
        leftbin = bins[i]
        rightbin = bins[i+1]
        kRangeL = t11.Draw(pim,pim+">= %f && "%(leftbin)+pim+"< %f"%(rightbin),"goff")
        #num += kRangeL*Effs[i]
        #err += kRangeL*Errs[i]
        num += kRangeL
        err += kRangeL*Errs[i]
        #err += kRangeL
        print("%f >= "%(leftbin)+pim+" < %f: %i"%(rightbin,kRangeL))
total = t11.Draw(pim,"","goff")
totalerr = t11.Draw(pim,pim+"<0.2","goff")
frac = num/total
fracerr = err/totalerr
print frac
print fracerr
print("Total Systematic: %.4f"%(frac*fracerr + Errs[-1]*(1-frac)))
