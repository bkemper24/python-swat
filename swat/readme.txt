For Python 3.12 Windows only:  

When building the swat C extensions, the pyport.h file was modified as follows:  
Change the #define for ALWAYS_INLINE 
from : #elif defined(__GNUC__) || defined(__clang__) || defined(__INTEL_COMPILER)
to   : #elif defined(__GNUC__) || defined(__clang__) || defined(__INTEL_LLVM_COMPILER) || (defined(__INTEL_COMPILER) && !defined(_WIN32))

This change was made to circumvent a compiler error that occurred when using the Intel compiler on windows.