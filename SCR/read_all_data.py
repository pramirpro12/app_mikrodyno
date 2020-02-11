from pandas import *
from batch_fitting_class import *
import matplotlib.backends.backend_pdf

####################################################################
# start with different substrates
####################################################################

# read from excel into a pandas dataframe
ss = read_excel("../Data/DMSP_dosage.xlsx", "substrate_forpy")

# times
dtimes = array(ss['T'])

# convert to numpy arrays
a1 = array(ss['A_2090'])
a1D = array(ss['A_2090_DMSP'])
a1G = array(ss['A_2090_Glycerol'])
a1P = array(ss['A_2090_Proprionate'])
a1b = array(ss['A_2090_D7'])
a1bD = array(ss['A_2090_D7_DMSP'])
a1bG = array(ss['A_2090_D7_Glycerol'])
a1bP = array(ss['A_2090_D7_Proprionate'])
a2 = array(ss['A_379'])
a2D = array(ss['A_379_DMSP'])
a2G = array(ss['A_379_Glycerol'])
a2P = array(ss['A_379_Proprionate'])
a2b = array(ss['A_379_D7'])
a2bD = array(ss['A_379_D7_DMSP'])
a2bG = array(ss['A_379_D7_Glycerol'])
a2bP = array(ss['A_379_D7_Proprionate'])
b1 = array(ss['B_2090'])
b1D = array(ss['B_2090_DMSP'])
b1G = array(ss['B_2090_Glycerol'])
b1P = array(ss['B_2090_Proprionate'])
b1a = array(ss['B_2090_D7'])
b1aD = array(ss['B_2090_D7_DMSP'])
b1aG = array(ss['B_2090_D7_Glycerol'])
b1aP = array(ss['B_2090_D7_Proprionate'])
b2 = array(ss['B_379'])
b2D = array(ss['B_379_DMSP'])
b2G = array(ss['B_379_Glycerol'])
b2P = array(ss['B_379_Proprionate'])
b2a = array(ss['B_379_D7'])
b2aD = array(ss['B_379_D7_DMSP'])
b2aG = array(ss['B_379_D7_Glycerol'])
b2aP = array(ss['B_379_D7_Proprionate'])

a1sd = array(ss['A_2090_sd'])
a1Dsd = array(ss['A_2090_DMSP_sd'])
a1Gsd = array(ss['A_2090_Glycerol_sd'])
a1Psd = array(ss['A_2090_Proprionate_sd'])
a1bsd = array(ss['A_2090_D7_sd'])
a1bDsd = array(ss['A_2090_D7_DMSP_sd'])
a1bGsd = array(ss['A_2090_D7_Glycerol_sd'])
a1bPsd = array(ss['A_2090_D7_Proprionate_sd'])
a2sd = array(ss['A_379_sd'])
a2Dsd = array(ss['A_379_DMSP_sd'])
a2Gsd = array(ss['A_379_Glycerol_sd'])
a2Psd = array(ss['A_379_Proprionate_sd'])
a2bsd = array(ss['A_379_D7_sd'])
a2bDsd = array(ss['A_379_D7_DMSP_sd'])
a2bGsd = array(ss['A_379_D7_Glycerol_sd'])
a2bPsd = array(ss['A_379_D7_Proprionate_sd'])
b1sd = array(ss['B_2090_sd'])
b1Dsd = array(ss['B_2090_DMSP_sd'])
b1Gsd = array(ss['B_2090_Glycerol_sd'])
b1Psd = array(ss['B_2090_Proprionate_sd'])
b1asd = array(ss['B_2090_D7_sd'])
b1aDsd = array(ss['B_2090_D7_DMSP_sd'])
b1aGsd = array(ss['B_2090_D7_Glycerol_sd'])
b1aPsd = array(ss['B_2090_D7_Proprionate_sd'])
b2sd = array(ss['B_379_sd'])
b2Dsd = array(ss['B_379_DMSP_sd'])
b2Gsd = array(ss['B_379_Glycerol_sd'])
b2Psd = array(ss['B_379_Proprionate_sd'])
b2asd = array(ss['B_379_D7_sd'])
b2aDsd = array(ss['B_379_D7_DMSP_sd'])
b2aGsd = array(ss['B_379_D7_Glycerol_sd'])
b2aPsd = array(ss['B_379_D7_Proprionate_sd'])

# put in dictionaries
cont_a2090 = {'htimes': dtimes, 'hms': a1, 'hss': a1sd}
contD_a2090 = {'htimes': dtimes, 'hms': a1D, 'hss': a1Dsd}
contG_a2090 = {'htimes': dtimes, 'hms': a1G, 'hss': a1Gsd}
contP_a2090 = {'htimes': dtimes, 'hms': a1P, 'hss': a1Psd}

cont_b2090 = {'htimes': dtimes, 'hms': b1, 'hss': b1sd}
contD_b2090 = {'htimes': dtimes, 'hms': b1D, 'hss': b1Dsd}
contG_b2090 = {'htimes': dtimes, 'hms': b1G, 'hss': b1Gsd}
contP_b2090 = {'htimes': dtimes, 'hms': b1P, 'hss': b1Psd}

inf_2090 = {'htimes': dtimes, 'vtimes': dtimes,
            'hms': a1b, 'vms': b1a, 'hss': a1bsd, 'vss': b1asd}
infD_2090 = {'htimes': dtimes, 'vtimes': dtimes,
             'hms': a1bD, 'vms': b1aD, 'hss': a1bDsd, 'vss': b1aDsd}
infG_2090 = {'htimes': dtimes, 'vtimes': dtimes,
             'hms': a1bG, 'vms': b1aG, 'hss': a1bGsd, 'vss': b1aGsd}
infP_2090 = {'htimes': dtimes, 'vtimes': dtimes,
             'hms': a1bP, 'vms': b1aP, 'hss': a1bPsd, 'vss': b1aPsd}

# put in dictionaries
cont_a379 = {'htimes': dtimes, 'hms': a2, 'hss': a2sd}
contD_a379 = {'htimes': dtimes, 'hms': a2D, 'hss': a2Dsd}
contG_a379 = {'htimes': dtimes, 'hms': a2G, 'hss': a2Gsd}
contP_a379 = {'htimes': dtimes, 'hms': a2P, 'hss': a2Psd}

cont_b379 = {'htimes': dtimes, 'hms': b2, 'hss': b2sd}
contD_b379 = {'htimes': dtimes, 'hms': b2D, 'hss': b2Dsd}
contG_b379 = {'htimes': dtimes, 'hms': b2G, 'hss': b2Gsd}
contP_b379 = {'htimes': dtimes, 'hms': b2P, 'hss': b2Psd}

inf_379 = {'htimes': dtimes, 'vtimes': dtimes,
            'hms': a2b, 'vms': b2a, 'hss': a2bsd, 'vss': b2asd}
infD_379 = {'htimes': dtimes, 'vtimes': dtimes,
             'hms': a2bD, 'vms': b2aD, 'hss': a2bDsd, 'vss': b2aDsd}
infG_379 = {'htimes': dtimes, 'vtimes': dtimes,
             'hms': a2bG, 'vms': b2aG, 'hss': a2bGsd, 'vss': b2aGsd}
infP_379 = {'htimes': dtimes, 'vtimes': dtimes,
             'hms': a2bP, 'vms': b2aP, 'hss': a2bPsd, 'vss': b2aPsd}

####################################################################
# now do DMSP dosage
####################################################################

# read excel sheet into a pandas dataframe
ss = read_excel("DMSP_dosage.xlsx", "doses_forpy")

# times
dtimes = array(ss['T'])

# convert data from pandas data frame to arrays
a0 = array(ss['A_379_0'])
a10 = array(ss['A_379_10'])
a100 = array(ss['A_379_100'])
a500 = array(ss['A_379_500'])
ab0 = array(ss['A_379_D7_0'])
ab10 = array(ss['A_379_D7_10'])
ab100 = array(ss['A_379_D7_100'])
ab500 = array(ss['A_379_D7_500'])
b0 = array(ss['B_379_0'])
b10 = array(ss['B_379_10'])
b100 = array(ss['B_379_100'])
b500 = array(ss['B_379_500'])
ba0 = array(ss['B_379_D7_0'])
ba10 = array(ss['B_379_D7_10'])
ba100 = array(ss['B_379_D7_100'])
ba500 = array(ss['B_379_D7_500'])

a0sd = array(ss['A_379_0_sd'])
a10sd = array(ss['A_379_10_sd'])
a100sd = array(ss['A_379_100_sd'])
a500sd = array(ss['A_379_500_sd'])
ab0sd = array(ss['A_379_D7_0_sd'])
ab10sd = array(ss['A_379_D7_10_sd'])
ab100sd = array(ss['A_379_D7_100_sd'])
ab500sd = array(ss['A_379_D7_500_sd'])
b0sd = array(ss['B_379_0_sd'])
b10sd = array(ss['B_379_10_sd'])
b100sd = array(ss['B_379_100_sd'])
b500sd = array(ss['B_379_500_sd'])
ba0sd = array(ss['B_379_D7_0_sd'])
ba10sd = array(ss['B_379_D7_10_sd'])
ba100sd = array(ss['B_379_D7_100_sd'])
ba500sd = array(ss['B_379_D7_500_sd'])

# put in dictionaries to call the function
cont_a0 = {'htimes': dtimes, 'hms': a0, 'hss': a0sd}
cont_a10 = {'htimes': dtimes, 'hms': a10, 'hss': a10sd}
cont_a100 = {'htimes': dtimes, 'hms': a100, 'hss': a100sd}
cont_a500 = {'htimes': dtimes, 'hms': a500, 'hss': a500sd}

cont_b0 = {'htimes': dtimes, 'hms': b0, 'hss': b0sd}
cont_b10 = {'htimes': dtimes, 'hms': b10, 'hss': b10sd}
cont_b100 = {'htimes': dtimes, 'hms': b100, 'hss': b100sd}
cont_b500 = {'htimes': dtimes, 'hms': b500, 'hss': b500sd}

inf_0 = {'htimes': dtimes, 'vtimes': dtimes,
         'hms': ab0, 'vms': ba0, 'hss': ab0sd, 'vss': ba0sd}
inf_10 = {'htimes': dtimes, 'vtimes': dtimes, 'hms': ab10,
          'vms': ba10, 'hss': ab10sd, 'vss': ba10sd}
inf_100 = {'htimes': dtimes, 'vtimes': dtimes, 'hms': ab100,
           'vms': ba100, 'hss': ab100sd, 'vss': ba100sd}
inf_500 = {'htimes': dtimes, 'vtimes': dtimes, 'hms': ab500,
           'vms': ba500, 'hss': ab500sd, 'vss': ba500sd}

####################################################################
# now do data from mixed experiments
####################################################################

# read excel sheet into a pandas dataframe
sv = read_excel("DMSP_dosage.xlsx", "vir_forpy")
sb = read_excel("DMSP_dosage.xlsx", "bac_forpy")
oh = read_excel("DMSP_dosage.xlsx", "onehost_forpy")
th = read_excel("DMSP_dosage.xlsx", "twohost_forpy")

# convert to numpy arrays
# times
dtimes = array(sv['T'])

# algae
a2090 = array(sv['A_2090'])
a2090v = array(sv['A_2090_V'])
a2090b = array(sb['A_2090_D7'])
a2090vb = array(oh['A_2090_D7_V'])
a379 = array(sb['A_379'])
a379b = array(sb['A_379_D7'])
a379vb = array(oh['A_379_D7_V'])
a2090a379 = array(th['A_2090_A_379'])
a2090a379v = array(th['A_2090_A_379_V'])
a2090a379b = array(th['A_2090_A_379_D7'])
a2090a379vb = array(th['A_2090_A_379_D7_V'])

# bacteria
b2090b = array(sb['B_A_2090_D7'])
b2090vb = array(oh['B_A_2090_D7_V'])
b = array(sb['B'])
b379b = array(sb['B_A_379_D7'])
b379vb = array(oh['B_A_379_D7_V'])
ba2090a379b = array(th['B_A_2090_A_379_D7'])
ba2090a379vb = array(th['B_A_2090_A_379_D7_V'])

# bacteria
v2090v = array(sv['V_A_2090_V'])
v2090vb = array(oh['V_A_2090_D7_V'])
v379vb = array(oh['V_A_379_D7_V'])
va2090a379b = array(th['V_A_2090_A_379_D7'])
va2090a379vb = array(th['V_A_2090_A_379_D7_V'])

# algae
a2090sd = array(sv['A_2090_sd'])
a2090vsd = array(sv['A_2090_V_sd'])
a2090bsd = array(sb['A_2090_D7_sd'])
a2090vbsd = array(oh['A_2090_D7_V_sd'])
a379sd = array(sb['A_379_sd'])
a379bsd = array(sb['A_379_D7_sd'])
a379vbsd = array(oh['A_379_D7_V_sd'])
a2090a379sd = array(th['A_2090_A_379_sd'])
a2090a379vsd = array(th['A_2090_A_379_V_sd'])
a2090a379bsd = array(th['A_2090_A_379_D7_sd'])
a2090a379vbsd = array(th['A_2090_A_379_D7_V_sd'])

# bacteria
b2090bsd = array(sb['B_A_2090_D7_sd'])
b2090vbsd = array(oh['B_A_2090_D7_V_sd'])
bsd = array(sb['B_sd'])
b379bsd = array(sb['B_A_379_D7_sd'])
b379vbsd = array(oh['B_A_379_D7_V_sd'])
ba2090a379bsd = array(th['B_A_2090_A_379_D7_sd'])
ba2090a379vbsd = array(th['B_A_2090_A_379_D7_V_sd'])

# bacteria
v2090vsd = array(sv['V_A_2090_V_sd'])
v2090vbsd = array(oh['V_A_2090_D7_V_sd'])
v379vbsd = array(oh['V_A_379_D7_V_sd'])
va2090a379bsd = array(th['V_A_2090_A_379_D7_sd'])
va2090a379vbsd = array(th['V_A_2090_A_379_D7_V_sd'])

# put in dictionaries for fitting
cont_2090 = {'htimes': dtimes, 'hms': a2090, 'hss': a2090sd}
cont_379 = {'htimes': dtimes, 'hms': a379, 'hss': a379sd}
cont_D7 = {'htimes': dtimes, 'hms': b, 'hss': bsd}

inf_379bac = {'htimes': dtimes, 'vtimes': dtimes,
              'hms': a379b, 'vms': b379b, 'hss': a379bsd, 'vss': b379bsd}
inf_2090bac = {'htimes': dtimes, 'vtimes': dtimes,
               'hms': a2090b, 'vms': b2090b, 'hss': a2090bsd, 'vss': b2090bsd}
inf_2090vir = {'htimes': dtimes[:6], 'vtimes': dtimes[:6], 'hms': a2090v[:6],
               'vms': v2090v[:6], 'hss': a2090vsd[:6], 'vss': v2090vsd[:6]}
