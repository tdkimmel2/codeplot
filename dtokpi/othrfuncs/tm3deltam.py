from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/nomfdtokpi.root","READ")
t = f.Get("dsplrecontree")

deltam = RooRealVar("deltam","deltam",0.138,0.18)
nBins = 100
lb = deltam.getMin()
rb = deltam.getMax()
frame = deltam.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)
h3 = TH1F("h3","h3",nBins,lb,rb)

plot_variable3histos(rb,lb,t,"deltam","whomi>2","Truth Matched D^{*+}","whoru==1","Truth Matched #pi^{0}","klid==1","Truth Matched K^{0}_{L}","From MC: #DeltaM_{D^{*+}D^{0}}","#DeltaM (GeV/c^{2})",h1,h2,h3,frame,0.5,"/home/taylor/Research/plots/dtokpi/newtm3deltam")
