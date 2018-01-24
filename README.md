
ext_cloc
=======

The CLOC(Count Lines of Code) counts blank lines, comment lines, and physical lines of source code in many programming languages.
The ext_cloc(Extended CLOC) count a ratio of two direcotry by using cloc (ex, fixed and variant Directory)

How to use it
==================
The uftrace command has following.

	$ copy ext_cloc.py into your directory.
    $ ./ext_cloc.py  "find_string"

	It will find directories of including find_string. If you just write "Mgr" and then
	it will find all directories which MgrXXX, XXXMgr.

Output
============================================================================================================
Mgr Name Fixed File      Variant File    File Ratio      Fixed Line      Variant Line    Line Ratio
MgrAlert      2              21               9              30            4797               1
MgrDS         14              32              30            5649            7797              42
MgrDiag         19               6              76            1578            1272              55
MgrHWIO         10              52              16             314            3775               8
MgrLog         20               0             100            4065               0             100
MgrODI         68              45              60            2504            1360              65
MgrSnd         10              19              34             221            2056              10
MgrSys         16               1              94             894               2             100
MgrTelltale    2               8              20              26            2420               1
MgrTsk         16               0             100            2467               0             100
MgrUpg        130              49              73           16774           15822              51
MgrUsb         16               1              94             935               2             100
MgrVDS          1              15               6              24            2149               1
Total        324             249              56           35481           41452              46


