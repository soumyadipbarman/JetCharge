#this fake PSET is needed for local test and for crab to figure the output filename
#you do not need to edit it unless you want to do a local test using a different input file than
#the one marked below
import FWCore.ParameterSet.Config as cms
process = cms.Process('NANO')
process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring(),
#	lumisToProcess=cms.untracked.VLuminosityBlockRange("254231:1-254231:24")
)
process.source.fileNames = [
# JetHT 2017 Custom NanoAOD DATA
#'root://cms-xrd-global.cern.ch//store/user/algomez/PFNano/106x_v01/JetHT/Run2017B-09Aug2019_UL2017-v1_PFNanoAOD/200716_075309/0000/nano106X_on_mini106X_2017_data_NANO_370.root',
'root://cms-xrd-global.cern.ch//store/user/algomez/PFNano/106x_v01/JetHT/Run2017B-09Aug2019_UL2017-v1_PFNanoAOD/200716_075309/0000/nano106X_on_mini106X_2017_data_NANO_371.root',
#'root://cms-xrd-global.cern.ch//store/user/algomez/PFNano/106x_v01/JetHT/Run2017B-09Aug2019_UL2017-v1_PFNanoAOD/200716_075309/0000/nano106X_on_mini106X_2017_data_NANO_372.root',
#'root://cms-xrd-global.cern.ch//store/user/algomez/PFNano/106x_v01/JetHT/Run2017B-09Aug2019_UL2017-v1_PFNanoAOD/200716_075309/0000/nano106X_on_mini106X_2017_data_NANO_373.root',
#'root://cms-xrd-global.cern.ch//store/user/algomez/PFNano/106x_v01/JetHT/Run2017B-09Aug2019_UL2017-v1_PFNanoAOD/200716_075309/0000/nano106X_on_mini106X_2017_data_NANO_374.root',
#'root://cms-xrd-global.cern.ch//store/user/algomez/PFNano/106x_v01/JetHT/Run2017D-09Aug2019_UL2017-v1_PFNanoAOD/200716_075602/0000/nano106X_on_mini106X_2017_data_NANO_163.root',

# JetHT	2017 Custom NanoAOD MC
#'root://cms-xrd-global.cern.ch//store/user/mmorris/PFNano/106x_v01/QCD_Pt-15to7000_TuneCP5_Flat_13TeV_pythia8/RunIISummer19UL17PFNanoAOD-106X_mc2017_realistic_v6_ext2-v2/200720_195938/0000/nano106X_on_mini106X_2017_mc_NANO_2.root'
]
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.options = cms.untracked.PSet()
process.output = cms.OutputModule("PoolOutputModule", 
	fileName = cms.untracked.string('JetCharge_skimmer-trees.root'),
	fakeNameForCrab =cms.untracked.bool(True))
process.out = cms.EndPath(process.output)

