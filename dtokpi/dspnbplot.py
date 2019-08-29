from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/inclusivemfreconnb.root","READ")
t = f.Get("dsprecontree")
#t = f.Get("dsplrecontree")

dnb = RooRealVar("dnb","dnb",-1,1)
nBins = 100
lb = dnb.getMin()
rb = dnb.getMax()
frame = dnb.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)

plot_variable(t,"dnb","","From MC: D^{*+} NeuroBayes Output","D^{*+} NB",h1,frame,0.5,0.6,"/home/taylor/Research/plots/dtokpiinclusive/ksdspnbplot")
#plot_variable(t,"dnb","whomi>3","From MC: Truth Matched D^{*+} NeuroBayes Output","D^{*+} NB",h1,frame,0.5,0.6,"/home/taylor/Research/plots/dtokpiinclusive/kssigdspnbplot")
#plot_variable(t,"dnb","whomi<4","From MC: Background D^{*+} NeuroBayes Output","D^{*+} NB",h1,frame,0.5,0.6,"/home/taylor/Research/plots/dtokpiinclusive/ksbkgdspnbplot")
