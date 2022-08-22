// Do NOT change. Changes will be lost next time file is generated

#define R__DICTIONARY_FILENAME LumiSectMapDict
#define R__NO_DEPRECATION

/*******************************************************************/
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#define G__DICTIONARY
#include "RConfig.h"
#include "TClass.h"
#include "TDictAttributeMap.h"
#include "TInterpreter.h"
#include "TROOT.h"
#include "TBuffer.h"
#include "TMemberInspector.h"
#include "TInterpreter.h"
#include "TVirtualMutex.h"
#include "TError.h"

#ifndef G__ROOT
#define G__ROOT
#endif

#include "RtypesImp.h"
#include "TIsAProxy.h"
#include "TFileMergeInfo.h"
#include <algorithm>
#include "TCollectionProxyInfo.h"
/*******************************************************************/

#include "TDataMember.h"

// The generated code does not explicitly qualifies STL entities
namespace std {} using namespace std;

// Header files passed as explicit arguments
#include "LumiSectMap.h"

// Header files passed via #pragma extra_include

namespace ROOT {
   static void *new_LumiSectMap(void *p = 0);
   static void *newArray_LumiSectMap(Long_t size, void *p);
   static void delete_LumiSectMap(void *p);
   static void deleteArray_LumiSectMap(void *p);
   static void destruct_LumiSectMap(void *p);
   static void streamer_LumiSectMap(TBuffer &buf, void *obj);
   static Long64_t merge_LumiSectMap(void *obj, TCollection *coll,TFileMergeInfo *info);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::LumiSectMap*)
   {
      ::LumiSectMap *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::LumiSectMap >(0);
      static ::ROOT::TGenericClassInfo 
         instance("LumiSectMap", ::LumiSectMap::Class_Version(), "LumiSectMap.h", 8,
                  typeid(::LumiSectMap), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::LumiSectMap::Dictionary, isa_proxy, 16,
                  sizeof(::LumiSectMap) );
      instance.SetNew(&new_LumiSectMap);
      instance.SetNewArray(&newArray_LumiSectMap);
      instance.SetDelete(&delete_LumiSectMap);
      instance.SetDeleteArray(&deleteArray_LumiSectMap);
      instance.SetDestructor(&destruct_LumiSectMap);
      instance.SetStreamerFunc(&streamer_LumiSectMap);
      instance.SetMerge(&merge_LumiSectMap);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::LumiSectMap*)
   {
      return GenerateInitInstanceLocal((::LumiSectMap*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::LumiSectMap*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

//______________________________________________________________________________
atomic_TClass_ptr LumiSectMap::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *LumiSectMap::Class_Name()
{
   return "LumiSectMap";
}

//______________________________________________________________________________
const char *LumiSectMap::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::LumiSectMap*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int LumiSectMap::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::LumiSectMap*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *LumiSectMap::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::LumiSectMap*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *LumiSectMap::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::LumiSectMap*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
void LumiSectMap::Streamer(TBuffer &R__b)
{
   // Stream an object of class LumiSectMap.

   UInt_t R__s, R__c;
   if (R__b.IsReading()) {
      Version_t R__v = R__b.ReadVersion(&R__s, &R__c); if (R__v) { }
      TObject::Streamer(R__b);
      {
         unordered_map<int,set<int> > &R__stl =  lumiSectMap;
         R__stl.clear();
         int R__i, R__n;
         R__b >> R__n;
         for (R__i = 0; R__i < R__n; R__i++) {
            int R__t;
            R__b >> R__t;
            typedef int Value_t;
            std::pair<Value_t const, class std::set<int, struct std::less<int>, class std::allocator<int> > > R__t3(R__t,R__t2);
            R__stl.insert(R__t3);
         }
      }
      R__b.CheckByteCount(R__s, R__c, LumiSectMap::IsA());
   } else {
      R__c = R__b.WriteVersion(LumiSectMap::IsA(), kTRUE);
      TObject::Streamer(R__b);
      {
         unordered_map<int,set<int> > &R__stl =  lumiSectMap;
         int R__n=int(R__stl.size());
         R__b << R__n;
         if(R__n) {
            unordered_map<int,set<int> >::iterator R__k;
            for (R__k = R__stl.begin(); R__k != R__stl.end(); ++R__k) {
            R__b << (*R__k);
            }
         }
      }
      R__b.SetByteCount(R__c, kTRUE);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_LumiSectMap(void *p) {
      return  p ? new(p) ::LumiSectMap : new ::LumiSectMap;
   }
   static void *newArray_LumiSectMap(Long_t nElements, void *p) {
      return p ? new(p) ::LumiSectMap[nElements] : new ::LumiSectMap[nElements];
   }
   // Wrapper around operator delete
   static void delete_LumiSectMap(void *p) {
      delete ((::LumiSectMap*)p);
   }
   static void deleteArray_LumiSectMap(void *p) {
      delete [] ((::LumiSectMap*)p);
   }
   static void destruct_LumiSectMap(void *p) {
      typedef ::LumiSectMap current_t;
      ((current_t*)p)->~current_t();
   }
   // Wrapper around a custom streamer member function.
   static void streamer_LumiSectMap(TBuffer &buf, void *obj) {
      ((::LumiSectMap*)obj)->::LumiSectMap::Streamer(buf);
   }
   // Wrapper around the merge function.
   static Long64_t  merge_LumiSectMap(void *obj,TCollection *coll,TFileMergeInfo *) {
      return ((::LumiSectMap*)obj)->Merge(coll);
   }
} // end of namespace ROOT for class ::LumiSectMap

namespace ROOT {
   static TClass *unordered_maplEintcOsetlEintgRsPgR_Dictionary();
   static void unordered_maplEintcOsetlEintgRsPgR_TClassManip(TClass*);
   static void *new_unordered_maplEintcOsetlEintgRsPgR(void *p = 0);
   static void *newArray_unordered_maplEintcOsetlEintgRsPgR(Long_t size, void *p);
   static void delete_unordered_maplEintcOsetlEintgRsPgR(void *p);
   static void deleteArray_unordered_maplEintcOsetlEintgRsPgR(void *p);
   static void destruct_unordered_maplEintcOsetlEintgRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const unordered_map<int,set<int> >*)
   {
      unordered_map<int,set<int> > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(unordered_map<int,set<int> >));
      static ::ROOT::TGenericClassInfo 
         instance("unordered_map<int,set<int> >", -2, "unordered_map", 102,
                  typeid(unordered_map<int,set<int> >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &unordered_maplEintcOsetlEintgRsPgR_Dictionary, isa_proxy, 0,
                  sizeof(unordered_map<int,set<int> >) );
      instance.SetNew(&new_unordered_maplEintcOsetlEintgRsPgR);
      instance.SetNewArray(&newArray_unordered_maplEintcOsetlEintgRsPgR);
      instance.SetDelete(&delete_unordered_maplEintcOsetlEintgRsPgR);
      instance.SetDeleteArray(&deleteArray_unordered_maplEintcOsetlEintgRsPgR);
      instance.SetDestructor(&destruct_unordered_maplEintcOsetlEintgRsPgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::MapInsert< unordered_map<int,set<int> > >()));

      ::ROOT::AddClassAlternate("unordered_map<int,set<int> >","std::unordered_map<int, std::set<int, std::less<int>, std::allocator<int> >, std::hash<int>, std::equal_to<int>, std::allocator<std::pair<int const, std::set<int, std::less<int>, std::allocator<int> > > > >");
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const unordered_map<int,set<int> >*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *unordered_maplEintcOsetlEintgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const unordered_map<int,set<int> >*)0x0)->GetClass();
      unordered_maplEintcOsetlEintgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void unordered_maplEintcOsetlEintgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_unordered_maplEintcOsetlEintgRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) unordered_map<int,set<int> > : new unordered_map<int,set<int> >;
   }
   static void *newArray_unordered_maplEintcOsetlEintgRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) unordered_map<int,set<int> >[nElements] : new unordered_map<int,set<int> >[nElements];
   }
   // Wrapper around operator delete
   static void delete_unordered_maplEintcOsetlEintgRsPgR(void *p) {
      delete ((unordered_map<int,set<int> >*)p);
   }
   static void deleteArray_unordered_maplEintcOsetlEintgRsPgR(void *p) {
      delete [] ((unordered_map<int,set<int> >*)p);
   }
   static void destruct_unordered_maplEintcOsetlEintgRsPgR(void *p) {
      typedef unordered_map<int,set<int> > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class unordered_map<int,set<int> >

namespace ROOT {
   static TClass *setlEintgR_Dictionary();
   static void setlEintgR_TClassManip(TClass*);
   static void *new_setlEintgR(void *p = 0);
   static void *newArray_setlEintgR(Long_t size, void *p);
   static void delete_setlEintgR(void *p);
   static void deleteArray_setlEintgR(void *p);
   static void destruct_setlEintgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const set<int>*)
   {
      set<int> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(set<int>));
      static ::ROOT::TGenericClassInfo 
         instance("set<int>", -2, "set", 94,
                  typeid(set<int>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &setlEintgR_Dictionary, isa_proxy, 0,
                  sizeof(set<int>) );
      instance.SetNew(&new_setlEintgR);
      instance.SetNewArray(&newArray_setlEintgR);
      instance.SetDelete(&delete_setlEintgR);
      instance.SetDeleteArray(&deleteArray_setlEintgR);
      instance.SetDestructor(&destruct_setlEintgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Insert< set<int> >()));

      ::ROOT::AddClassAlternate("set<int>","std::set<int, std::less<int>, std::allocator<int> >");
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const set<int>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *setlEintgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const set<int>*)0x0)->GetClass();
      setlEintgR_TClassManip(theClass);
   return theClass;
   }

   static void setlEintgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_setlEintgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) set<int> : new set<int>;
   }
   static void *newArray_setlEintgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) set<int>[nElements] : new set<int>[nElements];
   }
   // Wrapper around operator delete
   static void delete_setlEintgR(void *p) {
      delete ((set<int>*)p);
   }
   static void deleteArray_setlEintgR(void *p) {
      delete [] ((set<int>*)p);
   }
   static void destruct_setlEintgR(void *p) {
      typedef set<int> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class set<int>

namespace {
  void TriggerDictionaryInitialization_LumiSectMapDict_Impl() {
    static const char* headers[] = {
"LumiSectMap.h",
0
    };
    static const char* includePaths[] = {
"/cvmfs/cms.cern.ch/slc7_amd64_gcc900/lcg/root/6.22.08-ljfedo/include/",
"/afs/desy.de/user/n/nissanuv/CMSSW_11_3_1/src/cms-tools/lib/classes/",
0
    };
    static const char* fwdDeclCode = R"DICTFWDDCLS(
#line 1 "LumiSectMapDict dictionary forward declarations' payload"
#pragma clang diagnostic ignored "-Wkeyword-compat"
#pragma clang diagnostic ignored "-Wignored-attributes"
#pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
extern int __Cling_AutoLoading_Map;
class __attribute__((annotate("$clingAutoload$LumiSectMap.h")))  LumiSectMap;
)DICTFWDDCLS";
    static const char* payloadCode = R"DICTPAYLOAD(
#line 1 "LumiSectMapDict dictionary payload"


#define _BACKWARD_BACKWARD_WARNING_H
// Inline headers
#include "LumiSectMap.h"

#undef  _BACKWARD_BACKWARD_WARNING_H
)DICTPAYLOAD";
    static const char* classesHeaders[] = {
"LumiSectMap", payloadCode, "@",
nullptr
};
    static bool isInitialized = false;
    if (!isInitialized) {
      TROOT::RegisterModule("LumiSectMapDict",
        headers, includePaths, payloadCode, fwdDeclCode,
        TriggerDictionaryInitialization_LumiSectMapDict_Impl, {}, classesHeaders, /*hasCxxModule*/false);
      isInitialized = true;
    }
  }
  static struct DictInit {
    DictInit() {
      TriggerDictionaryInitialization_LumiSectMapDict_Impl();
    }
  } __TheDictionaryInitializer;
}
void TriggerDictionaryInitialization_LumiSectMapDict() {
  TriggerDictionaryInitialization_LumiSectMapDict_Impl();
}
