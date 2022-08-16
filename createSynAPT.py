import sys
import os.path
import argparse
import math
import json
import csv
import random
import shutil
from tqdm import tqdm
from operator import itemgetter



def main():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    with open('synAPT_total.txt') as f:
        total_labels = f.readlines() 

    os.mkdir('SynAPT_videos')

    path, eldersim_dirs, eldersim_files = next(os.walk('eldersim'))
    path, phav_classes, _ = next(os.walk('phav'))
    path, surreact_dirs, surreact_files = next(os.walk('surreact'))

    phav_dirs = []
    phav_files = []
    for phav_class in phav_classes:
        path, _phav_dirs, _phav_files = next(os.walk('phav/'+phav_class))
        if '.DS_Store' in _phav_files:
            _phav_files.remove('.DS_Store')
        for i in range(len(_phav_dirs)):
            _phav_dirs[i] = phav_class + '/'+ _phav_dirs[i]
        for i in range(len(_phav_files)):
            _phav_files[i] = phav_class + '/' + _phav_files[i]

        phav_dirs += _phav_dirs
        phav_files += _phav_files


    created_classes=[]
    for instance in total_labels:
        instance = instance.strip()
        instance_split = instance.split('/')
        class_name, video_name = instance_split[0], instance_split[1]
        if '.avi' == video_name[-4:] or '.mp4' == video_name[-4:]:
            video_name = video_name[:-4]
        if 'PRE_' in video_name:
            video_name = video_name[4:]

        if class_name not in created_classes:
            created_classes.append(class_name)
            os.mkdir('SynAPT_videos/'+class_name)


        not_found= True
        for _dir in eldersim_dirs:
            if video_name in _dir:
                os.system('cp -r eldersim/'+_dir +' SynAPT_videos/'+class_name)
                break
        if not_found:
            for _file in eldersim_files:
                if video_name in _file:
                    os.system('cp -r eldersim/'+_file +' SynAPT_videos/'+class_name)
                    not_found = False
                    break
        if not_found:
            for _dir in phav_dirs:
                if video_name in _dir:
                    os.system('cp -r phav/'+_dir +' SynAPT_videos/'+class_name)
                    not_found = False
                    break
        if not_found:
             for _file in phav_files:
                if video_name in _file:
                    os.system('cp -r phav/'+_file +' SynAPT_videos/'+class_name)
                    not_found = False
                    break
        if not_found:
            for _dir in surreact_dirs:
                if video_name in _dir:
                    os.system('cp -r surreact/'+_dir +' SynAPT_videos/'+class_name)
                    not_found = False
                    break
        if not_found:
             for _file in surreact_files:
                if video_name in _file:
                    os.system('cp -r surreact/'+_file +' SynAPT_videos/'+class_name)
                    not_found = False
                    break





if __name__ == '__main__':
    main()
