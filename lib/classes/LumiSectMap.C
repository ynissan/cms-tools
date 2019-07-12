#include "LumiSectMap.h"
#include <iostream>

void LumiSectMap::insert(int runNum, int lumiSection) {
    lumiSectMap[runNum].insert(lumiSection);
}

std::unordered_map<int, std::set<int>> LumiSectMap::getMap() {
    return lumiSectMap;
}

Long64_t LumiSectMap::Merge(TCollection *lumiList) {
    if (lumiList) {
      LumiSectMap *lh = 0;
      TIter nlh(lumiList);
      while ((lh = (LumiSectMap *) nlh())) {
         for (auto& it: lh->lumiSectMap) {
            for(const auto& v : it.second) {
                insert(it.first, v);
            }
         }
      }
    }
    return (Long64_t)lumiSectMap.size(); 
}