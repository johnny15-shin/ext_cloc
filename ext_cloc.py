#!/usr/bin/env python
# =*- coding: UTF-8 -*-

DEBUGGING = True

# get argument list using sys module
import sys
import os

if DEBUGGING:
    print ("User Interest : %s" % str(sys.argv[1]))




#def usage():
#    print "We should hava a directory path."
#    print "./ext_cloc direcotry_path"
#    print "example) ./ext_cloc filename1 filename2"
#    exit()



# List contains the final result
RESULT_LIST = []

# Current Directory
CURRENT_DIR = os.getcwd()
# Output Directory for cloc output csv files
OUTPUT_DIR = 'CLOC_OUTPUT'

# Get list of Directory in CURRENT_DIR
file_list = os.listdir(CURRENT_DIR)
file_list.sort()

# Get Ready for making output files
if any(OUTPUT_DIR in s for s in file_list):
    print ("Remove Existing Files")
    os.system('rm -rf %s' % OUTPUT_DIR)
    os.system('mkdir %s' % OUTPUT_DIR)
else:
    os.system('mkdir %s' % OUTPUT_DIR)

os.system('rm output_data.txt')

# Making User Interest List
user_interest_list = []
for item in file_list:
    if item.find(str(sys.argv[1])) is not -1:
        user_interest_list.append(item)

if DEBUGGING:
    print user_interest_list

# Generate CSV output files
for item in user_interest_list:
    os.system('cloc ./%s --csv --out=./%s/%s_output.csv' % (item, OUTPUT_DIR, item))
    os.system('cloc ./CheetahVariants/%sVariant --csv --out=./%s/%sVariant_output.csv' % (item, OUTPUT_DIR, item))

# data processing
for mgr in user_interest_list:
    try:
        fixed_file_num = 0
        fixed_line_num = 0
        f_fixed = open(os.getcwd()+'/'+OUTPUT_DIR+'/'+mgr+'_output.csv')
        line = f_fixed.readline()
        while True:
            line = f_fixed.readline()
            if not line: break
            line = line[:-1]
            temp_list = line.split(',')
            if ((temp_list[1] == 'C++') or (temp_list[1] == 'C/C++ Header') or (temp_list[1] == 'C')):
                fixed_file_num += int(temp_list[0])
                fixed_line_num += int(temp_list[4])
        f_fixed.close()
    except IOError as e:
        pass

    try:
        variant_file_num = 0
        variant_line_num = 0
        f_variant = open(os.getcwd()+'/'+OUTPUT_DIR+'/'+mgr+'Variant_output.csv')
        line = f_variant.readline()
        while True:
            line = f_variant.readline()
            if not line: break
            line = line[:-1]
            temp_list = line.split(',')
            if ((temp_list[1] == 'C++') or (temp_list[1] == 'C/C++ Header') or (temp_list[1] == 'C')):
                variant_file_num += int(temp_list[0])
                variant_line_num += int(temp_list[4])
        f_variant.close()
    except IOError as e:
        pass

    file_ratio = int(round(float(fixed_file_num) / float(fixed_file_num + variant_file_num), 2)*100)
    line_ratio = int(round(float(fixed_line_num) / float(fixed_line_num + variant_line_num), 2)*100)

    data_list = [mgr, fixed_file_num, variant_file_num, file_ratio, fixed_line_num, variant_line_num, line_ratio]
    RESULT_LIST.append(data_list)

total_fixed_file = 0
total_fixed_line = 0
total_variant_file = 0
total_variant_line = 0
for s in RESULT_LIST:
    total_fixed_file += s[1]
    total_variant_file += s[2]
    total_fixed_line += s[4]
    total_variant_line += s[5]

total_file_ratio = int(round(float(total_fixed_file) / float(total_fixed_file + total_variant_file), 2)*100)
total_line_ratio = int(round(float(total_fixed_line) / float(total_fixed_line + total_variant_line), 2)*100)

RESULT_LIST.append(['Total', total_fixed_file, total_variant_file, total_file_ratio, total_fixed_line, total_variant_line, total_line_ratio])

print('============================================================================================================')
print('   Mgr Name\t    Fixed File\t   Variant File\t   File Ratio\t   Fixed Line\t Variant Line\t   Line Ratio')
for s in RESULT_LIST:
    print('%15s\t%10d\t%10d\t%10d\t%10d\t%10d\t%10d' % (s[0], s[1], s[2], s[3], s[4], s[5], s[6]))

f = open(os.getcwd()+'/output_data.txt', 'w')
f.write('============================================================================================================\n')
f.write('   Mgr Name\t    Fixed File\t   Variant File\t   File Ratio\t   Fixed Line\t Variant Line\t   Line Ratio\n')
for s in RESULT_LIST:
    f.write('%15s\t%10d\t%10d\t%10d\t%10d\t%10d\t%10d\n' % (s[0], s[1], s[2], s[3], s[4], s[5], s[6]))
f.close()

os.system('rm -rf %s' % OUTPUT_DIR)
