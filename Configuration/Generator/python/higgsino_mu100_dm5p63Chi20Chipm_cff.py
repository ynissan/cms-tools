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
        23     1.00000000E+02   # mu(EWSB)            
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
        24     8.05079296E+01   # W+
        25     1.70262726E+02   # h
        35     1.00000300E+05   # H
        36     1.00000000E+05   # A
        37     9.99999171E+04   # H+
         5     4.87877839E+00   # b-quark pole mass calculated from mb(mb)_Msbar
   1000001     1.02565628E+05   # ~d_L
   2000001     1.02565615E+05   # ~d_R
   1000002     1.02565600E+05   # ~u_L
   2000002     1.02565606E+05   # ~u_R
   1000003     1.02565628E+05   # ~s_L
   2000003     1.02565615E+05   # ~s_R
   1000004     1.02565600E+05   # ~c_L
   2000004     1.02565606E+05   # ~c_R
   1000005     1.02564572E+05   # ~b_1
   2000005     1.02566671E+05   # ~b_2
   1000006     1.00819542E+05   # ~t_1
   2000006     1.02323537E+05   # ~t_2
   1000011     1.00000009E+05   # ~e_L
   2000011     1.00000010E+05   # ~e_R
   1000012     9.99999810E+04   # ~nu_eL
   1000013     1.00000009E+05   # ~mu_L
   2000013     1.00000010E+05   # ~mu_R
   1000014     9.99999810E+04   # ~nu_muL
   1000015     9.99978174E+04   # ~tau_1
   2000015     1.00002202E+05   # ~tau_2
   1000016     9.99999810E+04   # ~nu_tauL
   1000021     1.04586111E+05   # ~g
   1000022     1.03186587E+02   # ~chi_10
   1000023    -1.08819110E+02   # ~chi_20
   1000025     1.28271748E+03   # ~chi_30
   1000035     1.47021167E+03   # ~chi_40
   1000024     1.05633665E+02   # ~chi_1+
   1000037     1.47018671E+03   # ~chi_2+
#
BLOCK NMIX  # Neutralino Mixing Matrix
  1  1     2.93921249E-02   # N_11
  1  2    -4.29879907E-02   # N_12
  1  3     7.15777748E-01   # N_13
  1  4    -6.96383767E-01   # N_14
  2  1     2.05632303E-02   # N_21
  2  2    -3.07109917E-02   # N_22
  2  3    -6.98233535E-01   # N_23
  2  4    -7.14915323E-01   # N_24
  3  1     9.99276295E-01   # N_31
  3  2     1.45412821E-02   # N_32
  3  3    -6.56563274E-03   # N_33
  3  4     3.45301262E-02   # N_34
  4  1     1.26547456E-02   # N_41
  4  2    -9.98497581E-01   # N_42
  4  3    -9.43605246E-03   # N_43
  4  4     5.24728460E-02   # N_44
#
BLOCK UMIX  # Chargino Mixing Matrix U
  1  1    -1.32435223E-02   # U_11
  1  2     9.99912301E-01   # U_12
  2  1     9.99912301E-01   # U_21
  2  2     1.32435223E-02   # U_22
#
BLOCK VMIX  # Chargino Mixing Matrix V
  1  1    -7.37603018E-02   # V_11
  1  2     9.97275999E-01   # V_12
  2  1     9.97275999E-01   # V_21
  2  2     7.37603018E-02   # V_22
#
BLOCK STOPMIX  # Stop Mixing Matrix
  1  1     3.61244110E-02   # cos(theta_t)
  1  2     9.99347300E-01   # sin(theta_t)
  2  1    -9.99347300E-01   # -sin(theta_t)
  2  2     3.61244110E-02   # cos(theta_t)
#
BLOCK SBOTMIX  # Sbottom Mixing Matrix
  1  1     7.05061238E-01   # cos(theta_b)
  1  2     7.09146424E-01   # sin(theta_b)
  2  1    -7.09146424E-01   # -sin(theta_b)
  2  2     7.05061238E-01   # cos(theta_b)
#
BLOCK STAUMIX  # Stau Mixing Matrix
  1  1     7.07160759E-01   # cos(theta_tau)
  1  2     7.07052799E-01   # sin(theta_tau)
  2  1    -7.07052799E-01   # -sin(theta_tau)
  2  2     7.07160759E-01   # cos(theta_tau)
#
BLOCK ALPHA  # Higgs mixing
          -1.08197787E-01   # Mixing angle in the neutral Higgs boson sector
#
BLOCK HMIX Q=  1.00000031E+05  # DRbar Higgs Parameters
         1     1.00000000E+02   # mu(Q)               
         2     9.20625480E+00   # tanbeta(Q)          
         3     2.40669503E+02   # vev(Q)              
         4     9.92203678E+09   # MA^2(Q)             
#
BLOCK GAUGE Q=  1.00000031E+05  # The gauge couplings
     1     3.73851944E-01   # gprime(Q) DRbar
     2     6.32665169E-01   # g(Q) DRbar
     3     8.77149866E-01   # g3(Q) DRbar
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
  3  3     7.49929624E-01   # y_t(Q) DRbar
#
BLOCK Yd Q=  1.00000031E+05  # The Yukawa couplings
  1  1     0.00000000E+00   # y_d(Q) DRbar
  2  2     0.00000000E+00   # y_s(Q) DRbar
  3  3     1.16401978E-01   # y_b(Q) DRbar
#
BLOCK Ye Q=  1.00000031E+05  # The Yukawa couplings
  1  1     0.00000000E+00   # y_e(Q) DRbar
  2  2     0.00000000E+00   # y_mu(Q) DRbar
  3  3     9.46692211E-02   # y_tau(Q) DRbar
#
BLOCK MSOFT Q=  1.00000031E+05  # The soft SUSY breaking masses at the scale Q
         1     1.29349486E+03   # M_1                 
         2     1.29349486E+03   # M_2                 
         3     1.00000000E+05   # M_3                 
        14    -6.77437438E+05   # A_u                 
        15    -8.59633345E+05   # A_d                 
        16    -2.53493493E+05   # A_e                 
        21     9.85907564E+09   # M^2_Hd              
        22     3.33746453E+08   # M^2_Hu              
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
DECAY         6     1.38473479E+00   # top decays
#          BR         NDA      ID1       ID2
     1.00000000E+00    2           5        24   # BR(t ->  b    W+)
#
#         PDG            Width
DECAY   1000021     3.47414959E+01   # gluino decays
#          BR         NDA      ID1       ID2
     3.42825489E-02    2     1000001        -1   # BR(~g -> ~d_L  db)
     3.42825489E-02    2    -1000001         1   # BR(~g -> ~d_L* d )
     3.42829857E-02    2     2000001        -1   # BR(~g -> ~d_R  db)
     3.42829857E-02    2    -2000001         1   # BR(~g -> ~d_R* d )
     3.42834898E-02    2     1000002        -2   # BR(~g -> ~u_L  ub)
     3.42834898E-02    2    -1000002         2   # BR(~g -> ~u_L* u )
     3.42832882E-02    2     2000002        -2   # BR(~g -> ~u_R  ub)
     3.42832882E-02    2    -2000002         2   # BR(~g -> ~u_R* u )
     3.42825489E-02    2     1000003        -3   # BR(~g -> ~s_L  sb)
     3.42825489E-02    2    -1000003         3   # BR(~g -> ~s_L* s )
     3.42829857E-02    2     2000003        -3   # BR(~g -> ~s_R  sb)
     3.42829857E-02    2    -2000003         3   # BR(~g -> ~s_R* s )
     3.42834898E-02    2     1000004        -4   # BR(~g -> ~c_L  cb)
     3.42834898E-02    2    -1000004         4   # BR(~g -> ~c_L* c )
     3.42832882E-02    2     2000004        -4   # BR(~g -> ~c_R  cb)
     3.42832882E-02    2    -2000004         4   # BR(~g -> ~c_R* c )
     3.42449899E-02    2     1000005        -5   # BR(~g -> ~b_1  bb)
     3.42449899E-02    2    -1000005         5   # BR(~g -> ~b_1* b )
     3.43033159E-02    2     2000005        -5   # BR(~g -> ~b_2  bb)
     3.43033159E-02    2    -2000005         5   # BR(~g -> ~b_2* b )
     1.14330288E-01    2     1000006        -6   # BR(~g -> ~t_1  tb)
     1.14330288E-01    2    -1000006         6   # BR(~g -> ~t_1* t )
     4.28567807E-02    2     2000006        -6   # BR(~g -> ~t_2  tb)
     4.28567807E-02    2    -2000006         6   # BR(~g -> ~t_2* t )
#
#         PDG            Width
DECAY   1000006     2.45781710E+03   # stop1 decays
#          BR         NDA      ID1       ID2
     2.19515071E-01    2     1000022         6   # BR(~t_1 -> ~chi_10 t )
     2.31021681E-01    2     1000023         6   # BR(~t_1 -> ~chi_20 t )
     9.87118101E-02    2     1000025         6   # BR(~t_1 -> ~chi_30 t )
     3.96932307E-04    2     1000035         6   # BR(~t_1 -> ~chi_40 t )
     4.49592791E-01    2     1000024         5   # BR(~t_1 -> ~chi_1+ b )
     7.61714669E-04    2     1000037         5   # BR(~t_1 -> ~chi_2+ b )
#
#         PDG            Width
DECAY   2000006     2.34819013E+03   # stop2 decays
#          BR         NDA      ID1       ID2
     2.31215657E-01    2     1000022         6   # BR(~t_2 -> ~chi_10 t )
     2.43860306E-01    2     1000023         6   # BR(~t_2 -> ~chi_20 t )
     8.70083869E-03    2     1000025         6   # BR(~t_2 -> ~chi_30 t )
     1.69762770E-01    2     1000035         6   # BR(~t_2 -> ~chi_40 t )
     1.17480919E-02    2     1000024         5   # BR(~t_2 -> ~chi_1+ b )
     3.37637456E-01    2     1000037         5   # BR(~t_2 -> ~chi_2+ b )
     7.31707126E-03    2     1000006        25   # BR(~t_2 -> ~t_1    h )
    -1.02421910E-02    2     1000006        23   # BR(~t_2 -> ~t_1    Z )
#
#         PDG            Width
DECAY   1000005     1.06907991E+03   # sbottom1 decays
#          BR         NDA      ID1       ID2
     1.76410939E-02    2     1000022         5   # BR(~b_1 -> ~chi_10 b )
     9.68607437E-03    2     1000023         5   # BR(~b_1 -> ~chi_20 b )
     3.47189641E-02    2     1000025         5   # BR(~b_1 -> ~chi_30 b )
     1.84296375E-01    2     1000035         5   # BR(~b_1 -> ~chi_40 b )
     5.35351393E-01    2    -1000024         6   # BR(~b_1 -> ~chi_1- t )
     3.70745369E-01    2    -1000037         6   # BR(~b_1 -> ~chi_2- t )
    -4.88817182E-02    2     1000006       -24   # BR(~b_1 -> ~t_1    W-)
    -1.03557551E-01    2     2000006       -24   # BR(~b_1 -> ~t_2    W-)
#
#         PDG            Width
DECAY   2000005     1.07509184E+03   # sbottom2 decays
#          BR         NDA      ID1       ID2
     9.20843057E-03    2     1000022         5   # BR(~b_2 -> ~chi_10 b )
     1.54107365E-02    2     1000023         5   # BR(~b_2 -> ~chi_20 b )
     3.50246005E-02    2     1000025         5   # BR(~b_2 -> ~chi_30 b )
     1.87001247E-01    2     1000035         5   # BR(~b_2 -> ~chi_40 b )
     5.33970459E-01    2    -1000024         6   # BR(~b_2 -> ~chi_1- t )
     3.76116626E-01    2    -1000037         6   # BR(~b_2 -> ~chi_2- t )
    -4.93877997E-02    2     1000006       -24   # BR(~b_2 -> ~t_1    W-)
    -1.07344300E-01    2     2000006       -24   # BR(~b_2 -> ~t_2    W-)
#
#         PDG            Width
DECAY   1000002     1.20753704E+03   # sup_L decays
#          BR         NDA      ID1       ID2
     4.55439991E-04    2     1000022         2   # BR(~u_L -> ~chi_10 u)
     2.33947975E-04    2     1000023         2   # BR(~u_L -> ~chi_20 u)
     1.47033618E-02    2     1000025         2   # BR(~u_L -> ~chi_30 u)
     3.26452787E-01    2     1000035         2   # BR(~u_L -> ~chi_40 u)
     3.58141193E-03    2     1000024         1   # BR(~u_L -> ~chi_1+ d)
     6.54573051E-01    2     1000037         1   # BR(~u_L -> ~chi_2+ d)
#
#         PDG            Width
DECAY   2000002     2.46692787E+02   # sup_R decays
#          BR         NDA      ID1       ID2
     8.63999889E-04    2     1000022         2   # BR(~u_R -> ~chi_10 u)
     4.22897094E-04    2     1000023         2   # BR(~u_R -> ~chi_20 u)
     9.98552971E-01    2     1000025         2   # BR(~u_R -> ~chi_30 u)
     1.60131645E-04    2     1000035         2   # BR(~u_R -> ~chi_40 u)
#
#         PDG            Width
DECAY   1000001     1.20753634E+03   # sdown_L decays
#          BR         NDA      ID1       ID2
     7.83099071E-04    2     1000022         1   # BR(~d_L -> ~chi_10 d)
     3.97716175E-04    2     1000023         1   # BR(~d_L -> ~chi_20 d)
     1.09356410E-02    2     1000025         1   # BR(~d_L -> ~chi_30 d)
     3.29729195E-01    2     1000035         1   # BR(~d_L -> ~chi_40 d)
     1.15455938E-04    2    -1000024         2   # BR(~d_L -> ~chi_1- u)
     6.58038893E-01    2    -1000037         2   # BR(~d_L -> ~chi_2- u)
#
#         PDG            Width
DECAY   2000001     6.16732013E+01   # sdown_R decays
#          BR         NDA      ID1       ID2
     8.63999888E-04    2     1000022         1   # BR(~d_R -> ~chi_10 d)
     4.22897094E-04    2     1000023         1   # BR(~d_R -> ~chi_20 d)
     9.98552971E-01    2     1000025         1   # BR(~d_R -> ~chi_30 d)
     1.60131645E-04    2     1000035         1   # BR(~d_R -> ~chi_40 d)
#
#         PDG            Width
DECAY   1000004     1.20753704E+03   # scharm_L decays
#          BR         NDA      ID1       ID2
     4.55439991E-04    2     1000022         4   # BR(~c_L -> ~chi_10 c)
     2.33947975E-04    2     1000023         4   # BR(~c_L -> ~chi_20 c)
     1.47033618E-02    2     1000025         4   # BR(~c_L -> ~chi_30 c)
     3.26452787E-01    2     1000035         4   # BR(~c_L -> ~chi_40 c)
     3.58141193E-03    2     1000024         3   # BR(~c_L -> ~chi_1+ s)
     6.54573051E-01    2     1000037         3   # BR(~c_L -> ~chi_2+ s)
#
#         PDG            Width
DECAY   2000004     2.46692787E+02   # scharm_R decays
#          BR         NDA      ID1       ID2
     8.63999889E-04    2     1000022         4   # BR(~c_R -> ~chi_10 c)
     4.22897094E-04    2     1000023         4   # BR(~c_R -> ~chi_20 c)
     9.98552971E-01    2     1000025         4   # BR(~c_R -> ~chi_30 c)
     1.60131645E-04    2     1000035         4   # BR(~c_R -> ~chi_40 c)
#
#         PDG            Width
DECAY   1000003     1.20753634E+03   # sstrange_L decays
#          BR         NDA      ID1       ID2
     7.83099071E-04    2     1000022         3   # BR(~s_L -> ~chi_10 s)
     3.97716175E-04    2     1000023         3   # BR(~s_L -> ~chi_20 s)
     1.09356410E-02    2     1000025         3   # BR(~s_L -> ~chi_30 s)
     3.29729195E-01    2     1000035         3   # BR(~s_L -> ~chi_40 s)
     1.15455938E-04    2    -1000024         4   # BR(~s_L -> ~chi_1- c)
     6.58038893E-01    2    -1000037         4   # BR(~s_L -> ~chi_2- c)
#
#         PDG            Width
DECAY   2000003     6.16732013E+01   # sstrange_R decays
#          BR         NDA      ID1       ID2
     8.63999888E-04    2     1000022         3   # BR(~s_R -> ~chi_10 s)
     4.22897094E-04    2     1000023         3   # BR(~s_R -> ~chi_20 s)
     9.98552971E-01    2     1000025         3   # BR(~s_R -> ~chi_30 s)
     1.60131645E-04    2     1000035         3   # BR(~s_R -> ~chi_40 s)
#
#         PDG            Width
DECAY   1000011     1.33291961E+03   # selectron_L decays
#          BR         NDA      ID1       ID2
     1.96061241E-04    2     1000022        11   # BR(~e_L -> ~chi_10 e-)
     1.02894465E-04    2     1000023        11   # BR(~e_L -> ~chi_20 e-)
     1.09308614E-01    2     1000025        11   # BR(~e_L -> ~chi_30 e-)
     2.93238426E-01    2     1000035        11   # BR(~e_L -> ~chi_40 e-)
     1.04780417E-04    2    -1000024        12   # BR(~e_L -> ~chi_1- nu_e)
     5.97049224E-01    2    -1000037        12   # BR(~e_L -> ~chi_2- nu_e)
#
#         PDG            Width
DECAY   2000011     5.55925659E+02   # selectron_R decays
#          BR         NDA      ID1       ID2
     8.64179172E-04    2     1000022        11   # BR(~e_R -> ~chi_10 e-)
     4.22984449E-04    2     1000023        11   # BR(~e_R -> ~chi_20 e-)
     9.98552710E-01    2     1000025        11   # BR(~e_R -> ~chi_30 e-)
     1.60125987E-04    2     1000035        11   # BR(~e_R -> ~chi_40 e-)
#
#         PDG            Width
DECAY   1000013     1.33291961E+03   # smuon_L decays
#          BR         NDA      ID1       ID2
     1.96061241E-04    2     1000022        13   # BR(~mu_L -> ~chi_10 mu-)
     1.02894465E-04    2     1000023        13   # BR(~mu_L -> ~chi_20 mu-)
     1.09308614E-01    2     1000025        13   # BR(~mu_L -> ~chi_30 mu-)
     2.93238426E-01    2     1000035        13   # BR(~mu_L -> ~chi_40 mu-)
     1.04780417E-04    2    -1000024        14   # BR(~mu_L -> ~chi_1- nu_mu)
     5.97049224E-01    2    -1000037        14   # BR(~mu_L -> ~chi_2- nu_mu)
#
#         PDG            Width
DECAY   2000013     5.55925659E+02   # smuon_R decays
#          BR         NDA      ID1       ID2
     8.64179172E-04    2     1000022        13   # BR(~mu_R -> ~chi_10 mu-)
     4.22984449E-04    2     1000023        13   # BR(~mu_R -> ~chi_20 mu-)
     9.98552710E-01    2     1000025        13   # BR(~mu_R -> ~chi_30 mu-)
     1.60125987E-04    2     1000035        13   # BR(~mu_R -> ~chi_40 mu-)
#
#         PDG            Width
DECAY   1000015     9.71205257E+02   # stau_1 decays
#          BR         NDA      ID1       ID2
     1.35351694E-02    2     1000022        15   # BR(~tau_1 -> ~chi_10  tau-)
     6.54547523E-03    2     1000023        15   # BR(~tau_1 -> ~chi_20  tau-)
     3.60432351E-01    2     1000025        15   # BR(~tau_1 -> ~chi_30  tau-)
     2.00476504E-01    2     1000035        15   # BR(~tau_1 -> ~chi_40  tau-)
     1.08725587E-02    2    -1000024        16   # BR(~tau_1 -> ~chi_1-  nu_tau)
     4.08137942E-01    2    -1000037        16   # BR(~tau_1 -> ~chi_2-  nu_tau)
#
#         PDG            Width
DECAY   2000015     9.71129456E+02   # stau_2 decays
#          BR         NDA      ID1       ID2
     6.04033054E-03    2     1000022        15   # BR(~tau_2 -> ~chi_10  tau-)
     1.17394724E-02    2     1000023        15   # BR(~tau_2 -> ~chi_20  tau-)
     3.61196361E-01    2     1000025        15   # BR(~tau_2 -> ~chi_30  tau-)
     2.02085976E-01    2     1000035        15   # BR(~tau_2 -> ~chi_40  tau-)
     7.62699127E-03    2    -1000024        16   # BR(~tau_2 -> ~chi_1-  nu_tau)
     4.11310870E-01    2    -1000037        16   # BR(~tau_2 -> ~chi_2-  nu_tau)
#
#         PDG            Width
DECAY   1000012     1.33292039E+03   # snu_eL decays
#          BR         NDA      ID1       ID2
     1.08814686E-03    2     1000022        12   # BR(~nu_eL -> ~chi_10 nu_e)
     5.48769830E-04    2     1000023        12   # BR(~nu_eL -> ~chi_20 nu_e)
     9.90525952E-02    2     1000025        12   # BR(~nu_eL -> ~chi_30 nu_e)
     3.02155650E-01    2     1000035        12   # BR(~nu_eL -> ~chi_40 nu_e)
     3.25025998E-03    2     1000024        11   # BR(~nu_eL -> ~chi_1+ e-)
     5.93904578E-01    2     1000037        11   # BR(~nu_eL -> ~chi_2+ e-)
#
#         PDG            Width
DECAY   1000014     1.33292039E+03   # snu_muL decays
#          BR         NDA      ID1       ID2
     1.08814686E-03    2     1000022        14   # BR(~nu_muL -> ~chi_10 nu_mu)
     5.48769830E-04    2     1000023        14   # BR(~nu_muL -> ~chi_20 nu_mu)
     9.90525952E-02    2     1000025        14   # BR(~nu_muL -> ~chi_30 nu_mu)
     3.02155650E-01    2     1000035        14   # BR(~nu_muL -> ~chi_40 nu_mu)
     3.25025998E-03    2     1000024        13   # BR(~nu_muL -> ~chi_1+ mu-)
     5.93904578E-01    2     1000037        13   # BR(~nu_muL -> ~chi_2+ mu-)
#
#         PDG            Width
DECAY   1000016     1.35075020E+03   # snu_tauL decays
#          BR         NDA      ID1       ID2
     1.07378339E-03    2     1000022        16   # BR(~nu_tauL -> ~chi_10 nu_tau)
     5.41526107E-04    2     1000023        16   # BR(~nu_tauL -> ~chi_20 nu_tau)
     9.77451078E-02    2     1000025        16   # BR(~nu_tauL -> ~chi_30 nu_tau)
     2.98167217E-01    2     1000035        16   # BR(~nu_tauL -> ~chi_40 nu_tau)
     1.64049721E-02    2     1000024        15   # BR(~nu_tauL -> ~chi_1+ tau-)
     5.86067394E-01    2     1000037        15   # BR(~nu_tauL -> ~chi_2+ tau-)
#
#         PDG            Width
DECAY   1000024     6.05862247E-11   # chargino1+ decays
#           BR         NDA      ID1       ID2       ID3
     5.39097036E-01    3     1000022         2        -1   # BR(~chi_1+ -> ~chi_10 u    db)
     9.41976804E-02    3     1000022         4        -3   # BR(~chi_1+ -> ~chi_10 c    sb)
     1.79699012E-01    3     1000022       -11        12   # BR(~chi_1+ -> ~chi_10 e+   nu_e)
     1.78040710E-01    3     1000022       -13        14   # BR(~chi_1+ -> ~chi_10 mu+  nu_mu)
     8.96556157E-03    3     1000022       -15        16   # BR(~chi_1+ -> ~chi_10 tau+ nu_tau)
#
#         PDG            Width
DECAY   1000037     1.11075561E+01   # chargino2+ decays
#          BR         NDA      ID1       ID2
     2.53982042E-01    2     1000024        23   # BR(~chi_2+ -> ~chi_1+  Z )
     2.35247146E-01    2     1000022        24   # BR(~chi_2+ -> ~chi_10  W+)
     2.47370565E-01    2     1000023        24   # BR(~chi_2+ -> ~chi_20  W+)
     6.56288702E-04    2     1000025        24   # BR(~chi_2+ -> ~chi_30  W+)
     2.62743959E-01    2     1000024        25   # BR(~chi_2+ -> ~chi_1+  h )
#
#         PDG            Width
DECAY   1000022     0.00000000E+00   # neutralino1 decays
#
#         PDG            Width
DECAY   1000023     4.88575987E-09   # neutralino2 decays
##          BR         NDA      ID1       ID2
#     4.91423377E-02    2     1000022        22   # BR(~chi_20 -> ~chi_10 gam)
##           BR         NDA      ID1       ID2       ID3
#     1.24652069E-01    3     1000022        -2         2   # BR(~chi_20 -> ~chi_10 ub      u)
#     1.62516171E-01    3     1000022        -1         1   # BR(~chi_20 -> ~chi_10 db      d)
#     7.80692131E-02    3     1000022        -4         4   # BR(~chi_20 -> ~chi_10 cb      c)
#     1.61036975E-01    3     1000022        -3         3   # BR(~chi_20 -> ~chi_10 sb      s)
     3.79582627E-02    3     1000022       -11        11   # BR(~chi_20 -> ~chi_10 e+      e-)
     3.78904318E-02    3     1000022       -13        13   # BR(~chi_20 -> ~chi_10 mu+     mu-)
#     1.67723487E-02    3     1000022       -15        15   # BR(~chi_20 -> ~chi_10 tau+    tau-)
#     7.58223659E-02    3     1000022       -12        12   # BR(~chi_20 -> ~chi_10 nu_eb   nu_e)
#     7.58223659E-02    3     1000022       -14        14   # BR(~chi_20 -> ~chi_10 nu_mub  nu_mu)
#     7.58223659E-02    3     1000022       -16        16   # BR(~chi_20 -> ~chi_10 nu_taub nu_tau)
#     2.47076138E-02    3     1000024        -2         1   # BR(~chi_20 -> ~chi_1+ ub      d)
#     2.47076138E-02    3    -1000024        -1         2   # BR(~chi_20 -> ~chi_1- db      u)
#     9.39253825E-03    3     1000024        -4         3   # BR(~chi_20 -> ~chi_1+ cb      s)
#     9.39253825E-03    3    -1000024        -3         4   # BR(~chi_20 -> ~chi_1- sb      c)
#     8.23587129E-03    3     1000024       -12        11   # BR(~chi_20 -> ~chi_1+ nu_eb   e-)
#     8.23587129E-03    3    -1000024        12       -11   # BR(~chi_20 -> ~chi_1- nu_e    e+)
#     8.19084978E-03    3     1000024       -14        13   # BR(~chi_20 -> ~chi_1+ nu_mub  mu-)
#     8.19084978E-03    3    -1000024        14       -13   # BR(~chi_20 -> ~chi_1- nu_mu   mu+)
#     1.72067387E-03    3     1000024       -16        15   # BR(~chi_20 -> ~chi_1+ nu_taub tau-)
#     1.72067387E-03    3    -1000024        16       -15   # BR(~chi_20 -> ~chi_1- nu_tau  tau+)
#         PDG            Width
DECAY   1000025     3.34944354E+00   # neutralino3 decays
#          BR         NDA      ID1       ID2
     7.48910419E-02    2     1000022        23   # BR(~chi_30 -> ~chi_10   Z )
     1.70187693E-01    2     1000023        23   # BR(~chi_30 -> ~chi_20   Z )
     2.53780855E-01    2     1000024       -24   # BR(~chi_30 -> ~chi_1+   W-)
     2.53780855E-01    2    -1000024        24   # BR(~chi_30 -> ~chi_1-   W+)
     1.66429339E-01    2     1000022        25   # BR(~chi_30 -> ~chi_10   h )
     8.09302162E-02    2     1000023        25   # BR(~chi_30 -> ~chi_20   h )
#
#         PDG            Width
DECAY   1000035     1.11045266E+01   # neutralino4 decays
#          BR         NDA      ID1       ID2
     8.09418346E-02    2     1000022        23   # BR(~chi_40 -> ~chi_10   Z )
     1.76546051E-01    2     1000023        23   # BR(~chi_40 -> ~chi_20   Z )
     4.95313219E-06    2     1000025        23   # BR(~chi_40 -> ~chi_30   Z )
     2.39768573E-01    2     1000024       -24   # BR(~chi_40 -> ~chi_1+   W-)
     2.39768573E-01    2    -1000024        24   # BR(~chi_40 -> ~chi_1-   W+)
     1.74062543E-01    2     1000022        25   # BR(~chi_40 -> ~chi_10   h )
     8.85087169E-02    2     1000023        25   # BR(~chi_40 -> ~chi_20   h )
     3.98755468E-04    2     1000025        25   # BR(~chi_40 -> ~chi_30   h )
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
DECAY        36     1.51439229E+03   # A decays
#          BR         NDA      ID1       ID2
     4.51141100E-02    2           5        -5   # BR(A -> b       bb     )
     1.16003275E-02    2         -15        15   # BR(A -> tau+    tau-   )
     4.10066684E-05    2         -13        13   # BR(A -> mu+     mu-    )
     3.40831692E-05    2           3        -3   # BR(A -> s       sb     )
     2.14705316E-07    2           4        -4   # BR(A -> c       cb     )
     2.14189083E-02    2           6        -6   # BR(A -> t       tb     )
     1.99686223E-07    2          21        21   # BR(A -> g       g      )
     8.00452882E-10    2          22        22   # BR(A -> gam     gam    )
     5.72585138E-10    2          23        22   # BR(A -> Z       gam    )
     7.26174344E-09    2          23        25   # BR(A -> Z       h      )
     3.13902681E-03    2     1000024  -1000024   # BR(A -> ~chi_1+ ~chi_1-)
     2.49887382E-04    2     1000037  -1000037   # BR(A -> ~chi_2+ ~chi_2-)
     2.79089975E-01    2     1000024  -1000037   # BR(A -> ~chi_1+ ~chi_2-)
     2.79089975E-01    2     1000037  -1000024   # BR(A -> ~chi_2+ ~chi_1-)
     1.19511849E-03    2     1000022   1000022   # BR(A -> ~chi_10 ~chi_10)
     3.70914444E-04    2     1000023   1000023   # BR(A -> ~chi_20 ~chi_20)
     1.57867552E-05    2     1000025   1000025   # BR(A -> ~chi_30 ~chi_30)
     1.28482227E-04    2     1000035   1000035   # BR(A -> ~chi_40 ~chi_40)
     3.24294568E-06    2     1000022   1000023   # BR(A -> ~chi_10 ~chi_20)
     4.63180351E-02    2     1000022   1000025   # BR(A -> ~chi_10 ~chi_30)
     1.75251858E-01    2     1000022   1000035   # BR(A -> ~chi_10 ~chi_40)
     2.86386462E-02    2     1000023   1000025   # BR(A -> ~chi_20 ~chi_30)
     1.08208320E-01    2     1000023   1000035   # BR(A -> ~chi_20 ~chi_40)
     9.18722161E-05    2     1000025   1000035   # BR(A -> ~chi_30 ~chi_40)
#
#         PDG            Width
DECAY        37     1.51305696E+03   # H+ decays
#          BR         NDA      ID1       ID2
     7.10314178E-05    2           4        -5   # BR(H+ -> c       bb     )
     1.16105556E-02    2         -15        16   # BR(H+ -> tau+    nu_tau )
     4.10428242E-05    2         -13        14   # BR(H+ -> mu+     nu_mu  )
     4.54599128E-07    2           2        -5   # BR(H+ -> u       bb     )
     1.64364985E-06    2           2        -3   # BR(H+ -> u       sb     )
     3.39958415E-05    2           4        -3   # BR(H+ -> c       sb     )
     6.56382739E-02    2           6        -5   # BR(H+ -> t       bb     )
     7.26813811E-09    2          24        25   # BR(H+ -> W+      h      )
     6.07959234E-05    2     1000024   1000022   # BR(H+ -> ~chi_1+ ~chi_10)
     3.09715752E-04    2     1000024   1000023   # BR(H+ -> ~chi_1+ ~chi_20)
     8.37271466E-02    2     1000024   1000025   # BR(H+ -> ~chi_1+ ~chi_30)
     2.76490365E-01    2     1000024   1000035   # BR(H+ -> ~chi_1+ ~chi_40)
     2.87935913E-01    2     1000037   1000022   # BR(H+ -> ~chi_2+ ~chi_10)
     2.73977338E-01    2     1000037   1000023   # BR(H+ -> ~chi_2+ ~chi_20)
     1.01706016E-04    2     1000037   1000025   # BR(H+ -> ~chi_2+ ~chi_30)
     1.45059742E-08    2     1000037   1000035   # BR(H+ -> ~chi_2+ ~chi_40)
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
