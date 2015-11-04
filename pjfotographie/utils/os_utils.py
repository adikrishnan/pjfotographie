'''
OS Utilities file.
'''
import os


def fetch_all_files(rel_path):
    '''
    Get all files in a directory.

    :arg string rel_path: relative path of directory.

    :arg list: files in a directory.
    '''
    file_path = os.path.abspath(__file__)
    dir_path = os.path.sep.join(file_path.split(os.path.sep)[:-2])
    final_path = '%s%s' % (dir_path, rel_path)
    return os.listdir(final_path)
