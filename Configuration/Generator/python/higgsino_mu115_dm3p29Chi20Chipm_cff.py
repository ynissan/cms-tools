baseSLHATable = '''#
#                              ======================
#                              | THE SUSYHIT OUTPUT |
#                              ======================
#
#
#              ------------------------------------------------------
#              |     This is the output of the SUSY-HIT package     |
#              |  created by A.Djouadi, M.Muehlleitner and M.Spira. |
#              |  In case of problems with SUSY-HIT email to        |
#              |           margarete.muehlleitner@kit.edu           |
#              |           michael.spira@psi.ch                     |
#              |           abdelhak.djouadi@cern.ch                 |
#              ------------------------------------------------------
#
#              ------------------------------------------------------
#              |  SUSY Les Houches Accord - MSSM Spectrum + Decays  |
#              |              based on the decay programs           |
#              |                                                    |
#              |                     SDECAY 1.5a                    |
#              |                                                    |
#              |  Authors: M.Muhlleitner, A.Djouadi and Y.Mambrini  |
#              |  Ref.:    Comput.Phys.Commun.168(2005)46           |
#              |           [hep-ph/0311167]                         |
#              |                                                    |
#              |                     HDECAY 3.4                     |
#              |                                                    |
#              |  By: A.Djouadi,J.Kalinowski,M.Muhlleitner,M.Spira  |
#              |  Ref.:    Comput.Phys.Commun.108(1998)56           |
#              |           [hep-ph/9704448]                         |
#              |                                                    |
#              |                                                    |
#              |  If not stated otherwise all DRbar couplings and   |
#              |  soft SUSY breaking masses are given at the scale  |
#              |  Q=  0.10000003E+06
#              |                                                    |
#              ------------------------------------------------------
#
#
BLOCK DCINFO  # Decay Program information
     1   SDECAY/HDECAY # decay calculator
     2   1.5a /3.4    # version number
#
BLOCK SPINFO  # Spectrum calculator information
     1   SuSpect     # RGE +Spectrum calculator            
     2   2.41        # version number                      
#
BLOCK MODSEL  # Model selection
     1     0   # #general MSSM low scale                           
#
BLOCK SMINPUTS  # Standard Model inputs
         1     1.27934000E+02   # alpha_em^-1(M_Z)^MSbar
         2     1.16639000E-05   # G_F [GeV^-2]
         3     1.17200000E-01   # alpha_S(M_Z)^MSbar
         4     9.11870000E+01   # M_Z pole mass
         5     4.25000000E+00   # mb(mb)^MSbar
         6     1.72500000E+02   # mt pole mass
         7     1.77710000E+00   # mtau pole mass
#
BLOCK MINPAR  # Input parameters - minimal models
         1     1.00000000E+02   # 3                   
         4     1.00000000E+00   # sign(mu)            
#
BLOCK EXTPAR  # Input parameters - non-minimal models
         0     1.00000030E+05   # EWSB                
         1     2.22361105E+03   # M_1                 
         2     2.22361105E+03   # M_2                 
         3     1.00000000E+05   # M_3                 
        11    -1.00000000E+05   # A_t                 
        12    -1.00000000E+05   # A_b                 
        13    -2.51737263E+05   # A_tau               
        14    -6.77437438E+05   # A_u                 
        15    -8.59633345E+05   # A_d                 
        16    -2.53493493E+05   # A_e                 
        23     1.15000000E+02   # mu(EWSB)            
        25     1.00000000E+01   # tanbeta(in)         
        26     1.00000000E+05   # MA_pole             
        31     1.00000000E+05   # M_eL                
        32     1.00000000E+05   # M_muL               
        33     1.00000000E+05   # M_tauL              
        34     1.00000000E+05   # M_eR                
        35     1.00000000E+05   # M_muR               
        36     1.00000000E+05   # M_tauR              
        41     1.00000000E+05   # M_q1L               
        42     1.00000000E+05   # M_q2L               
        43     1.00000000E+05   # M_q3L               
        44     1.00000000E+05   # M_uR                
        45     1.00000000E+05   # M_cR                
        46     1.00000000E+05   # M_tR                
        47     1.00000000E+05   # M_dR                
        48     1.00000000E+05   # M_sR                
        49     1.00000000E+05   # M_bR                
#
BLOCK MASS  # Mass Spectrum
# PDG code           mass       particle
        24     8.05146384E+01   # W+
        25     2.06265992E+02   # h
        35     1.00000297E+05   # H
        36     1.00000000E+05   # A
        37     9.99999108E+04   # H+
         5     4.87877839E+00   # b-quark pole mass calculated from mb(mb)_Msbar
   1000001     1.02565622E+05   # ~d_L
   2000001     1.02565610E+05   # ~d_R
   1000002     1.02565594E+05   # ~u_L
   2000002     1.02565600E+05   # ~u_R
   1000003     1.02565622E+05   # ~s_L
   2000003     1.02565610E+05   # ~s_R
   1000004     1.02565594E+05   # ~c_L
   2000004     1.02565600E+05   # ~c_R
   1000005     1.02564565E+05   # ~b_1
   2000005     1.02566666E+05   # ~b_2
   1000006     1.00829701E+05   # ~t_1
   2000006     1.02326135E+05   # ~t_2
   1000011     1.00000009E+05   # ~e_L
   2000011     1.00000010E+05   # ~e_R
   1000012     9.99999810E+04   # ~nu_eL
   1000013     1.00000009E+05   # ~mu_L
   2000013     1.00000010E+05   # ~mu_R
   1000014     9.99999810E+04   # ~nu_muL
   1000015     9.99978166E+04   # ~tau_1
   2000015     1.00002202E+05   # ~tau_2
   1000016     9.99999810E+04   # ~nu_tauL
   1000021     1.04586100E+05   # ~g
   1000022     1.20711028E+02   # ~chi_10
   1000023    -1.24001244E+02   # ~chi_20
   1000025     2.20453199E+03   # ~chi_30
   1000035     2.49022754E+03   # ~chi_40
   1000024     1.22162653E+02   # ~chi_1+
   1000037     2.49022177E+03   # ~chi_2+
#
BLOCK NMIX  # Neutralino Mixing Matrix
  1  1     1.67618257E-02   # N_11
  1  2    -2.49087075E-02   # N_12
  1  3     7.11596562E-01   # N_13
  1  4    -7.01946530E-01   # N_14
  2  1     1.22235284E-02   # N_21
  2  2    -1.83968877E-02   # N_22
  2  3    -7.02563941E-01   # N_23
  2  4    -7.11277758E-01   # N_24
  3  1     9.99772878E-01   # N_31
  3  2     5.52176033E-03   # N_32
  3  3    -3.31707324E-03   # N_33
  3  4     2.03150244E-02   # N_34
  4  1     4.88053085E-03   # N_41
  4  2    -9.99505188E-01   # N_42
  4  3    -4.82066214E-03   # N_43
  4  4     3.06972419E-02   # N_44
#
BLOCK UMIX  # Chargino Mixing Matrix U
  1  1    -6.79674004E-03   # U_11
  1  2     9.99976902E-01   # U_12
  2  1     9.99976902E-01   # U_21
  2  2     6.79674004E-03   # U_22
#
BLOCK VMIX  # Chargino Mixing Matrix V
  1  1    -4.33076189E-02   # V_11
  1  2     9.99061785E-01   # V_12
  2  1     9.99061785E-01   # V_21
  2  2     4.33076189E-02   # V_22
#
BLOCK STOPMIX  # Stop Mixing Matrix
  1  1     3.62966862E-02   # cos(theta_t)
  1  2     9.99341058E-01   # sin(theta_t)
  2  1    -9.99341058E-01   # -sin(theta_t)
  2  2     3.62966862E-02   # cos(theta_t)
#
BLOCK SBOTMIX  # Sbottom Mixing Matrix
  1  1     7.05063266E-01   # cos(theta_b)
  1  2     7.09144408E-01   # sin(theta_b)
  2  1    -7.09144408E-01   # -sin(theta_b)
  2  2     7.05063266E-01   # cos(theta_b)
#
BLOCK STAUMIX  # Stau Mixing Matrix
  1  1     7.07165630E-01   # cos(theta_tau)
  1  2     7.07047927E-01   # sin(theta_tau)
  2  1    -7.07047927E-01   # -sin(theta_tau)
  2  2     7.07165630E-01   # cos(theta_tau)
#
BLOCK ALPHA  # Higgs mixing
          -1.08152043E-01   # Mixing angle in the neutral Higgs boson sector
#
BLOCK HMIX Q=  1.00000030E+05  # DRbar Higgs Parameters
         1     1.15000000E+02   # mu(Q)               
         2     9.21017407E+00   # tanbeta(Q)          
         3     2.41124527E+02   # vev(Q)              
         4     9.92260603E+09   # MA^2(Q)             
#
BLOCK GAUGE Q=  1.00000030E+05  # The gauge couplings
     1     3.73825028E-01   # gprime(Q) DRbar
     2     6.31331278E-01   # g(Q) DRbar
     3     8.77148868E-01   # g3(Q) DRbar
#
BLOCK AU Q=  1.00000030E+05  # The trilinear couplings
  1  1    -6.77437438E+05   # A_u(Q) DRbar
  2  2    -6.77437438E+05   # A_c(Q) DRbar
  3  3    -1.00000000E+05   # A_t(Q) DRbar
#
BLOCK AD Q=  1.00000030E+05  # The trilinear couplings
  1  1    -8.59633345E+05   # A_d(Q) DRbar
  2  2    -8.59633345E+05   # A_s(Q) DRbar
  3  3    -1.00000000E+05   # A_b(Q) DRbar
#
BLOCK AE Q=  1.00000030E+05  # The trilinear couplings
  1  1    -2.53493493E+05   # A_e(Q) DRbar
  2  2    -2.53493493E+05   # A_mu(Q) DRbar
  3  3    -2.51737263E+05   # A_tau(Q) DRbar
#
BLOCK Yu Q=  1.00000030E+05  # The Yukawa couplings
  1  1     0.00000000E+00   # y_u(Q) DRbar
  2  2     0.00000000E+00   # y_c(Q) DRbar
  3  3     7.47758556E-01   # y_t(Q) DRbar
#
BLOCK Yd Q=  1.00000030E+05  # The Yukawa couplings
  1  1     0.00000000E+00   # y_d(Q) DRbar
  2  2     0.00000000E+00   # y_s(Q) DRbar
  3  3     1.16133095E-01   # y_b(Q) DRbar
#
BLOCK Ye Q=  1.00000030E+05  # The Yukawa couplings
  1  1     0.00000000E+00   # y_e(Q) DRbar
  2  2     0.00000000E+00   # y_mu(Q) DRbar
  3  3     9.44653121E-02   # y_tau(Q) DRbar
#
BLOCK MSOFT Q=  1.00000030E+05  # The soft SUSY breaking masses at the scale Q
         1     2.22361105E+03   # M_1                 
         2     2.22361105E+03   # M_2                 
         3     1.00000000E+05   # M_3                 
        14    -6.77437438E+05   # A_u                 
        15    -8.59633345E+05   # A_d                 
        16    -2.53493493E+05   # A_e                 
        21     9.85919748E+09   # M^2_Hd              
        22     3.32160716E+08   # M^2_Hu              
        31     1.00000000E+05   # M_eL                
        32     1.00000000E+05   # M_muL               
        33     1.00000000E+05   # M_tauL              
        34     1.00000000E+05   # M_eR                
        35     1.00000000E+05   # M_muR               
        36     1.00000000E+05   # M_tauR              
        41     1.00000000E+05   # M_q1L               
        42     1.00000000E+05   # M_q2L               
        43     1.00000000E+05   # M_q3L               
        44     1.00000000E+05   # M_uR                
        45     1.00000000E+05   # M_cR                
        46     1.00000000E+05   # M_tR                
        47     1.00000000E+05   # M_dR                
        48     1.00000000E+05   # M_sR                
        49     1.00000000E+05   # M_bR                
#
#
#
#                             =================
#                             |The decay table|
#                             =================
#
# - The QCD corrections to the decays gluino -> squark  + quark
#                                     squark -> gaugino + quark_prime
#                                     squark -> squark_prime + Higgs
#                                     squark -> gluino  + quark
#   are included.
#
# - The multi-body decays for the inos, stops and sbottoms are included.
#
# - The loop induced decays for the gluino, neutralinos and stops
#   are included.
#
# - The SUSY decays of the top quark are included.
#
#
#         PDG            Width
DECAY         6     1.37861385E+00   # top decays
#          BR         NDA      ID1       ID2
     1.00000000E+00    2           5        24   # BR(t ->  b    W+)
#
#         PDG            Width
DECAY   1000021     3.46946274E+01   # gluino decays
#          BR         NDA      ID1       ID2
     3.43286854E-02    2     1000001        -1   # BR(~g -> ~d_L  db)
     3.43286854E-02    2    -1000001         1   # BR(~g -> ~d_L* d )
     3.43290891E-02    2     2000001        -1   # BR(~g -> ~d_R  db)
     3.43290891E-02    2    -2000001         1   # BR(~g -> ~d_R* d )
     3.43296275E-02    2     1000002        -2   # BR(~g -> ~u_L  ub)
     3.43296275E-02    2    -1000002         2   # BR(~g -> ~u_L* u )
     3.43294256E-02    2     2000002        -2   # BR(~g -> ~u_R  ub)
     3.43294256E-02    2    -2000002         2   # BR(~g -> ~u_R* u )
     3.43286854E-02    2     1000003        -3   # BR(~g -> ~s_L  sb)
     3.43286854E-02    2    -1000003         3   # BR(~g -> ~s_L* s )
     3.43290891E-02    2     2000003        -3   # BR(~g -> ~s_R  sb)
     3.43290891E-02    2    -2000003         3   # BR(~g -> ~s_R* s )
     3.43296275E-02    2     1000004        -4   # BR(~g -> ~c_L  cb)
     3.43296275E-02    2    -1000004         4   # BR(~g -> ~c_L* c )
     3.43294256E-02    2     2000004        -4   # BR(~g -> ~c_R  cb)
     3.43294256E-02    2    -2000004         4   # BR(~g -> ~c_R* c )
     3.43017494E-02    2     1000005        -5   # BR(~g -> ~b_1  bb)
     3.43017494E-02    2    -1000005         5   # BR(~g -> ~b_1* b )
     3.43600599E-02    2     2000005        -5   # BR(~g -> ~b_2  bb)
     3.43600599E-02    2    -2000005         5   # BR(~g -> ~b_2* b )
     1.13884938E-01    2     1000006        -6   # BR(~g -> ~t_1  tb)
     1.13884938E-01    2    -1000006         6   # BR(~g -> ~t_1* t )
     4.28195969E-02    2     2000006        -6   # BR(~g -> ~t_2  tb)
     4.28195969E-02    2    -2000006         6   # BR(~g -> ~t_2* t )
#
#         PDG            Width
DECAY   1000006     2.44543313E+03   # stop1 decays
#          BR         NDA      ID1       ID2
     2.22454504E-01    2     1000022         6   # BR(~t_1 -> ~chi_10 t )
     2.28250925E-01    2     1000023         6   # BR(~t_1 -> ~chi_20 t )
     9.90669988E-02    2     1000025         6   # BR(~t_1 -> ~chi_30 t )
     2.49224409E-05    2     1000035         6   # BR(~t_1 -> ~chi_40 t )
     4.50155048E-01    2     1000024         5   # BR(~t_1 -> ~chi_1+ b )
     4.76015603E-05    2     1000037         5   # BR(~t_1 -> ~chi_2+ b )
#
#         PDG            Width
DECAY   2000006     2.33606076E+03   # stop2 decays
#          BR         NDA      ID1       ID2
     2.35024668E-01    2     1000022         6   # BR(~t_2 -> ~chi_10 t )
     2.41429279E-01    2     1000023         6   # BR(~t_2 -> ~chi_20 t )
     7.56361384E-03    2     1000025         6   # BR(~t_2 -> ~chi_30 t )
     1.69326598E-01    2     1000035         6   # BR(~t_2 -> ~chi_40 t )
     1.15051713E-02    2     1000024         5   # BR(~t_2 -> ~chi_1+ b )
     3.38124842E-01    2     1000037         5   # BR(~t_2 -> ~chi_2+ b )
     7.25276396E-03    2     1000006        25   # BR(~t_2 -> ~t_1    h )
    -1.02269365E-02    2     1000006        23   # BR(~t_2 -> ~t_1    Z )
#
#         PDG            Width
DECAY   1000005     1.06786976E+03   # sbottom1 decays
#          BR         NDA      ID1       ID2
     1.53450618E-02    2     1000022         5   # BR(~b_1 -> ~chi_10 b )
     1.08104836E-02    2     1000023         5   # BR(~b_1 -> ~chi_20 b )
     3.55865453E-02    2     1000025         5   # BR(~b_1 -> ~chi_30 b )
     1.83929357E-01    2     1000035         5   # BR(~b_1 -> ~chi_40 b )
     5.33807192E-01    2    -1000024         6   # BR(~b_1 -> ~chi_1- t )
     3.68446483E-01    2    -1000037         6   # BR(~b_1 -> ~chi_2- t )
    -4.83964106E-02    2     1000006       -24   # BR(~b_1 -> ~t_1    W-)
    -9.95287122E-02    2     2000006       -24   # BR(~b_1 -> ~t_2    W-)
#
#         PDG            Width
DECAY   2000005     1.07394732E+03   # sbottom2 decays
#          BR         NDA      ID1       ID2
     1.04900364E-02    2     1000022         5   # BR(~b_2 -> ~chi_10 b )
     1.42159231E-02    2     1000023         5   # BR(~b_2 -> ~chi_20 b )
     3.55355156E-02    2     1000025         5   # BR(~b_2 -> ~chi_30 b )
     1.85711249E-01    2     1000035         5   # BR(~b_2 -> ~chi_40 b )
     5.34154661E-01    2    -1000024         6   # BR(~b_2 -> ~chi_1- t )
     3.72002743E-01    2    -1000037         6   # BR(~b_2 -> ~chi_2- t )
    -4.88949574E-02    2     1000006       -24   # BR(~b_2 -> ~t_1    W-)
    -1.03215171E-01    2     2000006       -24   # BR(~b_2 -> ~t_2    W-)
#
#         PDG            Width
DECAY   1000002     1.20178549E+03   # sup_L decays
#          BR         NDA      ID1       ID2
     1.53653319E-04    2     1000022         2   # BR(~u_L -> ~chi_10 u)
     8.41407524E-05    2     1000023         2   # BR(~u_L -> ~chi_20 u)
     1.35431273E-02    2     1000025         2   # BR(~u_L -> ~chi_30 u)
     3.28100095E-01    2     1000035         2   # BR(~u_L -> ~chi_40 u)
     1.23531767E-03    2     1000024         1   # BR(~u_L -> ~chi_1+ d)
     6.56883666E-01    2     1000037         1   # BR(~u_L -> ~chi_2+ d)
#
#         PDG            Width
DECAY   2000002     2.46542553E+02   # sup_R decays
#          BR         NDA      ID1       ID2
     2.81123603E-04    2     1000022         2   # BR(~u_R -> ~chi_10 u)
     1.49502347E-04    2     1000023         2   # BR(~u_R -> ~chi_20 u)
     9.99545559E-01    2     1000025         2   # BR(~u_R -> ~chi_30 u)
     2.38145617E-05    2     1000035         2   # BR(~u_R -> ~chi_40 u)
#
#         PDG            Width
DECAY   1000001     1.20178441E+03   # sdown_L decays
#          BR         NDA      ID1       ID2
     2.62206730E-04    2     1000022         1   # BR(~d_L -> ~chi_10 d)
     1.42607924E-04    2     1000023         1   # BR(~d_L -> ~chi_20 d)
     1.21086629E-02    2     1000025         1   # BR(~d_L -> ~chi_30 d)
     3.29367756E-01    2     1000035         1   # BR(~d_L -> ~chi_40 d)
     3.04264897E-05    2    -1000024         2   # BR(~d_L -> ~chi_1- u)
     6.58088340E-01    2    -1000037         2   # BR(~d_L -> ~chi_2- u)
#
#         PDG            Width
DECAY   2000001     6.16356435E+01   # sdown_R decays
#          BR         NDA      ID1       ID2
     2.81123603E-04    2     1000022         1   # BR(~d_R -> ~chi_10 d)
     1.49502347E-04    2     1000023         1   # BR(~d_R -> ~chi_20 d)
     9.99545559E-01    2     1000025         1   # BR(~d_R -> ~chi_30 d)
     2.38145617E-05    2     1000035         1   # BR(~d_R -> ~chi_40 d)
#
#         PDG            Width
DECAY   1000004     1.20178549E+03   # scharm_L decays
#          BR         NDA      ID1       ID2
     1.53653319E-04    2     1000022         4   # BR(~c_L -> ~chi_10 c)
     8.41407524E-05    2     1000023         4   # BR(~c_L -> ~chi_20 c)
     1.35431273E-02    2     1000025         4   # BR(~c_L -> ~chi_30 c)
     3.28100095E-01    2     1000035         4   # BR(~c_L -> ~chi_40 c)
     1.23531767E-03    2     1000024         3   # BR(~c_L -> ~chi_1+ s)
     6.56883666E-01    2     1000037         3   # BR(~c_L -> ~chi_2+ s)
#
#         PDG            Width
DECAY   2000004     2.46542553E+02   # scharm_R decays
#          BR         NDA      ID1       ID2
     2.81123603E-04    2     1000022         4   # BR(~c_R -> ~chi_10 c)
     1.49502347E-04    2     1000023         4   # BR(~c_R -> ~chi_20 c)
     9.99545559E-01    2     1000025         4   # BR(~c_R -> ~chi_30 c)
     2.38145617E-05    2     1000035         4   # BR(~c_R -> ~chi_40 c)
#
#         PDG            Width
DECAY   1000003     1.20178441E+03   # sstrange_L decays
#          BR         NDA      ID1       ID2
     2.62206730E-04    2     1000022         3   # BR(~s_L -> ~chi_10 s)
     1.42607924E-04    2     1000023         3   # BR(~s_L -> ~chi_20 s)
     1.21086629E-02    2     1000025         3   # BR(~s_L -> ~chi_30 s)
     3.29367756E-01    2     1000035         3   # BR(~s_L -> ~chi_40 s)
     3.04264897E-05    2    -1000024         4   # BR(~s_L -> ~chi_1- c)
     6.58088340E-01    2    -1000037         4   # BR(~s_L -> ~chi_2- c)
#
#         PDG            Width
DECAY   2000003     6.16356435E+01   # sstrange_R decays
#          BR         NDA      ID1       ID2
     2.81123603E-04    2     1000022         3   # BR(~s_R -> ~chi_10 s)
     1.49502347E-04    2     1000023         3   # BR(~s_R -> ~chi_20 s)
     9.99545559E-01    2     1000025         3   # BR(~s_R -> ~chi_30 s)
     2.38145617E-05    2     1000035         3   # BR(~s_R -> ~chi_40 s)
#
#         PDG            Width
DECAY   1000011     1.32682043E+03   # selectron_L decays
#          BR         NDA      ID1       ID2
     6.70868617E-05    2     1000022        11   # BR(~e_L -> ~chi_10 e-)
     3.72097970E-05    2     1000023        11   # BR(~e_L -> ~chi_20 e-)
     1.06578466E-01    2     1000025        11   # BR(~e_L -> ~chi_30 e-)
     2.96427826E-01    2     1000035        11   # BR(~e_L -> ~chi_40 e-)
     2.76078552E-05    2    -1000024        12   # BR(~e_L -> ~chi_1- nu_e)
     5.96861803E-01    2    -1000037        12   # BR(~e_L -> ~chi_2- nu_e)
#
#         PDG            Width
DECAY   2000011     5.55488252E+02   # selectron_R decays
#          BR         NDA      ID1       ID2
     2.81231154E-04    2     1000022        11   # BR(~e_R -> ~chi_10 e-)
     1.49559461E-04    2     1000023        11   # BR(~e_R -> ~chi_20 e-)
     9.99545396E-01    2     1000025        11   # BR(~e_R -> ~chi_30 e-)
     2.38131792E-05    2     1000035        11   # BR(~e_R -> ~chi_40 e-)
#
#         PDG            Width
DECAY   1000013     1.32682043E+03   # smuon_L decays
#          BR         NDA      ID1       ID2
     6.70868617E-05    2     1000022        13   # BR(~mu_L -> ~chi_10 mu-)
     3.72097970E-05    2     1000023        13   # BR(~mu_L -> ~chi_20 mu-)
     1.06578466E-01    2     1000025        13   # BR(~mu_L -> ~chi_30 mu-)
     2.96427826E-01    2     1000035        13   # BR(~mu_L -> ~chi_40 mu-)
     2.76078552E-05    2    -1000024        14   # BR(~mu_L -> ~chi_1- nu_mu)
     5.96861803E-01    2    -1000037        14   # BR(~mu_L -> ~chi_2- nu_mu)
#
#         PDG            Width
DECAY   2000013     5.55488252E+02   # smuon_R decays
#          BR         NDA      ID1       ID2
     2.81231154E-04    2     1000022        13   # BR(~mu_R -> ~chi_10 mu-)
     1.49559461E-04    2     1000023        13   # BR(~mu_R -> ~chi_20 mu-)
     9.99545396E-01    2     1000025        13   # BR(~mu_R -> ~chi_30 mu-)
     2.38131792E-05    2     1000035        13   # BR(~mu_R -> ~chi_40 mu-)
#
#         PDG            Width
DECAY   1000015     9.67827278E+02   # stau_1 decays
#          BR         NDA      ID1       ID2
     1.15636073E-02    2     1000022        15   # BR(~tau_1 -> ~chi_10  tau-)
     7.56119770E-03    2     1000023        15   # BR(~tau_1 -> ~chi_20  tau-)
     3.59690604E-01    2     1000025        15   # BR(~tau_1 -> ~chi_30  tau-)
     2.02808695E-01    2     1000035        15   # BR(~tau_1 -> ~chi_40  tau-)
     1.00215751E-02    2    -1000024        16   # BR(~tau_1 -> ~chi_1-  nu_tau)
     4.08354321E-01    2    -1000037        16   # BR(~tau_1 -> ~chi_2-  nu_tau)
#
#         PDG            Width
DECAY   2000015     9.67740625E+02   # stau_2 decays
#          BR         NDA      ID1       ID2
     7.26724342E-03    2     1000022        15   # BR(~tau_2 -> ~chi_10  tau-)
     1.06849688E-02    2     1000023        15   # BR(~tau_2 -> ~chi_20  tau-)
     3.60146323E-01    2     1000025        15   # BR(~tau_2 -> ~chi_30  tau-)
     2.03604946E-01    2     1000035        15   # BR(~tau_2 -> ~chi_40  tau-)
     8.35936557E-03    2    -1000024        16   # BR(~tau_2 -> ~chi_1-  nu_tau)
     4.09937153E-01    2    -1000037        16   # BR(~tau_2 -> ~chi_2-  nu_tau)
#
#         PDG            Width
DECAY   1000012     1.32682121E+03   # snu_eL decays
#          BR         NDA      ID1       ID2
     3.62578024E-04    2     1000022        12   # BR(~nu_eL -> ~chi_10 nu_e)
     1.96362073E-04    2     1000023        12   # BR(~nu_eL -> ~chi_20 nu_e)
     1.02675091E-01    2     1000025        12   # BR(~nu_eL -> ~chi_30 nu_e)
     2.99875723E-01    2     1000035        12   # BR(~nu_eL -> ~chi_40 nu_e)
     1.12088120E-03    2     1000024        11   # BR(~nu_eL -> ~chi_1+ e-)
     5.95769365E-01    2     1000037        11   # BR(~nu_eL -> ~chi_2+ e-)
#
#         PDG            Width
DECAY   1000014     1.32682121E+03   # snu_muL decays
#          BR         NDA      ID1       ID2
     3.62578024E-04    2     1000022        14   # BR(~nu_muL -> ~chi_10 nu_mu)
     1.96362073E-04    2     1000023        14   # BR(~nu_muL -> ~chi_20 nu_mu)
     1.02675091E-01    2     1000025        14   # BR(~nu_muL -> ~chi_30 nu_mu)
     2.99875723E-01    2     1000035        14   # BR(~nu_muL -> ~chi_40 nu_mu)
     1.12088120E-03    2     1000024        13   # BR(~nu_muL -> ~chi_1+ mu-)
     5.95769365E-01    2     1000037        13   # BR(~nu_muL -> ~chi_2+ mu-)
#
#         PDG            Width
DECAY   1000016     1.34457428E+03   # snu_tauL decays
#          BR         NDA      ID1       ID2
     3.57790729E-04    2     1000022        16   # BR(~nu_tauL -> ~chi_10 nu_tau)
     1.93769409E-04    2     1000023        16   # BR(~nu_tauL -> ~chi_20 nu_tau)
     1.01319422E-01    2     1000025        16   # BR(~nu_tauL -> ~chi_30 nu_tau)
     2.95916317E-01    2     1000035        16   # BR(~nu_tauL -> ~chi_40 nu_tau)
     1.43089600E-02    2     1000024        15   # BR(~nu_tauL -> ~chi_1+ tau-)
     5.87903741E-01    2     1000037        15   # BR(~nu_tauL -> ~chi_2+ tau-)
#
#         PDG            Width
DECAY   1000024     4.00344994E-12   # chargino1+ decays
#           BR         NDA      ID1       ID2       ID3
     6.03117314E-01    3     1000022         2        -1   # BR(~chi_1+ -> ~chi_10 u    db)
     2.01039105E-01    3     1000022       -11        12   # BR(~chi_1+ -> ~chi_10 e+   nu_e)
     1.95843581E-01    3     1000022       -13        14   # BR(~chi_1+ -> ~chi_10 mu+  nu_mu)
#
#         PDG            Width
DECAY   1000037     1.86897475E+01   # chargino2+ decays
#          BR         NDA      ID1       ID2
     2.53299472E-01    2     1000024        23   # BR(~chi_2+ -> ~chi_1+  Z )
     2.37433364E-01    2     1000022        24   # BR(~chi_2+ -> ~chi_10  W+)
     2.43561963E-01    2     1000023        24   # BR(~chi_2+ -> ~chi_20  W+)
     2.45404606E-04    2     1000025        24   # BR(~chi_2+ -> ~chi_30  W+)
     2.65459796E-01    2     1000024        25   # BR(~chi_2+ -> ~chi_1+  h )
#
#         PDG            Width
DECAY   1000022     0.00000000E+00   # neutralino1 decays
#
#         PDG            Width
DECAY   1000023     3.41060399E-10   # neutralino2 decays
##          BR         NDA      ID1       ID2
#     1.56740962E-01    2     1000022        22   # BR(~chi_20 -> ~chi_10 gam)
##           BR         NDA      ID1       ID2       ID3
#     1.25477644E-01    3     1000022        -2         2   # BR(~chi_20 -> ~chi_10 ub      u)
#     1.63628607E-01    3     1000022        -1         1   # BR(~chi_20 -> ~chi_10 db      d)
#     1.20762745E-02    3     1000022        -4         4   # BR(~chi_20 -> ~chi_10 cb      c)
#     1.59299773E-01    3     1000022        -3         3   # BR(~chi_20 -> ~chi_10 sb      s)
     3.82634724E-02    3     1000022       -11        11   # BR(~chi_20 -> ~chi_10 e+      e-)
     3.80632956E-02    3     1000022       -13        13   # BR(~chi_20 -> ~chi_10 mu+     mu-)
#     7.64144350E-02    3     1000022       -12        12   # BR(~chi_20 -> ~chi_10 nu_eb   nu_e)
#     7.64144350E-02    3     1000022       -14        14   # BR(~chi_20 -> ~chi_10 nu_mub  nu_mu)
#     7.64144350E-02    3     1000022       -16        16   # BR(~chi_20 -> ~chi_10 nu_taub nu_tau)
#     2.29594633E-02    3     1000024        -2         1   # BR(~chi_20 -> ~chi_1+ ub      d)
#     2.29594633E-02    3    -1000024        -1         2   # BR(~chi_20 -> ~chi_1- db      u)
#     4.61537165E-04    3     1000024        -4         3   # BR(~chi_20 -> ~chi_1+ cb      s)
#     4.61537165E-04    3    -1000024        -3         4   # BR(~chi_20 -> ~chi_1- sb      c)
#     7.65315442E-03    3     1000024       -12        11   # BR(~chi_20 -> ~chi_1+ nu_eb   e-)
#     7.65315442E-03    3    -1000024        12       -11   # BR(~chi_20 -> ~chi_1- nu_e    e+)
#     7.52885243E-03    3     1000024       -14        13   # BR(~chi_20 -> ~chi_1+ nu_mub  mu-)
#     7.52885243E-03    3    -1000024        14       -13   # BR(~chi_20 -> ~chi_1- nu_mu   mu+)
#     3.26188254E-07    3     1000024       -16        15   # BR(~chi_20 -> ~chi_1+ nu_taub tau-)
#     3.26188254E-07    3    -1000024        16       -15   # BR(~chi_20 -> ~chi_1- nu_tau  tau+)
#         PDG            Width
DECAY   1000025     5.78479326E+00   # neutralino3 decays
#          BR         NDA      ID1       ID2
     8.37349199E-02    2     1000022        23   # BR(~chi_30 -> ~chi_10   Z )
     1.66231465E-01    2     1000023        23   # BR(~chi_30 -> ~chi_20   Z )
     2.45262852E-01    2     1000024       -24   # BR(~chi_30 -> ~chi_1+   W-)
     2.45262852E-01    2    -1000024        24   # BR(~chi_30 -> ~chi_1-   W+)
     1.69535788E-01    2     1000022        25   # BR(~chi_30 -> ~chi_10   h )
     8.99721233E-02    2     1000023        25   # BR(~chi_30 -> ~chi_20   h )
#
#         PDG            Width
DECAY   1000035     1.86900779E+01   # neutralino4 decays
#          BR         NDA      ID1       ID2
     8.67463571E-02    2     1000022        23   # BR(~chi_40 -> ~chi_10   Z )
     1.67907601E-01    2     1000023        23   # BR(~chi_40 -> ~chi_20   Z )
     1.13318123E-06    2     1000025        23   # BR(~chi_40 -> ~chi_30   Z )
     2.39797673E-01    2     1000024       -24   # BR(~chi_40 -> ~chi_1+   W-)
     2.39797673E-01    2    -1000024        24   # BR(~chi_40 -> ~chi_1-   W+)
     1.71894253E-01    2     1000022        25   # BR(~chi_40 -> ~chi_10   h )
     9.36443482E-02    2     1000023        25   # BR(~chi_40 -> ~chi_20   h )
     2.10961254E-04    2     1000025        25   # BR(~chi_40 -> ~chi_30   h )
#
#         PDG            Width
DECAY        25                NaN   # h decays
#          BR         NDA      ID1       ID2
                NaN    2           5        -5   # BR(h -> b       bb     )
                NaN    2         -15        15   # BR(h -> tau+    tau-   )
                NaN    2         -13        13   # BR(h -> mu+     mu-    )
                NaN    2           3        -3   # BR(h -> s       sb     )
                NaN    2           4        -4   # BR(h -> c       cb     )
                NaN    2           6        -6   # BR(h -> t       tb     )
                NaN    2          21        21   # BR(h -> g       g      )
                NaN    2          22        22   # BR(h -> gam     gam    )
                NaN    2          22        23   # BR(h -> Z       gam    )
                NaN    2          24       -24   # BR(h -> W+      W-     )
                NaN    2          23        23   # BR(h -> Z       Z      )
                NaN    2     1000024  -1000024   # BR(h -> ~chi_1+ ~chi_1-)
                NaN    2     1000037  -1000037   # BR(h -> ~chi_2+ ~chi_2-)
                NaN    2     1000024  -1000037   # BR(h -> ~chi_1+ ~chi_2-)
                NaN    2     1000037  -1000024   # BR(h -> ~chi_2+ ~chi_1-)
                NaN    2     1000022   1000022   # BR(h -> ~chi_10 ~chi_10)
                NaN    2     1000023   1000023   # BR(h -> ~chi_20 ~chi_20)
                NaN    2     1000025   1000025   # BR(h -> ~chi_30 ~chi_30)
                NaN    2     1000035   1000035   # BR(h -> ~chi_40 ~chi_40)
                NaN    2     1000022   1000023   # BR(h -> ~chi_10 ~chi_20)
                NaN    2     1000022   1000025   # BR(h -> ~chi_10 ~chi_30)
                NaN    2     1000022   1000035   # BR(h -> ~chi_10 ~chi_40)
                NaN    2     1000023   1000025   # BR(h -> ~chi_20 ~chi_30)
                NaN    2     1000023   1000035   # BR(h -> ~chi_20 ~chi_40)
                NaN    2     1000025   1000035   # BR(h -> ~chi_30 ~chi_40)
                NaN    2     1000002  -1000002   # BR(h -> ~u_L    ~u_L*  )
                NaN    2     2000002  -2000002   # BR(h -> ~u_R    ~u_R*  )
                NaN    2     1000004  -1000004   # BR(h -> ~c_L    ~c_L*  )
                NaN    2     2000004  -2000004   # BR(h -> ~c_R    ~c_R*  )
                NaN    2     1000006  -1000006   # BR(h -> ~t_1    ~t_1*  )
                NaN    2     2000006  -2000006   # BR(h -> ~t_2    ~t_2*  )
                NaN    2     1000006  -2000006   # BR(h -> ~t_1    ~t_2*  )
                NaN    2     2000006  -1000006   # BR(h -> ~t_2    ~t_1*  )
                NaN    2     1000001  -1000001   # BR(h -> ~d_L    ~d_L*  )
                NaN    2     2000001  -2000001   # BR(h -> ~d_R    ~d_R*  )
                NaN    2     1000003  -1000003   # BR(h -> ~s_L    ~s_L*  )
                NaN    2     2000003  -2000003   # BR(h -> ~s_R    ~s_R*  )
                NaN    2     1000005  -1000005   # BR(h -> ~b_1    ~b_1*  )
                NaN    2     2000005  -2000005   # BR(h -> ~b_2    ~b_2*  )
                NaN    2     1000005  -2000005   # BR(h -> ~b_1    ~b_2*  )
                NaN    2     2000005  -1000005   # BR(h -> ~b_2    ~b_1*  )
                NaN    2     1000011  -1000011   # BR(h -> ~e_L-   ~e_L+  )
                NaN    2     2000011  -2000011   # BR(h -> ~e_R-   ~e_R+  )
                NaN    2     1000013  -1000013   # BR(h -> ~mu_L-  ~mu_L+ )
                NaN    2     2000013  -2000013   # BR(h -> ~mu_R-  ~mu_R+ )
                NaN    2     1000015  -1000015   # BR(h -> ~tau_1- ~tau_1+)
                NaN    2     2000015  -2000015   # BR(h -> ~tau_2- ~tau_2+)
                NaN    2     1000015  -2000015   # BR(h -> ~tau_1- ~tau_2+)
                NaN    2     2000015  -1000015   # BR(h -> ~tau_2- ~tau_1+)
                NaN    2     1000012  -1000012   # BR(h -> ~nu_eL  ~nu_eL*   )
                NaN    2     1000014  -1000014   # BR(h -> ~nu_muL ~nu_muL*  )
                NaN    2     1000016  -1000016   # BR(h -> ~nu_tauL ~nu_tauL*)
#
#         PDG            Width
DECAY        35                NaN   # H decays
#          BR         NDA      ID1       ID2
                NaN    2           5        -5   # BR(H -> b       bb     )
                NaN    2         -15        15   # BR(H -> tau+    tau-   )
                NaN    2         -13        13   # BR(H -> mu+     mu-    )
                NaN    2           3        -3   # BR(H -> s       sb     )
                NaN    2           4        -4   # BR(H -> c       cb     )
                NaN    2           6        -6   # BR(H -> t       tb     )
                NaN    2          21        21   # BR(H -> g       g      )
                NaN    2          22        22   # BR(H -> gam     gam    )
                NaN    2          23        22   # BR(H -> Z       gam    )
                NaN    2          24       -24   # BR(H -> W+      W-     )
                NaN    2          23        23   # BR(H -> Z       Z      )
                NaN    2          25        25   # BR(H -> h       h      )
                NaN    2          36        36   # BR(H -> A       A      )
                NaN    2          23        36   # BR(H -> Z       A      )
                NaN    2          24       -37   # BR(H -> W+      H-     )
                NaN    2         -24        37   # BR(H -> W-      H+     )
                NaN    2     1000024  -1000024   # BR(H -> ~chi_1+ ~chi_1-)
                NaN    2     1000037  -1000037   # BR(H -> ~chi_2+ ~chi_2-)
                NaN    2     1000024  -1000037   # BR(H -> ~chi_1+ ~chi_2-)
                NaN    2     1000037  -1000024   # BR(H -> ~chi_2+ ~chi_1-)
                NaN    2     1000022   1000022   # BR(H -> ~chi_10 ~chi_10)
                NaN    2     1000023   1000023   # BR(H -> ~chi_20 ~chi_20)
                NaN    2     1000025   1000025   # BR(H -> ~chi_30 ~chi_30)
                NaN    2     1000035   1000035   # BR(H -> ~chi_40 ~chi_40)
                NaN    2     1000022   1000023   # BR(H -> ~chi_10 ~chi_20)
                NaN    2     1000022   1000025   # BR(H -> ~chi_10 ~chi_30)
                NaN    2     1000022   1000035   # BR(H -> ~chi_10 ~chi_40)
                NaN    2     1000023   1000025   # BR(H -> ~chi_20 ~chi_30)
                NaN    2     1000023   1000035   # BR(H -> ~chi_20 ~chi_40)
                NaN    2     1000025   1000035   # BR(H -> ~chi_30 ~chi_40)
                NaN    2     1000002  -1000002   # BR(H -> ~u_L    ~u_L*  )
                NaN    2     2000002  -2000002   # BR(H -> ~u_R    ~u_R*  )
                NaN    2     1000004  -1000004   # BR(H -> ~c_L    ~c_L*  )
                NaN    2     2000004  -2000004   # BR(H -> ~c_R    ~c_R*  )
                NaN    2     1000006  -1000006   # BR(H -> ~t_1    ~t_1*  )
                NaN    2     2000006  -2000006   # BR(H -> ~t_2    ~t_2*  )
                NaN    2     1000006  -2000006   # BR(H -> ~t_1    ~t_2*  )
                NaN    2     2000006  -1000006   # BR(H -> ~t_2    ~t_1*  )
                NaN    2     1000001  -1000001   # BR(H -> ~d_L    ~d_L*  )
                NaN    2     2000001  -2000001   # BR(H -> ~d_R    ~d_R*  )
                NaN    2     1000003  -1000003   # BR(H -> ~s_L    ~s_L*  )
                NaN    2     2000003  -2000003   # BR(H -> ~s_R    ~s_R*  )
                NaN    2     1000005  -1000005   # BR(H -> ~b_1    ~b_1*  )
                NaN    2     2000005  -2000005   # BR(H -> ~b_2    ~b_2*  )
                NaN    2     1000005  -2000005   # BR(H -> ~b_1    ~b_2*  )
                NaN    2     2000005  -1000005   # BR(H -> ~b_2    ~b_1*  )
                NaN    2     1000011  -1000011   # BR(H -> ~e_L-   ~e_L+  )
                NaN    2     2000011  -2000011   # BR(H -> ~e_R-   ~e_R+  )
                NaN    2     1000013  -1000013   # BR(H -> ~mu_L-  ~mu_L+ )
                NaN    2     2000013  -2000013   # BR(H -> ~mu_R-  ~mu_R+ )
                NaN    2     1000015  -1000015   # BR(H -> ~tau_1- ~tau_1+)
                NaN    2     2000015  -2000015   # BR(H -> ~tau_2- ~tau_2+)
                NaN    2     1000015  -2000015   # BR(H -> ~tau_1- ~tau_2+)
                NaN    2     2000015  -1000015   # BR(H -> ~tau_2- ~tau_1+)
                NaN    2     1000012  -1000012   # BR(H -> ~nu_eL  ~nu_eL*   )
                NaN    2     1000014  -1000014   # BR(H -> ~nu_muL ~nu_muL*  )
                NaN    2     1000016  -1000016   # BR(H -> ~nu_tauL ~nu_tauL*)
#
#         PDG            Width
DECAY        36     1.51347712E+03   # A decays
#          BR         NDA      ID1       ID2
     4.51783916E-02    2           5        -5   # BR(A -> b       bb     )
     1.16172270E-02    2         -15        15   # BR(A -> tau+    tau-   )
     4.10664075E-05    2         -13        13   # BR(A -> mu+     mu-    )
     3.41328086E-05    2           3        -3   # BR(A -> s       sb     )
     2.14652343E-07    2           4        -4   # BR(A -> c       cb     )
     2.14136237E-02    2           6        -6   # BR(A -> t       tb     )
     1.99681734E-07    2          21        21   # BR(A -> g       g      )
     7.43871632E-10    2          22        22   # BR(A -> gam     gam    )
     5.73437886E-10    2          23        22   # BR(A -> Z       gam    )
     3.27391779E-09    2          23        25   # BR(A -> Z       h      )
     1.07796067E-03    2     1000024  -1000024   # BR(A -> ~chi_1+ ~chi_1-)
     7.33019382E-05    2     1000037  -1000037   # BR(A -> ~chi_2+ ~chi_2-)
     2.80199958E-01    2     1000024  -1000037   # BR(A -> ~chi_1+ ~chi_2-)
     2.80199958E-01    2     1000037  -1000024   # BR(A -> ~chi_2+ ~chi_1-)
     3.94489115E-04    2     1000022   1000022   # BR(A -> ~chi_10 ~chi_10)
     1.34682339E-04    2     1000023   1000023   # BR(A -> ~chi_20 ~chi_20)
     4.68538337E-06    2     1000025   1000025   # BR(A -> ~chi_30 ~chi_30)
     3.70525509E-05    2     1000035   1000035   # BR(A -> ~chi_40 ~chi_40)
     6.55527833E-07    2     1000022   1000023   # BR(A -> ~chi_10 ~chi_20)
     4.76291385E-02    2     1000022   1000025   # BR(A -> ~chi_10 ~chi_30)
     1.72842915E-01    2     1000022   1000035   # BR(A -> ~chi_10 ~chi_40)
     3.00582768E-02    2     1000023   1000025   # BR(A -> ~chi_20 ~chi_30)
     1.09035284E-01    2     1000023   1000035   # BR(A -> ~chi_20 ~chi_40)
     2.67820931E-05    2     1000025   1000035   # BR(A -> ~chi_30 ~chi_40)
#
#         PDG            Width
DECAY        37     1.51214263E+03   # H+ decays
#          BR         NDA      ID1       ID2
     7.11342388E-05    2           4        -5   # BR(H+ -> c       bb     )
     1.16274691E-02    2         -15        16   # BR(H+ -> tau+    nu_tau )
     4.11026126E-05    2         -13        14   # BR(H+ -> mu+     nu_mu  )
     4.55257183E-07    2           2        -5   # BR(H+ -> u       bb     )
     1.64604281E-06    2           2        -3   # BR(H+ -> u       sb     )
     3.40450121E-05    2           4        -3   # BR(H+ -> c       sb     )
     6.56972940E-02    2           6        -5   # BR(H+ -> t       bb     )
     3.27680011E-09    2          24        25   # BR(H+ -> W+      h      )
     2.57077733E-05    2     1000024   1000022   # BR(H+ -> ~chi_1+ ~chi_10)
     1.00023192E-04    2     1000024   1000023   # BR(H+ -> ~chi_1+ ~chi_20)
     8.10620597E-02    2     1000024   1000025   # BR(H+ -> ~chi_1+ ~chi_30)
     2.79307719E-01    2     1000024   1000035   # BR(H+ -> ~chi_1+ ~chi_40)
     2.84559351E-01    2     1000037   1000022   # BR(H+ -> ~chi_2+ ~chi_10)
     2.77443823E-01    2     1000037   1000023   # BR(H+ -> ~chi_2+ ~chi_20)
     2.81666342E-05    2     1000037   1000025   # BR(H+ -> ~chi_2+ ~chi_30)
     6.07559492E-10    2     1000037   1000035   # BR(H+ -> ~chi_2+ ~chi_40)
'''

import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *


SLHATable = baseSLHATable.replace('%MSQ%','1200').replace('%MCHI%','10').replace('%MSINGLINO%','900').replace('%MSINGLET%','800')

generator = cms.EDFilter("Pythia8GeneratorFilter",
    #crossSection = cms.untracked.double(5.72e+07),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(True),
    comEnergy = cms.double(13000.0),
    SLHATableForPythia8  = cms.string(SLHATable),    
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(
            #'SUSY:all = on',        
            #'SUSY:qqbar2chi0chi0 = on',
            'SUSY:qqbar2chi+-chi0 = on',            
            'SUSY:idA = 1000023',
            'SUSY:idB = 1000024',
            'print:quiet=false',
            'SLHA:allowUserOverride = true',  
            'SLHA:keepSM = on',
            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'processParameters',
                                    )
        
        )
                         )

ProductionFilterSequence = cms.Sequence(generator)
