from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/signalmfrecon.root","READ")
t = f.Get("dsprecontree")

coskpiz = RooRealVar("coskpiz", "coskpiz",-1,1)
cosdpipcm = RooRealVar("cosdpipcm", "cosdpipcm",-1,1)
pipp = RooRealVar("pipp", "pipp",0,1)
deltam = RooRealVar("deltam", "deltam", 0.138, 0.18)
nBins = 100
cklb = coskpiz.getMin()
ckub = coskpiz.getMax()
cdlb = cosdpipcm.getMax()
cdub = cosdpipcm.getMin()
pilb = pipp.getMin()
piub = pipp.getMax()
dllb = deltam.getMin()
dlub = deltam.getMax()

ckcd = TH2F("h2","h2",nBins,cklb,ckub,nBins,cdlb,cdub)
t.Draw("coskpiz:cosdpipcm>>ckcd")
cor = ckcd.GetCorrelationFactor()
#print("The correlation factor for %s and %s is %.5f"%("cos(#theta_{K#pi^{0}})","cos(#theta_{D^{0}#pi^{+}})",cor))
del ckcd
cor = ckcd.GetCorrelationFactor()
print("The correlation factor for %s and %s is %.5f"%("cos(#theta_{K#pi^{0}})","cos(#theta_{D^{0}#pi^{+}})",cor))
ckpi = TH2F("h2","h2",nBins,cklb,ckub,nBins,pilb,piub)
t.Draw("coskpiz:pipp>>ckpi")
#print("The correlation factor for %s and %s is %.5f"%("cos(#theta_{K#pi^{0}})","|p_{#pi^{+}}|",cor))
del ckpi
cor = ckpi.GetCorrelationFactor()
print("The correlation factor for %s and %s is %.5f"%("cos(#theta_{K#pi^{0}})","|p_{#pi^{+}}|",cor))
ckdl = TH2F("h2","h2",nBins,cklb,ckub,nBins,dllb,dlub)
t.Draw("coskpiz:deltam>>ckdl")
#print("The correlation factor for %s and %s is %.5f"%("cos(#theta_{K#pi^{0}})","#DeltaM_{D^{*+}D^{0}}",cor))
del ckdl
cor = ckdl.GetCorrelationFactor()
print("The correlation factor for %s and %s is %.5f"%("cos(#theta_{K#pi^{0}})","#DeltaM_{D^{*+}D^{0}}",cor))
cdpi = TH2F("h2","h2",nBins,cdlb,cdub,nBins,pilb,piub)
t.Draw("cosdpipcm:pipp>>cdpi")
#print("The correlation factor for %s and %s is %.5f"%("cos(#theta_{D^{0}#pi^{+}})","|p_{#pi^{+}}|",cor))
del cdpi
cor = cdpi.GetCorrelationFactor()
print("The correlation factor for %s and %s is %.5f"%("cos(#theta_{D^{0}#pi^{+}})","|p_{#pi^{+}}|",cor))
cddl = TH2F("h2","h2",nBins,cdlb,cdub,nBins,dllb,dlub)
t.Draw("cosdpipcm:deltam>>cddl")
#print("The correlation factor for %s and %s is %.5f"%("cos(#theta_{D^{0}#pi^{+}})","#DeltaM_{D^{*+}D^{0}}",cor))
del cddl
cor = cddl.GetCorrelationFactor()
print("The correlation factor for %s and %s is %.5f"%("cos(#theta_{D^{0}#pi^{+}})","#DeltaM_{D^{*+}D^{0}}",cor))
pidl = TH2F("h2","h2",nBins,pilb,piub,nBins,dllb,dlub)
t.Draw("pipp:deltam>>pidl")
#print("The correlation factor for %s and %s is %.5f"%("|p_{#pi^{+}}|","#DeltaM_{D^{*+}D^{0}}",cor))
del pidl
cor = pidl.GetCorrelationFactor()
print("The correlation factor for %s and %s is %.5f"%("|p_{#pi^{+}}|","#DeltaM_{D^{*+}D^{0}}",cor))


#plot_2d(t,"coskpiz","cosdpipcm","","COLZ","From MC: Title","XTitle","YTitle",h2,frame,0.65,"/home/taylor/Research/plots/tmklbothanglesplottest")
