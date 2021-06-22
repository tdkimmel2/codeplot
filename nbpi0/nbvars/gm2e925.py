from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/nbvars.root","READ")
t = f.Get("pi0tree")

gm2e925 = RooRealVar("gm2e925","gm2e925",0.75,1)

nBins = 100
lb = gm2e925.getMin()
rb = gm2e925.getMax()
frame = gm2e925.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

#plot_variable2histos(t,"gm2e925","whomi==1","Signal","whomi!=1","Background","From All Generic MC: #frac{E_{9}}{E_{25}} of the Less Energetic Photon ","#frac{E_{9}}{E_{25}}_{#gamma_{2}}",h1,h2,frame,0.25,0.65,"/home/tkimmel/Research/plots/nbpi0/nbvars/gm2e925")
plot_variable2histos(t,"gm2e925","whomi==1","Signal","whomi!=1","Background","From All Generic MC: E_{9}/E_{25} of the Less Energetic Photon ","E_{9}/E_{25}_{#gamma_{2}}",h1,h2,frame,0.17,0.66,"/home/tkimmel/Research/plots/nbpi0/nbvars/gm2e925")
