from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/klsignalmfrecon.root","READ")
#f = TFile("/home/tkimmel/Research/root/kssignalmfrecon.root","READ")
#f = TFile("/home/tkimmel/Research/root/allmfrecon.root","READ")

#t1 = f.Get("dsrecontree")
t1 = f.Get("dslrecontree")

f2 = TFile("/home/tkimmel/Research/root/b2biiklsignalmfrecon.root","READ")
#f2 = TFile("/home/tkimmel/Research/root/b2biikssignalmfrecon.root","READ")
#f2 = TFile("/home/tkimmel/Research/root/b2biiallmfrecon.root","READ")

#t2 = f2.Get("dsprecontree")
#t3 = f2.Get("dsmrecontree")
t2 = f2.Get("dsplrecontree")
t3 = f2.Get("dsmlrecontree")

tlist = TList()
tlist.Add(t2)
tlist.Add(t3)
t4 = TTree.MergeTrees(tlist)

deltam = RooRealVar("deltam","deltam",0.138,0.18)
#nb = RooRealVar("nb","nb",-1,1)
nBins = 75
lb = deltam.getMin()
rb = deltam.getMax()
frame = deltam.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

# KL Signal MC
plot_variable2trees(t1,t4,"deltam","","BASF","","B2BII","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From K_{L}^{0} Signal Monte Carlo","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,frame,0.55,0.55,"/home/tkimmel/Research/plots/b2biiCompare/klSigNoCuts")
#plot_variable2trees(t1,t4,"deltam","abs(dsflag)==1","BASF","abs(dsflag)==1","B2BII","Truth Matched #DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From K_{L}^{0} Signal Monte Carlo","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,frame,0.55,0.65,"/home/tkimmel/Research/plots/b2biiCompare/klSigTM")

# KS Signal MC
#plot_variable2trees(t1,t4,"deltam","","BASF","","B2BII","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K_{S}^{0} Signal Monte Carlo","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,frame,0.35,0.55,"/home/tkimmel/Research/plots/b2biiCompare/ksSigNoCuts")
#plot_variable2trees(t1,t4,"deltam","abs(dsflag)==1","BASF","abs(dsflag)==1","B2BII","Truth Matched #DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K_{L}^{0} Signal Monte Carlo","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,frame,0.35,0.55,"/home/tkimmel/Research/plots/b2biiCompare/ksSigTM")

# All Generic MC
#plot_variable2trees(t1,t4,"deltam","","BASF","","B2BII","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From All Generic Monte Carlo","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,frame,0.15,0.6,"/home/tkimmel/Research/plots/b2biiCompare/genericNoCuts")
#plot_variable2trees(t1,t4,"deltam","abs(dsflag)==1","BASF","abs(dsflag)==1","B2BII","Truth Matched #DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From All Generic Monte Carlo","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,frame,0.35,0.55,"/home/tkimmel/Research/plots/b2biiCompare/genericTM")
