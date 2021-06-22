from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/nbvars.root","READ")
t = f.Get("pi0tree")

gm2eerror = RooRealVar("gm2eerror","gm2eerror",0,0.0001)

nBins = 100
lb = gm2eerror.getMin()
rb = gm2eerror.getMax()
frame = gm2eerror.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

plot_variable2histos(t,"gm2eerror","whomi==1","Signal","whomi!=1","Background","From All Generic MC: Error in the ECL of the Less Energetic Photon ","Error_{#gamma_{2}}",h1,h2,frame,0.59,0.66,"/home/tkimmel/Research/plots/nbpi0/nbvars/gm2eerror")
