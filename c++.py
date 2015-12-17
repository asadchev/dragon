from dvc import *

dvc = DVC(
    
    "terminal-c++.dvc",

    List("include-list",
	 "memory",
	 "vector",
	 "list",
	 "set",
	 "map",
	 "algorithm",
	 "string",
	 "atomic",
	 "chrono"
	 "thread"
	 ),
	 
    Script("include <include-list>", '"#include <" + _arg1 + ">"'),

)

print dvc
