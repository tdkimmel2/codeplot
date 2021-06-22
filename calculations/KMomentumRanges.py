from ROOT import *
import sys
import math
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

#f = TFile("/home/tkimmel/Research/root/partialMC.root","READ")
#f2 = TFile("/home/tkimmel/Research/root/partialData.root","READ")
f = TFile("/home/tkimmel/Research/root/systematics/dsSystematics.root","READ")
f2 = TFile("/home/tkimmel/Research/root/systematics/dsSystematicsData.root","READ")
t11 = f.Get("dsrecontree")
t12 = f.Get("dslrecontree")
t21 = f2.Get("dsrecontree")
t22 = f2.Get("dslrecontree")

kp = "kpPl"
mc = "mcflag"
truth = "abs(dsflag)==1"

bins=[0,0.5,0.625,0.75,0.875,1.0,1.25,1.5,1.75,2,2.5,3.5]
Effs = [0.678,0.392,0.385,0.377,0.464,0.477,0.488,0.511,0.556,0.694,0.208]
Errs = [0.099,0.038,0.031,0.030,0.035,0.029,0.033,0.044,0.062,0.087,0.097]

binsS=[0,0.5,1.0,1.5,2.0,2.5,3.0,3.5]
EffsS = [0.9421,0.9778,0.9831,0.9828,0.9833,0.9833,1.0024,0.9848]
ErrsS = [0.0192,0.0091,0.0073,0.0070,0.0078,0.0096,0.0129,0.0135]

print("KLONG MODE")
num=float(0)
err=float(0)
for i in range(len(bins)):
    if i == len(bins)-1:
        rightbin = bins[i]
        kRangeL = t12.Draw(kp,kp+">= %f"%(rightbin),"goff")
        num += kRangeL*Effs[i-1]
        err += kRangeL*Errs[i-1]
    else:
        leftbin = bins[i]
        rightbin = bins[i+1]
        kRangeL = t12.Draw(kp,kp+">= %f && "%(leftbin)+kp+"< %f"%(rightbin),"goff")
        num += kRangeL*Effs[i]
        err += kRangeL*Errs[i]
    print("%f >= "%(leftbin)+kp+" < %f: %i"%(rightbin,kRangeL))
total = t12.Draw(kp,"","goff")
#total = t12.Draw(kp,kp+"<%f"%(bins[-1]),"goff")
print("Weighted Efficiency: %.4f"%(num/total))
print("Weighted Systematic: %.4f"%(err/total))


print("KSHORT MODE")
num=float(0)
err=float(0)
for i in range(len(binsS)-1):
    if i == len(binsS)-1:
        rightbin = binsS[i]
        kRangeS = t11.Draw(kp,kp+">= %f"%(rightbin),"goff")
    else:
        leftbin = binsS[i]
        rightbin = binsS[i+1]
        kRangeS = t11.Draw(kp,kp+">= %f && "%(leftbin)+kp+"< %f"%(rightbin),"goff")
    print("%f >= "%(leftbin)+kp+" < %f: %i"%(rightbin,kRangeL))
    num += kRangeS*EffsS[i]
    err += kRangeS*ErrsS[i]
#total = t11.Draw(kp,kp+"<%i"%(bins[-1]),"goff")
total = t11.Draw(kp,"","goff")
print("Weighted Efficiency: %.4f"%(num/total))
print("Weighted Systematic: %.4f"%(err/total))
