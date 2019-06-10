from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
#sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/allmfdtokpi.root","READ")
#f = TFile("/home/taylor/Research/root/allmfdtokpi.root","READ")
t = f.Get("dsplrecontree")

deltam = RooRealVar("deltam","deltam",0.138,0.18)
nBins = 75
lb = deltam.getMin()
rb = deltam.getMax()
frame = deltam.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)
h3 = TH1F("h3","h3",nBins,lb,rb)

plot_variable3histos(rb,lb,t,"deltam","whomi>3 && mcflag==2","Tight TM","whomi>0 && mcflag==2","Loose TM","mcflag==2","Total","Truth Matched #DeltaM_{D^{*+}D^{0}}  D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From Charm MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,h3,frame,0.7,0.6,"/home/tkimmel/Research/plots/dtokpigeneric/tmks")
plot_variable3histos(rb,lb,t,"deltam","whomi>3 && mcflag==3","Tight TM","whomi>0 && mcflag==3","Loose TM","mcflag==3","Total","Truth Matched #DeltaM_{D^{*+}D^{0}}  D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From Mixed MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,h3,frame,0.7,0.6,"/home/tkimmel/Research/plots/dtokpimixed/tmks")
plot_variable3histos(rb,lb,t,"deltam","whomi>3 && mcflag==4","Tight TM","whomi>0 && mcflag==4","Loose TM","mcflag==4","Total","Truth Matched #DeltaM_{D^{*+}D^{0}}  D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From Charged MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,h3,frame,0.7,0.6,"/home/tkimmel/Research/plots/dtokpicharged/tmks")
plot_variable3histos(rb,lb,t,"deltam","whomi>3 && mcflag==5","Tight TM","whomi>0 && mcflag==5","Loose TM","mcflag==5","Total","Truth Matched #DeltaM_{D^{*+}D^{0}}  D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From UDS MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,h3,frame,0.7,0.6,"/home/tkimmel/Research/plots/dtokpiuds/tmks")
#plot_variable3histos(rb,lb,t,"deltam","whomi>3 && mcflag==2","Tight TM","whomi>0 && mcflag==2","Loose TM","mcflag==2","Total","Truth Matched #DeltaM_{D^{*+}D^{0}}  D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From Charm MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,h3,frame,0.7,0.6,"/home/taylor/Research/plots/dtokpigeneric/tmks")
#plot_variable3histos(rb,lb,t,"deltam","whomi>3 && mcflag==3","Tight TM","whomi>0 && mcflag==3","Loose TM","mcflag==3","Total","Truth Matched #DeltaM_{D^{*+}D^{0}}  D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From Mixed MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,h3,frame,0.7,0.6,"/home/taylor/Research/plots/dtokpimixed/tmks")
#plot_variable3histos(rb,lb,t,"deltam","whomi>3 && mcflag==4","Tight TM","whomi>0 && mcflag==4","Loose TM","mcflag==4","Total","Truth Matched #DeltaM_{D^{*+}D^{0}}  D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From Charged MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,h3,frame,0.7,0.6,"/home/taylor/Research/plots/dtokpicharged/tmks")
#plot_variable3histos(rb,lb,t,"deltam","whomi>3 && mcflag==5","Tight TM","whomi>0 && mcflag==5","Loose TM","mcflag==5","Total","Truth Matched #DeltaM_{D^{*+}D^{0}}  D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From UDS MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,h3,frame,0.7,0.6,"/home/taylor/Research/plots/dtokpiuds/tmks")
