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

piz = "pizP"
mc = "mcflag"
truth = "abs(dsflag)==1"

bins=[0.0,1.25,1.625,2.0,2.375,2.75,3.125,3.5]
Effs = [0.9544,0.9887,1.0285,1.0539,1.1519,1.1563,1.4143,1.7034]
Errs = [0.0021,0.0038,0.0133,0.0363,0.0209,0.0635,0.0602,0.2508]

print("KS Pizs")
num=float(0)
eff=float(0)
err=float(0)
for i in range(len(bins)):
    if i == len(bins)-1:
        #continue
        rightbin = bins[i]
        kRangeL = t11.Draw(piz,piz+">= %f"%(rightbin),"goff")
        eff += kRangeL*Effs[i]
        num += kRangeL
        err += kRangeL*Errs[i]
        print(piz+" >= %f: %i"%(rightbin,kRangeL))
    else:
        leftbin = bins[i]
        rightbin = bins[i+1]
        kRangeL = t11.Draw(piz,piz+">= %f && "%(leftbin)+piz+"< %f"%(rightbin),"goff")
        num += kRangeL
        eff += kRangeL*Effs[i]
        err += kRangeL*Errs[i]
        print("%f >= "%(leftbin)+piz+" < %f: %i"%(rightbin,kRangeL))
total = t11.Draw(piz,"","goff")
totalerr = t11.Draw(piz,"","goff")
frac = num/total
fraceff = eff/total
fracerr = err/totalerr
print frac
print fraceff
print fracerr
print("Total Systematic: %.4f"%(frac*fracerr + Errs[-1]*(1-frac)))

print("\nKL Pizs")
num=float(0)
eff=float(0)
err=float(0)
for i in range(len(bins)):
    if i == len(bins)-1:
        #continue
        rightbin = bins[i]
        kRangeL = t12.Draw(piz,piz+">= %f"%(rightbin),"goff")
        eff += kRangeL*Effs[i]
        num += kRangeL
        err += kRangeL*Errs[i]
        print(piz+" >= %f: %i"%(rightbin,kRangeL))
    else:
        leftbin = bins[i]
        rightbin = bins[i+1]
        kRangeL = t12.Draw(piz,piz+">= %f && "%(leftbin)+piz+"< %f"%(rightbin),"goff")
        num += kRangeL
        eff += kRangeL*Effs[i]
        err += kRangeL*Errs[i]
        print("%f >= "%(leftbin)+piz+" < %f: %i"%(rightbin,kRangeL))
total = t12.Draw(piz,"","goff")
totalerr = t12.Draw(piz,"","goff")
frac = num/total
fraceff = eff/total
fracerr = err/totalerr
print frac
print fraceff
print fracerr
print("Total Systematic: %.4f"%(frac*fracerr + Errs[-1]*(1-frac)))
