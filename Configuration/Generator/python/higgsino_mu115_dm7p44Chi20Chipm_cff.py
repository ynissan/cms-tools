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
         1     9.86546697E+02   # M_1                 
         2     9.86546697E+02   # M_2                 
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
        24     8.05035939E+01   # W+
        25     1.59713667E+02   # h
        35     1.00000302E+05   # H
        36     1.00000000E+05   # A
        37     9.99999190E+04   # H+
         5     4.87877839E+00   # b-quark pole mass calculated from mb(mb)_Msbar
   1000001     1.02565629E+05   # ~d_L
   2000001     1.02565617E+05   # ~d_R
   1000002     1.02565601E+05   # ~u_L
   2000002     1.02565607E+05   # ~u_R
   1000003     1.02565629E+05   # ~s_L
   2000003     1.02565617E+05   # ~s_R
   1000004     1.02565601E+05   # ~c_L
   2000004     1.02565607E+05   # ~c_R
   1000005     1.02564572E+05   # ~b_1
   2000005     1.02566674E+05   # ~b_2
   1000006     1.00815248E+05   # ~t_1
   2000006     1.02322159E+05   # ~t_2
   1000011     1.00000009E+05   # ~e_L
   2000011     1.00000010E+05   # ~e_R
   1000012     9.99999810E+04   # ~nu_eL
   1000013     1.00000009E+05   # ~mu_L
   2000013     1.00000010E+05   # ~mu_R
   1000014     9.99999810E+04   # ~nu_muL
   1000015     9.99978163E+04   # ~tau_1
   2000015     1.00002203E+05   # ~tau_2
   1000016     9.99999810E+04   # ~nu_tauL
   1000021     1.04586113E+05   # ~g
   1000022     1.17790207E+02   # ~chi_10
   1000023    -1.25227822E+02   # ~chi_20
   1000025     9.78850625E+02   # ~chi_30
   1000035     1.13040094E+03   # ~chi_40
   1000024     1.20970049E+02   # ~chi_1+
   1000037     1.13034789E+03   # ~chi_2+
#
BLOCK NMIX  # Neutralino Mixing Matrix
  1  1     4.01396580E-02   # N_11
  1  2    -5.79720634E-02   # N_12
  1  3     7.16709580E-01   # N_13
  1  4    -6.93797827E-01   # N_14
  2  1     2.59368181E-02   # N_21
  2  2    -3.87160592E-02   # N_22
  2  3    -6.97136188E-01   # N_23
  2  4    -7.15422591E-01   # N_24
  3  1     9.98645096E-01   # N_31
  3  2     2.39002986E-02   # N_32
  3  3    -1.03953147E-02   # N_33
  3  4     4.50409329E-02   # N_34
  4  1     2.05927607E-02   # N_41
  4  2    -9.97280844E-01   # N_42
  4  3    -1.48475914E-02   # N_43
  4  4     6.91838484E-02   # N_44
#
BLOCK UMIX  # Chargino Mixing Matrix U
  1  1    -2.07515529E-02   # U_11
  1  2     9.99784663E-01   # U_12
  2  1     9.99784663E-01   # U_21
  2  2     2.07515529E-02   # U_22
#
BLOCK VMIX  # Chargino Mixing Matrix V
  1  1    -9.69044587E-02   # V_11
  1  2     9.95293688E-01   # V_12
  2  1     9.95293688E-01   # V_21
  2  2     9.69044587E-02   # V_22
#
BLOCK STOPMIX  # Stop Mixing Matrix
  1  1     3.60534094E-02   # cos(theta_t)
  1  2     9.99349864E-01   # sin(theta_t)
  2  1    -9.99349864E-01   # -sin(theta_t)
  2  2     3.60534094E-02   # cos(theta_t)
#
BLOCK SBOTMIX  # Sbottom Mixing Matrix
  1  1     7.05065793E-01   # cos(theta_b)
  1  2     7.09141895E-01   # sin(theta_b)
  2  1    -7.09141895E-01   # -sin(theta_b)
  2  2     7.05065793E-01   # cos(theta_b)
#
BLOCK STAUMIX  # Stau Mixing Matrix
  1  1     7.07158966E-01   # cos(theta_tau)
  1  2     7.07054593E-01   # sin(theta_tau)
  2  1    -7.07054593E-01   # -sin(theta_tau)
  2  2     7.07158966E-01   # cos(theta_tau)
#
BLOCK ALPHA  # Higgs mixing
          -1.08216731E-01   # Mixing angle in the neutral Higgs boson sector
#
BLOCK HMIX Q=  1.00000031E+05  # DRbar Higgs Parameters
         1     1.15000000E+02   # mu(Q)               
         2     9.20463073E+00   # tanbeta(Q)          
         3     2.40461743E+02   # vev(Q)              
         4     9.92190152E+09   # MA^2(Q)             
#
BLOCK GAUGE Q=  1.00000031E+05  # The gauge couplings
     1     3.73825598E-01   # gprime(Q) DRbar
     2     6.33076486E-01   # g(Q) DRbar
     3     8.77150105E-01   # g3(Q) DRbar
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
  3  3     7.50839736E-01   # y_t(Q) DRbar
#
BLOCK Yd Q=  1.00000031E+05  # The Yukawa couplings
  1  1     0.00000000E+00   # y_d(Q) DRbar
  2  2     0.00000000E+00   # y_s(Q) DRbar
  3  3     1.16517623E-01   # y_b(Q) DRbar
#
BLOCK Ye Q=  1.00000031E+05  # The Yukawa couplings
  1  1     0.00000000E+00   # y_e(Q) DRbar
  2  2     0.00000000E+00   # y_mu(Q) DRbar
  3  3     9.47579613E-02   # y_tau(Q) DRbar
#
BLOCK MSOFT Q=  1.00000031E+05  # The soft SUSY breaking masses at the scale Q
         1     9.86546697E+02   # M_1                 
         2     9.86546697E+02   # M_2                 
         3     1.00000000E+05   # M_3                 
        14    -6.77437438E+05   # A_u                 
        15    -8.59633345E+05   # A_d                 
        16    -2.53493493E+05   # A_e                 
        21     9.85902732E+09   # M^2_Hd              
        22     3.34362432E+08   # M^2_Hu              
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
DECAY         6     1.38672312E+00   # top decays
#          BR         NDA      ID1       ID2
     1.00000000E+00    2           5        24   # BR(t ->  b    W+)
#
#         PDG            Width
DECAY   1000021     3.47641267E+01   # gluino decays
#          BR         NDA      ID1       ID2
     3.42602533E-02    2     1000001        -1   # BR(~g -> ~d_L  db)
     3.42602533E-02    2    -1000001         1   # BR(~g -> ~d_L* d )
     3.42606563E-02    2     2000001        -1   # BR(~g -> ~d_R  db)
     3.42606563E-02    2    -2000001         1   # BR(~g -> ~d_R* d )
     3.42611936E-02    2     1000002        -2   # BR(~g -> ~u_L  ub)
     3.42611936E-02    2    -1000002         2   # BR(~g -> ~u_L* u )
     3.42609921E-02    2     2000002        -2   # BR(~g -> ~u_R  ub)
     3.42609921E-02    2    -2000002         2   # BR(~g -> ~u_R* u )
     3.42602533E-02    2     1000003        -3   # BR(~g -> ~s_L  sb)
     3.42602533E-02    2    -1000003         3   # BR(~g -> ~s_L* s )
     3.42606563E-02    2     2000003        -3   # BR(~g -> ~s_R  sb)
     3.42606563E-02    2    -2000003         3   # BR(~g -> ~s_R* s )
     3.42611936E-02    2     1000004        -4   # BR(~g -> ~c_L  cb)
     3.42611936E-02    2    -1000004         4   # BR(~g -> ~c_L* c )
     3.42609921E-02    2     2000004        -4   # BR(~g -> ~c_R  cb)
     3.42609921E-02    2    -2000004         4   # BR(~g -> ~c_R* c )
     3.42336363E-02    2     1000005        -5   # BR(~g -> ~b_1  bb)
     3.42336363E-02    2    -1000005         5   # BR(~g -> ~b_1* b )
     3.42918562E-02    2     2000005        -5   # BR(~g -> ~b_2  bb)
     3.42918562E-02    2    -2000005         5   # BR(~g -> ~b_2* b )
     1.14509094E-01    2     1000006        -6   # BR(~g -> ~t_1  tb)
     1.14509094E-01    2    -1000006         6   # BR(~g -> ~t_1* t )
     4.28792228E-02    2     2000006        -6   # BR(~g -> ~t_2  tb)
     4.28792228E-02    2    -2000006         6   # BR(~g -> ~t_2* t )
#
#         PDG            Width
DECAY   1000006     2.46345110E+03   # stop1 decays
#          BR         NDA      ID1       ID2
     2.18290782E-01    2     1000022         6   # BR(~t_1 -> ~chi_10 t )
     2.31560168E-01    2     1000023         6   # BR(~t_1 -> ~chi_20 t )
     9.86163893E-02    2     1000025         6   # BR(~t_1 -> ~chi_30 t )
     9.86192248E-04    2     1000035         6   # BR(~t_1 -> ~chi_40 t )
     4.48676300E-01    2     1000024         5   # BR(~t_1 -> ~chi_1+ b )
     1.87016841E-03    2     1000037         5   # BR(~t_1 -> ~chi_2+ b )
#
#         PDG            Width
DECAY   2000006     2.35294613E+03   # stop2 decays
#          BR         NDA      ID1       ID2
     2.29455479E-01    2     1000022         6   # BR(~t_2 -> ~chi_10 t )
     2.44198485E-01    2     1000023         6   # BR(~t_2 -> ~chi_20 t )
     9.87939837E-03    2     1000025         6   # BR(~t_2 -> ~chi_30 t )
     1.70074979E-01    2     1000035         6   # BR(~t_2 -> ~chi_40 t )
     1.23656801E-02    2     1000024         5   # BR(~t_2 -> ~chi_1+ b )
     3.36925747E-01    2     1000037         5   # BR(~t_2 -> ~chi_2+ b )
     7.34054220E-03    2     1000006        25   # BR(~t_2 -> ~t_1    h )
    -1.02403119E-02    2     1000006        23   # BR(~t_2 -> ~t_1    Z )
#
#         PDG            Width
DECAY   1000005     1.06893884E+03   # sbottom1 decays
#          BR         NDA      ID1       ID2
     1.95925032E-02    2     1000022         5   # BR(~b_1 -> ~chi_10 b )
     9.05815088E-03    2     1000023         5   # BR(~b_1 -> ~chi_20 b )
     3.38691431E-02    2     1000025         5   # BR(~b_1 -> ~chi_30 b )
     1.84248479E-01    2     1000035         5   # BR(~b_1 -> ~chi_40 b )
     5.35770826E-01    2    -1000024         6   # BR(~b_1 -> ~chi_1- t )
     3.72274948E-01    2    -1000037         6   # BR(~b_1 -> ~chi_2- t )
    -4.90996118E-02    2     1000006       -24   # BR(~b_1 -> ~t_1    W-)
    -1.05714438E-01    2     2000006       -24   # BR(~b_1 -> ~t_2    W-)
#
#         PDG            Width
DECAY   2000005     1.07487342E+03   # sbottom2 decays
#          BR         NDA      ID1       ID2
     8.16931455E-03    2     1000022         5   # BR(~b_2 -> ~chi_10 b )
     1.62978801E-02    2     1000023         5   # BR(~b_2 -> ~chi_20 b )
     3.45841023E-02    2     1000025         5   # BR(~b_2 -> ~chi_30 b )
     1.88034872E-01    2     1000035         5   # BR(~b_2 -> ~chi_40 b )
     5.32348861E-01    2    -1000024         6   # BR(~b_2 -> ~chi_1- t )
     3.79742429E-01    2    -1000037         6   # BR(~b_2 -> ~chi_2- t )
    -4.96100712E-02    2     1000006       -24   # BR(~b_2 -> ~t_1    W-)
    -1.09567387E-01    2     2000006       -24   # BR(~b_2 -> ~t_2    W-)
#
#         PDG            Width
DECAY   1000002     1.20922203E+03   # sup_L decays
#          BR         NDA      ID1       ID2
     8.25120557E-04    2     1000022         2   # BR(~u_L -> ~chi_10 u)
     3.71791490E-04    2     1000023         2   # BR(~u_L -> ~chi_20 u)
     1.59954271E-02    2     1000025         2   # BR(~u_L -> ~chi_30 u)
     3.24640866E-01    2     1000035         2   # BR(~u_L -> ~chi_40 u)
     6.18096319E-03    2     1000024         1   # BR(~u_L -> ~chi_1+ d)
     6.51985832E-01    2     1000037         1   # BR(~u_L -> ~chi_2+ d)
#
#         PDG            Width
DECAY   2000002     2.46678183E+02   # sup_R decays
#          BR         NDA      ID1       ID2
     1.61125518E-03    2     1000022         2   # BR(~u_R -> ~chi_10 u)
     6.72745445E-04    2     1000023         2   # BR(~u_R -> ~chi_20 u)
     9.97291953E-01    2     1000025         2   # BR(~u_R -> ~chi_30 u)
     4.24046338E-04    2     1000035         2   # BR(~u_R -> ~chi_40 u)
#
#         PDG            Width
DECAY   1000001     1.20922158E+03   # sdown_L decays
#          BR         NDA      ID1       ID2
     1.42807308E-03    2     1000022         1   # BR(~d_L -> ~chi_10 d)
     6.31986481E-04    2     1000023         1   # BR(~d_L -> ~chi_20 d)
     9.81117582E-03    2     1000025         1   # BR(~d_L -> ~chi_30 d)
     3.29962017E-01    2     1000035         1   # BR(~d_L -> ~chi_40 d)
     2.83445851E-04    2    -1000024         2   # BR(~d_L -> ~chi_1- u)
     6.57883301E-01    2    -1000037         2   # BR(~d_L -> ~chi_2- u)
#
#         PDG            Width
DECAY   2000001     6.16695508E+01   # sdown_R decays
#          BR         NDA      ID1       ID2
     1.61125518E-03    2     1000022         1   # BR(~d_R -> ~chi_10 d)
     6.72745445E-04    2     1000023         1   # BR(~d_R -> ~chi_20 d)
     9.97291953E-01    2     1000025         1   # BR(~d_R -> ~chi_30 d)
     4.24046338E-04    2     1000035         1   # BR(~d_R -> ~chi_40 d)
#
#         PDG            Width
DECAY   1000004     1.20922203E+03   # scharm_L decays
#          BR         NDA      ID1       ID2
     8.25120557E-04    2     1000022         4   # BR(~c_L -> ~chi_10 c)
     3.71791490E-04    2     1000023         4   # BR(~c_L -> ~chi_20 c)
     1.59954271E-02    2     1000025         4   # BR(~c_L -> ~chi_30 c)
     3.24640866E-01    2     1000035         4   # BR(~c_L -> ~chi_40 c)
     6.18096319E-03    2     1000024         3   # BR(~c_L -> ~chi_1+ s)
     6.51985832E-01    2     1000037         3   # BR(~c_L -> ~chi_2+ s)
#
#         PDG            Width
DECAY   2000004     2.46678183E+02   # scharm_R decays
#          BR         NDA      ID1       ID2
     1.61125518E-03    2     1000022         4   # BR(~c_R -> ~chi_10 c)
     6.72745445E-04    2     1000023         4   # BR(~c_R -> ~chi_20 c)
     9.97291953E-01    2     1000025         4   # BR(~c_R -> ~chi_30 c)
     4.24046338E-04    2     1000035         4   # BR(~c_R -> ~chi_40 c)
#
#         PDG            Width
DECAY   1000003     1.20922158E+03   # sstrange_L decays
#          BR         NDA      ID1       ID2
     1.42807308E-03    2     1000022         3   # BR(~s_L -> ~chi_10 s)
     6.31986481E-04    2     1000023         3   # BR(~s_L -> ~chi_20 s)
     9.81117582E-03    2     1000025         3   # BR(~s_L -> ~chi_30 s)
     3.29962017E-01    2     1000035         3   # BR(~s_L -> ~chi_40 s)
     2.83445851E-04    2    -1000024         4   # BR(~s_L -> ~chi_1- c)
     6.57883301E-01    2    -1000037         4   # BR(~s_L -> ~chi_2- c)
#
#         PDG            Width
DECAY   2000003     6.16695508E+01   # sstrange_R decays
#          BR         NDA      ID1       ID2
     1.61125518E-03    2     1000022         3   # BR(~s_R -> ~chi_10 s)
     6.72745445E-04    2     1000023         3   # BR(~s_R -> ~chi_20 s)
     9.97291953E-01    2     1000025         3   # BR(~s_R -> ~chi_30 s)
     4.24046338E-04    2     1000035         3   # BR(~s_R -> ~chi_40 s)
#
#         PDG            Width
DECAY   1000011     1.33468347E+03   # selectron_L decays
#          BR         NDA      ID1       ID2
     3.50800958E-04    2     1000022        11   # BR(~e_L -> ~chi_10 e-)
     1.63563922E-04    2     1000023        11   # BR(~e_L -> ~chi_20 e-)
     1.12436812E-01    2     1000025        11   # BR(~e_L -> ~chi_30 e-)
     2.89802712E-01    2     1000035        11   # BR(~e_L -> ~chi_40 e-)
     2.57255223E-04    2    -1000024        12   # BR(~e_L -> ~chi_1- nu_e)
     5.96988856E-01    2    -1000037        12   # BR(~e_L -> ~chi_2- nu_e)
#
#         PDG            Width
DECAY   2000011     5.55923720E+02   # selectron_R decays
#          BR         NDA      ID1       ID2
     1.61149582E-03    2     1000022        11   # BR(~e_R -> ~chi_10 e-)
     6.72845082E-04    2     1000023        11   # BR(~e_R -> ~chi_20 e-)
     9.97291625E-01    2     1000025        11   # BR(~e_R -> ~chi_30 e-)
     4.24034509E-04    2     1000035        11   # BR(~e_R -> ~chi_40 e-)
#
#         PDG            Width
DECAY   1000013     1.33468347E+03   # smuon_L decays
#          BR         NDA      ID1       ID2
     3.50800958E-04    2     1000022        13   # BR(~mu_L -> ~chi_10 mu-)
     1.63563922E-04    2     1000023        13   # BR(~mu_L -> ~chi_20 mu-)
     1.12436812E-01    2     1000025        13   # BR(~mu_L -> ~chi_30 mu-)
     2.89802712E-01    2     1000035        13   # BR(~mu_L -> ~chi_40 mu-)
     2.57255223E-04    2    -1000024        14   # BR(~mu_L -> ~chi_1- nu_mu)
     5.96988856E-01    2    -1000037        14   # BR(~mu_L -> ~chi_2- nu_mu)
#
#         PDG            Width
DECAY   2000013     5.55923720E+02   # smuon_R decays
#          BR         NDA      ID1       ID2
     1.61149582E-03    2     1000022        13   # BR(~mu_R -> ~chi_10 mu-)
     6.72845082E-04    2     1000023        13   # BR(~mu_R -> ~chi_20 mu-)
     9.97291625E-01    2     1000025        13   # BR(~mu_R -> ~chi_30 mu-)
     4.24034509E-04    2     1000035        13   # BR(~mu_R -> ~chi_40 mu-)
#
#         PDG            Width
DECAY   1000015     9.72134421E+02   # stau_1 decays
#          BR         NDA      ID1       ID2
     1.52215490E-02    2     1000022        15   # BR(~tau_1 -> ~chi_10  tau-)
     5.96506834E-03    2     1000023        15   # BR(~tau_1 -> ~chi_20  tau-)
     3.61792596E-01    2     1000025        15   # BR(~tau_1 -> ~chi_30  tau-)
     1.97790622E-01    2     1000035        15   # BR(~tau_1 -> ~chi_40  tau-)
     1.19057073E-02    2    -1000024        16   # BR(~tau_1 -> ~chi_1-  nu_tau)
     4.07324457E-01    2    -1000037        16   # BR(~tau_1 -> ~chi_2-  nu_tau)
#
#         PDG            Width
DECAY   2000015     9.72062497E+02   # stau_2 decays
#          BR         NDA      ID1       ID2
     5.05954074E-03    2     1000022        15   # BR(~tau_2 -> ~chi_10  tau-)
     1.25060647E-02    2     1000023        15   # BR(~tau_2 -> ~chi_20  tau-)
     3.62917478E-01    2     1000025        15   # BR(~tau_2 -> ~chi_30  tau-)
     2.00356952E-01    2     1000035        15   # BR(~tau_2 -> ~chi_40  tau-)
     6.81525058E-03    2    -1000024        16   # BR(~tau_2 -> ~chi_1-  nu_tau)
     4.12344714E-01    2    -1000037        16   # BR(~tau_2 -> ~chi_2-  nu_tau)
#
#         PDG            Width
DECAY   1000012     1.33468425E+03   # snu_eL decays
#          BR         NDA      ID1       ID2
     1.99251639E-03    2     1000022        12   # BR(~nu_eL -> ~chi_10 nu_e)
     8.72020330E-04    2     1000023        12   # BR(~nu_eL -> ~chi_20 nu_e)
     9.56007491E-02    2     1000025        12   # BR(~nu_eL -> ~chi_30 nu_e)
     3.04287770E-01    2     1000035        12   # BR(~nu_eL -> ~chi_40 nu_e)
     5.60983568E-03    2     1000024        11   # BR(~nu_eL -> ~chi_1+ e-)
     5.91637108E-01    2     1000037        11   # BR(~nu_eL -> ~chi_2+ e-)
#
#         PDG            Width
DECAY   1000014     1.33468425E+03   # snu_muL decays
#          BR         NDA      ID1       ID2
     1.99251639E-03    2     1000022        14   # BR(~nu_muL -> ~chi_10 nu_mu)
     8.72020330E-04    2     1000023        14   # BR(~nu_muL -> ~chi_20 nu_mu)
     9.56007491E-02    2     1000025        14   # BR(~nu_muL -> ~chi_30 nu_mu)
     3.04287770E-01    2     1000035        14   # BR(~nu_muL -> ~chi_40 nu_mu)
     5.60983568E-03    2     1000024        13   # BR(~nu_muL -> ~chi_1+ mu-)
     5.91637108E-01    2     1000037        13   # BR(~nu_muL -> ~chi_2+ mu-)
#
#         PDG            Width
DECAY   1000016     1.35254749E+03   # snu_tauL decays
#          BR         NDA      ID1       ID2
     1.96620102E-03    2     1000022        16   # BR(~nu_tauL -> ~chi_10 nu_tau)
     8.60503466E-04    2     1000023        16   # BR(~nu_tauL -> ~chi_20 nu_tau)
     9.43381399E-02    2     1000025        16   # BR(~nu_tauL -> ~chi_30 nu_tau)
     3.00269010E-01    2     1000035        16   # BR(~nu_tauL -> ~chi_40 nu_tau)
     1.87371645E-02    2     1000024        15   # BR(~nu_tauL -> ~chi_1+ tau-)
     5.83828981E-01    2     1000037        15   # BR(~nu_tauL -> ~chi_2+ tau-)
#
#         PDG            Width
DECAY   1000024     2.55763804E-10   # chargino1+ decays
#           BR         NDA      ID1       ID2       ID3
     4.73299681E-01    3     1000022         2        -1   # BR(~chi_1+ -> ~chi_10 u    db)
     1.79275278E-01    3     1000022         4        -3   # BR(~chi_1+ -> ~chi_10 c    sb)
     1.57766561E-01    3     1000022       -11        12   # BR(~chi_1+ -> ~chi_10 e+   nu_e)
     1.56901131E-01    3     1000022       -13        14   # BR(~chi_1+ -> ~chi_10 mu+  nu_mu)
     3.27573496E-02    3     1000022       -15        16   # BR(~chi_1+ -> ~chi_10 tau+ nu_tau)
#
#         PDG            Width
DECAY   1000037     8.59889168E+00   # chargino2+ decays
#          BR         NDA      ID1       ID2
     2.54799607E-01    2     1000024        23   # BR(~chi_2+ -> ~chi_1+  Z )
     2.35046663E-01    2     1000022        24   # BR(~chi_2+ -> ~chi_10  W+)
     2.49011928E-01    2     1000023        24   # BR(~chi_2+ -> ~chi_20  W+)
     9.82329973E-04    2     1000025        24   # BR(~chi_2+ -> ~chi_30  W+)
     2.60159472E-01    2     1000024        25   # BR(~chi_2+ -> ~chi_1+  h )
#
#         PDG            Width
DECAY   1000022     0.00000000E+00   # neutralino1 decays
#
#         PDG            Width
DECAY   1000023     1.99845855E-08   # neutralino2 decays
##          BR         NDA      ID1       ID2
#     2.73102427E-02    2     1000022        22   # BR(~chi_20 -> ~chi_10 gam)
##           BR         NDA      ID1       ID2       ID3
#     1.21001254E-01    3     1000022        -2         2   # BR(~chi_20 -> ~chi_10 ub      u)
#     1.57743888E-01    3     1000022        -1         1   # BR(~chi_20 -> ~chi_10 db      d)
#     9.47440012E-02    3     1000022        -4         4   # BR(~chi_20 -> ~chi_10 cb      c)
#     1.56917781E-01    3     1000022        -3         3   # BR(~chi_20 -> ~chi_10 sb      s)
     3.68283584E-02    3     1000022       -11        11   # BR(~chi_20 -> ~chi_10 e+      e-)
     3.67904439E-02    3     1000022       -13        13   # BR(~chi_20 -> ~chi_10 mu+     mu-)
#     2.48900329E-02    3     1000022       -15        15   # BR(~chi_20 -> ~chi_10 tau+    tau-)
#     7.35709940E-02    3     1000022       -12        12   # BR(~chi_20 -> ~chi_10 nu_eb   nu_e)
#     7.35709940E-02    3     1000022       -14        14   # BR(~chi_20 -> ~chi_10 nu_mub  nu_mu)
#     7.35709940E-02    3     1000022       -16        16   # BR(~chi_20 -> ~chi_10 nu_taub nu_tau)
#     2.56612999E-02    3     1000024        -2         1   # BR(~chi_20 -> ~chi_1+ ub      d)
#     2.56612999E-02    3    -1000024        -1         2   # BR(~chi_20 -> ~chi_1- db      u)
#     1.50934149E-02    3     1000024        -4         3   # BR(~chi_20 -> ~chi_1+ cb      s)
#     1.50934149E-02    3    -1000024        -3         4   # BR(~chi_20 -> ~chi_1- sb      c)
#     8.55376664E-03    3     1000024       -12        11   # BR(~chi_20 -> ~chi_1+ nu_eb   e-)
#     8.55376664E-03    3    -1000024        12       -11   # BR(~chi_20 -> ~chi_1- nu_e    e+)
#     8.52752574E-03    3     1000024       -14        13   # BR(~chi_20 -> ~chi_1+ nu_mub  mu-)
#     8.52752574E-03    3    -1000024        14       -13   # BR(~chi_20 -> ~chi_1- nu_mu   mu+)
#     3.69450011E-03    3     1000024       -16        15   # BR(~chi_20 -> ~chi_1+ nu_taub tau-)
#     3.69450011E-03    3    -1000024        16       -15   # BR(~chi_20 -> ~chi_1- nu_tau  tau+)
#         PDG            Width
DECAY   1000025     2.55126802E+00   # neutralino3 decays
#          BR         NDA      ID1       ID2
     6.48323471E-02    2     1000022        23   # BR(~chi_30 -> ~chi_10   Z )
     1.74976412E-01    2     1000023        23   # BR(~chi_30 -> ~chi_20   Z )
     2.62498955E-01    2     1000024       -24   # BR(~chi_30 -> ~chi_1+   W-)
     2.62498955E-01    2    -1000024        24   # BR(~chi_30 -> ~chi_1-   W+)
     1.66674715E-01    2     1000022        25   # BR(~chi_30 -> ~chi_10   h )
     6.85186155E-02    2     1000023        25   # BR(~chi_30 -> ~chi_20   h )
#
#         PDG            Width
DECAY   1000035     8.58851480E+00   # neutralino4 decays
#          BR         NDA      ID1       ID2
     7.37369446E-02    2     1000022        23   # BR(~chi_40 -> ~chi_10   Z )
     1.86817948E-01    2     1000023        23   # BR(~chi_40 -> ~chi_20   Z )
     1.02541532E-05    2     1000025        23   # BR(~chi_40 -> ~chi_30   Z )
     2.39849967E-01    2     1000024       -24   # BR(~chi_40 -> ~chi_1+   W-)
     2.39849967E-01    2    -1000024        24   # BR(~chi_40 -> ~chi_1-   W+)
     1.80084518E-01    2     1000022        25   # BR(~chi_40 -> ~chi_10   h )
     7.96504008E-02    2     1000023        25   # BR(~chi_40 -> ~chi_20   h )
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
DECAY        36     1.51454458E+03   # A decays
#          BR         NDA      ID1       ID2
     4.51087144E-02    2           5        -5   # BR(A -> b       bb     )
     1.15950690E-02    2         -15        15   # BR(A -> tau+    tau-   )
     4.09880800E-05    2         -13        13   # BR(A -> mu+     mu-    )
     3.40677248E-05    2           3        -3   # BR(A -> s       sb     )
     2.14759492E-07    2           4        -4   # BR(A -> c       cb     )
     2.14243129E-02    2           6        -6   # BR(A -> t       tb     )
     1.99718052E-07    2          21        21   # BR(A -> g       g      )
     7.82455791E-10    2          22        22   # BR(A -> gam     gam    )
     5.72111171E-10    2          23        22   # BR(A -> Z       gam    )
     7.43964810E-09    2          23        25   # BR(A -> Z       h      )
     5.45491635E-03    2     1000024  -1000024   # BR(A -> ~chi_1+ ~chi_1-)
     5.39543502E-04    2     1000037  -1000037   # BR(A -> ~chi_2+ ~chi_2-)
     2.77777943E-01    2     1000024  -1000037   # BR(A -> ~chi_1+ ~chi_2-)
     2.77777943E-01    2     1000037  -1000024   # BR(A -> ~chi_2+ ~chi_1-)
     2.19168931E-03    2     1000022   1000022   # BR(A -> ~chi_10 ~chi_10)
     5.87377851E-04    2     1000023   1000023   # BR(A -> ~chi_20 ~chi_20)
     3.33980675E-05    2     1000025   1000025   # BR(A -> ~chi_30 ~chi_30)
     2.82166824E-04    2     1000035   1000035   # BR(A -> ~chi_40 ~chi_40)
     1.57794063E-05    2     1000022   1000023   # BR(A -> ~chi_10 ~chi_20)
     4.45535454E-02    2     1000022   1000025   # BR(A -> ~chi_10 ~chi_30)
     1.76200359E-01    2     1000022   1000035   # BR(A -> ~chi_10 ~chi_40)
     2.75498309E-02    2     1000023   1000025   # BR(A -> ~chi_20 ~chi_30)
     1.08633189E-01    2     1000023   1000035   # BR(A -> ~chi_20 ~chi_40)
     1.98743743E-04    2     1000025   1000035   # BR(A -> ~chi_30 ~chi_40)
#
#         PDG            Width
DECAY        37     1.51318613E+03   # H+ decays
#          BR         NDA      ID1       ID2
     7.09996554E-05    2           4        -5   # BR(H+ -> c       bb     )
     1.16054690E-02    2         -15        16   # BR(H+ -> tau+    nu_tau )
     4.10248433E-05    2         -13        14   # BR(H+ -> mu+     nu_mu  )
     4.54395848E-07    2           2        -5   # BR(H+ -> u       bb     )
     1.64293034E-06    2           2        -3   # BR(H+ -> u       sb     )
     3.39810938E-05    2           4        -3   # BR(H+ -> c       sb     )
     6.56241058E-02    2           6        -5   # BR(H+ -> t       bb     )
     7.44631295E-09    2          24        25   # BR(H+ -> W+      h      )
     7.86789580E-05    2     1000024   1000022   # BR(H+ -> ~chi_1+ ~chi_10)
     5.89489977E-04    2     1000024   1000023   # BR(H+ -> ~chi_1+ ~chi_20)
     8.64624288E-02    2     1000024   1000025   # BR(H+ -> ~chi_1+ ~chi_30)
     2.73546851E-01    2     1000024   1000035   # BR(H+ -> ~chi_1+ ~chi_40)
     2.88797306E-01    2     1000037   1000022   # BR(H+ -> ~chi_2+ ~chi_10)
     2.72911518E-01    2     1000037   1000023   # BR(H+ -> ~chi_2+ ~chi_20)
     2.35954678E-04    2     1000037   1000025   # BR(H+ -> ~chi_2+ ~chi_30)
     8.72833851E-08    2     1000037   1000035   # BR(H+ -> ~chi_2+ ~chi_40)
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
