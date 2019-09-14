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
         1     5.73883224E+02   # M_1                 
         2     5.73883224E+02   # M_2                 
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
        24     8.04998571E+01   # W+
        25     1.47238737E+02   # h
        35     1.00000314E+05   # H
        36     1.00000000E+05   # A
        37     9.99999228E+04   # H+
         5     4.87877839E+00   # b-quark pole mass calculated from mb(mb)_Msbar
   1000001     1.02565646E+05   # ~d_L
   2000001     1.02565634E+05   # ~d_R
   1000002     1.02565618E+05   # ~u_L
   2000002     1.02565624E+05   # ~u_R
   1000003     1.02565646E+05   # ~s_L
   2000003     1.02565634E+05   # ~s_R
   1000004     1.02565618E+05   # ~c_L
   2000004     1.02565624E+05   # ~c_R
   1000005     1.02564877E+05   # ~b_1
   2000005     1.02566402E+05   # ~b_2
   1000006     1.00805197E+05   # ~t_1
   2000006     1.02328350E+05   # ~t_2
   1000011     1.00000009E+05   # ~e_L
   2000011     1.00000010E+05   # ~e_R
   1000012     9.99999811E+04   # ~nu_eL
   1000013     1.00000009E+05   # ~mu_L
   2000013     1.00000010E+05   # ~mu_R
   1000014     9.99999811E+04   # ~nu_muL
   1000015     9.99978178E+04   # ~tau_1
   2000015     1.00002201E+05   # ~tau_2
   1000016     9.99999811E+04   # ~nu_tauL
   1000021     1.04586145E+05   # ~g
   1000022     9.80640811E+01   # ~chi_10
   1000023    -1.10900190E+02   # ~chi_20
   1000025     5.71195339E+02   # ~chi_30
   1000035     6.71691878E+02   # ~chi_40
   1000024     1.03348536E+02   # ~chi_1+
   1000037     6.71462725E+02   # ~chi_2+
#
BLOCK NMIX  # Neutralino Mixing Matrix
  1  1     7.18117829E-02   # N_11
  1  2    -1.01487512E-01   # N_12
  1  3     7.24910854E-01   # N_13
  1  4    -6.77530521E-01   # N_14
  2  1     4.25162140E-02   # N_21
  2  2    -6.33507161E-02   # N_22
  2  3    -6.87788527E-01   # N_23
  2  4    -7.21890574E-01   # N_24
  3  1     9.95096984E-01   # N_31
  3  2     6.28821875E-02   # N_32
  3  3    -2.12405699E-02   # N_33
  3  4     7.33257184E-02   # N_34
  4  1     5.30794845E-02   # N_41
  4  2    -9.90824304E-01   # N_42
  4  3    -3.16233228E-02   # N_43
  4  4     1.20207036E-01   # N_44
#
BLOCK UMIX  # Chargino Mixing Matrix U
  1  1    -4.35077973E-02   # U_11
  1  2     9.99053087E-01   # U_12
  2  1     9.99053087E-01   # U_21
  2  2     4.35077973E-02   # U_22
#
BLOCK VMIX  # Chargino Mixing Matrix V
  1  1    -1.66189833E-01   # V_11
  1  2     9.86093778E-01   # V_12
  2  1     9.86093778E-01   # V_21
  2  2     1.66189833E-01   # V_22
#
BLOCK STOPMIX  # Stop Mixing Matrix
  1  1     3.56726811E-02   # cos(theta_t)
  1  2     9.99363527E-01   # sin(theta_t)
  2  1    -9.99363527E-01   # -sin(theta_t)
  2  2     3.56726811E-02   # cos(theta_t)
#
BLOCK SBOTMIX  # Sbottom Mixing Matrix
  1  1     7.04290816E-01   # cos(theta_b)
  1  2     7.09911577E-01   # sin(theta_b)
  2  1    -7.09911577E-01   # -sin(theta_b)
  2  2     7.04290816E-01   # cos(theta_b)
#
BLOCK STAUMIX  # Stau Mixing Matrix
  1  1     7.07153589E-01   # cos(theta_tau)
  1  2     7.07059970E-01   # sin(theta_tau)
  2  1    -7.07059970E-01   # -sin(theta_tau)
  2  2     7.07153589E-01   # cos(theta_tau)
#
BLOCK ALPHA  # Higgs mixing
          -1.08385804E-01   # Mixing angle in the neutral Higgs boson sector
#
BLOCK HMIX Q=  1.00000031E+05  # DRbar Higgs Parameters
         1     1.00000000E+02   # mu(Q)               
         2     9.19016314E+00   # tanbeta(Q)          
         3     2.39996957E+02   # vev(Q)              
         4     9.91881403E+09   # MA^2(Q)             
#
BLOCK GAUGE Q=  1.00000031E+05  # The gauge couplings
     1     3.73833197E-01   # gprime(Q) DRbar
     2     6.34533562E-01   # g(Q) DRbar
     3     8.77153019E-01   # g3(Q) DRbar
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
  3  3     7.52989634E-01   # y_t(Q) DRbar
#
BLOCK Yd Q=  1.00000031E+05  # The Yukawa couplings
  1  1     0.00000000E+00   # y_d(Q) DRbar
  2  2     0.00000000E+00   # y_s(Q) DRbar
  3  3     8.47079194E-02   # y_b(Q) DRbar
#
BLOCK Ye Q=  1.00000031E+05  # The Yukawa couplings
  1  1     0.00000000E+00   # y_e(Q) DRbar
  2  2     0.00000000E+00   # y_mu(Q) DRbar
  3  3     9.48319349E-02   # y_tau(Q) DRbar
#
BLOCK MSOFT Q=  1.00000031E+05  # The soft SUSY breaking masses at the scale Q
         1     5.73883224E+02   # M_1                 
         2     5.73883224E+02   # M_2                 
         3     1.00000000E+05   # M_3                 
        14    -6.77437438E+05   # A_u                 
        15    -8.59633345E+05   # A_d                 
        16    -2.53493493E+05   # A_e                 
        21     9.85324114E+09   # M^2_Hd              
        22     3.35974465E+08   # M^2_Hu              
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
DECAY         6     1.39327589E+00   # top decays
#          BR         NDA      ID1       ID2
     1.00000000E+00    2           5        24   # BR(t ->  b    W+)
#
#         PDG            Width
DECAY   1000021     3.47889190E+01   # gluino decays
#          BR         NDA      ID1       ID2
     3.42365585E-02    2     1000001        -1   # BR(~g -> ~d_L  db)
     3.42365585E-02    2    -1000001         1   # BR(~g -> ~d_L* d )
     3.42369612E-02    2     2000001        -1   # BR(~g -> ~d_R  db)
     3.42369612E-02    2    -2000001         1   # BR(~g -> ~d_R* d )
     3.42374981E-02    2     1000002        -2   # BR(~g -> ~u_L  ub)
     3.42374981E-02    2    -1000002         2   # BR(~g -> ~u_L* u )
     3.42372968E-02    2     2000002        -2   # BR(~g -> ~u_R  ub)
     3.42372968E-02    2    -2000002         2   # BR(~g -> ~u_R* u )
     3.42365585E-02    2     1000003        -3   # BR(~g -> ~s_L  sb)
     3.42365585E-02    2    -1000003         3   # BR(~g -> ~s_L* s )
     3.42369612E-02    2     2000003        -3   # BR(~g -> ~s_R  sb)
     3.42369612E-02    2    -2000003         3   # BR(~g -> ~s_R* s )
     3.42374981E-02    2     1000004        -4   # BR(~g -> ~c_L  cb)
     3.42374981E-02    2    -1000004         4   # BR(~g -> ~c_L* c )
     3.42372968E-02    2     2000004        -4   # BR(~g -> ~c_R  cb)
     3.42372968E-02    2    -2000004         4   # BR(~g -> ~c_R* c )
     3.41902747E-02    2     1000005        -5   # BR(~g -> ~b_1  bb)
     3.41902747E-02    2    -1000005         5   # BR(~g -> ~b_1* b )
     3.42674464E-02    2     2000005        -5   # BR(~g -> ~b_2  bb)
     3.42674464E-02    2    -2000005         5   # BR(~g -> ~b_2* b )
     1.15025477E-01    2     1000006        -6   # BR(~g -> ~t_1  tb)
     1.15025477E-01    2    -1000006         6   # BR(~g -> ~t_1* t )
     4.26201727E-02    2     2000006        -6   # BR(~g -> ~t_2  tb)
     4.26201727E-02    2    -2000006         6   # BR(~g -> ~t_2* t )
#
#         PDG            Width
DECAY   1000006     2.47562477E+03   # stop1 decays
#          BR         NDA      ID1       ID2
     2.09552156E-01    2     1000022         6   # BR(~t_1 -> ~chi_10 t )
     2.36533148E-01    2     1000023         6   # BR(~t_1 -> ~chi_20 t )
     9.86994889E-02    2     1000025         6   # BR(~t_1 -> ~chi_30 t )
     4.49750082E-03    2     1000035         6   # BR(~t_1 -> ~chi_40 t )
     4.42581527E-01    2     1000024         5   # BR(~t_1 -> ~chi_1+ b )
     8.13617983E-03    2     1000037         5   # BR(~t_1 -> ~chi_2+ b )
#
#         PDG            Width
DECAY   2000006     2.35205078E+03   # stop2 decays
#          BR         NDA      ID1       ID2
     2.20124066E-01    2     1000022         6   # BR(~t_2 -> ~chi_10 t )
     2.49960588E-01    2     1000023         6   # BR(~t_2 -> ~chi_20 t )
     1.48834610E-02    2     1000025         6   # BR(~t_2 -> ~chi_30 t )
     1.72464294E-01    2     1000035         6   # BR(~t_2 -> ~chi_40 t )
     1.10315578E-02    2     1000024         5   # BR(~t_2 -> ~chi_1+ b )
     3.34461628E-01    2     1000037         5   # BR(~t_2 -> ~chi_2+ b )
     7.47107199E-03    2     1000006        25   # BR(~t_2 -> ~t_1    h )
    -1.03966674E-02    2     1000006        23   # BR(~t_2 -> ~t_1    Z )
#
#         PDG            Width
DECAY   1000005     1.06258906E+03   # sbottom1 decays
#          BR         NDA      ID1       ID2
     1.71709436E-02    2     1000022         5   # BR(~b_1 -> ~chi_10 b )
     3.06769012E-03    2     1000023         5   # BR(~b_1 -> ~chi_20 b )
     3.14188205E-02    2     1000025         5   # BR(~b_1 -> ~chi_30 b )
     1.85074201E-01    2     1000035         5   # BR(~b_1 -> ~chi_40 b )
     5.27467621E-01    2    -1000024         6   # BR(~b_1 -> ~chi_1- t )
     3.83280109E-01    2    -1000037         6   # BR(~b_1 -> ~chi_2- t )
    -4.92746520E-02    2     1000006       -24   # BR(~b_1 -> ~t_1    W-)
    -9.82047329E-02    2     2000006       -24   # BR(~b_1 -> ~t_2    W-)
#
#         PDG            Width
DECAY   2000005     1.07282435E+03   # sbottom2 decays
#          BR         NDA      ID1       ID2
     2.32291693E-03    2     1000022         5   # BR(~b_2 -> ~chi_10 b )
     1.16339390E-02    2     1000023         5   # BR(~b_2 -> ~chi_20 b )
     3.23505171E-02    2     1000025         5   # BR(~b_2 -> ~chi_30 b )
     1.90384305E-01    2     1000035         5   # BR(~b_2 -> ~chi_40 b )
     5.20604104E-01    2    -1000024         6   # BR(~b_2 -> ~chi_1- t )
     3.93507391E-01    2    -1000037         6   # BR(~b_2 -> ~chi_2- t )
    -4.97435803E-02    2     1000006       -24   # BR(~b_2 -> ~t_1    W-)
    -1.01059593E-01    2     2000006       -24   # BR(~b_2 -> ~t_2    W-)
#
#         PDG            Width
DECAY   1000002     1.21482370E+03   # sup_L decays
#          BR         NDA      ID1       ID2
     2.51304593E-03    2     1000022         2   # BR(~u_L -> ~chi_10 u)
     9.95573899E-04    2     1000023         2   # BR(~u_L -> ~chi_20 u)
     2.19577747E-02    2     1000025         2   # BR(~u_L -> ~chi_30 u)
     3.16328513E-01    2     1000035         2   # BR(~u_L -> ~chi_40 u)
     1.81788428E-02    2     1000024         1   # BR(~u_L -> ~chi_1+ d)
     6.40026250E-01    2     1000037         1   # BR(~u_L -> ~chi_2+ d)
#
#         PDG            Width
DECAY   2000002     2.46701495E+02   # sup_R decays
#          BR         NDA      ID1       ID2
     5.15684369E-03    2     1000022         2   # BR(~u_R -> ~chi_10 u)
     1.80760034E-03    2     1000023         2   # BR(~u_R -> ~chi_20 u)
     9.90218145E-01    2     1000025         2   # BR(~u_R -> ~chi_30 u)
     2.81741122E-03    2     1000035         2   # BR(~u_R -> ~chi_40 u)
#
#         PDG            Width
DECAY   1000001     1.21482400E+03   # sdown_L decays
#          BR         NDA      ID1       ID2
     4.39711730E-03    2     1000022         1   # BR(~d_L -> ~chi_10 d)
     1.69187302E-03    2     1000023         1   # BR(~d_L -> ~chi_20 d)
     5.78108652E-03    2     1000025         1   # BR(~d_L -> ~chi_30 d)
     3.29924682E-01    2     1000035         1   # BR(~d_L -> ~chi_40 d)
     1.24592391E-03    2    -1000024         2   # BR(~d_L -> ~chi_1- u)
     6.56959317E-01    2    -1000037         2   # BR(~d_L -> ~chi_2- u)
#
#         PDG            Width
DECAY   2000001     6.16753788E+01   # sdown_R decays
#          BR         NDA      ID1       ID2
     5.15684369E-03    2     1000022         1   # BR(~d_R -> ~chi_10 d)
     1.80760034E-03    2     1000023         1   # BR(~d_R -> ~chi_20 d)
     9.90218145E-01    2     1000025         1   # BR(~d_R -> ~chi_30 d)
     2.81741122E-03    2     1000035         1   # BR(~d_R -> ~chi_40 d)
#
#         PDG            Width
DECAY   1000004     1.21482370E+03   # scharm_L decays
#          BR         NDA      ID1       ID2
     2.51304593E-03    2     1000022         4   # BR(~c_L -> ~chi_10 c)
     9.95573899E-04    2     1000023         4   # BR(~c_L -> ~chi_20 c)
     2.19577747E-02    2     1000025         4   # BR(~c_L -> ~chi_30 c)
     3.16328513E-01    2     1000035         4   # BR(~c_L -> ~chi_40 c)
     1.81788428E-02    2     1000024         3   # BR(~c_L -> ~chi_1+ s)
     6.40026250E-01    2     1000037         3   # BR(~c_L -> ~chi_2+ s)
#
#         PDG            Width
DECAY   2000004     2.46701495E+02   # scharm_R decays
#          BR         NDA      ID1       ID2
     5.15684369E-03    2     1000022         4   # BR(~c_R -> ~chi_10 c)
     1.80760034E-03    2     1000023         4   # BR(~c_R -> ~chi_20 c)
     9.90218145E-01    2     1000025         4   # BR(~c_R -> ~chi_30 c)
     2.81741122E-03    2     1000035         4   # BR(~c_R -> ~chi_40 c)
#
#         PDG            Width
DECAY   1000003     1.21482400E+03   # sstrange_L decays
#          BR         NDA      ID1       ID2
     4.39711730E-03    2     1000022         3   # BR(~s_L -> ~chi_10 s)
     1.69187302E-03    2     1000023         3   # BR(~s_L -> ~chi_20 s)
     5.78108652E-03    2     1000025         3   # BR(~s_L -> ~chi_30 s)
     3.29924682E-01    2     1000035         3   # BR(~s_L -> ~chi_40 s)
     1.24592391E-03    2    -1000024         4   # BR(~s_L -> ~chi_1- c)
     6.56959317E-01    2    -1000037         4   # BR(~s_L -> ~chi_2- c)
#
#         PDG            Width
DECAY   2000003     6.16753788E+01   # sstrange_R decays
#          BR         NDA      ID1       ID2
     5.15684369E-03    2     1000022         3   # BR(~s_R -> ~chi_10 s)
     1.80760034E-03    2     1000023         3   # BR(~s_R -> ~chi_20 s)
     9.90218145E-01    2     1000025         3   # BR(~s_R -> ~chi_30 s)
     2.81741122E-03    2     1000035         3   # BR(~s_R -> ~chi_40 s)
#
#         PDG            Width
DECAY   1000011     1.34041576E+03   # selectron_L decays
#          BR         NDA      ID1       ID2
     1.04644598E-03    2     1000022        11   # BR(~e_L -> ~chi_10 e-)
     4.38350654E-04    2     1000023        11   # BR(~e_L -> ~chi_20 e-)
     1.25897852E-01    2     1000025        11   # BR(~e_L -> ~chi_30 e-)
     2.75085909E-01    2     1000035        11   # BR(~e_L -> ~chi_40 e-)
     1.13118365E-03    2    -1000024        12   # BR(~e_L -> ~chi_1- nu_e)
     5.96400258E-01    2    -1000037        12   # BR(~e_L -> ~chi_2- nu_e)
#
#         PDG            Width
DECAY   2000011     5.56016570E+02   # selectron_R decays
#          BR         NDA      ID1       ID2
     5.15725686E-03    2     1000022        11   # BR(~e_R -> ~chi_10 e-)
     1.80774130E-03    2     1000023        11   # BR(~e_R -> ~chi_20 e-)
     9.90217642E-01    2     1000025        11   # BR(~e_R -> ~chi_30 e-)
     2.81736025E-03    2     1000035        11   # BR(~e_R -> ~chi_40 e-)
#
#         PDG            Width
DECAY   1000013     1.34041576E+03   # smuon_L decays
#          BR         NDA      ID1       ID2
     1.04644598E-03    2     1000022        13   # BR(~mu_L -> ~chi_10 mu-)
     4.38350654E-04    2     1000023        13   # BR(~mu_L -> ~chi_20 mu-)
     1.25897852E-01    2     1000025        13   # BR(~mu_L -> ~chi_30 mu-)
     2.75085909E-01    2     1000035        13   # BR(~mu_L -> ~chi_40 mu-)
     1.13118365E-03    2    -1000024        14   # BR(~mu_L -> ~chi_1- nu_mu)
     5.96400258E-01    2    -1000037        14   # BR(~mu_L -> ~chi_2- nu_mu)
#
#         PDG            Width
DECAY   2000013     5.56016570E+02   # smuon_R decays
#          BR         NDA      ID1       ID2
     5.15725686E-03    2     1000022        13   # BR(~mu_R -> ~chi_10 mu-)
     1.80774130E-03    2     1000023        13   # BR(~mu_R -> ~chi_20 mu-)
     9.90217642E-01    2     1000025        13   # BR(~mu_R -> ~chi_30 mu-)
     2.81736025E-03    2     1000035        13   # BR(~mu_R -> ~chi_40 mu-)
#
#         PDG            Width
DECAY   1000015     9.75083088E+02   # stau_1 decays
#          BR         NDA      ID1       ID2
     2.08802900E-02    2     1000022        15   # BR(~tau_1 -> ~chi_10  tau-)
     4.21814235E-03    2     1000023        15   # BR(~tau_1 -> ~chi_20  tau-)
     3.67866563E-01    2     1000025        15   # BR(~tau_1 -> ~chi_30  tau-)
     1.87112655E-01    2     1000035        15   # BR(~tau_1 -> ~chi_40  tau-)
     1.52693134E-02    2    -1000024        16   # BR(~tau_1 -> ~chi_1-  nu_tau)
     4.04653036E-01    2    -1000037        16   # BR(~tau_1 -> ~chi_2-  nu_tau)
#
#         PDG            Width
DECAY   2000015     9.75022714E+02   # stau_2 decays
#          BR         NDA      ID1       ID2
     2.78275371E-03    2     1000022        15   # BR(~tau_2 -> ~chi_10  tau-)
     1.47758833E-02    2     1000023        15   # BR(~tau_2 -> ~chi_20  tau-)
     3.69887383E-01    2     1000025        15   # BR(~tau_2 -> ~chi_30  tau-)
     1.92694489E-01    2     1000035        15   # BR(~tau_2 -> ~chi_40  tau-)
     4.59935097E-03    2    -1000024        16   # BR(~tau_2 -> ~chi_1-  nu_tau)
     4.15260140E-01    2    -1000037        16   # BR(~tau_2 -> ~chi_2-  nu_tau)
#
#         PDG            Width
DECAY   1000012     1.34041656E+03   # snu_eL decays
#          BR         NDA      ID1       ID2
     6.17813274E-03    2     1000022        12   # BR(~nu_eL -> ~chi_10 nu_e)
     2.33487182E-03    2     1000023        12   # BR(~nu_eL -> ~chi_20 nu_e)
     8.18404860E-02    2     1000025        12   # BR(~nu_eL -> ~chi_30 nu_e)
     3.12114235E-01    2     1000035        12   # BR(~nu_eL -> ~chi_40 nu_e)
     1.65046930E-02    2     1000024        11   # BR(~nu_eL -> ~chi_1+ e-)
     5.81027581E-01    2     1000037        11   # BR(~nu_eL -> ~chi_2+ e-)
#
#         PDG            Width
DECAY   1000014     1.34041656E+03   # snu_muL decays
#          BR         NDA      ID1       ID2
     6.17813274E-03    2     1000022        14   # BR(~nu_muL -> ~chi_10 nu_mu)
     2.33487182E-03    2     1000023        14   # BR(~nu_muL -> ~chi_20 nu_mu)
     8.18404860E-02    2     1000025        14   # BR(~nu_muL -> ~chi_30 nu_mu)
     3.12114235E-01    2     1000035        14   # BR(~nu_muL -> ~chi_40 nu_mu)
     1.65046930E-02    2     1000024        13   # BR(~nu_muL -> ~chi_1+ mu-)
     5.81027581E-01    2     1000037        13   # BR(~nu_muL -> ~chi_2+ mu-)
#
#         PDG            Width
DECAY   1000016     1.35830771E+03   # snu_tauL decays
#          BR         NDA      ID1       ID2
     6.09675655E-03    2     1000022        16   # BR(~nu_tauL -> ~chi_10 nu_tau)
     2.30411771E-03    2     1000023        16   # BR(~nu_tauL -> ~chi_20 nu_tau)
     8.07625119E-02    2     1000025        16   # BR(~nu_tauL -> ~chi_30 nu_tau)
     3.08003176E-01    2     1000035        16   # BR(~nu_tauL -> ~chi_40 nu_tau)
     2.94340152E-02    2     1000024        15   # BR(~nu_tauL -> ~chi_1+ tau-)
     5.73399423E-01    2     1000037        15   # BR(~nu_tauL -> ~chi_2+ tau-)
#
#         PDG            Width
DECAY   1000024     3.87463300E-09   # chargino1+ decays
#           BR         NDA      ID1       ID2       ID3
     3.89270648E-01    3     1000022         2        -1   # BR(~chi_1+ -> ~chi_10 u    db)
     2.75920035E-01    3     1000022         4        -3   # BR(~chi_1+ -> ~chi_10 c    sb)
     1.29756883E-01    3     1000022       -11        12   # BR(~chi_1+ -> ~chi_10 e+   nu_e)
     1.29498072E-01    3     1000022       -13        14   # BR(~chi_1+ -> ~chi_10 mu+  nu_mu)
     7.55543612E-02    3     1000022       -15        16   # BR(~chi_1+ -> ~chi_10 tau+ nu_tau)
#
#         PDG            Width
DECAY   1000037     5.02223510E+00   # chargino2+ decays
#          BR         NDA      ID1       ID2
     2.59007068E-01    2     1000024        23   # BR(~chi_2+ -> ~chi_1+  Z )
     2.31438185E-01    2     1000022        24   # BR(~chi_2+ -> ~chi_10  W+)
     2.59591795E-01    2     1000023        24   # BR(~chi_2+ -> ~chi_20  W+)
     1.16058007E-03    2     1000025        24   # BR(~chi_2+ -> ~chi_30  W+)
     2.48802372E-01    2     1000024        25   # BR(~chi_2+ -> ~chi_1+  h )
#
#         PDG            Width
DECAY   1000022     0.00000000E+00   # neutralino1 decays
#
#         PDG            Width
DECAY   1000023     3.02903452E-07   # neutralino2 decays
##          BR         NDA      ID1       ID2
#     7.03650637E-03    2     1000022        22   # BR(~chi_20 -> ~chi_10 gam)
##           BR         NDA      ID1       ID2       ID3
#     1.11913129E-01    3     1000022        -2         2   # BR(~chi_20 -> ~chi_10 ub      u)
#     1.45858883E-01    3     1000022        -1         1   # BR(~chi_20 -> ~chi_10 db      d)
#     1.03647928E-01    3     1000022        -4         4   # BR(~chi_20 -> ~chi_10 cb      c)
#     1.45599133E-01    3     1000022        -3         3   # BR(~chi_20 -> ~chi_10 sb      s)
#     2.60519905E-02    3     1000022        -5         5   # BR(~chi_20 -> ~chi_10 bb      b)
     3.40095702E-02    3     1000022       -11        11   # BR(~chi_20 -> ~chi_10 e+      e-)
     3.39974220E-02    3     1000022       -13        13   # BR(~chi_20 -> ~chi_10 mu+     mu-)
#     3.03659420E-02    3     1000022       -15        15   # BR(~chi_20 -> ~chi_10 tau+    tau-)
#     6.79553273E-02    3     1000022       -12        12   # BR(~chi_20 -> ~chi_10 nu_eb   nu_e)
#     6.79553273E-02    3     1000022       -14        14   # BR(~chi_20 -> ~chi_10 nu_mub  nu_mu)
#     6.79553273E-02    3     1000022       -16        16   # BR(~chi_20 -> ~chi_10 nu_taub nu_tau)
#     2.85018077E-02    3     1000024        -2         1   # BR(~chi_20 -> ~chi_1+ ub      d)
#     2.85018077E-02    3    -1000024        -1         2   # BR(~chi_20 -> ~chi_1- db      u)
#     2.40516007E-02    3     1000024        -4         3   # BR(~chi_20 -> ~chi_1+ cb      s)
#     2.40516007E-02    3    -1000024        -3         4   # BR(~chi_20 -> ~chi_1- sb      c)
#     9.50060260E-03    3     1000024       -12        11   # BR(~chi_20 -> ~chi_1+ nu_eb   e-)
#     9.50060260E-03    3    -1000024        12       -11   # BR(~chi_20 -> ~chi_1- nu_e    e+)
#     9.49130710E-03    3     1000024       -14        13   # BR(~chi_20 -> ~chi_1+ nu_mub  mu-)
#     9.49130710E-03    3    -1000024        14       -13   # BR(~chi_20 -> ~chi_1- nu_mu   mu+)
#     7.28143891E-03    3     1000024       -16        15   # BR(~chi_20 -> ~chi_1+ nu_taub tau-)
#     7.28143891E-03    3    -1000024        16       -15   # BR(~chi_20 -> ~chi_1- nu_tau  tau+)
#         PDG            Width
DECAY   1000025     1.41045971E+00   # neutralino3 decays
#          BR         NDA      ID1       ID2
     4.72035681E-02    2     1000022        23   # BR(~chi_30 -> ~chi_10   Z )
     1.68440427E-01    2     1000023        23   # BR(~chi_30 -> ~chi_20   Z )
     2.99437562E-01    2     1000024       -24   # BR(~chi_30 -> ~chi_1+   W-)
     2.99437562E-01    2    -1000024        24   # BR(~chi_30 -> ~chi_1-   W+)
     1.39644632E-01    2     1000022        25   # BR(~chi_30 -> ~chi_10   h )
     4.58362486E-02    2     1000023        25   # BR(~chi_30 -> ~chi_20   h )
#
#         PDG            Width
DECAY   1000035     5.00386531E+00   # neutralino4 decays
#          BR         NDA      ID1       ID2
     6.40471156E-02    2     1000022        23   # BR(~chi_40 -> ~chi_10   Z )
     2.08731917E-01    2     1000023        23   # BR(~chi_40 -> ~chi_20   Z )
     3.05033789E-05    2     1000025        23   # BR(~chi_40 -> ~chi_30   Z )
     2.40949570E-01    2     1000024       -24   # BR(~chi_40 -> ~chi_1+   W-)
     2.40949570E-01    2    -1000024        24   # BR(~chi_40 -> ~chi_1-   W+)
     1.78052472E-01    2     1000022        25   # BR(~chi_40 -> ~chi_10   h )
     6.72388509E-02    2     1000023        25   # BR(~chi_40 -> ~chi_20   h )
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
DECAY        36     1.51456161E+03   # A decays
#          BR         NDA      ID1       ID2
     4.49932916E-02    2           5        -5   # BR(A -> b       bb     )
     1.15585180E-02    2         -15        15   # BR(A -> tau+    tau-   )
     4.08588737E-05    2         -13        13   # BR(A -> mu+     mu-    )
     3.39603834E-05    2           3        -3   # BR(A -> s       sb     )
     2.15433770E-07    2           4        -4   # BR(A -> c       cb     )
     2.14915786E-02    2           6        -6   # BR(A -> t       tb     )
     2.00179455E-07    2          21        21   # BR(A -> g       g      )
     8.26213897E-10    2          22        22   # BR(A -> gam     gam    )
     5.73031267E-10    2          23        22   # BR(A -> Z       gam    )
     1.13343091E-08    2          23        25   # BR(A -> Z       h      )
     1.61737424E-02    2     1000024  -1000024   # BR(A -> ~chi_1+ ~chi_1-)
     2.06310163E-03    2     1000037  -1000037   # BR(A -> ~chi_2+ ~chi_2-)
     2.71673372E-01    2     1000024  -1000037   # BR(A -> ~chi_1+ ~chi_2-)
     2.71673372E-01    2     1000037  -1000024   # BR(A -> ~chi_2+ ~chi_1-)
     6.90916050E-03    2     1000022   1000022   # BR(A -> ~chi_10 ~chi_10)
     1.52282292E-03    2     1000023   1000023   # BR(A -> ~chi_20 ~chi_20)
     1.03176833E-04    2     1000025   1000025   # BR(A -> ~chi_30 ~chi_30)
     1.15182624E-03    2     1000035   1000035   # BR(A -> ~chi_40 ~chi_40)
     7.50849788E-05    2     1000022   1000023   # BR(A -> ~chi_10 ~chi_20)
     3.77004349E-02    2     1000022   1000025   # BR(A -> ~chi_10 ~chi_30)
     1.81003987E-01    2     1000022   1000035   # BR(A -> ~chi_10 ~chi_40)
     2.28256024E-02    2     1000023   1000025   # BR(A -> ~chi_20 ~chi_30)
     1.08294147E-01    2     1000023   1000035   # BR(A -> ~chi_20 ~chi_40)
     7.11533073E-04    2     1000025   1000035   # BR(A -> ~chi_30 ~chi_40)
#
#         PDG            Width
DECAY        37     1.51316567E+03   # H+ decays
#          BR         NDA      ID1       ID2
     7.07782230E-05    2           4        -5   # BR(H+ -> c       bb     )
     1.15691722E-02    2         -15        16   # BR(H+ -> tau+    nu_tau )
     4.08965357E-05    2         -13        14   # BR(H+ -> mu+     nu_mu  )
     4.52978675E-07    2           2        -5   # BR(H+ -> u       bb     )
     1.63779716E-06    2           2        -3   # BR(H+ -> u       sb     )
     3.38761182E-05    2           4        -3   # BR(H+ -> c       sb     )
     6.55529555E-02    2           6        -5   # BR(H+ -> t       bb     )
     1.13447453E-08    2          24        25   # BR(H+ -> W+      h      )
     1.27075519E-04    2     1000024   1000022   # BR(H+ -> ~chi_1+ ~chi_10)
     1.96918354E-03    2     1000024   1000023   # BR(H+ -> ~chi_1+ ~chi_20)
     9.79181649E-02    2     1000024   1000025   # BR(H+ -> ~chi_1+ ~chi_30)
     2.61057933E-01    2     1000024   1000035   # BR(H+ -> ~chi_1+ ~chi_40)
     2.95942225E-01    2     1000037   1000022   # BR(H+ -> ~chi_2+ ~chi_10)
     2.64716460E-01    2     1000037   1000023   # BR(H+ -> ~chi_2+ ~chi_20)
     9.96806382E-04    2     1000037   1000025   # BR(H+ -> ~chi_2+ ~chi_30)
     2.37076192E-06    2     1000037   1000035   # BR(H+ -> ~chi_2+ ~chi_40)
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
