#file path will be:
#outLFNDirBase/inputDataset/requestName/time_tag/...
from CRABClient.UserUtilities import config
config = config()
config.General.transferOutputs = True
config.General.requestName = 'ReggeGribovPartonMC_EposLHC_5020GeV_PbPb_step2_750_60kevt_20151126_v1'
config.General.workArea = 'crab_projects'
config.JobType.psetName = 'step2_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco.py'
config.JobType.pluginName = 'Analysis'
config.JobType.inputFiles = ['rssLimit']
config.JobType.outputFiles = ['step2_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco.root']
config.Data.inputDataset = '/ReggeGribovPartonMC_EposLHC_5020GeV_PbPb/twang-crab_ReggeGribovPartonMC_EposLHC_5020GeV_PbPb_GEN_SIM_750_60kevt_20151126_v1-4f575002e197e545b83aa7c136fcb1f8/USER'
config.Data.totalUnits = -1
config.Data.unitsPerJob = 20
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'EventAwareLumiBased'
config.Data.outLFNDirBase = '/store/user/twang/Run2PrivateMC'
config.Data.publication = True
config.Site.whitelist = ['T2_US_MIT']
config.Site.storageSite = 'T2_US_MIT'
#config.Site.storageSite = 'T2_CH_CERN'
