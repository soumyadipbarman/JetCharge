#!/usr/bin/env python
#import FWCore.ParameterSet.Config as cms  # for local only
import os, sys
#import ROOT
#ROOT.PyConfig.IgnoreCommandLineOptions = True
from importlib import import_module
#from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import *
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis
#from PhysicsTools.NanoAODTools.postprocessing.examples.skimmer import jetskimmer                        #local
from PhysicsTools.NanoAODTools.postprocessing.examples.Triggerffi import *                                  #crab
#from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetUncertainties import *
#from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2 import *

name= 'JetCharge_Trigger'

## DATA ##
p=PostProcessor(".",inputFiles(),"Jet_pt>0","keep_and_drop.txt", modules=[Jettrigger()],provenance=True,fwkJobReport=True,histFileName= name +'-histOut_Trigger.root',histDirName="JetCharge_2017",haddFileName = name +'-trees.root',jsonInput=runsAndLumis(),outputbranchsel='output_tree.txt')

p.run()
print "Done"
#os.system("ls -lR")       
