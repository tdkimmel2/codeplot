from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/allmfrecon_kpi.root","READ")
t = f.Get("chargedkpi")

prob_kpi = RooRealVar("prob_kpi","prob_kpi",0,1)

nBins = 100
lb = prob_kpi.getMin()
rb = prob_kpi.getMax()
frame = prob_kpi.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

plot_variable(t,"prob_kpi","","Kaon:Pion Probability: From All Generic MC","K:#pi Probability",h1,frame,0.65,0.25,"/home/tkimmel/Research/plots/prob_kpi")
