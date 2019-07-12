#include "TClass.h"
#include "TObject.h"
#include <vector>
#include <unordered_map>
#include <set>
#include "TCollection.h" 

class LumiSectMap : public TObject {
public:
    LumiSectMap() {};
    void insert(int runNum, int lumiSection);
    std::unordered_map<int, std::set<int>> getMap();
    virtual Long64_t  Merge(TCollection *lumiList);
    ClassDef(LumiSectMap,1);
protected:
    std::unordered_map<int, std::set<int>> lumiSectMap;
};
