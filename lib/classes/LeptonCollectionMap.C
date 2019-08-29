#include "LeptonCollectionMap.h"
#include <iostream>

ClassImp(LeptonCollection);
ClassImp(LeptonCollectionArrayHasher);
ClassImp(LeptonCollectionMap);

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
         //std::cout << "My size=" << getSize() << " Going to merge " << lh->leptonCollectionMap.size() << "\n";
         for (auto& it: lh->leptonCollectionMap) {
            if (leptonCollectionMap.find(it.first) != leptonCollectionMap.end())
                std::cout << "Already had runNum=" << it.first[0] << " lumiBlockNum=" << it.first[1] << " evtNum=" << it.first[2] << "\n";
            //else
            //    std::cout << "Size=" << getSize() << " Inserting runNum=" << it.first[0] << " lumiBlockNum=" << it.first[1] << " evtNum=" << it.first[2] << "\n";
            insert(it.first[0], it.first[1], it.first[2], it.second);
         }
      }
    }
    return (Long64_t)leptonCollectionMap.size(); 
}

int LeptonCollectionMap::getSize() const {
    return leptonCollectionMap.size(); 
}