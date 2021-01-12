from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/expert.root","READ")
t = f.Get("experttree")

nn = RooRealVar("nn","nn",-1,1)
nBins = 100
lb = nn.getMin()
rb = nn.getMax()
frame = nn.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

plot_variable2histos(t,"nn","truth==1","Signal","truth==0","Background","#pi^{0} Neurobayes Expert Output","NB Output",h1,h2,frame,0.45,0.5,"/home/tkimmel/Research/plots/nbpi0/expertplot")
