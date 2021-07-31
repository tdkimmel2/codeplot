from ROOT import *
import math
import os
import sys

def calcFOM(S, B):
    sb = S + B
    if sb != 0:
        denominator = math.sqrt(sb)
        fom = S / float(denominator)
    else:
        fom=0
    return fom
"""
def getCounts(TREES, VAR, CUT='1'):
    s1 = trees[0].Draw(VAR.GetName(), CUT + " && pi0tru==1", 'goff')
    s2 = trees[1].Draw(VAR.GetName(), CUT + " && pi0tru==1", 'goff')
    nSig = s1 + s2
    nBkg = trees[2].Draw(VAR.GetName(), CUT, 'goff')

    return [nSig, nBkg]
"""
def getCounts(TREES, VAR, CUT='1'):
    #s1 = trees[0].Draw(VAR.GetName(), CUT + " && whomi==1", 'goff')
    #s2 = trees[1].Draw(VAR.GetName(), CUT + " && whomi==1", 'goff')
    #nSig = s1 + s2
    nSig = trees[0].Draw(VAR.GetName(), CUT+" && whomi==1", 'goff')
    nBkg = trees[0].Draw(VAR.GetName(), CUT+" && whomi==0", 'goff')

    return [nSig, nBkg]

# ================================================================================
# Instantiate TTrees
# ================================================================================
"""
# Signal MC Files
filename_sig = "./mc_u3s_chib1_omega.root"
filename_sig2 = "./mc_u3s_chib2_omega.root"

# Resonant Background MC Files
fi_dbRad_dipi = "./mc_u3s_dbRad_dipi.root"
fi_zz_dipi = "./mc_u3s_zz_dipi.root"
fi_isr_u2s_dipi = "./mc_isr_u2s_dipi.root"
fi_dipi_dipi = "./mc_u3s_dipi_dipi.root"

tree = 'inclusiveTree'
fsig = TFile(filename_sig, "READ")
fsig2 = TFile(filename_sig2, "READ")
tSIG = fsig.Get(tree)
tSIG2 = fsig2.Get(tree)

t_bkg = TChain(tree)
t_bkg.Add(fi_dbRad_dipi,0) # The trailing zero here is critical. It specifies the number of events to read in from the file. Zero indicates all events.
t_bkg.Add(fi_zz_dipi,0) # The trailing zero here is critical. It specifies the number of events to read in from the file. Zero indicates all events.
t_bkg.Add(fi_isr_u2s_dipi,0)
t_bkg.Add(fi_dipi_dipi,0)

trees = [tSIG, tSIG2, t_bkg]
"""
#filename_sig = "/home/tkimmel/Research/root/allmfrecon.root"
filename_sig = "/home/tkimmel/Research/root/allmfrecon_reducedpi0fittingsample.root"
tree = 'pi0tree'
fsig = TFile(filename_sig, "READ")
tSIG = fsig.Get(tree)
trees = [tSIG]
# ================================================================================
# Define parameters
# ================================================================================
# Define fit observable of analysis
var = RooRealVar('pi0mass','#pi^{0} Mass (GeV/c^{2})',0.12,0.149)
#var1 = RooRealVar('mfchi2','Mass Fit #Chi^{2}',0,60)
var1 = RooRealVar('mfchi2','Mass Fit #Chi^{2}',0,20)
var2 = RooRealVar('gmthetacms','#theta_{#gamma_{1}#gamma_{2}}_{CMS}',0,3.14)
var3 = RooRealVar('pi0p3cms','|p_{#pi^{0}}|_{CMS}',0,4)

# I optimize a grid cut on deltamDiPi. Replace with your variable here.
var_name = 'pi0mass'
var1_name = 'mfchi2'
var2_name = 'gmthetacms'
var3_name = 'pi0p3cms'
#lt = RooRealVar('lt', 'Mass Fit #Chi^{2} < CUT',0,60)
lt = RooRealVar('lt', 'Mass Fit #Chi^{2} < CUT',0,20)
gt = RooRealVar('gt', '#theta_{#gamma_{1}#gamma_{2}}_{CMS} > CUT',0,3.14)
#lt = RooRealVar('lt', '#theta_{#gamma_{1}#gamma_{2}}_{CMS} < CUT',0,3.14)
#gt = RooRealVar('gt', '|p_{#pi^{0}}|_{CMS} < CUT',0,4)
#nLTBins = 5
#nGTBins = 5
nLTBins = 20
nGTBins = 20

#baseCut = 'deltamChi>=10.2 && deltamChi<10.32 && CF_oneDiLepton==1 && CF_costhPipPim>=1 && CF_oneDiPion==1 && pi0mass<=0.15 && pi0mass>=0.11 && pstarPi0>=0.08 && pstarPi0<=0.43&& pi0MF_chisq<=84 && deltamDiPi>=9.83 && deltamDiPi<=10.12 && mOmega>=0.71 && mOmega<=0.83  && cllp>0 && cllm>0 && clpip>0 && clpim>0 && pi0_bcs>0'
baseCut = 'nb>0'
#baseCut = 'mfchi2<0.01'

# PDF Output Parameters
path2PDF = '/home/tkimmel/Research/plots/'
#os.system('mkdir -p ' + path2PDF)
pdf = path2PDF + 'gridOpt'

# ---------------------------
# Begin Optimization Routine
# ---------------------------
nSigRetained = list()
nBkgRetained = list()
FOM = list()
optimal_i = list()

# First Count total number of Bkg and Signal
allCandidates = getCounts(trees, var, baseCut)
nSigTotal = allCandidates[0]
nBkgTotal = allCandidates[1]

# Initialize Optima to Junk values
optimalLT_cut = -5
optimalGT_cut = -5
optimalFOM = 0

# Determine Step Sizes
rbGT = gt.getMax()
lbGT = gt.getMin()
rbLT = lt.getMax()
lbLT = lt.getMin()
stepGT = (rbGT - lbGT) / nGTBins
stepLT = (rbLT - lbLT) / nLTBins

for iLT in range(0, nLTBins):
    FOM_for_fixedLT = list()
    nSigRetained_for_fixedLT = list()
    nBkgRetained_for_fixedLT = list()

    LT_CUT = rbLT - iLT * stepLT
    for iGT in range(0, nGTBins):
        GT_CUT = rbGT - iGT * stepGT
        #CUT = baseCut+" "+var_name+"<%f||"+var_name+">%f" % (LT_CUT, GT_CUT)
        CUT = baseCut+" && mfchi2<%f && gmthetacms<%f" % (LT_CUT, GT_CUT)
        #CUT = baseCut+" && gmthetacms<%f && pi0p3cms<%f" % (LT_CUT, GT_CUT)
        #CUT = baseCut+" && mfchi2<%f && pi0p3cms<%f" % (LT_CUT, GT_CUT)
        infos = getCounts(trees, var, CUT)
        nSigRetained_for_fixedLT.append(infos[0])
        nBkgRetained_for_fixedLT.append(infos[1])
        print("\n %s < %.4f, %s < %.4f" % (var1_name, LT_CUT, var2_name, GT_CUT))
        #print("\n %s < %.4f, %s < %.4f" % (var2_name, LT_CUT, var3_name, GT_CUT))
        #print("\n %s < %.4f, %s < %.4f" % (var1_name, LT_CUT, var3_name, GT_CUT))
        FOM_for_fixedLT.append(calcFOM(nSigRetained_for_fixedLT[iGT], nBkgRetained_for_fixedLT[iGT]))
        print("FOM = %.3f" % FOM_for_fixedLT[iGT])

    FOM.append(FOM_for_fixedLT)
    nSigRetained.append(nSigRetained_for_fixedLT)
    nBkgRetained.append(nBkgRetained_for_fixedLT)

    FOM_localMax = max(FOM_for_fixedLT)
    print("local maximum of FOM is %.4f" % FOM_localMax)
    if FOM_localMax > optimalFOM:
        print("local max supercedes the optimalFOM, redefining!")
        optimalFOM = FOM_localMax
        optimalLT_cut = LT_CUT
        localOpt_iGT = FOM_for_fixedLT.index(FOM_localMax)
        optimalGT_cut = rbGT - stepGT * (localOpt_iGT)
        optimal_i = [iLT, localOpt_iGT]
        print("FOUND New Optimal Cuts are %s < %.3f and %s < %.3f" % (var1_name, optimalLT_cut, var2_name, optimalGT_cut))
        #print("FOUND New Optimal Cuts are %s < %.3f and %s < %.3f" % (var2_name, optimalLT_cut, var2_name, optimalGT_cut))
        #print("FOUND New Optimal Cuts are %s < %.3f and %s < %.3f" % (var1_name, optimalLT_cut, var3_name, optimalGT_cut))
    else:
        print("The local maximum is suboptimal...")

print(15 * '=')
print("\nThe optimal FOM (%.4f) is attained for:" % optimalFOM)
print("\t%s < %.4f" % (var1_name, optimalLT_cut))
print("\t%s < %.4f\n" % (var2_name, optimalGT_cut))
#print("\t%s < %.4f\n" % (var2_name, optimalLT_cut))
#print("\t%s < %.4f\n" % (var3_name, optimalGT_cut))
print(15 * '=')

CUT = baseCut + " && %s<%f && %s<%f" % (var1_name, optimalLT_cut, var2_name,optimalGT_cut)
#CUT = baseCut + " && %s<%f && %s<%f" % (var2_name, optimalLT_cut, var2_name,optimalGT_cut)
#CUT = baseCut + " && %s<%f && %s<%f" % (var1_name, optimalLT_cut, var3_name,optimalGT_cut)
optimalCutDetails = getCounts(trees, var, CUT)
baseCutDetails = getCounts(trees, var, baseCut)

nSigTotal = baseCutDetails[0]
nBkgTotal = baseCutDetails[1]
nSig = optimalCutDetails[0]
nBkg = optimalCutDetails[1]
effiRetainSIG = nSig/float(nSigTotal)
effiRejectBKG = (nBkgTotal - nBkg)/float(nBkgTotal)

print("Effi_rejectBKG = %.3f" % effiRejectBKG)
print("Effi_retainSIG = %.3f" % effiRetainSIG)

# ---------------------------
# End Optimization Routine
# ---------------------------

# ---------------------------
# Draw Resulting FOM plot
# ---------------------------
# This section draws a 2D histogram of the FOM 
bw_lt = (lt.getMax() - lt.getMin()) / nLTBins
bw_gt = (gt.getMax() - gt.getMin()) / nGTBins

elf = TH2F("h2d", ' ', nGTBins, lbGT + bw_gt, rbGT + bw_gt, nLTBins, lbLT + bw_lt, rbLT + bw_lt)
# elf = TH2F("h2d", ' ', nGTBins, lbGT+0.001, rbGT+0.001, nLTBins, lbLT+0.001, rbLT+0.001)

for iLT in range(0, nLTBins):
    for iGT in range(0, nGTBins):
        elf.SetBinContent(nGTBins - iGT, nLTBins - iLT, FOM[iLT][iGT])

c = TCanvas("c", "",2000, 900)
gPad.SetLeftMargin(0.15)
gPad.SetRightMargin(0.1)
gPad.SetBottomMargin(0.2)
gStyle.SetOptStat(0)
gStyle.SetPaintTextFormat('.2f') # number of significatn digits in overlaid FOM values
c.SetGrid()
c.cd()

gPad.Update()
"""
h2d.GetYaxis().SetTitle(lt.GetTitle())
h2d.GetXaxis().SetTitle(gt.GetTitle())
h2d.SetStats(0)
h2d.SetMarkerSize(2)
"""
elf.GetYaxis().SetTitle(lt.GetTitle())
elf.GetXaxis().SetTitle(gt.GetTitle())
elf.SetStats(0)
elf.SetMarkerSize(2)

#xaxis = h2d.GetXaxis()
xaxis = elf.GetXaxis()
xaxis.SetTitleSize(0.06)
xaxis.SetLabelOffset(0.02)
xaxis.SetTitleOffset(1.3)
xaxis.CenterTitle()
xaxis.CenterLabels()
xaxis.SetLabelSize(0.045)
xaxis.SetNdivisions(306)

#yaxis = h2d.GetYaxis()
yaxis = elf.GetYaxis()
yaxis.SetLabelOffset(0.02)
yaxis.SetTitleSize(0.06)
yaxis.SetTitleOffset(1.3)
yaxis.CenterTitle()
yaxis.CenterLabels()
yaxis.SetLabelSize(0.045)
yaxis.SetNdivisions(306)

gStyle.SetPalette(kViridis)

elf.Draw("COLZ4 TEXT")
c.Update()

outfile = pdf + ".png"
c.SaveAs(outfile)
