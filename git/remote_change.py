#!/usr/bin/env python3

import os
import sys

args = sys.argv

oldRepoName = args[1] if len(args) > 1 else None
newRepoName = args[2] if len(args) > 2 else None

remoteName = args[3] if len(args) > 3 else 'origin'

if oldRepoName is None or newRepoName is None :
    print('Old and New Repo names are required')
    raise SystemExit

if oldRepoName == newRepoName:
    print('Old and New Repo should be unique')
    raise SystemExit

remoteUrl = os.popen('git remote get-url ' + remoteName, 'r')
remoteUrl = remoteUrl.readline().replace('\n', '')

os.system('git remote set-url ' + remoteName + ' ' + remoteUrl.replace(oldRepoName, newRepoName))
