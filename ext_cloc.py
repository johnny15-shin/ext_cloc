#!/usr/bin/env python
# =*- coding: UTF-8 -*-

# get argument list using sys module
import sys



def usage():
    print "We should hava a directory path."
    print "./ext_cloc direcotry_path"
    print "example) ./ext_cloc ~/workspace/c300_cheetha/Apps/Src"
    exit()

print "######################################################"
print "##############  Welcome to Python World  #############"
print "######################################################"

#
#git 주소를 받아 소스를 받아 온다 (Option)
# -- folder 지정으로.
#지정된 폴더를 찾아 cloc를 수행한다. (csv 파일로 떨굼)
# -- 실행 위치에 output폴더를 생성하고, 그곳에 manager_date.csv 파일로 남긴다.
#csv파일을 파싱한다.
#파일수로 공용부/변동부를 계산한다.
#라인수로 공용부/변동부를 계산한다.
#출력한다.


# check argument
# Get the total number of args passed to this
total = len(sys.argv)
if total < 2:
    usage()

# check path
print ("Directory Path : %s" % str(sys.argv[1]))




