from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
#sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/allmfdtokpi.root","READ")
#f = TFile("/home/taylor/Research/root/allmfdtokpi.root","READ")
t = f.Get("dsprecontree")

deltam = RooRealVar("deltam","deltam",0.138,0.18)
nBins = 75
lb = deltam.getMin()
rb = deltam.getMax()
frame = deltam.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)

plot_variable(t,"deltam","mcflag == 2 && coskpiz>0.24 && cosdpipcm>0.985 && pipp<0.38","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From Charm MC and All Cuts Applied","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,frame,0.65,0.65,"/home/tkimmel/Research/plots/dtokpigeneric/deltamswithcuts")
plot_variable(t,"deltam","mcflag == 3 && coskpiz>0.24 && cosdpipcm>0.985 && pipp<0.38","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From Mixed MC and All Cuts Applied","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,frame,0.65,0.65,"/home/tkimmel/Research/plots/dtokpimixed/deltamswithcuts")
plot_variable(t,"deltam","mcflag == 4 && coskpiz>0.24 && cosdpipcm>0.985 && pipp<0.38","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From Charged MC and All Cuts Applied","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,frame,0.65,0.65,"/home/tkimmel/Research/plots/dtokpicharged/deltamswithcuts")
plot_variable(t,"deltam","mcflag == 5 && coskpiz>0.24 && cosdpipcm>0.985 && pipp<0.38","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From UDS MC and All Cuts Applied","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,frame,0.65,0.65,"/home/tkimmel/Research/plots/dtokpiuds/deltamswithcuts")
#plot_variable(t,"deltam","mcflag == 2 && coskpiz>0.24 && cosdpipcm>0.985 && pipp<0.38","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From Charm MC and All Cuts Applied","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,frame,0.65,0.65,"/home/taylor/Research/plots/dtokpigeneric/deltamswithcuts")
#plot_variable(t,"deltam","mcflag == 3 && coskpiz>0.24 && cosdpipcm>0.985 && pipp<0.38","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From Mixed MC and All Cuts Applied","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,frame,0.65,0.65,"/home/taylor/Research/plots/dtokpimixed/deltamswithcuts")
#plot_variable(t,"deltam","mcflag == 4 && coskpiz>0.24 && cosdpipcm>0.985 && pipp<0.38","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From Charged MC and All Cuts Applied","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,frame,0.65,0.65,"/home/taylor/Research/plots/dtokpicharged/deltamswithcuts")
#plot_variable(t,"deltam","mcflag == 5 && coskpiz>0.24 && cosdpipcm>0.985 && pipp<0.38","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From UDS MC and All Cuts Applied","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,frame,0.65,0.65,"/home/taylor/Research/plots/dtokpiuds/deltamswithcuts")
