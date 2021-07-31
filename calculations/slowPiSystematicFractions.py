from ROOT import *
import sys
import math
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

#f = TFile("/home/tkimmel/Research/root/partialMC.root","READ")
#f2 = TFile("/home/tkimmel/Research/root/partialData.root","READ")
#f = TFile("/home/tkimmel/Research/root/systematics/dsSystematics.root","READ")
#f = TFile("/home/tkimmel/Research/root/systematics/dsSystematicsData.root","READ")
#f = TFile("/home/tkimmel/Research/root/allmfrecon.root","READ")
#f = TFile("/home/tkimmel/Research/root/partialData.root","READ")
f = TFile("/home/tkimmel/Research/root/fullStream.root","READ")
t11 = f.Get("dsrecontree")
t12 = f.Get("dslrecontree")
#t21 = f2.Get("dsrecontree")
#t22 = f2.Get("dslrecontree")

pip = "pip"
mc = "mcflag"
truth = "abs(dsflag)==1"
exp = "exp!=43"

bins=[0.05,0.075,0.1,0.125,0.15,0.175,0.2]
Effs = [0.832,0.930,0.967,0.984,1.009,1.008,1.0]
Errs = [0.07,0.027,0.021,0.017,0.016,0.018,0.0013]

print("KS Slow Pions")
num=float(0)
eff=float(0)
err=float(0)
for i in range(len(bins)):
    if i == len(bins)-1:
        #continue
        rightbin = bins[i]
        #kRangeL = t11.Draw(pip,pip+">= %f"%(rightbin),"goff")
        kRangeL = t11.Draw(pip,pip+">= %f && "%(rightbin)+exp,"goff")
        eff += kRangeL*Effs[i]
        num += kRangeL
        err += kRangeL*Errs[i]
        print(pip+" >= %f: %i"%(rightbin,kRangeL))
    else:
        leftbin = bins[i]
        rightbin = bins[i+1]
        #kRangeL = t11.Draw(pip,pip+">= %f && "%(leftbin)+pip+"< %f"%(rightbin),"goff")
        kRangeL = t11.Draw(pip,pip+">= %f && "%(leftbin)+pip+"< %f && "%(rightbin)+exp,"goff")
        num += kRangeL
        eff += kRangeL*Effs[i]
        err += kRangeL*Errs[i]
        print("%f >= "%(leftbin)+pip+" < %f: %i"%(rightbin,kRangeL))
#total = t11.Draw(pip,"","goff")
total = t11.Draw(pip,exp,"goff")
frac = num/total
fraceff = eff/total
fracerr = err/total
print total
print frac
print fraceff
print fracerr
print("Total Systematic: %.4f"%(math.sqrt((frac*fracerr)**2 + (Errs[-1]*(1-frac))**2)))

print("\nKL Slow Pions")
num=float(0)
eff=float(0)
err=float(0)
for i in range(len(bins)):
    if i == len(bins)-1:
        #continue
        rightbin = bins[i]
        #kRangeL = t12.Draw(pip,pip+">= %f"%(rightbin),"goff")
        kRangeL = t12.Draw(pip,pip+">= %f && "%(rightbin)+exp,"goff")
        eff += kRangeL*Effs[i]
        num += kRangeL
        err += kRangeL*Errs[i]
        print(pip+" >= %f: %i"%(rightbin,kRangeL))
    else:
        leftbin = bins[i]
        rightbin = bins[i+1]
        #kRangeL = t12.Draw(pip,pip+">= %f && "%(leftbin)+pip+"< %f"%(rightbin),"goff")
        kRangeL = t12.Draw(pip,pip+">= %f && "%(leftbin)+pip+"< %f && "%(rightbin)+exp,"goff")
        num += kRangeL
        eff += kRangeL*Effs[i]
        err += kRangeL*Errs[i]
        print("%f >= "%(leftbin)+pip+" < %f: %i"%(rightbin,kRangeL))
#total = t12.Draw(pip,"","goff")
total = t12.Draw(pip,exp,"goff")
frac = num/total
fraceff = eff/total
fracerr = err/total
print total
print frac
print fraceff
print fracerr
print("Total Systematic: %.4f"%(math.sqrt((frac*fracerr)**2 + (Errs[-1]*(1-frac))**2)))
