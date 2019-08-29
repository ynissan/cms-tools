#include "TClass.h"
#include "TObject.h"
#include <vector>
#include "TLorentzVector.h"

class LeptonCollection : public TObject {
public:
    LeptonCollection() {};

    vector<TLorentzVector> Electrons;
    vector<int> Electrons_charge;
    vector<double> Electrons_EnergyCorr;
    vector<bool> Electrons_mediumID;
    vector<double> Electrons_MiniIso;
    vector<double> Electrons_MT2Activity;
    vector<double> Electrons_MTW;
    vector<bool> Electrons_passIso;
    vector<bool> Electrons_tightID;
    vector<double> Electrons_TrkEnergyCorr;
    vector<TLorentzVector> Muons;
    vector<int> Muons_charge;
    vector<bool> Muons_mediumID;
    vector<double> Muons_MiniIso;
    vector<double> Muons_MT2Activity;
    vector<double> Muons_MTW;
    vector<bool> Muons_passIso;
    vector<bool> Muons_tightID;
    
    ClassDef(LeptonCollection,1);
};

#if defined(__ROOTCLING__)
#pragma link C++ class LeptonCollection+;
#pragma link C++ class LeptonCollectionMap+;
#pragma link C++ nestedclasses;
#endif
