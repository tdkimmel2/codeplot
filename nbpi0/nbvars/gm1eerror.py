from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/nbvars.root","READ")
t = f.Get("pi0tree")

gm1eerror = RooRealVar("gm1eerror","gm1eerror",0,0.0002)

nBins = 100
lb = gm1eerror.getMin()
rb = gm1eerror.getMax()
frame = gm1eerror.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

plot_variable2histos(t,"gm1eerror","whomi==1","Signal","whomi!=1","Background","From All Generic MC: Error in the ECL of the More Energetic Photon ","Error_{#gamma_{1}}",h1,h2,frame,0.59,0.66,"/home/tkimmel/Research/plots/nbpi0/nbvars/gm1eerror")
