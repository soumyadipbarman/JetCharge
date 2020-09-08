#!/usr/bin/env python
#import os, sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
#from importlib import import_module
#from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.tools import *
#from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetUncertainties import *
#from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetSmearer import jetSmearer

import math as m
import array
import numpy
import random
import copy
import datetime

class Jetcharge_skimNANO(Module):
        #def __init__(self, jetSelection): #, jetSelection):       #crab                                       
        def __init__(self,EventLimit=-1):                          #local
                #self.jetSel = jetSelection  
		self.writeHistFile=True
                self.hltBranchName= "HLT"
		print "Running Jetcharge_skimNANO Module......"
                #pass
		#event counters
        	self.EventCounter = 0  
		self.EventLimit = EventLimit     #max events to be processed

		### Kinematics Cuts ###
        	self.minJetPt = 30.
        	self.maxObjEta = 2.5

        def beginJob(self, histFile, histDirName):
		Module.beginJob(self, histFile, histDirName)
		
		#ROOT.gSystem.Load("libPhysicsToolsNanoAODJMARTools.so")

		self.histotype = ['h_']

		for ihist, hist in enumerate(self.histotype):
		    self.addObject( ROOT.TH1F(hist + 'nrawjet',            hist + 'nrawjet',        8, 2, 10 ))
		    self.addObject( ROOT.TH1F(hist + 'rawjetpt',           hist + 'rawjetpt',        200, 20, 2020 ) )
		    self.addObject( ROOT.TH1F(hist + 'rawjeteta',          hist + 'rawjeteta',        40, -5, 5 ) )
		    self.addObject( ROOT.TH1F(hist + 'rawjetphi',          hist + 'rawjetphi',        100, -5, 5 ) )
		    self.addObject( ROOT.TH1F(hist + 'rawjetpt1',           hist + 'rawjetpt1',        200, 20, 2020 ) )
                    self.addObject( ROOT.TH1F(hist + 'rawjeteta1',          hist + 'rawjeteta1',        40, -5, 5 ) )
                    self.addObject( ROOT.TH1F(hist + 'rawjetphi1',          hist + 'rawjetphi1',        100, -5, 5 ) )
		    self.addObject( ROOT.TH1F(hist + 'rawjetpt2',           hist + 'rawjetpt2',        200, 20, 2020 ) )
                    self.addObject( ROOT.TH1F(hist + 'rawjeteta2',          hist + 'rawjeteta2',        40, -5, 5 ) )
                    self.addObject( ROOT.TH1F(hist + 'rawjetphi2',          hist + 'rawjetphi2',        100, -5, 5 ) )
	
		#self.h_recopt=ROOT.TH1F('recopt',   'recopt',   100, 0, 1000)
        	#self.addObject(self.h_recopt)
                  
        def endJob(self):
		Module.endJob(self)
                pass
        def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
                self.out = wrappedOutputTree
		self.out.branch("nrawjet", "I")
		self.out.branch("rawjetpt", "F")
		self.out.branch("rawjeteta", "F")
		self.out.branch("rawjetphi", "F")  
		#self.out.branch()  
		pass
        def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
                pass      
	def analyze(self, event):
		"""process event, return True (go to next module) or False (fail, go to next event)"""
	        #Event counters, max events to be processed for local running of jobs
		current_time = datetime.datetime.now()
                self.EventCounter +=1

		print'Number of Events processed :', self.EventCounter, 'at', current_time, 'CEST'
     		
		if self.EventCounter > self.EventLimit > -1:
                	return False
		
		###### Get list of reco jets #######
        	# List of reco jets:
        	allrecojets = list(Collection(event, "Jet"))
        	allrecoparts = list(Collection(event, "JetPFCands"))

		hlt = Object(event, self.hltBranchName)
		
		recojets = []	
		jet1 = ROOT.TLorentzVector()
		jet2 = ROOT.TLorentzVector()
		rawjet_count = []
		#dijet_count = []

		### applying basic selection to jets
                recojets = [ x for x in allrecojets if x.p4().Perp() > self.minJetPt and abs(x.p4().Eta()) < self.maxObjEta and x.jetId > 1 ]
                recojets.sort(key=lambda x:x.p4().Perp(),reverse=True)

		#event selection
		# Trigger
	        if(hlt.PFJet40==1 or hlt.PFJet60==1 or hlt.PFJet80==1 or hlt.PFJet140==1 or hlt.PFJet200==1 or hlt.PFJet260==1 or hlt.PFJet320==1 or hlt.PFJet400==1 or hlt.PFJet450==1 or hlt.PFJet500==1 or hlt.PFJet550==1):
			### applying basic selection to jets
			#recojets = [ x for x in allrecojets if x.p4().Perp() > self.minJetPt and abs(x.p4().Eta()) < self.maxObjEta and x.jetId > 1 ]
			#recojets.sort(key=lambda x:x.p4().Perp(),reverse=True)
		#global j1,j2
		# select events with at least 2 jets
			if len(recojets) > 1:
			#dijet_count.append(recojets)
				jet1 = recojets[0].p4()
				jet2 = recojets[1].p4()
				for irecojet,recojet in enumerate(recojets):
					rawjet_count.append((irecojet,recojet))
					self.out.fillBranch("rawjetpt", recojet.p4().Perp())
	                		self.out.fillBranch("rawjeteta", recojet.p4().Eta())
        	        		self.out.fillBranch("rawjetphi", recojet.p4().Phi())
					self.h_rawjetpt.Fill(recojet.p4().Perp())
	                		self.h_rawjeteta.Fill(recojet.p4().Eta())
                			self.h_rawjetphi.Fill(recojet.p4().Phi())
				
	
		jetsel = len(rawjet_count)
		self.out.fillBranch("nrawjet",jetsel)
		self.h_nrawjet.Fill(jetsel)
		self.h_rawjetpt1.Fill(jet1.Perp())
		self.h_rawjeteta1.Fill(jet1.Eta())
		self.h_rawjetphi1.Fill(jet1.Phi())
		self.h_rawjetpt2.Fill(jet2.Perp())
                self.h_rawjeteta2.Fill(jet2.Eta())
                self.h_rawjetphi2.Fill(jet2.Phi())
		#dijet = len(dijet_count)
		#print "Total Number of dijet Events : " + str(dijet)
				
		#print "Return True"
		return True

"""
preselection="Jet_pt[0] > 400"
files=["root://cmsxrootd.fnal.gov//store/data/Run2017B/JetHT/NANOAOD/Nano25Oct2019-v1/40000/F444480C-9D10-4041-9F8E-A67CF1D98368.root"]
p=PostProcessor(".",files,cut=preselection,branchsel=None,modules=[Jetcharge_skimNANO()],noOut=True,histFileName="histOut.root",histDirName="jets13")
p.run()
"""

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

#jetskimmer = lambda : Jetcharge_skimNANO(jetSelection= lambda j : j.pt > 30)
jetskimmer = lambda : Jetcharge_skimNANO()


