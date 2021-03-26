import os
import shutil


def my_move_file(src_file, dst_file):
    if not os.path.isfile(src_file):
        print('%s not exist!' % src_file)
    else:
        path, name = os.path.split(dst_file)
        if not os.path.exists(path):
            os.makedirs(path)
        shutil.move(src_file, dst_file)
        print('move %s -> %s' % (src_file, dst_file))


def my_copy_file(src_file, dst_file):
    if not os.path.isfile(src_file):
        print('%s not exist!' % src_file)
    else:
        path, name = os.path.split(dst_file)
        if not os.path.exists(path):
            os.makedirs(path)
        shutil.copyfile(src_file, dst_file)
        print('copy %s -> %s' % (src_file, dst_file))


def my_delete_file(file):
    if os.path.exists(file):
        os.remove(file)
        print('delete %s' % file)


