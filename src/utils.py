# -*-coding: utf-8 -*-

import subprocess
import os



def command_out(cmd):
    res = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = res.communicate()
    if isinstance(out, bytes):
        out = out.decode(errors='ignore')
    if isinstance(err, bytes):
        err = err.decode(errors='ignore')

    return out, err


def directory_tree(path):
    tree = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        tree['type'] = "directory"
        tree['children'] = [directory_tree(os.path.join(path,x)) for x in os.listdir(path)]
    else:
        tree['type'] = "file"
    return tree