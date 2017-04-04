#file path will be:
#outLFNDirBase/inputDataset/requestName/time_tag/...
from CRABClient.UserUtilities import config
config = config()
config.General.transferOutputs = True
config.General.requestName = 'BfinderData_pp_20151128_t2'
config.General.workArea = 'crab_projects'
config.JobType.psetName = 'finder_pp_75X_cfg.py'
config.JobType.pluginName = 'Analysis'
#config.JobType.inputFiles = ['rssLimit']
config.JobType.pyCfgParams = ['noprint']
config.JobType.outputFiles = ['finder_pp.root']
config.Data.inputDataset = '/DoubleMu/Run2015E-PromptReco-v1/RECO'
#config.Data.lumiMask = ''
config.Data.totalUnits = -1
config.Data.unitsPerJob = 1000
#config.Data.inputDBS = 'phys03'
config.Data.splitting = 'EventAwareLumiBased'
#config.Data.splitting = 'LumiBased'
config.Data.outLFNDirBase = '/store/user/twang/testSpace/20151127_t1'
#config.Data.outLFNDirBase = '/store/user/twang/BfinderRun2'
config.Site.storageSite = 'T2_US_MIT'
config.Site.whitelist = ['T2_US_MIT']
#config.Site.storageSite = 'T2_CH_CERN'
