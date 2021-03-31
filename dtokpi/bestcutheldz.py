from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/allmfrecon_egmMpizCuts.root","READ")
t = f.Get("dsrecontree")

heldz = RooRealVar("heldz","heldz",0,3)
nBins = 100
lb = heldz.getMin()
rb = heldz.getMax()
frame = heldz.frame()
frame2 = heldz.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

OptimizeCut_LessThan(rb,lb,t,"heldz","abs(dsflag)","","From All Generic MC: #pi^{#pm} Helix dz","dz",h1,h2,frame,frame2,0.7,"/home/tkimmel/Research/plots/alldtokpi/bestcutheldz","std")
