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
import numpy as np
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
        	self.maxJetEta = 2.4

		self.totalWeight = 1

        def beginJob(self, histFile, histDirName):
		Module.beginJob(self, histFile, histDirName)
		
		#ROOT.gSystem.Load("libPhysicsToolsNanoAODJMARTools.so")
	
		self.histotype = ['h_']
		
		for ihist, hist in enumerate(self.histotype):
		    self.addObject( ROOT.TH1F(hist + 'nrecojet',            hist + 'nrecojet',        8, 2, 10 ))
		    self.addObject( ROOT.TH1F(hist + 'rawjetpt',           hist + 'rawjetpt',        160, 400, 2000 ) )
		    self.addObject( ROOT.TH1F(hist + 'rawjeteta',          hist + 'rawjeteta',        100, -2.4, 2.4 ) )
		    self.addObject( ROOT.TH1F(hist + 'rawjetphi',          hist + 'rawjetphi',        100, -3.0, 3.0 ) )
		    #self.addObject( ROOT.TH1F(hist + 'rawjetpt1',           hist + 'rawjetpt1',        200, 20, 2020 ) )
                    #self.addObject( ROOT.TH1F(hist + 'rawjeteta1',          hist + 'rawjeteta1',        100, -2.4, 2.4 ) )
                    #self.addObject( ROOT.TH1F(hist + 'rawjetphi1',          hist + 'rawjetphi1',        100, -3.0, 3.0 ) )
		    #self.addObject( ROOT.TH1F(hist + 'rawjetpt2',           hist + 'rawjetpt2',        200, 20, 2020 ) )
                    #self.addObject( ROOT.TH1F(hist + 'rawjeteta2',          hist + 'rawjeteta2',        100, -2.4, 2.4 ) )
                    #self.addObject( ROOT.TH1F(hist + 'rawjetphi2',          hist + 'rawjetphi2',        100, -3.0, 3.0 ) )
		    self.addObject( ROOT.TH1F(hist + 'goodrecojetpt1',           hist + 'goodrecojetpt1',        160, 400, 2000 ) )
                    self.addObject( ROOT.TH1F(hist + 'goodrecojeteta1',          hist + 'goodrecojeteta1',        100, -2.4, 2.4 ) )
                    self.addObject( ROOT.TH1F(hist + 'goodrecojetphi1',          hist + 'goodrecojetphi1',        100, -3.0, 3.0 ) )
                    self.addObject( ROOT.TH1F(hist + 'goodrecojetpt2',           hist + 'goodrecojetpt2',        160, 400, 2000 ) )
                    self.addObject( ROOT.TH1F(hist + 'goodrecojeteta2',          hist + 'goodrecojeteta2',        100, -2.4, 2.4 ) )
                    self.addObject( ROOT.TH1F(hist + 'goodrecojetphi2',          hist + 'goodrecojetphi2',        100, -3.0, 3.0 ) )
		    #self.addObject( ROOT.TH1F(hist + 'goodrecojetchgpt1',           hist + 'goodrecojetchgpt1',        200, 20, 2020 ) )
                    #self.addObject( ROOT.TH1F(hist + 'goodrecojetchgeta1',          hist + 'goodrecojetchgeta1',        100, -2.4, 2.4 ) )
                    #self.addObject( ROOT.TH1F(hist + 'goodrecojetchgphi1',          hist + 'goodrecojetchgphi1',        100, -3.0, 3.0 ) )
		    self.addObject( ROOT.TH1F(hist + 'nochgcands',            hist + 'nochgcands',        190, 10, 200) )
		    self.addObject( ROOT.TH1F(hist + 'jetchgpt1',           hist + 'jetchgpt1',        200, 20, 2020 ) )
                    self.addObject( ROOT.TH1F(hist + 'jetchgeta1',          hist + 'jetchgeta1',        100, -2.4, 2.4 ) )
                    self.addObject( ROOT.TH1F(hist + 'jetchgphi1',          hist + 'jetchgphi1',        100, -3.0, 3.0 ) )
                    self.addObject( ROOT.TH1F(hist + 'jetcharge',           hist + 'jetcharge',        20, -1.0, 1.0 ) )

	
		#self.h_recopt=ROOT.TH1F('recopt',   'recopt',   100, 0, 1000)
        	#self.addObject(self.h_recopt)
                  
        def endJob(self):
		#print "Number:"+str(self.jelsel)
		Module.endJob(self)
                pass
        def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
                self.out = wrappedOutputTree
		self.out.branch("nrecojet", "I")
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
	
		#trigobj = ["hlt.PFJet40", "hlt.PFJet60", "hlt.PFJet80", "hlt.PFJet140", "hlt.PFJet200", "hlt.PFJet260", "hlt.PFJet320", "hlt.PFJet400","hlt.PFJet450", "hlt.PFJet500", "hlt.PFJet550"]	

		recojets = []	
		recojet_count = []
		recoChgCands = []

		Q = 0.0
		jetcharge = 0.0
		jet1pt = 0.0

		# All the charged particles within jets		
		pfcharged = [x for x in allrecoparts if (x.charge != 0)]
		
		# For constituents inside jets
		pfCandsVec = ROOT.vector("TLorentzVector")()
		pfCandsChg = []
		for p in pfcharged :
                	pfCandsVec.push_back( ROOT.TLorentzVector( p.p4().Px(), p.p4().Py(), p.p4().Pz(), p.p4().E()) )
			#pfCandsChg.push_back(p)
			pfCandsChg.append(p)

		### applying basic selection to jets
                recojets = [ x for x in allrecojets if x.p4().Perp() > self.minJetPt and abs(x.p4().Eta()) < self.maxJetEta and x.jetId>=2 ]  # recheck JETID criteria
                recojets.sort(key=lambda x:x.p4().Perp(),reverse=True)

		#event selection
		# Trigger
	        if(hlt.PFJet40==1 or hlt.PFJet60==1 or hlt.PFJet80==1 or hlt.PFJet140==1 or hlt.PFJet200==1 or hlt.PFJet260==1 or hlt.PFJet320==1 or hlt.PFJet400==1 or hlt.PFJet450==1 or hlt.PFJet500==1 or hlt.PFJet550==1):
		# select events with at least 2 jets
			#if len(recojets) >= 2:
			if (len(recojets) >= 2 and recojets[0].p4().Perp() > 400 and recojets[1].p4().Perp() > 100 and abs(recojets[0].p4().Eta()) < 1.5 and abs(recojets[1].p4().Eta()) < 1.5):
				#self.dijet +=1
				#print "Number of Dijet Event :"+str(self.dijet)
				#print "Dijet Event Selection..."
				for irecojet,recojet in enumerate(recojets):
					#print "Start Jet Loop..."
					recojet_count.append((irecojet,recojet))
					#recojetscands[irecojet] = {}
					# Cluster only the particles near the appropriate jet to save time
                    			#constituents = ROOT.vector("TLorentzVector")()
					constituents = []
					for ipfCandsVec,ipfCandsChg in zip(pfCandsVec,pfCandsChg) :
						#print "PF Loop..."
                				if abs(recojet.p4().DeltaR( ipfCandsVec )) < 0.4: # and x.charge:
							#print "Select Particles within cone 0.4..."
                    					#constituents.push_back( ROOT.TLorentzVector( x.p4().Px(), x.p4().Py(), x.p4().Pz(), x.p4().E()) )
							#recocands4v = [ ROOT.TLorentzVector( x.p4().px(), x.p4().py(), x.p4().pz(), x.p4().e() ) for x in constituents]
							constituents.append(ipfCandsChg)
							#recocands4v = ROOT.TLorentzVector()
							#recocands4v = [ x for x in constituents ]
					if (irecojet == 0):
						#if (recojet.p4().Perp > 400 and recojet.p4().Eta < 1.5):
							#print "First jet with only charged particles..."
						for irecocands,recocands in enumerate(constituents):
							recoChgCands.append((irecocands,recocands))
							Q += (1.0)*(recocands.charge)*(recocands.p4().Perp())
                                                        jet1pt += recojet.p4().Perp()                                                                        
							jetcharge += (1.0)*(Q/jet1pt)
                                                        self.h_jetchgpt1.Fill(recocands.p4().Perp(), self.totalWeight)
							self.h_jetchgeta1.Fill(recocands.p4().Eta(), self.totalWeight) 
							self.h_jetchgphi1.Fill(recocands.p4().Phi(), self.totalWeight)
							self.h_jetcharge.Fill(jetcharge, self.totalWeight)
							#print "Basic Distibutions using charged particles inside first Jet..."

					self.out.fillBranch("rawjetpt", recojet.p4().Perp())
	                		self.out.fillBranch("rawjeteta", recojet.p4().Eta())
        	        		self.out.fillBranch("rawjetphi", recojet.p4().Phi())
					self.h_rawjetpt.Fill(recojet.p4().Perp(), self.totalWeight)
	                		self.h_rawjeteta.Fill(recojet.p4().Eta(), self.totalWeight)
                			self.h_rawjetphi.Fill(recojet.p4().Phi(), self.totalWeight)
					if (irecojet == 0):
						self.h_goodrecojetpt1.Fill(recojet.p4().Perp(), self.totalWeight)
				                self.h_goodrecojeteta1.Fill(recojet.p4().Eta(), self.totalWeight)
                				self.h_goodrecojetphi1.Fill(recojet.p4().Phi(), self.totalWeight)
					if (irecojet == 1):
						self.h_goodrecojetpt2.Fill(recojet.p4().Perp(), self.totalWeight)
                                                self.h_goodrecojeteta2.Fill(recojet.p4().Eta(), self.totalWeight)
                                                self.h_goodrecojetphi2.Fill(recojet.p4().Phi(), self.totalWeight)

							
		jetsel = len(recojet_count)
		ncands = len(recoChgCands)
		#print "number:" + str(jetsel)
		self.out.fillBranch("nrecojet",jetsel)
		self.h_nrecojet.Fill(jetsel)
		self.h_nochgcands.Fill(ncands)
		#self.h_rawjetpt1.Fill(jet1.Perp())
		#self.h_rawjeteta1.Fill(jet1.Eta())
		#self.h_rawjetphi1.Fill(jet1.Phi())
		#self.h_rawjetpt2.Fill(jet2.Perp())
                #self.h_rawjeteta2.Fill(jet2.Eta())
                #self.h_rawjetphi2.Fill(jet2.Phi())
		#dijet = len(dijet_count)
		#print "Total Number of dijet Events : " + str(dijet)
				
		#print "Return True"
		#return jetsel 
		#if isDEBUG ==1:
		#	print "no"+str(jetsel)

		return True
	#print "Number of jets :" + str(xyz)
#print "Ok Done :"(jetsel)
#printer = Jetcharge_skimNANO()
#print printer.__init()__
#printer = Jetcharge_skimNANO()
#printer.analyze()

	#def printer(self):
		#return self.jetsel
#epson = Jetcharge_skimNANO()
#epson.printer()

#if __name__ == "__main__":
#	if analyze():
#		print "ElectronID_presel:", jetsel

#print(Module.event)
"""
preselection="Jet_pt[0] > 400"
files=["root://cmsxrootd.fnal.gov//store/data/Run2017B/JetHT/NANOAOD/Nano25Oct2019-v1/40000/F444480C-9D10-4041-9F8E-A67CF1D98368.root"]
p=PostProcessor(".",files,cut=preselection,branchsel=None,modules=[Jetcharge_skimNANO()],noOut=True,histFileName="histOut.root",histDirName="jets13")
p.run()
"""

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

#jetskimmer = lambda : Jetcharge_skimNANO(jetSelection= lambda j : j.pt > 30)
jetskimmer = lambda : Jetcharge_skimNANO()


