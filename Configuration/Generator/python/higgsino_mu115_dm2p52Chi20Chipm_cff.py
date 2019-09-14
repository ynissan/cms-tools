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
         1     2.91545191E+03   # M_1                 
         2     2.91545191E+03   # M_2                 
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
        24     8.05133940E+01   # W+
        25     2.33740384E+02   # h
        35     1.00000294E+05   # H
        36     1.00000000E+05   # A
        37     9.99999060E+04   # H+
         5     4.87877839E+00   # b-quark pole mass calculated from mb(mb)_Msbar
   1000001     1.02565617E+05   # ~d_L
   2000001     1.02565605E+05   # ~d_R
   1000002     1.02565590E+05   # ~u_L
   2000002     1.02565595E+05   # ~u_R
   1000003     1.02565617E+05   # ~s_L
   2000003     1.02565605E+05   # ~s_R
   1000004     1.02565590E+05   # ~c_L
   2000004     1.02565595E+05   # ~c_R
   1000005     1.02564560E+05   # ~b_1
   2000005     1.02566662E+05   # ~b_2
   1000006     1.00833876E+05   # ~t_1
   2000006     1.02326945E+05   # ~t_2
   1000011     1.00000009E+05   # ~e_L
   2000011     1.00000010E+05   # ~e_R
   1000012     9.99999810E+04   # ~nu_eL
   1000013     1.00000009E+05   # ~mu_L
   2000013     1.00000010E+05   # ~mu_R
   1000014     9.99999810E+04   # ~nu_muL
   1000015     9.99978161E+04   # ~tau_1
   2000015     1.00002203E+05   # ~tau_2
   1000016     9.99999810E+04   # ~nu_tauL
   1000021     1.04586091E+05   # ~g
   1000022     1.21250518E+02   # ~chi_10
   1000023    -1.23765534E+02   # ~chi_20
   1000025     2.89070478E+03   # ~chi_30
   1000035     3.24201743E+03   # ~chi_40
   1000024     1.22366662E+02   # ~chi_1+
   1000037     3.24201465E+03   # ~chi_2+
#
BLOCK NMIX  # Neutralino Mixing Matrix
  1  1     1.26436750E-02   # N_11
  1  2    -1.89321748E-02   # N_12
  1  3     7.10565902E-01   # N_13
  1  4    -7.03262262E-01   # N_14
  2  1     9.43655018E-03   # N_21
  2  2    -1.42601201E-02   # N_22
  2  3    -7.03618433E-01   # N_23
  2  4    -7.10372227E-01   # N_24
  3  1     9.99870908E-01   # N_31
  3  2     3.41604856E-03   # N_32
  3  3    -2.33430571E-03   # N_33
  3  4     1.55257749E-02   # N_34
  4  1     3.04254145E-03   # N_41
  4  2    -9.99713235E-01   # N_42
  4  3    -3.42783160E-03   # N_43
  4  4     2.35040542E-02   # N_44
#
BLOCK UMIX  # Chargino Mixing Matrix U
  1  1    -4.83835693E-03   # U_11
  1  2     9.99988295E-01   # U_12
  2  1     9.99988295E-01   # U_21
  2  2     4.83835693E-03   # U_22
#
BLOCK VMIX  # Chargino Mixing Matrix V
  1  1    -3.31889705E-02   # V_11
  1  2     9.99449094E-01   # V_12
  2  1     9.99449094E-01   # V_21
  2  2     3.31889705E-02   # V_22
#
BLOCK STOPMIX  # Stop Mixing Matrix
  1  1     3.63889744E-02   # cos(theta_t)
  1  2     9.99337702E-01   # sin(theta_t)
  2  1    -9.99337702E-01   # -sin(theta_t)
  2  2     3.63889744E-02   # cos(theta_t)
#
BLOCK SBOTMIX  # Sbottom Mixing Matrix
  1  1     7.05063545E-01   # cos(theta_b)
  1  2     7.09144130E-01   # sin(theta_b)
  2  1    -7.09144130E-01   # -sin(theta_b)
  2  2     7.05063545E-01   # cos(theta_b)
#
BLOCK STAUMIX  # Stau Mixing Matrix
  1  1     7.07168585E-01   # cos(theta_tau)
  1  2     7.07044972E-01   # sin(theta_tau)
  2  1    -7.07044972E-01   # -sin(theta_tau)
  2  2     7.07168585E-01   # cos(theta_tau)
#
BLOCK ALPHA  # Higgs mixing
          -1.08133112E-01   # Mixing angle in the neutral Higgs boson sector
#
BLOCK HMIX Q=  1.00000030E+05  # DRbar Higgs Parameters
         1     1.15000000E+02   # mu(Q)               
         2     9.21179746E+00   # tanbeta(Q)          
         3     2.41384772E+02   # vev(Q)              
         4     9.92299956E+09   # MA^2(Q)             
#
BLOCK GAUGE Q=  1.00000030E+05  # The gauge couplings
     1     3.73855743E-01   # gprime(Q) DRbar
     2     6.30605632E-01   # g(Q) DRbar
     3     8.77148072E-01   # g3(Q) DRbar
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
  3  3     7.46869053E-01   # y_t(Q) DRbar
#
BLOCK Yd Q=  1.00000030E+05  # The Yukawa couplings
  1  1     0.00000000E+00   # y_d(Q) DRbar
  2  2     0.00000000E+00   # y_s(Q) DRbar
  3  3     1.16020994E-01   # y_b(Q) DRbar
#
BLOCK Ye Q=  1.00000030E+05  # The Yukawa couplings
  1  1     0.00000000E+00   # y_e(Q) DRbar
  2  2     0.00000000E+00   # y_mu(Q) DRbar
  3  3     9.43800576E-02   # y_tau(Q) DRbar
#
BLOCK MSOFT Q=  1.00000030E+05  # The soft SUSY breaking masses at the scale Q
         1     2.91545191E+03   # M_1                 
         2     2.91545191E+03   # M_2                 
         3     1.00000000E+05   # M_3                 
        14    -6.77437438E+05   # A_u                 
        15    -8.59633345E+05   # A_d                 
        16    -2.53493493E+05   # A_e                 
        21     9.85923580E+09   # M^2_Hd              
        22     3.31369120E+08   # M^2_Hu              
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
DECAY         6     1.37549984E+00   # top decays
#          BR         NDA      ID1       ID2
     1.00000000E+00    2           5        24   # BR(t ->  b    W+)
#
#         PDG            Width
DECAY   1000021     3.46749111E+01   # gluino decays
#          BR         NDA      ID1       ID2
     3.43480374E-02    2     1000001        -1   # BR(~g -> ~d_L  db)
     3.43480374E-02    2    -1000001         1   # BR(~g -> ~d_L* d )
     3.43484414E-02    2     2000001        -1   # BR(~g -> ~d_R  db)
     3.43484414E-02    2    -2000001         1   # BR(~g -> ~d_R* d )
     3.43489465E-02    2     1000002        -2   # BR(~g -> ~u_L  ub)
     3.43489465E-02    2    -1000002         2   # BR(~g -> ~u_L* u )
     3.43487781E-02    2     2000002        -2   # BR(~g -> ~u_R  ub)
     3.43487781E-02    2    -2000002         2   # BR(~g -> ~u_R* u )
     3.43480374E-02    2     1000003        -3   # BR(~g -> ~s_L  sb)
     3.43480374E-02    2    -1000003         3   # BR(~g -> ~s_L* s )
     3.43484414E-02    2     2000003        -3   # BR(~g -> ~s_R  sb)
     3.43484414E-02    2    -2000003         3   # BR(~g -> ~s_R* s )
     3.43489465E-02    2     1000004        -4   # BR(~g -> ~c_L  cb)
     3.43489465E-02    2    -1000004         4   # BR(~g -> ~c_L* c )
     3.43487781E-02    2     2000004        -4   # BR(~g -> ~c_R  cb)
     3.43487781E-02    2    -2000004         4   # BR(~g -> ~c_R* c )
     3.43180300E-02    2     1000005        -5   # BR(~g -> ~b_1  bb)
     3.43180300E-02    2    -1000005         5   # BR(~g -> ~b_1* b )
     3.43763439E-02    2     2000005        -5   # BR(~g -> ~b_2  bb)
     3.43763439E-02    2    -2000005         5   # BR(~g -> ~b_2* b )
     1.13702921E-01    2     1000006        -6   # BR(~g -> ~t_1  tb)
     1.13702921E-01    2    -1000006         6   # BR(~g -> ~t_1* t )
     4.28142982E-02    2     2000006        -6   # BR(~g -> ~t_2  tb)
     4.28142982E-02    2    -2000006         6   # BR(~g -> ~t_2* t )
#
#         PDG            Width
DECAY   1000006     2.44008418E+03   # stop1 decays
#          BR         NDA      ID1       ID2
     2.23119489E-01    2     1000022         6   # BR(~t_1 -> ~chi_10 t )
     2.27544777E-01    2     1000023         6   # BR(~t_1 -> ~chi_20 t )
     9.92451826E-02    2     1000025         6   # BR(~t_1 -> ~chi_30 t )
    -9.01185842E-07    2     1000035         6   # BR(~t_1 -> ~chi_40 t )
     4.50093508E-01    2     1000024         5   # BR(~t_1 -> ~chi_1+ b )
    -2.05548900E-06    2     1000037         5   # BR(~t_1 -> ~chi_2+ b )
#
#         PDG            Width
DECAY   2000006     2.32966596E+03   # stop2 decays
#          BR         NDA      ID1       ID2
     2.36090696E-01    2     1000022         6   # BR(~t_2 -> ~chi_10 t )
     2.40975944E-01    2     1000023         6   # BR(~t_2 -> ~chi_20 t )
     7.29554625E-03    2     1000025         6   # BR(~t_2 -> ~chi_30 t )
     1.69128410E-01    2     1000035         6   # BR(~t_2 -> ~chi_40 t )
     1.15704732E-02    2     1000024         5   # BR(~t_2 -> ~chi_1+ b )
     3.37949498E-01    2     1000037         5   # BR(~t_2 -> ~chi_2+ b )
     7.21855268E-03    2     1000006        25   # BR(~t_2 -> ~t_1    h )
    -1.02291208E-02    2     1000006        23   # BR(~t_2 -> ~t_1    Z )
#
#         PDG            Width
DECAY   1000005     1.06630897E+03   # sbottom1 decays
#          BR         NDA      ID1       ID2
     1.46524085E-02    2     1000022         5   # BR(~b_1 -> ~chi_10 b )
     1.11991529E-02    2     1000023         5   # BR(~b_1 -> ~chi_20 b )
     3.58337485E-02    2     1000025         5   # BR(~b_1 -> ~chi_30 b )
     1.83706685E-01    2     1000035         5   # BR(~b_1 -> ~chi_40 b )
     5.33450161E-01    2    -1000024         6   # BR(~b_1 -> ~chi_1- t )
     3.67752172E-01    2    -1000037         6   # BR(~b_1 -> ~chi_2- t )
    -4.82794654E-02    2     1000006       -24   # BR(~b_1 -> ~t_1    W-)
    -9.83148623E-02    2     2000006       -24   # BR(~b_1 -> ~t_2    W-)
#
#         PDG            Width
DECAY   2000005     1.07240568E+03   # sbottom2 decays
#          BR         NDA      ID1       ID2
     1.09593644E-02    2     1000022         5   # BR(~b_2 -> ~chi_10 b )
     1.38223136E-02    2     1000023         5   # BR(~b_2 -> ~chi_20 b )
     3.56718252E-02    2     1000025         5   # BR(~b_2 -> ~chi_30 b )
     1.85211214E-01    2     1000035         5   # BR(~b_2 -> ~chi_40 b )
     5.34318275E-01    2    -1000024         6   # BR(~b_2 -> ~chi_1- t )
     3.70758330E-01    2    -1000037         6   # BR(~b_2 -> ~chi_2- t )
    -4.87759622E-02    2     1000006       -24   # BR(~b_2 -> ~t_1    W-)
    -1.01965361E-01    2     2000006       -24   # BR(~b_2 -> ~t_2    W-)
#
#         PDG            Width
DECAY   1000002     1.19822097E+03   # sup_L decays
#          BR         NDA      ID1       ID2
     8.89968719E-05    2     1000022         2   # BR(~u_L -> ~chi_10 u)
     5.06319848E-05    2     1000023         2   # BR(~u_L -> ~chi_20 u)
     1.32996362E-02    2     1000025         2   # BR(~u_L -> ~chi_30 u)
     3.28463785E-01    2     1000035         2   # BR(~u_L -> ~chi_40 u)
     7.25986818E-04    2     1000024         1   # BR(~u_L -> ~chi_1+ d)
     6.57370964E-01    2     1000037         1   # BR(~u_L -> ~chi_2+ d)
#
#         PDG            Width
DECAY   2000002     2.46445412E+02   # sup_R decays
#          BR         NDA      ID1       ID2
     1.60045644E-04    2     1000022         2   # BR(~u_R -> ~chi_10 u)
     8.91505131E-05    2     1000023         2   # BR(~u_R -> ~chi_20 u)
     9.99741550E-01    2     1000025         2   # BR(~u_R -> ~chi_30 u)
     9.25376062E-06    2     1000035         2   # BR(~u_R -> ~chi_40 u)
#
#         PDG            Width
DECAY   1000001     1.19821976E+03   # sdown_L decays
#          BR         NDA      ID1       ID2
     1.51351860E-04    2     1000022         1   # BR(~d_L -> ~chi_10 d)
     8.56856911E-05    2     1000023         1   # BR(~d_L -> ~chi_20 d)
     1.24109279E-02    2     1000025         1   # BR(~d_L -> ~chi_30 d)
     3.29255336E-01    2     1000035         1   # BR(~d_L -> ~chi_40 d)
     1.54289907E-05    2    -1000024         2   # BR(~d_L -> ~chi_1- u)
     6.58081269E-01    2    -1000037         2   # BR(~d_L -> ~chi_2- u)
#
#         PDG            Width
DECAY   2000001     6.16113583E+01   # sdown_R decays
#          BR         NDA      ID1       ID2
     1.60045644E-04    2     1000022         1   # BR(~d_R -> ~chi_10 d)
     8.91505131E-05    2     1000023         1   # BR(~d_R -> ~chi_20 d)
     9.99741550E-01    2     1000025         1   # BR(~d_R -> ~chi_30 d)
     9.25376062E-06    2     1000035         1   # BR(~d_R -> ~chi_40 d)
#
#         PDG            Width
DECAY   1000004     1.19822097E+03   # scharm_L decays
#          BR         NDA      ID1       ID2
     8.89968719E-05    2     1000022         4   # BR(~c_L -> ~chi_10 c)
     5.06319848E-05    2     1000023         4   # BR(~c_L -> ~chi_20 c)
     1.32996362E-02    2     1000025         4   # BR(~c_L -> ~chi_30 c)
     3.28463785E-01    2     1000035         4   # BR(~c_L -> ~chi_40 c)
     7.25986818E-04    2     1000024         3   # BR(~c_L -> ~chi_1+ s)
     6.57370964E-01    2     1000037         3   # BR(~c_L -> ~chi_2+ s)
#
#         PDG            Width
DECAY   2000004     2.46445412E+02   # scharm_R decays
#          BR         NDA      ID1       ID2
     1.60045644E-04    2     1000022         4   # BR(~c_R -> ~chi_10 c)
     8.91505131E-05    2     1000023         4   # BR(~c_R -> ~chi_20 c)
     9.99741550E-01    2     1000025         4   # BR(~c_R -> ~chi_30 c)
     9.25376062E-06    2     1000035         4   # BR(~c_R -> ~chi_40 c)
#
#         PDG            Width
DECAY   1000003     1.19821976E+03   # sstrange_L decays
#          BR         NDA      ID1       ID2
     1.51351860E-04    2     1000022         3   # BR(~s_L -> ~chi_10 s)
     8.56856911E-05    2     1000023         3   # BR(~s_L -> ~chi_20 s)
     1.24109279E-02    2     1000025         3   # BR(~s_L -> ~chi_30 s)
     3.29255336E-01    2     1000035         3   # BR(~s_L -> ~chi_40 s)
     1.54289907E-05    2    -1000024         4   # BR(~s_L -> ~chi_1- c)
     6.58081269E-01    2    -1000037         4   # BR(~s_L -> ~chi_2- c)
#
#         PDG            Width
DECAY   2000003     6.16113583E+01   # sstrange_R decays
#          BR         NDA      ID1       ID2
     1.60045644E-04    2     1000022         3   # BR(~s_R -> ~chi_10 s)
     8.91505131E-05    2     1000023         3   # BR(~s_R -> ~chi_20 s)
     9.99741550E-01    2     1000025         3   # BR(~s_R -> ~chi_30 s)
     9.25376062E-06    2     1000035         3   # BR(~s_R -> ~chi_40 s)
#
#         PDG            Width
DECAY   1000011     1.32299488E+03   # selectron_L decays
#          BR         NDA      ID1       ID2
     3.91048993E-05    2     1000022        11   # BR(~e_L -> ~chi_10 e-)
     2.24521542E-05    2     1000023        11   # BR(~e_L -> ~chi_20 e-)
     1.06096982E-01    2     1000025        11   # BR(~e_L -> ~chi_30 e-)
     2.97116360E-01    2     1000035        11   # BR(~e_L -> ~chi_40 e-)
     1.39985230E-05    2    -1000024        12   # BR(~e_L -> ~chi_1- nu_e)
     5.96711102E-01    2    -1000037        12   # BR(~e_L -> ~chi_2- nu_e)
#
#         PDG            Width
DECAY   2000011     5.55190932E+02   # selectron_R decays
#          BR         NDA      ID1       ID2
     1.60129484E-04    2     1000022        11   # BR(~e_R -> ~chi_10 e-)
     8.91971769E-05    2     1000023        11   # BR(~e_R -> ~chi_20 e-)
     9.99741420E-01    2     1000025        11   # BR(~e_R -> ~chi_30 e-)
     9.25306288E-06    2     1000035        11   # BR(~e_R -> ~chi_40 e-)
#
#         PDG            Width
DECAY   1000013     1.32299488E+03   # smuon_L decays
#          BR         NDA      ID1       ID2
     3.91048993E-05    2     1000022        13   # BR(~mu_L -> ~chi_10 mu-)
     2.24521542E-05    2     1000023        13   # BR(~mu_L -> ~chi_20 mu-)
     1.06096982E-01    2     1000025        13   # BR(~mu_L -> ~chi_30 mu-)
     2.97116360E-01    2     1000035        13   # BR(~mu_L -> ~chi_40 mu-)
     1.39985230E-05    2    -1000024        14   # BR(~mu_L -> ~chi_1- nu_mu)
     5.96711102E-01    2    -1000037        14   # BR(~mu_L -> ~chi_2- nu_mu)
#
#         PDG            Width
DECAY   2000013     5.55190932E+02   # smuon_R decays
#          BR         NDA      ID1       ID2
     1.60129484E-04    2     1000022        13   # BR(~mu_R -> ~chi_10 mu-)
     8.91971769E-05    2     1000023        13   # BR(~mu_R -> ~chi_20 mu-)
     9.99741420E-01    2     1000025        13   # BR(~mu_R -> ~chi_30 mu-)
     9.25306288E-06    2     1000035        13   # BR(~mu_R -> ~chi_40 mu-)
#
#         PDG            Width
DECAY   1000015     9.65721061E+02   # stau_1 decays
#          BR         NDA      ID1       ID2
     1.09656463E-02    2     1000022        15   # BR(~tau_1 -> ~chi_10  tau-)
     7.91442263E-03    2     1000023        15   # BR(~tau_1 -> ~chi_20  tau-)
     3.59884523E-01    2     1000025        15   # BR(~tau_1 -> ~chi_30  tau-)
     2.03255065E-01    2     1000035        15   # BR(~tau_1 -> ~chi_40  tau-)
     9.77580030E-03    2    -1000024        16   # BR(~tau_1 -> ~chi_1-  nu_tau)
     4.08204542E-01    2    -1000037        16   # BR(~tau_1 -> ~chi_2-  nu_tau)
#
#         PDG            Width
DECAY   2000015     9.65627894E+02   # stau_2 decays
#          BR         NDA      ID1       ID2
     7.71069812E-03    2     1000022        15   # BR(~tau_2 -> ~chi_10  tau-)
     1.03381263E-02    2     1000023        15   # BR(~tau_2 -> ~chi_20  tau-)
     3.60247743E-01    2     1000025        15   # BR(~tau_2 -> ~chi_30  tau-)
     2.03806554E-01    2     1000035        15   # BR(~tau_2 -> ~chi_40  tau-)
     8.59381780E-03    2    -1000024        16   # BR(~tau_2 -> ~chi_1-  nu_tau)
     4.09303060E-01    2    -1000037        16   # BR(~tau_2 -> ~chi_2-  nu_tau)
#
#         PDG            Width
DECAY   1000012     1.32299566E+03   # snu_eL decays
#          BR         NDA      ID1       ID2
     2.08826065E-04    2     1000022        12   # BR(~nu_eL -> ~chi_10 nu_e)
     1.17863179E-04    2     1000023        12   # BR(~nu_eL -> ~chi_20 nu_e)
     1.03679174E-01    2     1000025        12   # BR(~nu_eL -> ~chi_30 nu_e)
     2.99268201E-01    2     1000035        12   # BR(~nu_eL -> ~chi_40 nu_e)
     6.58678663E-04    2     1000024        11   # BR(~nu_eL -> ~chi_1+ e-)
     5.96067258E-01    2     1000037        11   # BR(~nu_eL -> ~chi_2+ e-)
#
#         PDG            Width
DECAY   1000014     1.32299566E+03   # snu_muL decays
#          BR         NDA      ID1       ID2
     2.08826065E-04    2     1000022        14   # BR(~nu_muL -> ~chi_10 nu_mu)
     1.17863179E-04    2     1000023        14   # BR(~nu_muL -> ~chi_20 nu_mu)
     1.03679174E-01    2     1000025        14   # BR(~nu_muL -> ~chi_30 nu_mu)
     2.99268201E-01    2     1000035        14   # BR(~nu_muL -> ~chi_40 nu_mu)
     6.58678663E-04    2     1000024        13   # BR(~nu_muL -> ~chi_1+ mu-)
     5.96067258E-01    2     1000037        13   # BR(~nu_muL -> ~chi_2+ mu-)
#
#         PDG            Width
DECAY   1000016     1.34071670E+03   # snu_tauL decays
#          BR         NDA      ID1       ID2
     2.06065888E-04    2     1000022        16   # BR(~nu_tauL -> ~chi_10 nu_tau)
     1.16305312E-04    2     1000023        16   # BR(~nu_tauL -> ~chi_20 nu_tau)
     1.02308785E-01    2     1000025        16   # BR(~nu_tauL -> ~chi_30 nu_tau)
     2.95312597E-01    2     1000035        16   # BR(~nu_tauL -> ~chi_40 nu_tau)
     1.38672511E-02    2     1000024        15   # BR(~nu_tauL -> ~chi_1+ tau-)
     5.88188996E-01    2     1000037        15   # BR(~nu_tauL -> ~chi_2+ tau-)
#
#         PDG            Width
DECAY   1000024     1.07132331E-12   # chargino1+ decays
#           BR         NDA      ID1       ID2       ID3
     6.05219087E-01    3     1000022         2        -1   # BR(~chi_1+ -> ~chi_10 u    db)
     2.01739696E-01    3     1000022       -11        12   # BR(~chi_1+ -> ~chi_10 e+   nu_e)
     1.93041217E-01    3     1000022       -13        14   # BR(~chi_1+ -> ~chi_10 mu+  nu_mu)
#
#         PDG            Width
DECAY   1000037     2.42028822E+01   # chargino2+ decays
#          BR         NDA      ID1       ID2
     2.53190012E-01    2     1000024        23   # BR(~chi_2+ -> ~chi_1+  Z )
     2.37933931E-01    2     1000022        24   # BR(~chi_2+ -> ~chi_10  W+)
     2.42614310E-01    2     1000023        24   # BR(~chi_2+ -> ~chi_20  W+)
     1.42843520E-04    2     1000025        24   # BR(~chi_2+ -> ~chi_30  W+)
     2.66118903E-01    2     1000024        25   # BR(~chi_2+ -> ~chi_1+  h )
#
#         PDG            Width
DECAY   1000022     0.00000000E+00   # neutralino1 decays
#
#         PDG            Width
DECAY   1000023     9.81552150E-11   # neutralino2 decays
##          BR         NDA      ID1       ID2
#     2.47582893E-01    2     1000022        22   # BR(~chi_20 -> ~chi_10 gam)
##           BR         NDA      ID1       ID2       ID3
#     1.14431313E-01    3     1000022        -2         2   # BR(~chi_20 -> ~chi_10 ub      u)
#     1.49243176E-01    3     1000022        -1         1   # BR(~chi_20 -> ~chi_10 db      d)
#     1.42528909E-01    3     1000022        -3         3   # BR(~chi_20 -> ~chi_10 sb      s)
     3.49249380E-02    3     1000022       -11        11   # BR(~chi_20 -> ~chi_10 e+      e-)
     3.46110409E-02    3     1000022       -13        13   # BR(~chi_20 -> ~chi_10 mu+     mu-)
#     6.97368012E-02    3     1000022       -12        12   # BR(~chi_20 -> ~chi_10 nu_eb   nu_e)
#     6.97368012E-02    3     1000022       -14        14   # BR(~chi_20 -> ~chi_10 nu_mub  nu_mu)
#     6.97368012E-02    3     1000022       -16        16   # BR(~chi_20 -> ~chi_10 nu_taub nu_tau)
#     2.03533006E-02    3     1000024        -2         1   # BR(~chi_20 -> ~chi_1+ ub      d)
#     2.03533006E-02    3    -1000024        -1         2   # BR(~chi_20 -> ~chi_1- db      u)
#     6.78443355E-03    3     1000024       -12        11   # BR(~chi_20 -> ~chi_1+ nu_eb   e-)
#     6.78443355E-03    3    -1000024        12       -11   # BR(~chi_20 -> ~chi_1- nu_e    e+)
#     6.59592884E-03    3     1000024       -14        13   # BR(~chi_20 -> ~chi_1+ nu_mub  mu-)
#     6.59592884E-03    3    -1000024        14       -13   # BR(~chi_20 -> ~chi_1- nu_mu   mu+)
#         PDG            Width
DECAY   1000025     7.57406609E+00   # neutralino3 decays
#          BR         NDA      ID1       ID2
     8.74674149E-02    2     1000022        23   # BR(~chi_30 -> ~chi_10   Z )
     1.63668548E-01    2     1000023        23   # BR(~chi_30 -> ~chi_20   Z )
     2.43241719E-01    2     1000024       -24   # BR(~chi_30 -> ~chi_1+   W-)
     2.43241719E-01    2    -1000024        24   # BR(~chi_30 -> ~chi_1-   W+)
     1.68583656E-01    2     1000022        25   # BR(~chi_30 -> ~chi_10   h )
     9.37969422E-02    2     1000023        25   # BR(~chi_30 -> ~chi_20   h )
#
#         PDG            Width
DECAY   1000035     2.42035880E+01   # neutralino4 decays
#          BR         NDA      ID1       ID2
     8.95372182E-02    2     1000022        23   # BR(~chi_40 -> ~chi_10   Z )
     1.64500676E-01    2     1000023        23   # BR(~chi_40 -> ~chi_20   Z )
     5.43983222E-07    2     1000025        23   # BR(~chi_40 -> ~chi_30   Z )
     2.39808908E-01    2     1000024       -24   # BR(~chi_40 -> ~chi_1+   W-)
     2.39808908E-01    2    -1000024        24   # BR(~chi_40 -> ~chi_1-   W+)
     1.69898870E-01    2     1000022        25   # BR(~chi_40 -> ~chi_10   h )
     9.63171904E-02    2     1000023        25   # BR(~chi_40 -> ~chi_20   h )
     1.27686139E-04    2     1000025        25   # BR(~chi_40 -> ~chi_30   h )
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
DECAY        36     1.51230959E+03   # A decays
#          BR         NDA      ID1       ID2
     4.52408291E-02    2           5        -5   # BR(A -> b       bb     )
     1.16302945E-02    2         -15        15   # BR(A -> tau+    tau-   )
     4.11126006E-05    2         -13        13   # BR(A -> mu+     mu-    )
     3.41711969E-05    2           3        -3   # BR(A -> s       sb     )
     2.14742350E-07    2           4        -4   # BR(A -> c       cb     )
     2.14226028E-02    2           6        -6   # BR(A -> t       tb     )
     1.99784026E-07    2          21        21   # BR(A -> g       g      )
     7.23300594E-10    2          22        22   # BR(A -> gam     gam    )
     5.73555317E-10    2          23        22   # BR(A -> Z       gam    )
     2.31077502E-09    2          23        25   # BR(A -> Z       h      )
     6.32067634E-04    2     1000024  -1000024   # BR(A -> ~chi_1+ ~chi_1-)
     3.95161637E-05    2     1000037  -1000037   # BR(A -> ~chi_2+ ~chi_2-)
     2.80406712E-01    2     1000024  -1000037   # BR(A -> ~chi_1+ ~chi_2-)
     2.80406712E-01    2     1000037  -1000024   # BR(A -> ~chi_2+ ~chi_1-)
     2.26644940E-04    2     1000022   1000022   # BR(A -> ~chi_10 ~chi_10)
     8.11162128E-05    2     1000023   1000023   # BR(A -> ~chi_20 ~chi_20)
     2.50298267E-06    2     1000025   1000025   # BR(A -> ~chi_30 ~chi_30)
     1.98931971E-05    2     1000035   1000035   # BR(A -> ~chi_40 ~chi_40)
     2.26797970E-07    2     1000022   1000023   # BR(A -> ~chi_10 ~chi_20)
     4.79400613E-02    2     1000022   1000025   # BR(A -> ~chi_10 ~chi_30)
     1.72219279E-01    2     1000022   1000035   # BR(A -> ~chi_10 ~chi_40)
     3.04125228E-02    2     1000023   1000025   # BR(A -> ~chi_20 ~chi_30)
     1.09228995E-01    2     1000023   1000035   # BR(A -> ~chi_20 ~chi_40)
     1.43210050E-05    2     1000025   1000035   # BR(A -> ~chi_30 ~chi_40)
#
#         PDG            Width
DECAY        37     1.51095720E+03   # H+ decays
#          BR         NDA      ID1       ID2
     7.12151463E-05    2           4        -5   # BR(H+ -> c       bb     )
     1.16406934E-02    2         -15        16   # BR(H+ -> tau+    nu_tau )
     4.11493601E-05    2         -13        14   # BR(H+ -> mu+     nu_mu  )
     4.55774990E-07    2           2        -5   # BR(H+ -> u       bb     )
     1.64791434E-06    2           2        -3   # BR(H+ -> u       sb     )
     3.40835869E-05    2           4        -3   # BR(H+ -> c       sb     )
     6.57570321E-02    2           6        -5   # BR(H+ -> t       bb     )
     2.31283805E-09    2          24        25   # BR(H+ -> W+      h      )
     1.64428918E-05    2     1000024   1000022   # BR(H+ -> ~chi_1+ ~chi_10)
     5.68974467E-05    2     1000024   1000023   # BR(H+ -> ~chi_1+ ~chi_20)
     8.04681662E-02    2     1000024   1000025   # BR(H+ -> ~chi_1+ ~chi_30)
     2.79933725E-01    2     1000024   1000035   # BR(H+ -> ~chi_1+ ~chi_40)
     2.83706601E-01    2     1000037   1000022   # BR(H+ -> ~chi_2+ ~chi_10)
     2.78257093E-01    2     1000037   1000023   # BR(H+ -> ~chi_2+ ~chi_20)
     1.47949036E-05    2     1000037   1000025   # BR(H+ -> ~chi_2+ ~chi_30)
     1.24835557E-10    2     1000037   1000035   # BR(H+ -> ~chi_2+ ~chi_40)
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
