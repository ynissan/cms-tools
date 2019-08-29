#include "TClass.h"
#include "TObject.h"
#include <vector>
#include <unordered_map>
#include "TCollection.h" 
#include "LeptonCollection.h"

struct ArrayHasher {
    std::size_t operator()(const std::array<long, 3>& a) const {
        std::size_t h = 0;

        for (auto e : a) {
            h ^= std::hash<long>{}(e)  + 0x9e3779b9 + (h << 6) + (h >> 2); 
        }
        return h;
    }   
};

class LeptonCollectionMap : public TObject {
public:
    LeptonCollectionMap() {};
    void insert(long runNum, long lumiBlockNum, long evtNum, const LeptonCollection& leptonCollection, bool checkExists=false);
    bool contains(long runNum, long lumiBlockNum, long evtNum);
    const LeptonCollection& get(long runNum, long lumiBlockNum, long evtNum);
    virtual Long64_t  Merge(TCollection *leptonCollectionMap);
    ClassDef(LeptonCollectionMap,1);
protected:    
    std::unordered_map< array<long,3> , LeptonCollection, ArrayHasher >  leptonCollectionMap;
};
