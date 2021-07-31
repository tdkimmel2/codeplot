from ROOT import *
import sys
import math
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

#f = TFile("/home/tkimmel/Research/root/partialMC.root","READ")
#f2 = TFile("/home/tkimmel/Research/root/partialData.root","READ")
#f = TFile("/home/tkimmel/Research/root/systematics/dsSystematics.root","READ")
#f = TFile("/home/tkimmel/Research/root/systematics/dsSystematicsData.root","READ")
f = TFile("/home/tkimmel/Research/root/fullStream.root","READ")
#f = TFile("/home/tkimmel/Research/root/partialData.root","READ")
t11 = f.Get("dsrecontree")
t12 = f.Get("dslrecontree")
#t21 = f2.Get("dsrecontree")
#t22 = f2.Get("dslrecontree")

kp = "kpP"
mc = "mcflag"
truth = "abs(dsflag)==1"
ecl = "klmecl"
#exp = "exp==43"
exp = "exp!=43"

bins = [0,0.5,0.625,0.75,0.875,1.0,1.25,1.5,1.75,2,2.5,3.5]
Effs = [0.678,0.392,0.385,0.377,0.464,0.477,0.488,0.511,0.556,0.694,0.208]
Errs = [0.101,0.042,0.034,0.032,0.037,0.032,0.035,0.045,0.063,0.088,0.097]
EclEffs = [0.000,0.333,0.334,0.327,0.292,0.253,0.286,0.333,0.326,0.280,0.466]
EclErrs = [0.361,0.093,0.065,0.051,0.044,0.026,0.031,0.037,0.047,0.049,0.146]

binsS = [0,0.5,1.0,1.5,2.0,2.5,3.0,3.5]
EffsS = [0.9421,0.9778,0.9831,0.9828,0.9833,0.9833,1.0024,0.9848]
ErrsS = [0.0192,0.0091,0.0073,0.0070,0.0078,0.0096,0.0129,0.0135]

print("KLONG MODE")
numkl=float(0)
errkl=float(0)
#for i in range(len(bins)):
for i in range(len(bins)-1):
    """
    if i == len(bins)-1:
        rightbin = bins[i]
        kRangeL = t12.Draw(kp,kp+">= %f"%(rightbin)+" && "+ecl+"==0","goff")
        numkl += kRangeL*Effs[i-1]
        errkl += kRangeL*Errs[i-1]
    else:
    """
    leftbin = bins[i]
    rightbin = bins[i+1]
    #kRangeL = t12.Draw(kp,kp+">= %f && "%(leftbin)+kp+"< %f"%(rightbin)+" && "+ecl+"==0","goff")
    kRangeL = t12.Draw(kp,kp+">= %f && "%(leftbin)+kp+"< %f"%(rightbin)+" && "+ecl+"==0 && "+exp,"goff")
    numkl += kRangeL*Effs[i]
    errkl += kRangeL*Errs[i]
    print("%f >= "%(leftbin)+kp+" < %f: %i"%(rightbin,kRangeL))
#totalkl = t12.Draw(kp,ecl+"==0 && "+kp+"<%i"%(bins[-1]),"goff")
totalkl = t12.Draw(kp,ecl+"==0 && "+kp+"<%i && "%(bins[-1])+exp,"goff")
print("Weighted Efficiency KLM KLongs: %.4f"%(numkl/totalkl))
print("Weighted Systematic KLM KLongs: %.4f"%(errkl/totalkl))

numecl=float(0)
errecl=float(0)
#for i in range(len(bins)):
for i in range(len(bins)-1):
    """
    if i == len(bins)-1:
        rightbin = bins[i]
        kRangeL = t12.Draw(kp,kp+">= %f"%(rightbin)+" && "+ecl+"==1","goff")
        numecl += kRangeL*EclEffs[i-1]
        errecl += kRangeL*EclErrs[i-1]
    else:
    """
    leftbin = bins[i]
    rightbin = bins[i+1]
    #kRangeL = t12.Draw(kp,kp+">= %f && "%(leftbin)+kp+"< %f"%(rightbin)+" && "+ecl+"==1","goff")
    kRangeL = t12.Draw(kp,kp+">= %f && "%(leftbin)+kp+"< %f"%(rightbin)+" && "+ecl+"==1 && "+exp,"goff")
    numecl += kRangeL*EclEffs[i]
    errecl += kRangeL*EclErrs[i]
    print("%f >= "%(leftbin)+kp+" < %f: %i"%(rightbin,kRangeL))
#totalecl = t12.Draw(kp,ecl+"==1 && "+kp+"<%i"%(bins[-1]),"goff")
totalecl = t12.Draw(kp,ecl+"==1 && "+kp+"<%i && "%(bins[-1])+exp,"goff")
print("Weighted Efficiency KLMECL KLongs: %.4f"%(numecl/totalecl))
print("Weighted Systematic KLMECL KLongs: %.4f"%(errecl/totalecl))

total = totalecl + totalkl
num = numkl + numecl
err = errkl + errecl
#total = t12.Draw(kp,kp+"<%f"%(bins[-1]),"goff")
print("Weighted Efficiency: %.4f"%(num/total))
print("Weighted Systematic: %.4f"%(err/total))


print("KSHORT MODE")
total=float(0)
num=float(0)
err=float(0)
for i in range(len(binsS)):
    if i == len(binsS)-1:
        rightbin = binsS[i]
        kRangeS = t11.Draw(kp,kp+">= %f"%(rightbin),"goff")
        print(kp+" >= %f: %i"%(rightbin,kRangeS))
    else:
        leftbin = binsS[i]
        rightbin = binsS[i+1]
        kRangeS = t11.Draw(kp,kp+">= %f && "%(leftbin)+kp+"< %f"%(rightbin),"goff")
        print("%f >= "%(leftbin)+kp+" < %f: %i"%(rightbin,kRangeS))
    #total+= kRangeS
    num += kRangeS*EffsS[i]
    err += kRangeS*ErrsS[i]
#total = t11.Draw(kp,kp+"<%i"%(bins[-1]),"goff")
total = t11.Draw(kp,"","goff")
print("Weighted Efficiency: %.4f"%(num/total))
print("Weighted Systematic: %.4f"%(err/total))
