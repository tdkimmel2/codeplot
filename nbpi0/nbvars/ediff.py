from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/nbvars.root","READ")
t = f.Get("pi0tree")

ediff = RooRealVar("ediff","ediff",0,0.5)

nBins = 100
lb = ediff.getMin()
rb = ediff.getMax()
frame = ediff.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

plot_variable2histos(t,"ediff","whomi==1","Signal","whomi!=1","Background","From All Generic MC: Difference Between the Photon Energies","#DeltaE_{#gamma_{1}#gamma_{2}}",h1,h2,frame,0.59,0.66,"/home/tkimmel/Research/plots/nbpi0/nbvars/ediff")
