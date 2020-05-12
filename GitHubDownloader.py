#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
GitHub Folder Downloader
Created by Fransiscus Emmanuel Bunaren
https://bunaren.com
'''

import json
import requests
import urllib.request
import os
from pprint import pprint


class Downloader:

    def __init__(self, repository_url='', branch=''):
        if not repository_url:
            self.repo_url = ''
            self.files = []
            self.location = dict()
        else:
            self.load_repository(repository_url, branch)

    def load_repository(self, url, branch=''):

        # Check if URL contains branch name

        if '/tree/' in url and not branch:
            branch = url.split('/tree/')[1]
            branch = branch.split('/')[0]
        else:
            branch = 'master'

        # Convert URL to match GitHub API URI

        tmp_url = url.replace('https://github.com/',
                              'https://api.github.com/repos/')
        tmp_url += '/git/trees/{}?recursive=1'.format(branch)

        # Make GET Request

        api = requests.get(tmp_url).text
        files = json.loads(api)

        # Turn the API Data into List

        output = []
        location = dict()
        for (k, i) in enumerate(files['tree']):
            if i['type'] == 'blob':
                tmp = [i['path']]

                # Get RAW URL

                tmp += [i['url'].replace('https://api.github.com/repos/',
                                         'https://raw.githubusercontent.com/')]
                tmp[-1] = tmp[-1].split('/git/blobs/')[0]
                tmp[-1] = tmp[-1] + '/' + branch + '/' + tmp[0]
                output.append(tmp)
            else:
                location[i['path']] = k
        self.files = output
        self.location = location

        # Set Repo URL for memoization

        self.repo_url = url

    def mkdirs(self, path):

        # Make directory if not exist

        if not os.path.isdir(path):
            os.makedirs(path)

    def download(
        self,
        destination,
        target_folder='*',
        recursive=True,
    ):

        # Make directory if not exist

        if not os.path.isdir(destination):
            os.makedirs(destination)

        # Find Folder Position

        if target_folder == '*':
            start = 0
        else:

            # Remove Relative Path Symbol from string

            tmp_target = target_folder.replace('./', '')
            tmp_target = tmp_target.replace('../', '')

            # Remove "/"

            tmp_target = (tmp_target if tmp_target[-1] != '/'
                          else tmp_target[:-1])
            start = self.location[target_folder]

        # Start Downloading

        for i in self.files[start:]:
            if recursive or i[0].split(target_folder)[1].count('/') \
                    <= 1:
                self.mkdirs(destination + '/' + os.path.dirname(i[0]))
                urllib.request.urlretrieve(i[1], destination + '/' + i[0])
