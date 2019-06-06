#from ROOT import TFile, TCanvas, TTree
from ROOT import *
import sys
#gSystem.Load("libCintex.so")
#Cintex.Enable()
#gSystem.Load("$SRT_PUBLIC_CONTEXT/lib/Linux2.6-GCC-debug/libStandardRecord_dict.so")
#gInterpreter.AddIncludePath("$SRT_PUBLIC_CONTEXT")

c1 = TCanvas( 'c1', 'c1', 200, 10, 700, 500 )
#c1.SetLogy()
f="/home/Taylor/Research/root/dsprecon.root"
sample=f[:-5]
file = TFile(f)

#tree = file.Get("fsrCorrectedMuonTree")
lb =0
rb=10
nBins=100

yDefault = "Events/[%s bins]"%nBins

h1 = TH1F("h1","h1",nBins,lb,rb)
#h1.GetXaxis().SetTitle("N_{#gamma_{FSR}}")
h1.GetYaxis().SetTitle(yDefault)


t1 = file.Get(sys.argv[1])

#frame1 = nMupFSR.frame(Bins(15),Title("N_{#gamma_{FSR}} recombined with #mu^{+}"))
#frame1.addTH1(h1)
def p(STR):
    draw="%s>>h1"%STR
    t1.Draw(draw)
    global xTitle
    xTitle = STR
    h1.GetXaxis().SetTitle(xTitle)
    h1.Draw()
    c1.Update()
    c1.Print("mc_u3s_generic_%s.pdf"%STR)


def pc( STR1, STR2 ):
    draw="%s>>h1"%STR1
    t1.Draw(draw, STR2)
    heading=STR1+' | '+STR2
    h1.GetXaxis().SetTitle(heading)
    h1.Draw()
    c1.Update()
    c1.Print("mc_u3s_generic_%s_%s.pdf"%(STR1,STR2))

def q():
    exit()

def b(LB,RB,BINS):
    global lb
    lb = LB
    global rb
    rb = RB
    global nBins
    nBins=BINS
    global h1
    h1=TH1F("h1","h1",nBins,lb,rb)
    global yDefault
    yDefault = "Events/[%s bins]"%nBins
    h1.GetYaxis().SetTitle(yDefault)
    h1.Draw()
    c1.Update()
def pb(STR, LB, RB, BINS):
    global lb
    lb = LB
    global rb
    rb = RB
    global nBins
    nBins=BINS
    global h1
    h1=TH1F("h1","h1",nBins,lb,rb)
    global yDefault
    yDefault = "Events/[%s bins]"%nBins
    draw="%s>>h1"%STR
    t1.Draw(draw)
    global xTitle
    xTitle = STR
    h1.GetXaxis().SetTitle(xTitle)
    h1.GetYaxis().SetTitle(yDefault)
    h1.Draw()
    c1.Update()
    c1.Print("%s_%s.pdf"%(sample,STR))

def pbc(STR1, LB, RB, BINS, STR2):
    global lb
    lb = LB
    global rb
    rb = RB
    global nBins
    nBins=BINS
    global h1
    h1=TH1F("h1","h1",nBins,lb,rb)
    global yDefault
    yDefault = "Events/[%s bins]"%nBins
    draw="%s>>h1"%STR1
    t1.Draw(draw, STR2)
    heading="From"+sample+': '+STR2
    h1.GetXaxis().SetTitle(heading)
    global xTitle
    xTitle = STR1
    h1.GetXaxis().SetTitle(xTitle)
    h1.GetYaxis().SetTitle(yDefault)
    h1.Draw()
    c1.Update()
    c1.Print(sample+'_'+STR1+'_'+STR2+'.pdf')
