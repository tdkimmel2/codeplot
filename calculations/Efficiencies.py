from ROOT import *
import sys
import math
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

#f = TFile("/home/tkimmel/Research/root/allmfrecon_noCuts.root","READ")
f = TFile("/home/tkimmel/Research/root/efficiencies/allmfrecon_gmcut.root","READ")
realtreel = f.Get("realdecayltree")
realtrees = f.Get("realdecaystree")
t = f.Get("dsrecontree")
t2 = f.Get("dslrecontree")

dm = "deltam"
mc = "mcflag"
dmcut = "deltam>0.139 && deltam<0.153"
cuts = ["deltam>0.139 && deltam<0.153","pi0mass>0.118998 && pi0mass<0.1489062","nb>0.832","bcsflag==1","heldr<0.178","heldz<0.819","dsPmag>2.765"]
cuts2 = ["deltam>0.139 && deltam<0.153","pi0mass>0.118998 && pi0mass<0.1489062","nb>0.832","bcsflag==1","heldr<0.178","heldz<0.819","dsPmag>2.765"]
#cuts = ["deltam>0.139 && deltam<0.153","egm2>0.06","pi0mass>0.118998 && pi0mass<0.1489062","nb>0.832","bcsflag==1","heldr<0.178","heldz<0.819","dsPmag>2.765"]
#cuts2 = ["deltam>0.139 && deltam<0.153","egm2>0.06","pi0mass>0.118998 && pi0mass<0.1489062","nb>0.832","bcsflag==1","heldr<0.178","heldz<0.819","dsPmag>2.765"]
#cuts = ["deltam>0.140 && deltam<0.152","egm2>0.06","pi0mass>0.118998 && pi0mass<0.1489062","nb>0.832","bcsflag==1","heldr<0.178","heldz<0.819","dsPmag>2.765"]
truth = "abs(dsflag)==1"

nTotl = realtreel.Draw(mc,"","goff")
nTots = realtrees.Draw(mc,"","goff")

cutstring=""
print("Cut  |Signal   |Figure of Merit |Efficiency  | Error")
for cut in cuts:
    cutstring+=cut
    nTot = t.Draw(dm,cutstring,"goff")
    nSig = t.Draw(dm,cutstring+" && "+truth,"goff")

    fom = float(nSig)/math.sqrt(float(nTot))
    eff = float(nSig)/float(nTots)

    sigerr = math.sqrt(float(nSig))
    toterr = math.sqrt(float(nTot))
    err = eff*math.sqrt((sigerr/float(nSig))**2 + (toterr/float(nTot))**2)
    print("%s   |%i     |%f     |%f     |%f"%(cut,nSig,fom,eff,err))
    print "\n"
    if cut!=cuts[-1]: cutstring+=" && "

print "\n"
print "\n"
print("Cut  |Signal   |Figure of Merit |Efficiency  | Error")
cutstring="kpP<3.5 && "
for cut in cuts2:
    cutstring+=cut
    nTot = t2.Draw(dm,cutstring,"goff")
    nSig = t2.Draw(dm,cutstring+" && "+truth,"goff")

    fom = float(nSig)/math.sqrt(float(nTot))
    eff = float(nSig)/float(nTots)

    sigerr = math.sqrt(float(nSig))
    toterr = math.sqrt(float(nTot))
    err = eff*math.sqrt((sigerr/float(nSig))**2 + (toterr/float(nTot))**2)
    print("%s   |%i     |%f     |%f     |%f"%(cut,nSig,fom,eff,err))
    print "\n"
    if cut!=cuts2[-1]: cutstring+=" && "
#print cutstring
