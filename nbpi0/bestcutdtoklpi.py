from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/nonbcutdtokpi.root","READ")
t = f.Get("dsplrecontree")

nb = RooRealVar("nb","nb",-1,1)
nBins = 100
lb = nb.getMin()
rb = nb.getMax()
frame = nb.frame()
frame2 = nb.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

OptimizeCut_GreaterThan(rb,lb,t,"nb","whomi","deltam<0.1481 && deltam>0.1428 && ","From MC: #pi^{0} Neurobayes Output","NB Output",h1,h2,frame,frame2,0.5,"/home/taylor/Research/plots/nbpi0/klpunzioptimalcutdsp")
