#include "LeptonCollectionMap.h"
#include <iostream>

ClassImp(LeptonCollection);
ClassImp(LeptonCollectionArrayHasher);
ClassImp(LeptonCollectionMap);
ClassImp(LeptonCollectionFilesMap);

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
         int i = 0;
         int size = lh->getSize();
         for (auto& it: lh->leptonCollectionMap) {
            ++i;
            //if (leptonCollectionMap.find(it.first) != leptonCollectionMap.end())
            //    std::cout << "Already had runNum=" << it.first[0] << " lumiBlockNum=" << it.first[1] << " evtNum=" << it.first[2] << "\n";
            //else
            //    std::cout << "Size=" << getSize() << " Inserting runNum=" << it.first[0] << " lumiBlockNum=" << it.first[1] << " evtNum=" << it.first[2] << "\n";
            if (i % 100000 == 0)
                std::cout << i << " out of Size=" << size << "\n";
            insert(it.first[0], it.first[1], it.first[2], it.second);
         }
      }
    }
    return (Long64_t)leptonCollectionMap.size(); 
}

int LeptonCollectionMap::getSize() const {
    return leptonCollectionMap.size(); 
}

Long64_t  LeptonCollectionMap::Merge(const LeptonCollectionMap& leptonCollectionMapM) {
    for (auto& it: leptonCollectionMapM.leptonCollectionMap) {
        insert(it.first[0], it.first[1], it.first[2], it.second);
    }
    return (Long64_t)leptonCollectionMap.size(); 
}


//-------------------------- LeptonCollectionFilesMap -------------------------

bool LeptonCollectionFilesMap::contains(long runNum, long lumiBlockNum, long evtNum) {
    std::array<long, 3> key = {runNum, lumiBlockNum, evtNum};
    return leptonCollectionFilesMap.find(key) != leptonCollectionFilesMap.end();
}

void LeptonCollectionFilesMap::insert(long runNum, long lumiBlockNum, long evtNum, const std::string& file, bool checkExists) {
    std::array<long, 3> key = {runNum, lumiBlockNum, evtNum};
    
    if (checkExists) {
        auto found = leptonCollectionFilesMap.find(key);
        if (found != leptonCollectionFilesMap.end())
            std::cout << "Already had runNum=" << runNum << " lumiBlockNum=" << lumiBlockNum << " evtNum=" << evtNum;
    }
    
    leptonCollectionFilesMap[key] = file;
}
const std::string& LeptonCollectionFilesMap::get(long runNum, long lumiBlockNum, long evtNum) {
    std::array<long, 3> key = {runNum, lumiBlockNum, evtNum};
    return leptonCollectionFilesMap[key];
}

Long64_t LeptonCollectionFilesMap::Merge(TCollection *leptonCollectionList) {
    if (leptonCollectionList) {
      LeptonCollectionFilesMap *lh = 0;
      TIter nlh(leptonCollectionList);
      while ((lh = (LeptonCollectionFilesMap *) nlh())) {
         //std::cout << "My size=" << getSize() << " Going to merge " << lh->leptonCollectionMap.size() << "\n";
         //int i = 0;
         //int size = lh->getSize();
         for (auto& it: lh->leptonCollectionFilesMap) {
            //++i;
            //if (leptonCollectionMap.find(it.first) != leptonCollectionMap.end())
            //    std::cout << "Already had runNum=" << it.first[0] << " lumiBlockNum=" << it.first[1] << " evtNum=" << it.first[2] << "\n";
            //else
            //    std::cout << "Size=" << getSize() << " Inserting runNum=" << it.first[0] << " lumiBlockNum=" << it.first[1] << " evtNum=" << it.first[2] << "\n";
            //if (i % 100000 == 0)
            //    std::cout << i << " out of Size=" << size << "\n";
            insert(it.first[0], it.first[1], it.first[2], it.second);
         }
      }
    }
    return (Long64_t)leptonCollectionFilesMap.size(); 
}

int LeptonCollectionFilesMap::getSize() const {
    return leptonCollectionFilesMap.size(); 
}

Long64_t  LeptonCollectionFilesMap::Merge(const LeptonCollectionFilesMap& leptonCollectionFilesMapM) {
    for (auto& it: leptonCollectionFilesMapM.leptonCollectionFilesMap) {
        insert(it.first[0], it.first[1], it.first[2], it.second);
    }
    return (Long64_t)leptonCollectionFilesMap.size();
}