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
         0     1.00000031E+05   # EWSB                
         1     1.29349486E+03   # M_1                 
         2     1.29349486E+03   # M_2                 
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
        24     8.05051401E+01   # W+
        25     1.70402413E+02   # h
        35     1.00000300E+05   # H
        36     1.00000000E+05   # A
        37     9.99999171E+04   # H+
         5     4.87877839E+00   # b-quark pole mass calculated from mb(mb)_Msbar
   1000001     1.02565625E+05   # ~d_L
   2000001     1.02565613E+05   # ~d_R
   1000002     1.02565598E+05   # ~u_L
   2000002     1.02565604E+05   # ~u_R
   1000003     1.02565625E+05   # ~s_L
   2000003     1.02565613E+05   # ~s_R
   1000004     1.02565598E+05   # ~c_L
   2000004     1.02565604E+05   # ~c_R
   1000005     1.02564568E+05   # ~b_1
   2000005     1.02566670E+05   # ~b_2
   1000006     1.00819916E+05   # ~t_1
   2000006     1.02323269E+05   # ~t_2
   1000011     1.00000009E+05   # ~e_L
   2000011     1.00000010E+05   # ~e_R
   1000012     9.99999810E+04   # ~nu_eL
   1000013     1.00000009E+05   # ~mu_L
   2000013     1.00000010E+05   # ~mu_R
   1000014     9.99999810E+04   # ~nu_muL
   1000015     9.99978162E+04   # ~tau_1
   2000015     1.00002203E+05   # ~tau_2
   1000016     9.99999810E+04   # ~nu_tauL
   1000021     1.04586106E+05   # ~g
   1000022     1.19054877E+02   # ~chi_10
   1000023    -1.24709746E+02   # ~chi_20
   1000025     1.28269575E+03   # ~chi_30
   1000035     1.47001412E+03   # ~chi_40
   1000024     1.21505592E+02   # ~chi_1+
   1000037     1.46998890E+03   # ~chi_2+
#
BLOCK NMIX  # Neutralino Mixing Matrix
  1  1     2.98351140E-02   # N_11
  1  2    -4.35467368E-02   # N_12
  1  3     7.14604355E-01   # N_13
  1  4    -6.97534346E-01   # N_14
  2  1     2.02919900E-02   # N_21
  2  2    -3.03397239E-02   # N_22
  2  3    -6.99422061E-01   # N_23
  2  4    -7.13776237E-01   # N_24
  3  1     9.99267936E-01   # N_31
  3  2     1.46221540E-02   # N_32
  3  3    -7.00540279E-03   # N_33
  3  4     3.46512462E-02   # N_34
  4  1     1.27158576E-02   # N_41
  4  2    -9.98483538E-01   # N_42
  4  3    -1.00160386E-02   # N_43
  4  4     5.26175869E-02   # N_44
#
BLOCK UMIX  # Chargino Mixing Matrix U
  1  1    -1.40582730E-02   # U_11
  1  2     9.99901178E-01   # U_12
  2  1     9.99901178E-01   # U_21
  2  2     1.40582730E-02   # U_22
#
BLOCK VMIX  # Chargino Mixing Matrix V
  1  1    -7.39609274E-02   # V_11
  1  2     9.97261140E-01   # V_12
  2  1     9.97261140E-01   # V_21
  2  2     7.39609274E-02   # V_22
#
BLOCK STOPMIX  # Stop Mixing Matrix
  1  1     3.61395799E-02   # cos(theta_t)
  1  2     9.99346752E-01   # sin(theta_t)
  2  1    -9.99346752E-01   # -sin(theta_t)
  2  2     3.61395799E-02   # cos(theta_t)
#
BLOCK SBOTMIX  # Sbottom Mixing Matrix
  1  1     7.05065351E-01   # cos(theta_b)
  1  2     7.09142335E-01   # sin(theta_b)
  2  1    -7.09142335E-01   # -sin(theta_b)
  2  2     7.05065351E-01   # cos(theta_b)
#
BLOCK STAUMIX  # Stau Mixing Matrix
  1  1     7.07161473E-01   # cos(theta_tau)
  1  2     7.07052085E-01   # sin(theta_tau)
  2  1    -7.07052085E-01   # -sin(theta_tau)
  2  2     7.07161473E-01   # cos(theta_tau)
#
BLOCK ALPHA  # Higgs mixing
          -1.08195716E-01   # Mixing angle in the neutral Higgs boson sector
#
BLOCK HMIX Q=  1.00000031E+05  # DRbar Higgs Parameters
         1     1.15000000E+02   # mu(Q)               
         2     9.20643098E+00   # tanbeta(Q)          
         3     2.40691537E+02   # vev(Q)              
         4     9.92211211E+09   # MA^2(Q)             
#
BLOCK GAUGE Q=  1.00000031E+05  # The gauge couplings
     1     3.73837254E-01   # gprime(Q) DRbar
     2     6.32434320E-01   # g(Q) DRbar
     3     8.77149495E-01   # g3(Q) DRbar
#
BLOCK AU Q=  1.00000031E+05  # The trilinear couplings
  1  1    -6.77437438E+05   # A_u(Q) DRbar
  2  2    -6.77437438E+05   # A_c(Q) DRbar
  3  3    -1.00000000E+05   # A_t(Q) DRbar
#
BLOCK AD Q=  1.00000031E+05  # The trilinear couplings
  1  1    -8.59633345E+05   # A_d(Q) DRbar
  2  2    -8.59633345E+05   # A_s(Q) DRbar
  3  3    -1.00000000E+05   # A_b(Q) DRbar
#
BLOCK AE Q=  1.00000031E+05  # The trilinear couplings
  1  1    -2.53493493E+05   # A_e(Q) DRbar
  2  2    -2.53493493E+05   # A_mu(Q) DRbar
  3  3    -2.51737263E+05   # A_tau(Q) DRbar
#
BLOCK Yu Q=  1.00000031E+05  # The Yukawa couplings
  1  1     0.00000000E+00   # y_u(Q) DRbar
  2  2     0.00000000E+00   # y_c(Q) DRbar
  3  3     7.49844727E-01   # y_t(Q) DRbar
#
BLOCK Yd Q=  1.00000031E+05  # The Yukawa couplings
  1  1     0.00000000E+00   # y_d(Q) DRbar
  2  2     0.00000000E+00   # y_s(Q) DRbar
  3  3     1.16393728E-01   # y_b(Q) DRbar
#
BLOCK Ye Q=  1.00000031E+05  # The Yukawa couplings
  1  1     0.00000000E+00   # y_e(Q) DRbar
  2  2     0.00000000E+00   # y_mu(Q) DRbar
  3  3     9.46636225E-02   # y_tau(Q) DRbar
#
BLOCK MSOFT Q=  1.00000031E+05  # The soft SUSY breaking masses at the scale Q
         1     1.29349486E+03   # M_1                 
         2     1.29349486E+03   # M_2                 
         3     1.00000000E+05   # M_3                 
        14    -6.77437438E+05   # A_u                 
        15    -8.59633345E+05   # A_d                 
        16    -2.53493493E+05   # A_e                 
        21     9.85910273E+09   # M^2_Hd              
        22     3.33691025E+08   # M^2_Hu              
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
DECAY         6     1.38384465E+00   # top decays
#          BR         NDA      ID1       ID2
     1.00000000E+00    2           5        24   # BR(t ->  b    W+)
#
#         PDG            Width
DECAY   1000021     3.47414594E+01   # gluino decays
#          BR         NDA      ID1       ID2
     3.42824911E-02    2     1000001        -1   # BR(~g -> ~d_L  db)
     3.42824911E-02    2    -1000001         1   # BR(~g -> ~d_L* d )
     3.42828944E-02    2     2000001        -1   # BR(~g -> ~d_R  db)
     3.42828944E-02    2    -2000001         1   # BR(~g -> ~d_R* d )
     3.42833985E-02    2     1000002        -2   # BR(~g -> ~u_L  ub)
     3.42833985E-02    2    -1000002         2   # BR(~g -> ~u_L* u )
     3.42831968E-02    2     2000002        -2   # BR(~g -> ~u_R  ub)
     3.42831968E-02    2    -2000002         2   # BR(~g -> ~u_R* u )
     3.42824911E-02    2     1000003        -3   # BR(~g -> ~s_L  sb)
     3.42824911E-02    2    -1000003         3   # BR(~g -> ~s_L* s )
     3.42828944E-02    2     2000003        -3   # BR(~g -> ~s_R  sb)
     3.42828944E-02    2    -2000003         3   # BR(~g -> ~s_R* s )
     3.42833985E-02    2     1000004        -4   # BR(~g -> ~c_L  cb)
     3.42833985E-02    2    -1000004         4   # BR(~g -> ~c_L* c )
     3.42831968E-02    2     2000004        -4   # BR(~g -> ~c_R  cb)
     3.42831968E-02    2    -2000004         4   # BR(~g -> ~c_R* c )
     3.42516649E-02    2     1000005        -5   # BR(~g -> ~b_1  bb)
     3.42516649E-02    2    -1000005         5   # BR(~g -> ~b_1* b )
     3.43099194E-02    2     2000005        -5   # BR(~g -> ~b_2  bb)
     3.43099194E-02    2    -2000005         5   # BR(~g -> ~b_2* b )
     1.14307880E-01    2     1000006        -6   # BR(~g -> ~t_1  tb)
     1.14307880E-01    2    -1000006         6   # BR(~g -> ~t_1* t )
     4.28665738E-02    2     2000006        -6   # BR(~g -> ~t_2  tb)
     4.28665738E-02    2    -2000006         6   # BR(~g -> ~t_2* t )
#
#         PDG            Width
DECAY   1000006     2.45752762E+03   # stop1 decays
#          BR         NDA      ID1       ID2
     2.20230717E-01    2     1000022         6   # BR(~t_1 -> ~chi_10 t )
     2.30254038E-01    2     1000023         6   # BR(~t_1 -> ~chi_20 t )
     9.87164116E-02    2     1000025         6   # BR(~t_1 -> ~chi_30 t )
     4.00730602E-04    2     1000035         6   # BR(~t_1 -> ~chi_40 t )
     4.49629030E-01    2     1000024         5   # BR(~t_1 -> ~chi_1+ b )
     7.69073062E-04    2     1000037         5   # BR(~t_1 -> ~chi_2+ b )
#
#         PDG            Width
DECAY   2000006     2.34723983E+03   # stop2 decays
#          BR         NDA      ID1       ID2
     2.32014687E-01    2     1000022         6   # BR(~t_2 -> ~chi_10 t )
     2.43131021E-01    2     1000023         6   # BR(~t_2 -> ~chi_20 t )
     8.71464175E-03    2     1000025         6   # BR(~t_2 -> ~chi_30 t )
     1.69709933E-01    2     1000035         6   # BR(~t_2 -> ~chi_40 t )
     1.17563147E-02    2     1000024         5   # BR(~t_2 -> ~chi_1+ b )
     3.37593907E-01    2     1000037         5   # BR(~t_2 -> ~chi_2+ b )
     7.31539061E-03    2     1000006        25   # BR(~t_2 -> ~t_1    h )
    -1.02358944E-02    2     1000006        23   # BR(~t_2 -> ~t_1    Z )
#
#         PDG            Width
DECAY   1000005     1.06825622E+03   # sbottom1 decays
#          BR         NDA      ID1       ID2
     1.76747206E-02    2     1000022         5   # BR(~b_1 -> ~chi_10 b )
     9.76215439E-03    2     1000023         5   # BR(~b_1 -> ~chi_20 b )
     3.47198149E-02    2     1000025         5   # BR(~b_1 -> ~chi_30 b )
     1.84286476E-01    2     1000035         5   # BR(~b_1 -> ~chi_40 b )
     5.35752139E-01    2    -1000024         6   # BR(~b_1 -> ~chi_1- t )
     3.70660692E-01    2    -1000037         6   # BR(~b_1 -> ~chi_2- t )
    -4.88995947E-02    2     1000006       -24   # BR(~b_1 -> ~t_1    W-)
    -1.03956402E-01    2     2000006       -24   # BR(~b_1 -> ~t_2    W-)
#
#         PDG            Width
DECAY   2000005     1.07423246E+03   # sbottom2 decays
#          BR         NDA      ID1       ID2
     9.13738343E-03    2     1000022         5   # BR(~b_2 -> ~chi_10 b )
     1.54284555E-02    2     1000023         5   # BR(~b_2 -> ~chi_20 b )
     3.50760667E-02    2     1000025         5   # BR(~b_2 -> ~chi_30 b )
     1.87107539E-01    2     1000035         5   # BR(~b_2 -> ~chi_40 b )
     5.34154065E-01    2    -1000024         6   # BR(~b_2 -> ~chi_1- t )
     3.76260190E-01    2    -1000037         6   # BR(~b_2 -> ~chi_2- t )
    -4.94064729E-02    2     1000006       -24   # BR(~b_2 -> ~t_1    W-)
    -1.07757226E-01    2     2000006       -24   # BR(~b_2 -> ~t_2    W-)
#
#         PDG            Width
DECAY   1000002     1.20666613E+03   # sup_L decays
#          BR         NDA      ID1       ID2
     4.67008026E-04    2     1000022         2   # BR(~u_L -> ~chi_10 u)
     2.28379030E-04    2     1000023         2   # BR(~u_L -> ~chi_20 u)
     1.47231860E-02    2     1000025         2   # BR(~u_L -> ~chi_30 u)
     3.26432437E-01    2     1000035         2   # BR(~u_L -> ~chi_40 u)
     3.60089773E-03    2     1000024         1   # BR(~u_L -> ~chi_1+ d)
     6.54548092E-01    2     1000037         1   # BR(~u_L -> ~chi_2+ d)
#
#         PDG            Width
DECAY   2000002     2.46673403E+02   # sup_R decays
#          BR         NDA      ID1       ID2
     8.90241753E-04    2     1000022         2   # BR(~u_R -> ~chi_10 u)
     4.11814966E-04    2     1000023         2   # BR(~u_R -> ~chi_20 u)
     9.98536261E-01    2     1000025         2   # BR(~u_R -> ~chi_30 u)
     1.61681998E-04    2     1000035         2   # BR(~u_R -> ~chi_40 u)
#
#         PDG            Width
DECAY   1000001     1.20666541E+03   # sdown_L decays
#          BR         NDA      ID1       ID2
     8.04036056E-04    2     1000022         1   # BR(~d_L -> ~chi_10 d)
     3.88084310E-04    2     1000023         1   # BR(~d_L -> ~chi_20 d)
     1.09333405E-02    2     1000025         1   # BR(~d_L -> ~chi_30 d)
     3.29725666E-01    2     1000035         1   # BR(~d_L -> ~chi_40 d)
     1.30097932E-04    2    -1000024         2   # BR(~d_L -> ~chi_1- u)
     6.58018775E-01    2    -1000037         2   # BR(~d_L -> ~chi_2- u)
#
#         PDG            Width
DECAY   2000001     6.16683554E+01   # sdown_R decays
#          BR         NDA      ID1       ID2
     8.90241753E-04    2     1000022         1   # BR(~d_R -> ~chi_10 d)
     4.11814966E-04    2     1000023         1   # BR(~d_R -> ~chi_20 d)
     9.98536261E-01    2     1000025         1   # BR(~d_R -> ~chi_30 d)
     1.61681998E-04    2     1000035         1   # BR(~d_R -> ~chi_40 d)
#
#         PDG            Width
DECAY   1000004     1.20666613E+03   # scharm_L decays
#          BR         NDA      ID1       ID2
     4.67008026E-04    2     1000022         4   # BR(~c_L -> ~chi_10 c)
     2.28379030E-04    2     1000023         4   # BR(~c_L -> ~chi_20 c)
     1.47231860E-02    2     1000025         4   # BR(~c_L -> ~chi_30 c)
     3.26432437E-01    2     1000035         4   # BR(~c_L -> ~chi_40 c)
     3.60089773E-03    2     1000024         3   # BR(~c_L -> ~chi_1+ s)
     6.54548092E-01    2     1000037         3   # BR(~c_L -> ~chi_2+ s)
#
#         PDG            Width
DECAY   2000004     2.46673403E+02   # scharm_R decays
#          BR         NDA      ID1       ID2
     8.90241753E-04    2     1000022         4   # BR(~c_R -> ~chi_10 c)
     4.11814966E-04    2     1000023         4   # BR(~c_R -> ~chi_20 c)
     9.98536261E-01    2     1000025         4   # BR(~c_R -> ~chi_30 c)
     1.61681998E-04    2     1000035         4   # BR(~c_R -> ~chi_40 c)
#
#         PDG            Width
DECAY   1000003     1.20666541E+03   # sstrange_L decays
#          BR         NDA      ID1       ID2
     8.04036056E-04    2     1000022         3   # BR(~s_L -> ~chi_10 s)
     3.88084310E-04    2     1000023         3   # BR(~s_L -> ~chi_20 s)
     1.09333405E-02    2     1000025         3   # BR(~s_L -> ~chi_30 s)
     3.29725666E-01    2     1000035         3   # BR(~s_L -> ~chi_40 s)
     1.30097932E-04    2    -1000024         4   # BR(~s_L -> ~chi_1- c)
     6.58018775E-01    2    -1000037         4   # BR(~s_L -> ~chi_2- c)
#
#         PDG            Width
DECAY   2000003     6.16683554E+01   # sstrange_R decays
#          BR         NDA      ID1       ID2
     8.90241753E-04    2     1000022         3   # BR(~s_R -> ~chi_10 s)
     4.11814966E-04    2     1000023         3   # BR(~s_R -> ~chi_20 s)
     9.98536261E-01    2     1000025         3   # BR(~s_R -> ~chi_30 s)
     1.61681998E-04    2     1000035         3   # BR(~s_R -> ~chi_40 s)
#
#         PDG            Width
DECAY   1000011     1.33203770E+03   # selectron_L decays
#          BR         NDA      ID1       ID2
     2.00530279E-04    2     1000022        11   # BR(~e_L -> ~chi_10 e-)
     1.00518641E-04    2     1000023        11   # BR(~e_L -> ~chi_20 e-)
     1.09398123E-01    2     1000025        11   # BR(~e_L -> ~chi_30 e-)
     2.93187381E-01    2     1000035        11   # BR(~e_L -> ~chi_40 e-)
     1.18061199E-04    2    -1000024        12   # BR(~e_L -> ~chi_1- nu_e)
     5.96995386E-01    2    -1000037        12   # BR(~e_L -> ~chi_2- nu_e)
#
#         PDG            Width
DECAY   2000011     5.55881979E+02   # selectron_R decays
#          BR         NDA      ID1       ID2
     8.90424121E-04    2     1000022        11   # BR(~e_R -> ~chi_10 e-)
     4.11898938E-04    2     1000023        11   # BR(~e_R -> ~chi_20 e-)
     9.98536001E-01    2     1000025        11   # BR(~e_R -> ~chi_30 e-)
     1.61676291E-04    2     1000035        11   # BR(~e_R -> ~chi_40 e-)
#
#         PDG            Width
DECAY   1000013     1.33203770E+03   # smuon_L decays
#          BR         NDA      ID1       ID2
     2.00530279E-04    2     1000022        13   # BR(~mu_L -> ~chi_10 mu-)
     1.00518641E-04    2     1000023        13   # BR(~mu_L -> ~chi_20 mu-)
     1.09398123E-01    2     1000025        13   # BR(~mu_L -> ~chi_30 mu-)
     2.93187381E-01    2     1000035        13   # BR(~mu_L -> ~chi_40 mu-)
     1.18061199E-04    2    -1000024        14   # BR(~mu_L -> ~chi_1- nu_mu)
     5.96995386E-01    2    -1000037        14   # BR(~mu_L -> ~chi_2- nu_mu)
#
#         PDG            Width
DECAY   2000013     5.55881979E+02   # smuon_R decays
#          BR         NDA      ID1       ID2
     8.90424121E-04    2     1000022        13   # BR(~mu_R -> ~chi_10 mu-)
     4.11898938E-04    2     1000023        13   # BR(~mu_R -> ~chi_20 mu-)
     9.98536001E-01    2     1000025        13   # BR(~mu_R -> ~chi_30 mu-)
     1.61676291E-04    2     1000035        13   # BR(~mu_R -> ~chi_40 mu-)
#
#         PDG            Width
DECAY   1000015     9.70740049E+02   # stau_1 decays
#          BR         NDA      ID1       ID2
     1.35636720E-02    2     1000022        15   # BR(~tau_1 -> ~chi_10  tau-)
     6.60189322E-03    2     1000023        15   # BR(~tau_1 -> ~chi_20  tau-)
     3.60567383E-01    2     1000025        15   # BR(~tau_1 -> ~chi_30  tau-)
     2.00355115E-01    2     1000035        15   # BR(~tau_1 -> ~chi_40  tau-)
     1.09847643E-02    2    -1000024        16   # BR(~tau_1 -> ~chi_1-  nu_tau)
     4.07927173E-01    2    -1000037        16   # BR(~tau_1 -> ~chi_2-  nu_tau)
#
#         PDG            Width
DECAY   2000015     9.70662710E+02   # stau_2 decays
#          BR         NDA      ID1       ID2
     5.97826885E-03    2     1000022        15   # BR(~tau_2 -> ~chi_10  tau-)
     1.17409967E-02    2     1000023        15   # BR(~tau_2 -> ~chi_20  tau-)
     3.61376978E-01    2     1000025        15   # BR(~tau_2 -> ~chi_30  tau-)
     2.02065452E-01    2     1000035        15   # BR(~tau_2 -> ~chi_40  tau-)
     7.53918674E-03    2    -1000024        16   # BR(~tau_2 -> ~chi_1-  nu_tau)
     4.11299118E-01    2    -1000037        16   # BR(~tau_2 -> ~chi_2-  nu_tau)
#
#         PDG            Width
DECAY   1000012     1.33203848E+03   # snu_eL decays
#          BR         NDA      ID1       ID2
     1.11806667E-03    2     1000022        12   # BR(~nu_eL -> ~chi_10 nu_e)
     5.35305209E-04    2     1000023        12   # BR(~nu_eL -> ~chi_20 nu_e)
     9.90824945E-02    2     1000025        12   # BR(~nu_eL -> ~chi_30 nu_e)
     3.02149853E-01    2     1000035        12   # BR(~nu_eL -> ~chi_40 nu_e)
     3.26774051E-03    2     1000024        11   # BR(~nu_eL -> ~chi_1+ e-)
     5.93846540E-01    2     1000037        11   # BR(~nu_eL -> ~chi_2+ e-)
#
#         PDG            Width
DECAY   1000014     1.33203848E+03   # snu_muL decays
#          BR         NDA      ID1       ID2
     1.11806667E-03    2     1000022        14   # BR(~nu_muL -> ~chi_10 nu_mu)
     5.35305209E-04    2     1000023        14   # BR(~nu_muL -> ~chi_20 nu_mu)
     9.90824945E-02    2     1000025        14   # BR(~nu_muL -> ~chi_30 nu_mu)
     3.02149853E-01    2     1000035        14   # BR(~nu_muL -> ~chi_40 nu_mu)
     3.26774051E-03    2     1000024        13   # BR(~nu_muL -> ~chi_1+ mu-)
     5.93846540E-01    2     1000037        13   # BR(~nu_muL -> ~chi_2+ mu-)
#
#         PDG            Width
DECAY   1000016     1.34986617E+03   # snu_tauL decays
#          BR         NDA      ID1       ID2
     1.10330036E-03    2     1000022        16   # BR(~nu_tauL -> ~chi_10 nu_tau)
     5.28235431E-04    2     1000023        16   # BR(~nu_tauL -> ~chi_20 nu_tau)
     9.77739117E-02    2     1000025        16   # BR(~nu_tauL -> ~chi_30 nu_tau)
     2.98159359E-01    2     1000035        16   # BR(~nu_tauL -> ~chi_40 nu_tau)
     1.64289766E-02    2     1000024        15   # BR(~nu_tauL -> ~chi_1+ tau-)
     5.86006217E-01    2     1000037        15   # BR(~nu_tauL -> ~chi_2+ tau-)
#
#         PDG            Width
DECAY   1000024     6.12775590E-11   # chargino1+ decays
#           BR         NDA      ID1       ID2       ID3
     5.38718701E-01    3     1000022         2        -1   # BR(~chi_1+ -> ~chi_10 u    db)
     9.47172222E-02    3     1000022         4        -3   # BR(~chi_1+ -> ~chi_10 c    sb)
     1.79572901E-01    3     1000022       -11        12   # BR(~chi_1+ -> ~chi_10 e+   nu_e)
     1.77920676E-01    3     1000022       -13        14   # BR(~chi_1+ -> ~chi_10 mu+  nu_mu)
     9.07049992E-03    3     1000022       -15        16   # BR(~chi_1+ -> ~chi_10 tau+ nu_tau)
#
#         PDG            Width
DECAY   1000037     1.11417406E+01   # chargino2+ decays
#          BR         NDA      ID1       ID2
     2.53977198E-01    2     1000024        23   # BR(~chi_2+ -> ~chi_1+  Z )
     2.35986112E-01    2     1000022        24   # BR(~chi_2+ -> ~chi_10  W+)
     2.46561556E-01    2     1000023        24   # BR(~chi_2+ -> ~chi_20  W+)
     6.58497688E-04    2     1000025        24   # BR(~chi_2+ -> ~chi_30  W+)
     2.62816636E-01    2     1000024        25   # BR(~chi_2+ -> ~chi_1+  h )
#
#         PDG            Width
DECAY   1000022     0.00000000E+00   # neutralino1 decays
#
#         PDG            Width
DECAY   1000023     5.04069549E-09   # neutralino2 decays
##          BR         NDA      ID1       ID2
#     5.03910165E-02    2     1000022        22   # BR(~chi_20 -> ~chi_10 gam)
##           BR         NDA      ID1       ID2       ID3
#     1.24302629E-01    3     1000022        -2         2   # BR(~chi_20 -> ~chi_10 ub      u)
#     1.62066356E-01    3     1000022        -1         1   # BR(~chi_20 -> ~chi_10 db      d)
#     7.82179888E-02    3     1000022        -4         4   # BR(~chi_20 -> ~chi_10 cb      c)
#     1.60603422E-01    3     1000022        -3         3   # BR(~chi_20 -> ~chi_10 sb      s)
     3.78603241E-02    3     1000022       -11        11   # BR(~chi_20 -> ~chi_10 e+      e-)
     3.77932429E-02    3     1000022       -13        13   # BR(~chi_20 -> ~chi_10 mu+     mu-)
#     1.68866341E-02    3     1000022       -15        15   # BR(~chi_20 -> ~chi_10 tau+    tau-)
#     7.56240518E-02    3     1000022       -12        12   # BR(~chi_20 -> ~chi_10 nu_eb   nu_e)
#     7.56240518E-02    3     1000022       -14        14   # BR(~chi_20 -> ~chi_10 nu_mub  nu_mu)
#     7.56240518E-02    3     1000022       -16        16   # BR(~chi_20 -> ~chi_10 nu_taub nu_tau)
#     2.47575163E-02    3     1000024        -2         1   # BR(~chi_20 -> ~chi_1+ ub      d)
#     2.47575163E-02    3    -1000024        -1         2   # BR(~chi_20 -> ~chi_1- db      u)
#     9.52517830E-03    3     1000024        -4         3   # BR(~chi_20 -> ~chi_1+ cb      s)
#     9.52517830E-03    3    -1000024        -3         4   # BR(~chi_20 -> ~chi_1- sb      c)
#     8.25250543E-03    3     1000024       -12        11   # BR(~chi_20 -> ~chi_1+ nu_eb   e-)
#     8.25250543E-03    3    -1000024        12       -11   # BR(~chi_20 -> ~chi_1- nu_e    e+)
#     8.20791712E-03    3     1000024       -14        13   # BR(~chi_20 -> ~chi_1+ nu_mub  mu-)
#     8.20791712E-03    3    -1000024        14       -13   # BR(~chi_20 -> ~chi_1- nu_mu   mu+)
#     1.75999854E-03    3     1000024       -16        15   # BR(~chi_20 -> ~chi_1+ nu_taub tau-)
#     1.75999854E-03    3    -1000024        16       -15   # BR(~chi_20 -> ~chi_1- nu_tau  tau+)
#         PDG            Width
DECAY   1000025     3.36393131E+00   # neutralino3 decays
#          BR         NDA      ID1       ID2
     7.26806767E-02    2     1000022        23   # BR(~chi_30 -> ~chi_10   Z )
     1.72323340E-01    2     1000023        23   # BR(~chi_30 -> ~chi_20   Z )
     2.53804385E-01    2     1000024       -24   # BR(~chi_30 -> ~chi_1+   W-)
     2.53804385E-01    2    -1000024        24   # BR(~chi_30 -> ~chi_1-   W+)
     1.69547696E-01    2     1000022        25   # BR(~chi_30 -> ~chi_10   h )
     7.78395173E-02    2     1000023        25   # BR(~chi_30 -> ~chi_20   h )
#
#         PDG            Width
DECAY   1000035     1.11386753E+01   # neutralino4 decays
#          BR         NDA      ID1       ID2
     7.89414081E-02    2     1000022        23   # BR(~chi_40 -> ~chi_10   Z )
     1.78550080E-01    2     1000023        23   # BR(~chi_40 -> ~chi_20   Z )
     4.94143588E-06    2     1000025        23   # BR(~chi_40 -> ~chi_30   Z )
     2.39719440E-01    2     1000024       -24   # BR(~chi_40 -> ~chi_1+   W-)
     2.39719440E-01    2    -1000024        24   # BR(~chi_40 -> ~chi_1-   W+)
     1.77079159E-01    2     1000022        25   # BR(~chi_40 -> ~chi_10   h )
     8.55883746E-02    2     1000023        25   # BR(~chi_40 -> ~chi_20   h )
     3.97155913E-04    2     1000025        25   # BR(~chi_40 -> ~chi_30   h )
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
DECAY        36     1.51438717E+03   # A decays
#          BR         NDA      ID1       ID2
     4.51498219E-02    2           5        -5   # BR(A -> b       bb     )
     1.16008107E-02    2         -15        15   # BR(A -> tau+    tau-   )
     4.10083766E-05    2         -13        13   # BR(A -> mu+     mu-    )
     3.40845884E-05    2           3        -3   # BR(A -> s       sb     )
     2.14697825E-07    2           4        -4   # BR(A -> c       cb     )
     2.14181610E-02    2           6        -6   # BR(A -> t       tb     )
     1.99681269E-07    2          21        21   # BR(A -> g       g      )
     7.74064959E-10    2          22        22   # BR(A -> gam     gam    )
     5.72199226E-10    2          23        22   # BR(A -> Z       gam    )
     6.00561135E-09    2          23        25   # BR(A -> Z       h      )
     3.16291014E-03    2     1000024  -1000024   # BR(A -> ~chi_1+ ~chi_1-)
     2.69896203E-04    2     1000037  -1000037   # BR(A -> ~chi_2+ ~chi_2-)
     2.79049632E-01    2     1000024  -1000037   # BR(A -> ~chi_1+ ~chi_2-)
     2.79049632E-01    2     1000037  -1000024   # BR(A -> ~chi_2+ ~chi_1-)
     1.22449417E-03    2     1000022   1000022   # BR(A -> ~chi_10 ~chi_10)
     3.63327977E-04    2     1000023   1000023   # BR(A -> ~chi_20 ~chi_20)
     1.72019023E-05    2     1000025   1000025   # BR(A -> ~chi_30 ~chi_30)
     1.38789169E-04    2     1000035   1000035   # BR(A -> ~chi_40 ~chi_40)
     5.47303638E-06    2     1000022   1000023   # BR(A -> ~chi_10 ~chi_20)
     4.61839016E-02    2     1000022   1000025   # BR(A -> ~chi_10 ~chi_30)
     1.74761850E-01    2     1000022   1000035   # BR(A -> ~chi_10 ~chi_40)
     2.87600249E-02    2     1000023   1000025   # BR(A -> ~chi_20 ~chi_30)
     1.08668822E-01    2     1000023   1000035   # BR(A -> ~chi_20 ~chi_40)
     9.97357676E-05    2     1000025   1000035   # BR(A -> ~chi_30 ~chi_40)
#
#         PDG            Width
DECAY        37     1.51299995E+03   # H+ decays
#          BR         NDA      ID1       ID2
     7.10361438E-05    2           4        -5   # BR(H+ -> c       bb     )
     1.16114375E-02    2         -15        16   # BR(H+ -> tau+    nu_tau )
     4.10459419E-05    2         -13        14   # BR(H+ -> mu+     nu_mu  )
     4.54629374E-07    2           2        -5   # BR(H+ -> u       bb     )
     1.64377464E-06    2           2        -3   # BR(H+ -> u       sb     )
     3.39984081E-05    2           4        -3   # BR(H+ -> c       sb     )
     6.56412151E-02    2           6        -5   # BR(H+ -> t       bb     )
     6.01110607E-09    2          24        25   # BR(H+ -> W+      h      )
     5.71286590E-05    2     1000024   1000022   # BR(H+ -> ~chi_1+ ~chi_10)
     3.20857405E-04    2     1000024   1000023   # BR(H+ -> ~chi_1+ ~chi_20)
     8.37666845E-02    2     1000024   1000025   # BR(H+ -> ~chi_1+ ~chi_30)
     2.76461561E-01    2     1000024   1000035   # BR(H+ -> ~chi_1+ ~chi_40)
     2.87013732E-01    2     1000037   1000022   # BR(H+ -> ~chi_2+ ~chi_10)
     2.74867188E-01    2     1000037   1000023   # BR(H+ -> ~chi_2+ ~chi_20)
     1.11994634E-04    2     1000037   1000025   # BR(H+ -> ~chi_2+ ~chi_30)
     1.60567213E-08    2     1000037   1000035   # BR(H+ -> ~chi_2+ ~chi_40)
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
