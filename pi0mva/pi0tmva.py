from ROOT import *
import ROOT

sig1 = "/home/taylor/Research/root/pi0mfsigfromd0.root"
#sig1 = "/home/taylor/Research/root/pi0mfsig.root"
bkg1 = "/home/taylor/Research/root/pi0mfbkg.root"
sig = TFile(sig1,"READ")
bkg = TFile(bkg1,"READ")
sigt = sig.Get("pi0tree")
bkgt = bkg.Get("pi0tree")

#whoru = RooRealVar("whoru", "whoru",0,1)
#pi0p3 = RooRealVar("pi0p3", "pi0p3",0,3)
#pi0p3cms = RooRealVar("pi0p3cms", "pi0p3cms",0,4)
#gm1e = RooRealVar("gm1e", "gm1e",0,2)
#gm2e = RooRealVar("gm2e", "gm2e",0,2)
#gm1e925 = RooRealVar("gm1e925", "gm1e925",0,1)
#gm2e925 = RooRealVar("gm2e925", "gm2e925",0,1)
#ediff = RooRealVar("ediff", "ediff",0,1.5)
#gm1eerror = RooRealVar("gm1eerror", "gm1eerror",0,0.002)
#gm2eerror = RooRealVar("gm2eerror", "gm2eerror",0,0.002)
#gm1p3 = RooRealVar("gm1p3", "gm1p3",0,2)
#gm2p3 = RooRealVar("gm2p3", "gm2p3",0,2)
#gm1p3cms = RooRealVar("gm1p3cms", "gm1p3cms",0,2.5)
#gm2p3cms = RooRealVar("gm2p3cms", "gm2p3cms",0,2.5)
#gmthetacms = RooRealVar("gmthetacms", "gmthetacms",0,3.14)
#mfchi2 = RooRealVar("mfchi2", "mfchi2",0,55)

ROOT.TMVA.Tools.Instance()

# note that it seems to be mandatory to have an
# output file, just passing None to TMVA::Factory(..)
# does not work. Make sure you don't overwrite an
# existing file.
fout = ROOT.TFile("TMVAOutput.root","RECREATE")

factory = ROOT.TMVA.Factory("TMVAClassification", fout,
                            ":".join([
                                "!V",
                                "!Silent",
                                "Color",
                                "DrawProgressBar",
                                "Transformations=I;D;P;G,D",
                                "AnalysisType=Classification"]
                                     ))

#factory.AddVariable("pi0p3","F")
#factory.AddVariable("pi0p3cms","F")
#factory.AddVariable("gm1e","F")
#factory.AddVariable("gm2e","F")
#factory.AddVariable("gm1e925","F")
#factory.AddVariable("gm2e925","F")
#factory.AddVariable("ediff","F")
#factory.AddVariable("gm1eerror","F")
#factory.AddVariable("gm2eerror","F")
#factory.AddVariable("gm1p3","F")
#factory.AddVariable("gm2p3","F")
#factory.AddVariable("gm1p3cms","F")
#factory.AddVariable("gm2p3cms","F")
#factory.AddVariable("gmthetacms","F")
#factory.AddVariable("mfchi2","F")

dataloader = TMVA.DataLoader("dataset")
dataloader.AddVariable("pi0p3","F")
#dataloader.AddVariable("pi0p3cms","F")
#dataloader.AddVariable("gm1e","F")
dataloader.AddVariable("gm2e","F")
dataloader.AddVariable("gm1e925","F")
#dataloader.AddVariable("gm2e925","F")
dataloader.AddVariable("ediff","F")
dataloader.AddVariable("gm1eerror","F")
dataloader.AddVariable("gm2eerror","F")
#dataloader.AddVariable("gm1p3","F")
#dataloader.AddVariable("gm2p3","F")
#dataloader.AddVariable("gm1p3cms","F")
#dataloader.AddVariable("gm2p3cms","F")
dataloader.AddVariable("gmthetacms","F")
dataloader.AddVariable("mfchi2","F")

#factory.AddSignalTree(t)
#factory.AddBackgroundTree(t)

sigWeight = 1
bkgWeight = 1
dataloader.AddSignalTree(sigt)
dataloader.AddBackgroundTree(bkgt)
#dataloader.AddSignalTree(tree,sigWeight)
#dataloader.AddBackgroundTree(tree,bkgWeight)

# cuts defining the signal and background sample
#sigCut = ROOT.TCut("whoru==1")
#bgCut = ROOT.TCut("whoru==0")
sigCut = ROOT.TCut("")
bgCut = ROOT.TCut("")

#factory.PrepareTrainingAndTestTree(sigCut,   # signal events
#                                   bgCut,    # background events
#                                   ":".join([
#                                        "nTrain_Signal=0",
#                                        "nTrain_Background=0",
#                                        "SplitMode=Random",
#                                        "NormMode=NumEvents",
#                                        "!V"
#                                       ]))

dataloader.PrepareTrainingAndTestTree(sigCut,   # signal events
                                   bgCut,    # background events
                                   ":".join([
                                        #"nTrain_Signal=1000000",
                                        #"nTrain_Background=1000000",
                                        #"nTest_Signal=1000000",
                                        #"nTest_Background=1000000",
                                        #"nTrain_Signal=87341",
                                        #"nTrain_Background=87341",
                                        #"nTest_Signal=87341",
                                        #"nTest_Background=87341",
                                        "nTrain_Signal=20000",
                                        "nTrain_Background=20000",
                                        "nTest_Signal=20000",
                                        "nTest_Background=20000",
                                        "SplitMode=Random",
                                        "NormMode=NumEvents",
                                        "!V"
                                       ]))

#From example, nEvents is depreciated
#method = factory.BookMethod(dataloader, ROOT.TMVA.Types.kBDT, "BDT",
#                   ":".join([
#                       "!H",
#                       "!V",
#                       "NTrees=850",
#                       "nEventsMin=150",
#                       "MaxDepth=3",
#                       "BoostType=AdaBoost",
#                       "AdaBoostBeta=0.5",
#                       "SeparationType=GiniIndex",
#                       "nCuts=20",
#                       "PruneMethod=NoPruning",
#                       ]))

# Example Options
#method = factory.BookMethod(dataloader, ROOT.TMVA.Types.kBDT, "BDT",
#                   ":".join([
#                       "!H",
#                       "!V",
#                       "NTrees=850",
#                       "MaxDepth=3",
#                       "BoostType=AdaBoost",
#                       "AdaBoostBeta=0.5",
#                       "SeparationType=GiniIndex",
#                       "nCuts=20",
#                       "PruneMethod=NoPruning",
#                       ]))

# Default Options
method = factory.BookMethod(dataloader, ROOT.TMVA.Types.kBDT, "BDT",
                    ":".join([
                        "NTrees=10",
                        #"MaxDepth=6",
                        #"UseNvars=8",
                        ]))

factory.TrainAllMethods()
factory.TestAllMethods()
factory.EvaluateAllMethods()

# Enable Javascript for ROOT so that we can draw the canvas
%jsroot on

# Print ROC
canvas = factory.GetROCCurve(dataloader)
canvas.Draw()
