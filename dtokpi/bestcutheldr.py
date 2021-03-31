from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/allmfrecon_egmMpizCuts.root","READ")
t = f.Get("dsrecontree")

heldr = RooRealVar("heldr","heldr",0,0.3)
nBins = 100
lb = heldr.getMin()
rb = heldr.getMax()
frame = heldr.frame()
frame2 = heldr.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

OptimizeCut_LessThan(rb,lb,t,"heldr","abs(dsflag)","","From All Generic MC: #pi^{#pm} Helix dr","dr",h1,h2,frame,frame2,0.7,"/home/tkimmel/Research/plots/alldtokpi/bestcutheldr","std")
