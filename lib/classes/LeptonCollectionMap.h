#include "TClass.h"
#include "TObject.h"
#include <vector>
#include <unordered_map>
#include "TCollection.h" 
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

class LeptonCollectionArrayHasher {
public:
    std::size_t operator()(const std::array<long, 3>& a) const {
        std::size_t h = 0;

        for (auto e : a) {
            h ^= std::hash<long>{}(e)  + 0x9e3779b9 + (h << 6) + (h >> 2); 
        }
        return h;
    }
    ClassDef(LeptonCollectionArrayHasher,1);
};

class LeptonCollectionMap : public TObject {
public:
    LeptonCollectionMap() {};
    void insert(long runNum, long lumiBlockNum, long evtNum, const LeptonCollection& leptonCollection, bool checkExists=false);
    bool contains(long runNum, long lumiBlockNum, long evtNum);
    const LeptonCollection& get(long runNum, long lumiBlockNum, long evtNum);
    virtual Long64_t  Merge(TCollection *leptonCollectionMap);
    virtual Long64_t  Merge(const LeptonCollectionMap& leptonCollectionMapM);
    ClassDef(LeptonCollectionMap,1);
    int getSize() const;
//protected:    
    std::unordered_map< array<long,3> , LeptonCollection, LeptonCollectionArrayHasher >  leptonCollectionMap;
};

class LeptonCollectionFilesMap : public TObject {
public:
    LeptonCollectionFilesMap() {};
    void insert(long runNum, long lumiBlockNum, long evtNum, const std::string& file, bool checkExists=false);
    bool contains(long runNum, long lumiBlockNum, long evtNum);
    const std::string& get(long runNum, long lumiBlockNum, long evtNum);
    virtual Long64_t  Merge(TCollection *leptonCollectionFilesMap);
    virtual Long64_t  Merge(const LeptonCollectionFilesMap& leptonCollectionFilesMapM);
    ClassDef(LeptonCollectionFilesMap,1);
    int getSize() const;
//protected:    
    std::unordered_map< array<long,3> , std::string, LeptonCollectionArrayHasher >  leptonCollectionFilesMap;
};
