from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/nbpi0/gmthetacms/expert.root","READ")
t = f.Get("experttree")

nn = RooRealVar("nn","nn",-1,1)
nBins = 100
lb = nn.getMin()
rb = nn.getMax()
frame = nn.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

plot_variable2histos(t,"nn","truth==1","Background","truth==0","Signal","From MC: #pi^{0} NeuroBayes Output","NB Output",h1,h2,frame,0.30,"/home/taylor/Research/plots/nbpi0/gmthetacms/35tm")
