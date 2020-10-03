# Jet Charge Observables at 13 TeV using NanoAOD format 

# JUNE2020-v1
This is the working version

# NanoAOD Workbook
https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookNanoAOD

# NanoAOD-tools
Tools for working with NanoAOD (requiring only python + root, not CMSSW)

## Checkout instructions: CMSSW

    mkdir JetCharge
    cd JetCharge
    cmsrel CMMSW_10_2_22           # CMSSW_10_2_22 minimum for NanaoAODv7
    cd CMSSW_10_2_22/src
    git clone https://github.com/cms-nanoAOD/nanoAOD-tools.git PhysicsTools/NanoAODTools    #ref
    cd PhysicsTools/NanoAODTools
    cmsenv
    scram b

## Setup the code

    git clone git@github.com:soumyadipbarman/JetCharge.git  
  
## General instructions to run the post-processing step

* The main code for running this module to create Histograms and Branches for ouput root files : [file](python/postprocessing/examples/skimmer.py)
* To test the module locally: [file](python/crab/)
```
python runPostProcessing.py 0
```
### Keep/drop branches





