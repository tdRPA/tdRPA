'''
统计代码行数工具
'''

# coding=utf-8
import os
import sys

#在指定目录下统计所有的py文件，以列表形式返回
def collect_files(dir):
    filelist = []
    for parent,dirnames,filenames in os.walk(dir):
         for filename in filenames:
             if filename.endswith('.py'):
                 #将文件名和目录名拼成绝对路径，添加到列表里
                 filelist.append(os.path.join(parent,filename))
    return filelist

#计算单个文件内的代码行数
def calc_linenum(file):
    with open(file,encoding='utf8') as fp:
        content_list = fp.readlines()
        code_num = 0  #当前文件代码行数计数变量
        blank_num = 0  #当前文件空行数计数变量
        annotate_num =0  #当前文件注释行数计数变量
        for content in content_list:
            content = content.strip()
            # 统计空行
            if content == '':
                blank_num += 1
            # 统计注释行
            elif content.startswith('#'):
                annotate_num += 1
            # 统计代码行
            else:
                code_num += 1
    # 返回代码行数，空行数，注释行数
    return code_num,blank_num,annotate_num

if __name__ == '__main__':
    #定义代码所在的目录
    base_path = sys.argv[1]

    files = collect_files(base_path)
    total_code_num = 0   #统计文件代码行数计数变量
    total_blank_num = 0   #统计文件空行数计数变量
    total_annotate_num = 0  #统计文件注释行数计数变量
    for f in files:
        code_num, blank_num, annotate_num = calc_linenum(f)
        total_code_num += code_num
        total_blank_num += blank_num
        total_annotate_num += annotate_num

    print( u'代码总行数为：  %s' % total_code_num  )
    print( u'空行总行数为：  %s' % total_blank_num)
    print( u'注释行总行数为： %s' % total_annotate_num)
