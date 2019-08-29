#include "LeptonCollectionMap.h"
#include <iostream>


bool LeptonCollectionMap::contains(long runNum, long lumiBlockNum, long evtNum) {
    std::array<long, 3> key = {runNum, lumiBlockNum, evtNum};
    return leptonCollectionMap.find(key) != leptonCollectionMap.end();
}

void LeptonCollectionMap::insert(long runNum, long lumiBlockNum, long evtNum, const LeptonCollection& leptonCollection, bool checkExists) {
    std::array<long, 3> key = {runNum, lumiBlockNum, evtNum};
    
    if (checkExists) {
        auto found = leptonCollectionMap.find(key);
        if (found != leptonCollectionMap.end())
            std::cout << "Already had runNum=" << runNum << " lumiBlockNum=" << lumiBlockNum << " evtNum=" << evtNum;
    }
    
    leptonCollectionMap[key] = leptonCollection;
}
const LeptonCollection& LeptonCollectionMap::get(long runNum, long lumiBlockNum, long evtNum) {
    std::array<long, 3> key = {runNum, lumiBlockNum, evtNum};
    return leptonCollectionMap[key];
}

Long64_t LeptonCollectionMap::Merge(TCollection *leptonCollectionList) {
    if (leptonCollectionList) {
      LeptonCollectionMap *lh = 0;
      TIter nlh(leptonCollectionList);
      while ((lh = (LeptonCollectionMap *) nlh())) {
         for (auto& it: lh->leptonCollectionMap) {
            insert(it.first[0], it.first[1], it.first[1], it.second);
         }
      }
    }
    return (Long64_t)leptonCollectionMap.size(); 
}

#if defined(__ROOTCLING__)
#pragma link C++ class LeptonCollection;
#endif