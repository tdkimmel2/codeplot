from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/mfsmallccset.root","READ")
t = f.Get("pi0tree")

mfchi2 = RooRealVar("mfchi2","mfchi2",0,50)

nBins = 100
lb = mfchi2.getMin()
rb = mfchi2.getMax()
frame = mfchi2.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

plot_variable(t,"mfchi2","","From Inclusive MC: Mass Fit #Chi^{2}","#Chi^{2}",h1,frame,0.65,0.65,"/home/taylor/Research/plots/nbpi0/mfchi2")
#plot_variable2histos(t,"mfchi2","whomi==1","Truth Matched","","All","From Inclusive MC: Truth Matched Mass Fit #Chi^{2}","#Chi^{2}",h1,h2,frame,0.65,0.65,"/home/taylor/Research/plots/nbpi0/mfchi2tm")
