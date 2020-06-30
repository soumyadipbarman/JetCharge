#!/usr/bin/env python
import os, sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
#from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.tools import *
#from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetUncertainties import *

import math as m
from array import array
import numpy
import random
import copy

class Jetcharge_skimNANO(Module):
        def __init__(self, jetSelection): #, jetSelection):
                self.jetSel = jetSelection
		self.writeHistFile=True
                #self.puppimetBranchName= "PuppiMET"
                #self.rawmetBranchName= "RawMET"
                #self.pfmetBranchName= "MET"
                #self.flagBranchName= "Flag"
                #self.hltBranchName= "HLT"
		print "Running Jetcharge_skimNANO Module......"
                pass
        def beginJob(self,histFile=None,histDirName=None):
		Module.beginJob(self,histFile,histDirName)

		#ROOT.gSystem.Load("libPhysicsToolsNanoAODJMARTools.so")

		self.h_recopt=ROOT.TH1F('recopt',   'recopt',   100, 0, 1000)
        	self.addObject(self.h_recopt)
		self.h_recoeta=ROOT.TH1F('recoeta',   'recoeta',   40, -3, 3)
		self.addObject(self.h_recoeta)
		self.h_recophi=ROOT.TH1F('recophi',   'recophi',   100, -5, 5)
                self.addObject(self.h_recophi)
                pass
        def endJob(self):
                pass
        def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
                self.out = wrappedOutputTree
                #self.out.branch("diele_mass", "F");
                #self.out.branch("ele_px", "F");
                #self.out.branch("ele_py", "F");
                #self.out.branch("uparallel_PFMET", "F");
                #self.out.branch("uparpendicular_PFMET", "F");
                #self.out.branch("ele_lead_pt", "F");
                #self.out.branch("ele_sublead_pt", "F");
                #self.out.branch("uparallel_RawMET", "F");
                #self.out.branch("uparpendicular_RawMET", "F");
                #self.out.branch("uparallel_PuppiMET", "F");
                #self.out.branch("uparpendicular_PuppiMET", "F");
                #self.out.branch("Gen_pdgID", "I");
                #self.out.branch("Gen_ele_pt", "F");
		self.out.branch("recojetpt", "F")
		self.out.branch("recojeteta", "F")
		self.out.branch("recojetphi", "F")
		#self.out.branch("jet_e", "F")
		self.out.branch()
        def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
                pass
	def analyze(self, event):
		"""process event, return True (go to next module) or False (fail, go to next event)"""

		jets = Collection(event, "Jet")
		#hlt = Object(event, self.hltBranchName)
		recojet = ROOT.TLorentzVector()
		#jet_count1 = 0
		#jet_count2 = 0
		#event selection
		#print("Event")
		for j in filter(self.jetSel,jets):
			#if (abs(j.pt>30 and j.eta<2.5)):
				#if(trigger_selection):
		 print("event: 1")
		recojet += j.p4()
		self.out.fillBranch("recojetpt", recojet.pt())
		self.out.fillBranch("recojeteta", recojet.eta())
		self.out.fillBranch("recojetphi", recojet.phi())
		
		self.h_recopt.Fill(recojet.pt())
		self.h_recoeta.Fill(recojet.eta())
		self.h_recophi.Fill(recojet.phi())
		return True


# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

jetskimmer = lambda : Jetcharge_skimNANO(jetSelection= lambda j : j.pt > 30)


