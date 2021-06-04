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

print("KLONG MODE")
for i in range(len(bins)-1):
    leftbin = bins[i]
    rightbin = bins[i+1]
    kRangeL = t12.Draw(kp,kp+">= %f && "%(leftbin)+kp+"< %f"%(rightbin),"goff")
    print("%f >= "%(leftbin)+kp+" < %f: %i"%(rightbin,kRangeL))


print("KSHORT MODE")
for i in range(len(bins)-1):
    leftbin = bins[i]
    rightbin = bins[i+1]
    kRangeL = t11.Draw(kp,kp+">= %f && "%(leftbin)+kp+"< %f"%(rightbin),"goff")
    print("%f >= "%(leftbin)+kp+" < %f: %i"%(rightbin,kRangeL))


print("TRUTH MATCHED")
print("KLONG MODE")
for i in range(len(bins)-1):
    leftbin = bins[i]
    rightbin = bins[i+1]
    kRangeL = t12.Draw(kp,kp+">= %f && "%(leftbin)+kp+"< %f && "%(rightbin)+truth,"goff")
    print("%f >= "%(leftbin)+kp+" < %f: %i"%(rightbin,kRangeL))


print("KSHORT MODE")
for i in range(len(bins)-1):
    leftbin = bins[i]
    rightbin = bins[i+1]
    kRangeL = t11.Draw(kp,kp+">= %f && "%(leftbin)+kp+"< %f && "%(rightbin)+truth,"goff")
    print("%f >= "%(leftbin)+kp+" < %f: %i"%(rightbin,kRangeL))

print("Efficiency MC")
num=float(0)
for i in range(len(bins)-1):
    leftbin = bins[i]
    rightbin = bins[i+1]
    kRangeL = t12.Draw(kp,kp+">= %f && "%(leftbin)+kp+"< %f && "%(rightbin)+truth,"goff")
    total = t12.Draw(kp,kp+"<%i && "%(bins[-1])+truth,"goff")
    num += kRangeL*Effs[i]
print num/total

print("Efficiency Data")
num=float(0)
for i in range(len(bins)-1):
    leftbin = bins[i]
    rightbin = bins[i+1]
    kRangeL = t22.Draw(kp,kp+">= %f && "%(leftbin)+kp+"< %f && "%(rightbin)+truth,"goff")
    total = t22.Draw(kp,kp+"<%i && "%(bins[-1])+truth,"goff")
    num += kRangeL*Effs[i]
print num/total

print("KLONG MODE MC DATA DIFF")
for i in range(len(bins)-1):
    leftbin = bins[i]
    rightbin = bins[i+1]
    totalmc = t12.Draw(kp,kp+"<3.5","goff")
    totald = t22.Draw(kp,kp+"<3.5","goff")
    kRangeLmc = t12.Draw(kp,kp+">= %f && "%(leftbin)+kp+"< %f"%(rightbin),"goff")
    kRangeLd = t22.Draw(kp,kp+">= %f && "%(leftbin)+kp+"< %f"%(rightbin),"goff")
    fracmc = float(kRangeLmc)/totalmc
    errRmc = math.sqrt(kRangeLmc)
    errTmc = math.sqrt(totalmc)
    fracd = float(kRangeLd)/totald
    errRd = math.sqrt(kRangeLd)
    errTd = math.sqrt(totald)
    #print fracmc
    #print fracd
    diff = fracmc - fracd
    err = math.sqrt((errRmc/kRangeLmc)**2 + (errTmc/totalmc)**2 + (errRd/kRangeLd)**2 + (errTd/totald)**2)
    #print("%f >= "%(leftbin)+kp+" < %f: %f pm %f"%(rightbin,diff,err))
    print("%f >= "%(leftbin)+kp+" < %f: %f"%(rightbin,diff))

"""
dwindow="deltam > 0.141938 && deltam < 0.148838"
num=float(0)
for i in range(len(bins)-1):
    leftbin = bins[i]
    rightbin = bins[i+1]
    kRangeL = t12.Draw(kp,kp+">= %f && "%(leftbin)+kp+"< %f && "%(rightbin)+truth+" && "+dwindow,"goff")
    total = t12.Draw(kp,kp+"<%i && "%(bins[-1])+truth+" && "+dwindow,"goff")
    num += kRangeL*Effs[i]
print num/total
"""
