# Jet Charge Observables at 13 TeV using NanoAOD format 

# JUNE2020-v1
This is the working version

# NanoAOD Workbook
https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookNanoAOD

# NanoAOD-tools
This module uses NanoAOD Tools to skim over DATA and MC.

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

* The main code for running this module to create Histograms and Branches for ouput root files : [skimmer.py](python/postprocessing/examples/skimmer.py)
* To test the module locally use this file: [runPostProcessor.py](python/crab/runPostProcessor.py)
```
python runPostProcessing.py 0
```
* To set root files for running the code locally use : [PSet.py](python/crab/runPostProcessor.py)
* Use keep_and_drop.txt to truncate some branches before the job starts.
* Use output_trees.txt to keep some branches and drop branches in the output root file.

### Crab Files
* The script [script_runPostProcessor.sh](python/crab/script_runPostProcessor.sh) runs the runPostProcessor.py when the jobs are submit in the crab.
* Use [crab_DATA.py](python/crab/crab_DATA.py) for running the jobs on DATA using crab.
* Use [crab_MC.py](python/crab/crab_MC.py) for running the jobs on MC using crab.
```
crab submit -c crab_DATA.py
crab submit -c crab_MC.py
```




