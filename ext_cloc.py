#!/usr/bin/env python
# =*- coding: UTF-8 -*-

# get argument list using sys module
import sys



def usage():
    print "We should hava a directory path."
    print "./ext_cloc direcotry_path"
    print "example) ./ext_cloc filename1 filename2"
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
if total < 3:
    usage()

# check path and gathering Directory list
# -f 고정부 파일 (고정부 Manager Direcotry List가 들어가 있음.)
# -v 변동부 파일 (변동부 Manager Directory List가 들어가 있음.)
print ("Directory Path : %s" % str(sys.argv[1]))
print ("Directory Path : %s" % str(sys.argv[2]))


fixed_list = []
variant_list = []
try:
    fixed_f = open(str(sys.argv[1]), 'r')
    variant_f = open(str(sys.argv[2]), 'r')
except IOError as e:
    print "file open error!"
    exit()

while True:
    line = fixed_f.readline()
    if not line: break;
    fixed_list.append(line[:-1])        # remove newline
#    print (line)

while True:
    line = variant_f.readline()
    if not line: break;
    variant_list.append(line[:-1])      # remove newline
#    print (line)

fixed_f.close()
variant_f.close()

print fixed_list
print variant_list








