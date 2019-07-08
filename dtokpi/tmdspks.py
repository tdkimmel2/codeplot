from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
#sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/allmfdtokpi.root","READ")
#f = TFile("/home/tkimmel/Research/root/genericmfdtokpi.root","READ")
#f = TFile("/home/taylor/Research/root/allmfdtokpi.root","READ")
#f = TFile("/home/taylor/Research/root/genericmfdtokpi.root","READ")
t = f.Get("dsprecontree")

deltam = RooRealVar("deltam","deltam",0.138,0.18)
#deltam = RooRealVar("deltam","deltam",0.143653,0.147379) #Three sigma window for Ks
nBins = 75
lb = deltam.getMin()
rb = deltam.getMax()
frame = deltam.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)
h3 = TH1F("h3","h3",nBins,lb,rb)

plot_variable2histos(rb,lb,t,"deltam","whomi>3","Truth Matched: ","","","Truth Matched #DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From All MC (No Cuts)","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,frame,0.175,0.7,"/home/tkimmel/Research/plots/alldtokpi/nocuttmks")
#plot_variable2histos(rb,lb,t,"deltam","whomi>3 && pipp<0.38","Truth Matched: ","pipp<0.38","","Truth Matched #DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From All MC (|#vec{p}_{#pi^{+}}| < 0.38)","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,frame,0.175,0.7,"/home/tkimmel/Research/plots/alldtokpi/pippcuttmks")
#plot_variable2histos(rb,lb,t,"deltam","whomi>3 && coskpiz>0.24","Truth Matched: ","coskpiz>0.24","","Truth Matched #DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From All MC (cos(#theta_{K^{0}#pi^{0}}) > 0.24)","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,frame,0.175,0.7,"/home/tkimmel/Research/plots/alldtokpi/coskpizcuttmks")
#plot_variable2histos(rb,lb,t,"deltam","whomi>3 && cosdpipcm>0.985","Truth Matched: ","cosdpipcm>0.985","","Truth Matched #DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From All MC (cos(#theta_{D^{0}#pi^{+}}) > 0.985)","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,frame,0.175,0.7,"/home/tkimmel/Research/plots/alldtokpi/cosdpipcuttmks")
#plot_variable2histos(rb,lb,t,"deltam","whomi>3 && dspPmag>3.2","Truth Matched: ","dspPmag>3.2","","Truth Matched #DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From All MC (|#vec{p}_{D^{*+}}| > 3.2)","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,frame,0.175,0.65,"/home/tkimmel/Research/plots/alldtokpi/dspPmagcuttmks")
#plot_variable2histos(rb,lb,t,"deltam","whomi>3 && coskpiz>0.24 && cosdpipcm>0.985","Truth Matched Both Angle Cuts: ","coskpiz>0.24 && cosdpipcm>0.985","Both Angle Cuts: ","Truth Matched #DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From All MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,frame,0.45,0.65,"/home/tkimmel/Research/plots/alldtokpi/coskpizcosdpipcutstmks")
#plot_variable2histos(rb,lb,t,"deltam","whomi>3 && pipp<0.38 && coskpiz>0.24 && cosdpipcm>0.985","Truth Matched: ","pipp<0.38 && coskpiz>0.24 && cosdpipcm>0.985","","Truth Matched #DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From All MC (All Cuts Except |#vec{p}_{D^{*+}}|)","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,frame,0.175,0.65,"/home/tkimmel/Research/plots/alldtokpi/allcutsexceptdspPmagtmks")
#plot_variable2histos(rb,lb,t,"deltam","whomi>3 && nb>0.54 && pipp<0.38 && coskpiz>0.24 && cosdpipcm>0.985 && dspPmag>3.2","Truth Matched: ","nb>0.54 && pipp<0.38 && coskpiz>0.24 && cosdpipcm>0.985 && dspPmag>3.2","","Truth Matched #DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From All MC (All Cuts)","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,frame,0.65,0.65,"/home/tkimmel/Research/plots/alldtokpi/allcutstmks")

#plot_variable2histos(rb,lb,t,"deltam","whomi>3 && pipp<0.38 && coskpiz>0.24 && cosdpipcm>0.985 && dspPmag>3.2","Truth Matched: ","pipp<0.38 && coskpiz>0.24 && cosdpipcm>0.985 && dspPmag>3.2","","Truth Matched #DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From All MC (All Cuts)","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,frame,0.575,0.65,"/home/tkimmel/Research/plots/recontest")

#plot_variable3histos(rb,lb,t,"deltam","whomi>3 && mcflag==2","Tight TM","whomi>0 && mcflag==2","Loose TM","mcflag==2","Total","Truth Matched #DeltaM_{D^{*+}D^{0}}  D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From Charm MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,h3,frame,0.7,0.6,"/home/tkimmel/Research/plots/dtokpigeneric/tmks")
#plot_variable3histos(rb,lb,t,"deltam","whomi>3 && mcflag==3","Tight TM","whomi>0 && mcflag==3","Loose TM","mcflag==3","Total","Truth Matched #DeltaM_{D^{*+}D^{0}}  D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From Mixed MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,h3,frame,0.7,0.6,"/home/tkimmel/Research/plots/dtokpimixed/tmks")
#plot_variable3histos(rb,lb,t,"deltam","whomi>3 && mcflag==4","Tight TM","whomi>0 && mcflag==4","Loose TM","mcflag==4","Total","Truth Matched #DeltaM_{D^{*+}D^{0}}  D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From Charged MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,h3,frame,0.7,0.6,"/home/tkimmel/Research/plots/dtokpicharged/tmks")
#plot_variable3histos(rb,lb,t,"deltam","whomi>3 && mcflag==5","Tight TM","whomi>0 && mcflag==5","Loose TM","mcflag==5","Total","Truth Matched #DeltaM_{D^{*+}D^{0}}  D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From UDS MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,h3,frame,0.7,0.6,"/home/tkimmel/Research/plots/dtokpiuds/tmks")

#plot_variable2histos(rb,lb,t,"deltam","whomi>3","Truth Matched","","No Cut","Truth Matched #DeltaM_{D^{*+}D^{0}}  D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From All MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,frame,0.7,0.6,"/home/tkimmel/Research/plots/alldtokpi/tmks")
#plot_variable3histos(rb,lb,t,"deltam","whomi>3 && mcflag==2","Tight TM","whomi>0 && mcflag==2","Loose TM","mcflag==2","Total","Truth Matched #DeltaM_{D^{*+}D^{0}}  D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From Charm MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,h3,frame,0.7,0.6,"/home/taylor/Research/plots/dtokpigeneric/tmks")
#plot_variable3histos(rb,lb,t,"deltam","whomi>3 && mcflag==3","Tight TM","whomi>0 && mcflag==3","Loose TM","mcflag==3","Total","Truth Matched #DeltaM_{D^{*+}D^{0}}  D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From Mixed MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,h3,frame,0.7,0.6,"/home/taylor/Research/plots/dtokpimixed/tmks")
#plot_variable3histos(rb,lb,t,"deltam","whomi>3 && mcflag==4","Tight TM","whomi>0 && mcflag==4","Loose TM","mcflag==4","Total","Truth Matched #DeltaM_{D^{*+}D^{0}}  D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From Charged MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,h3,frame,0.7,0.6,"/home/taylor/Research/plots/dtokpicharged/tmks")
#plot_variable3histos(rb,lb,t,"deltam","whomi>3 && mcflag==5","Tight TM","whomi>0 && mcflag==5","Loose TM","mcflag==5","Total","Truth Matched #DeltaM_{D^{*+}D^{0}}  D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From UDS MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,h3,frame,0.7,0.6,"/home/taylor/Research/plots/dtokpiuds/tmks")

#plot_variable2histos(rb,lb,t,"deltam","whomi>3","Truth Matched No Cuts: ","","No Cuts: ","Truth Matched #DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From All MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,frame,0.45,0.3,"/home/taylor/Research/plots/alldtokpi/nocuttmks")
#plot_variable2histos(rb,lb,t,"deltam","whomi>3 && pipp<0.38","Truth Matched |#vec{p}_{#pi^{+}}| < 0.38: ","pipp<0.38","|#vec{p}_{#pi^{+}}| < 0.38: ","Truth Matched #DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From All MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,frame,0.45,0.3,"/home/taylor/Research/plots/alldtokpi/pippcuttmks")
#plot_variable2histos(rb,lb,t,"deltam","whomi>3 && coskpiz>0.24","Truth Matched cos(#theta_{K^{0}#pi^{0}}) > 0.24: ","coskpiz>0.24","cos(#theta_{K^{0}#pi^{0}}) > 0.24: ","Truth Matched #DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From All MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,frame,0.45,0.3,"/home/taylor/Research/plots/alldtokpi/coskpizcuttmks")
#plot_variable2histos(rb,lb,t,"deltam","whomi>3 && cosdpipcm>0.985","Truth Matched cos(#theta_{D^{0}#pi^{+}}) > 0.985: ","cosdpipcm>0.985","cos(#theta_{D^{0}#pi^{+}}) > 0.985: ","Truth Matched #DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From All MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,frame,0.45,0.3,"/home/taylor/Research/plots/alldtokpi/cosdpipcuttmks")
#plot_variable2histos(rb,lb,t,"deltam","whomi>3 && dspPmag>3.2","Truth Matched |#vec{p}_{#D^{*+}}| > 3.2: ","dspPmag>3.2","|#vec{p}_{#D^{*+}}| > 3.2: ","Truth Matched #DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From All MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,frame,0.45,0.3,"/home/taylor/Research/plots/alldtokpi/dspPmagcuttmks")
#plot_variable2histos(rb,lb,t,"deltam","whomi>3 && coskpiz>0.24 && cosdpipcm>0.985","Truth Matched Both Angle Cuts: ","coskpiz>0.24 && cosdpipcm>0.985","Both Angle Cuts: ","Truth Matched #DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From All MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,frame,0.45,0.2,"/home/taylor/Research/plots/alldtokpi/coskpizcosdpipcutstmks")
#plot_variable2histos(rb,lb,t,"deltam","whomi>3 && pipp<0.38 && coskpiz>0.24 && cosdpipcm>0.985","Truth Matched All Cuts Except |#vec{p}_{#D^{*+}}|: ","pipp<0.38 && coskpiz>0.24 && cosdpipcm>0.985","All Cuts Except |#vec{p}_{#D^{*+}}|: ","Truth Matched #DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From All MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,frame,0.45,0.65,"/home/taylor/Research/plots/alldtokpi/allcutsexceptdspPmagtmks")
#plot_variable2histos(rb,lb,t,"deltam","whomi>3 && pipp<0.38 && coskpiz>0.24 && cosdpipcm>0.985 && dspPmag>3.2","Truth Matched All Cuts: ","pipp<0.38 && coskpiz>0.24 && cosdpipcm>0.985 && dspPmag>3.2","All Cuts: ","Truth Matched #DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From All MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,frame,0.55,0.65,"/home/taylor/Research/plots/alldtokpi/allcutstmks")
