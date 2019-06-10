from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
#sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/allmfdtokpi.root","READ")
#f = TFile("/home/taylor/Research/root/allmfdtokpi.root","READ")
t = f.Get("dsprecontree")

deltam = RooRealVar("deltam","deltam",0.138,0.18)
nBins = 100
lb = deltam.getMin()
rb = deltam.getMax()
frame = deltam.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)
h3 = TH1F("h3","h3",nBins,lb,rb)
h4 = TH1F("h4","h4",nBins,lb,rb)
h5 = TH1F("h5","h5",nBins,lb,rb)

plot_variable5histos(rb,lb,t,"deltam","mcflag==1 && coskpiz>0.24 && cosdpipcm>0.985 && pipp<0.38","Inclusive MC","mcflag==2 && coskpiz>0.24 && cosdpipcm>0.985 && pipp<0.38","Charm MC","mcflag==3 && coskpiz>0.24 && cosdpipcm>0.985 && pipp<0.38","Mixed MC","mcflag==4 && coskpiz>0.24 && cosdpipcm>0.985 && pipp<0.38","Charged MC","mcflag==5 && coskpiz>0.24 && cosdpipcm>0.985 && pipp<0.38","UDS MC","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From All MC and All Cuts Applied","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,h3,h4,h5,frame,0.65,0.65,"/home/tkimmel/Research/plots/alldtokpi/alldeltamswithcuts")
#plot_variable5histos(rb,lb,t,"deltam","mcflag==1 && coskpiz>0.24 && cosdpipcm>0.985 && pipp<0.38","Inclusive MC","mcflag==2 && coskpiz>0.24 && cosdpipcm>0.985 && pipp<0.38","Charm MC","mcflag==3 && coskpiz>0.24 && cosdpipcm>0.985 && pipp<0.38","Mixed MC","mcflag==4 && coskpiz>0.24 && cosdpipcm>0.985 && pipp<0.38","Charged MC","mcflag==5 && coskpiz>0.24 && cosdpipcm>0.985 && pipp<0.38","UDS MC","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From All MC and All Cuts Applied","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,h3,h4,h5,frame,0.65,0.65,"/home/taylor/Research/plots/alldtokpi/alldeltamswithcuts")
