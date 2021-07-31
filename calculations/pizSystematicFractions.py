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
f = TFile("/home/tkimmel/Research/root/fullStream.root","READ")
#f = TFile("/home/tkimmel/Research/root/partialData.root","READ")
t11 = f.Get("dsrecontree")
t12 = f.Get("dslrecontree")
#t21 = f2.Get("dsrecontree")
#t22 = f2.Get("dslrecontree")

piz = "pizP"
mc = "mcflag"
truth = "abs(dsflag)==1"
exp = "exp!=43"

bins=[1.0,1.25,1.625,2.0,2.375,2.75,3.125,3.5]
Effs = [0.9578,0.9613,1.0014,1.0361,1.0995,1.2202,1.1646,1.4163]
StatErrs = [0.0086,0.0069,0.0099,0.0156,0.0255,0.0452,0.0578,0.0648]
SysErrs = [0.0020,0.0001,0.0005,0.0010,0.0012,0.0306,0.0300,0.0037]

print("KS Pizs")
num=float(0)
eff=float(0)
err=float(0)
for i in range(len(bins)):
    if i == len(bins)-1:
        #continue
        rightbin = bins[i]
        #kRangeL = t11.Draw(piz,piz+">= %f"%(rightbin),"goff")
        kRangeL = t11.Draw(piz,piz+">= %f && "%(rightbin)+exp,"goff")
        eff += kRangeL*Effs[i]
        num += kRangeL
        err += kRangeL*math.sqrt(StatErrs[i]*StatErrs[i] + SysErrs[i]*SysErrs[i])
        print(piz+" >= %f: %i"%(rightbin,kRangeL))
    else:
        leftbin = bins[i]
        rightbin = bins[i+1]
        #kRangeL = t11.Draw(piz,piz+">= %f && "%(leftbin)+piz+"< %f"%(rightbin),"goff")
        kRangeL = t11.Draw(piz,piz+">= %f && "%(leftbin)+piz+"< %f && "%(rightbin)+exp,"goff")
        num += kRangeL
        eff += kRangeL*Effs[i]
        err += kRangeL*math.sqrt(StatErrs[i]*StatErrs[i] + SysErrs[i]*SysErrs[i])
        print("%f >= "%(leftbin)+piz+" < %f: %i"%(rightbin,kRangeL))
#total = t11.Draw(piz,"pizP>=1","goff")
total = t11.Draw(piz,"pizP>=1 && "+exp,"goff")
frac = num/total
fraceff = eff/total
fracerr = err/total
print frac
print fraceff
print fracerr
print("Total Systematic: %.4f"%(frac*fracerr + math.sqrt(SysErrs[-1]*SysErrs[-1] + StatErrs[-1]*StatErrs[-1])*(1-frac)))

print("\nKL Pizs")
num=float(0)
eff=float(0)
err=float(0)
for i in range(len(bins)):
    if i == len(bins)-1:
        #continue
        rightbin = bins[i]
        #kRangeL = t12.Draw(piz,piz+">= %f"%(rightbin),"goff")
        kRangeL = t12.Draw(piz,piz+">= %f && "%(rightbin)+exp,"goff")
        eff += kRangeL*Effs[i]
        num += kRangeL
        err += kRangeL*math.sqrt(StatErrs[i]*StatErrs[i] + SysErrs[i]*SysErrs[i])
        print(piz+" >= %f: %i"%(rightbin,kRangeL))
    else:
        leftbin = bins[i]
        rightbin = bins[i+1]
        #kRangeL = t12.Draw(piz,piz+">= %f && "%(leftbin)+piz+"< %f"%(rightbin),"goff")
        kRangeL = t12.Draw(piz,piz+">= %f && "%(leftbin)+piz+"< %f && "%(rightbin)+exp,"goff")
        num += kRangeL
        eff += kRangeL*Effs[i]
        err += kRangeL*math.sqrt(StatErrs[i]*StatErrs[i] + SysErrs[i]*SysErrs[i])
        print("%f >= "%(leftbin)+piz+" < %f: %i"%(rightbin,kRangeL))
#total = t12.Draw(piz,"pizP>=1","goff")
total = t12.Draw(piz,"pizP>=1 && "+exp,"goff")
frac = num/total
fraceff = eff/total
fracerr = err/total
print frac
print fraceff
print fracerr
print("Total Systematic: %.4f"%(frac*fracerr + math.sqrt(SysErrs[-1]*SysErrs[-1] + StatErrs[-1]*StatErrs[-1])*(1-frac)))
