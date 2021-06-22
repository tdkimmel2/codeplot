from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/nbvars.root","READ")
t = f.Get("pi0tree")

gm2p3cms = RooRealVar("gm2p3cms","gm2p3cms",0,1)

nBins = 100
lb = gm2p3cms.getMin()
rb = gm2p3cms.getMax()
frame = gm2p3cms.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

plot_variable2histos(t,"gm2p3cms","whomi==1","Signal","whomi!=1","Background","From All Generic MC: Magnitude of the Less Energetic Photon's 3-Momentum in the CMS Frame","|#vec{p}_{#gamma_{2}}^{CMS}|",h1,h2,frame,0.59,0.66,"/home/tkimmel/Research/plots/nbpi0/nbvars/gm2p3cms")
