import sys
from ROOT import *
import ROOT
from keras.models import Sequential
from keras.layers.core import Dense, Dropout
from keras.optimizers import Adam

#print(sys.argv[1])
numtrees = sys.argv[1]
mdepth = sys.argv[2]
nsigtrain = sys.argv[3]
nbkgtrain = sys.argv[4]
rocname = sys.argv[5]

bkgtrain = int(nbkgtrain)
nbkgtest = str(bkgtrain*20)

sig1 = "/home/taylor/Research/root/pi0mfsigfromd0.root"
#sig1 = "/home/taylor/Research/root/pi0mfsig.root"
bkg1 = "/home/taylor/Research/root/pi0mfbkg.root"
sig = TFile(sig1,"READ")
bkg = TFile(bkg1,"READ")
sigt = sig.Get("pi0tree")
bkgt = bkg.Get("pi0tree")



dataloader = TMVA.DataLoader("dataset")

dataloader.AddVariable("pi0p3","F")
dataloader.AddVariable("pi0p3cms","F")
dataloader.AddVariable("gm1e","F")
dataloader.AddVariable("gm2e","F")
dataloader.AddVariable("gm1e925","F")
dataloader.AddVariable("gm2e925","F")
dataloader.AddVariable("ediff","F")
dataloader.AddVariable("gm1eerror","F")
dataloader.AddVariable("gm2eerror","F")
#dataloader.AddVariable("gm1p3","F")
#dataloader.AddVariable("gm2p3","F")
dataloader.AddVariable("gm1p3cms","F")
dataloader.AddVariable("gm2p3cms","F")
dataloader.AddVariable("gmthetacms","F")
dataloader.AddVariable("mfchi2","F")

sigWeight = 1
bkgWeight = 1
dataloader.AddSignalTree(sigt)
dataloader.AddBackgroundTree(bkgt)

# cuts defining the signal and background sample
#sigCut = ROOT.TCut("whoru==1")
#bgCut = ROOT.TCut("whoru==0")
sigCut = ROOT.TCut("")
bgCut = ROOT.TCut("")

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
                                        "nTrain_Signal="+nsigtrain,
                                        "nTrain_Background="+nbkgtrain,
                                        "nTest_Signal="+nsigtrain,
                                        "nTest_Background="+nbkgtrain,
                                        "SplitMode=Random",
                                        "NormMode=NumEvents",
                                        "!V"
                                       ]))


ROOT.TMVA.Tools.Instance()
ROOT.TMVA.PyMethodBase.PyInitialize()


fout = ROOT.TFile("MVAOutput.root","RECREATE")

factory = ROOT.TMVA.Factory("TMVAClassification", fout,
                            ":".join([
                                "!V",
                                "!Silent",
                                "Color",
                                "DrawProgressBar",
                                "Transformations=I,G",
                                "AnalysisType=Classification"]
                                     ))

# Define Keras Model
# Define model

model = Sequential()
#model.add(Dense(32, init='glorot_normal', activation='relu',
#        input_dim=numVariables))
model.add(Dense(32, init='glorot_normal', activation='relu',
        input_dim=13))
model.add(Dropout(0.5))
model.add(Dense(32, init='glorot_normal', activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(2, init='glorot_uniform', activation='softmax'))

# Set loss and optimizer
model.compile(loss='categorical_crossentropy', optimizer=Adam(),
        metrics=['categorical_accuracy',])

# Store model to file
model.save('model.h5')

# Print summary of model
model.summary()

# Keras interface with previously defined model
factory.BookMethod(dataloader, ROOT.TMVA.Types.kPyKeras, 'PyKeras',
        'H:!V:VarTransform=G:FilenameModel=model.h5:'+\
        'NumEpochs='+numtrees+':BatchSize=32:'+\
        'TriesEarlyStopping=-1') # Never end before the last epoch
        #'TriesEarlyStopping=3') # If the loss value does not improve for 3 tries in a row, it stops

# Gradient tree boosting from scikit-learn package
factory.BookMethod(dataloader, ROOT.TMVA.Types.kPyGTB, 'GTB',
        'H:!V:VarTransform=None:'+\
        'NEstimators=100:LearningRate=0.1:MaxDepth='+mdepth)


factory.BookMethod(dataloader, ROOT.TMVA.Types.kBDT, "BDT",
                    ":".join([
                        "NTrees="+numtrees,
                        "MaxDepth="+mdepth,
                        "UseNvars=13",
                        ]))


factory.TrainAllMethods()
factory.TestAllMethods()
factory.EvaluateAllMethods()

#dataloader.DrawROCCurve(dataset)
# Enable Javascript for ROOT so that we can draw the canvas
#%jsroot on

# Print ROC
#rocname = sys.argv[1]
canvas = factory.GetROCCurve(dataloader)
canvas.Print('roccurves/d0pi0s/mva/'+rocname+'.png')
#canvas.Print('roccurves/allpi0s/mva/'+rocname+'.png')
