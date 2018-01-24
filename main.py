# -*- coding: utf-8 -*-

import os
import re

path_1 = './test/'
path_2 = 'D:/YoutubeVedio/Unreal/SideScrollGame/'
path_3 = 'D:/YoutubeVedio/Unreal/DetailBeginnerTutorials/'
path_4 = 'D:/YoutubeVedio/Unreal/Lets Create/'
path_5 = 'D:/YoutubeVedio/Unreal/FPS/'
def renamefile_srt(path):
    for dirpath, dirnames, filenames in os.walk(path):
        print(filenames)
        for item in filenames:
            regularParts = re.search(r'(\w*(?=#))(#)(\d*(?=\s))', item)
            a, b = item.split('.')
            print(a, "\n", b)
            if b == 'srt':
                if regularParts:
                    print(regularParts.group(3))
                    print(len(regularParts.group(3)))
                    if len(regularParts.group(3)) == 1:
                        add_num = '0' + str(regularParts.group(3))
                    else:
                        add_num = str(regularParts.group(3))
                    old_file_name = path + item
                    new_file_name = path + add_num + item
                    os.renames(old_file_name, new_file_name)
                else:
                    print(1)
                    old_file_name = path + item
                    new_file_name = path + '01' + item
                    os.renames(old_file_name, new_file_name)
            else:
                continue

def renamefile_mp4(path):
    for dirpath, dirnames, filenames in os.walk(path):
        print(filenames)
        for item in filenames:
            regularParts = re.search(r'(\w*(?=-))(-\s)(\d*(?=\s))', item)
            a, b = item.split('.')
            print(a, "\n", b)
            if b == 'mp4':
                if regularParts:
                    print(regularParts.group(3))
                    print(len(regularParts.group(3)))
                    if len(regularParts.group(3)) == 1:
                        add_num = '0' + str(regularParts.group(3))
                    else:
                        add_num = str(regularParts.group(3))
                    old_file_name = path + item
                    new_file_name = path + add_num + item
                    os.renames(old_file_name, new_file_name)
                else:
                    print(1)
                    old_file_name = path + item
                    new_file_name = path + '01' + item
                    os.renames(old_file_name, new_file_name)
            else:
                continue

def renamefile_srt_flexiable(path, pattern=r'(\w*(?=#))(#)(\d*(?=\s))'):
    for dirpath, dirnames, filenames in os.walk(path):
        print(filenames)
        for item in filenames:
            regularParts = re.search(pattern, item)
            a, b = item.split('.')
            print(a, "\n", b)
            if b == 'srt':
                if regularParts:
                    print(regularParts.group(3))
                    print(len(regularParts.group(3)))
                    if len(regularParts.group(3)) == 1:
                        add_num = '0' + str(regularParts.group(3))
                    else:
                        add_num = str(regularParts.group(3))
                    old_file_name = path + item
                    new_file_name = path + add_num + item
                    os.renames(old_file_name, new_file_name)
                else:
                    print(1)
                    old_file_name = path + item
                    new_file_name = path + '01' + item
                    os.renames(old_file_name, new_file_name)
            else:
                continue

def renamefile_mp4_flexiable(path, pattern=r'(\w*(?=-))(-\s)(\d*(?=\s))'):
    for dirpath, dirnames, filenames in os.walk(path):
        print(filenames)
        for item in filenames:
            regularParts = re.search(pattern, item)
            a, b = item.split('.')
            print(a, "\n", b)
            if b == 'mp4':
                if regularParts:
                    print(regularParts.group(3))
                    print(len(regularParts.group(3)))
                    if len(regularParts.group(3)) == 1:
                        add_num = '0' + str(regularParts.group(3))
                    else:
                        add_num = str(regularParts.group(3))
                    old_file_name = path + item
                    new_file_name = path + add_num + item
                    os.renames(old_file_name, new_file_name)
                else:
                    print(1)
                    old_file_name = path + item
                    new_file_name = path + '01' + item
                    os.renames(old_file_name, new_file_name)
            else:
                continue

def renamefile_recover(path):
    for dirpath, dirnames, filenames in os.walk(path):
        print(filenames)
        for item in filenames:
            regularParts = re.search(r'(\d*(?=\D))(.*)', item)
            if regularParts:
                degits = regularParts.group(1)
                origin_name = regularParts.group(2)
                old_file_name = path + item
                new_file_name = path + origin_name
                os.renames(old_file_name, new_file_name)

def process(type = 0, path = path_1):
    if type == 0:
        renamefile_srt(path)
        renamefile_mp4(path)
    elif type == 1:
        renamefile_recover(path)
    else:
        print("Error, Please input right type!")

def process_flexiable(type = 0, path = path_1, pattern_srt = r'(\w*(?=#))(#)(\d*(?=\s))', pattern_mp4 = r'(\w*(?=Blueprints\s))(Blueprints\s)(\d*(?=\s))'):
    if type == 0:
        renamefile_srt_flexiable(path, pattern_srt)
        renamefile_mp4_flexiable(path, pattern_mp4)
    elif type == 1:
        renamefile_recover(path)
    else:
        print("Error, Please input right type!")

def delete_something_in_names(path, pattern=r'(.*(?=英语\s\(自动生成\)))(英语\s\(自动生成\))(.*)'):
    for dirpath, dirnames, filenames in os.walk(path):
        print(filenames)
        for item in filenames:
            regularParts = re.search(pattern, item)
            a, b = item.split('.')
            print(a, "\n", b)
            if b == 'srt':
                if regularParts:
                    print(regularParts.group(3))
                    print(len(regularParts.group(3)))
                    if len(regularParts.group(3)) == 1:
                        add_num = '0' + str(regularParts.group(3))
                    else:
                        add_num = str(regularParts.group(3))
                    old_file_name = path + item
                    new_file_name = path + str(regularParts.group(1)) + str(regularParts.group(3))
                    os.renames(old_file_name, new_file_name)
                else:
                    pass
            else:
                continue

if __name__ == '__main__':

    # renamefile_srt(path_1)
    # renamefile_mp4(path_1)
    # renamefile_recover(path_1)
    # process(0, path_1)

    ##method #2
    # pattern_srt = r'(\w*(?=#))(#)(\d*(?=\s|\[))'
    # pattern_mp4 = r'(\w*(?=Blueprints\s))(Blueprints\s)(\d*(?=\s|\[))'
    # pattern_delete = r'(.*(?=英语\s\(自动生成\)))(英语\s\(自动生成\))(.*)'
    pattern_srt = r'(\w*(?=#))(#)(\d*(?=\D))'
    pattern_mp4 = r'(\w*(?=\-\s))(\-\s)(\d*(?=\D))'
    pattern_delete = r'(.*(?=英语\s\(自动生成\)))(英语\s\(自动生成\))(.*)'
    pattern_delete = r'(.*(?=英语\s\(自动生成\)))(英语\s\(自动生成\))(.*)'
    # process_flexiable(0, path_5, pattern_srt, pattern_mp4)
    delete_something_in_names(path_5, pattern_delete)
