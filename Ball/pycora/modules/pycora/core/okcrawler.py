#!/usr/bin/env python

#
# WARNING:: this file .is not. ready yet ..
#

# This is my :local: content imports. My ::stuff: here, so :it::went::to::the::top.:
##$#from puley import Labeled, Node, Eye

## Labeled .is. labeling Class
## Node .is. Node [[; Web-Node;; Tree;; Dom ]];
## Eye() .is. Eye().of.things.something

# These are all the Pythonic imports I need
import os, sys, re
import requests
import sqlalchemy
import BeautifulSoup
#from yaml import *

# Haha! We .forgot: about _that_ guy.
import threading

#######################################################
# Public Interface::
#  All functions: here::
#   must :accept::
#       *) ONE ARGUMENT and
#       *) A keyword dictionary
# These are PUBLIC interface so they should be left
#   DE-COUPLED as much as possible
#  ONE FUNCTION, ONE UNIT, ONE TRANSLATION
#  This .is. single-threaded for now.
#
######################################################
######################################################
#
# Sheme for Three-Group Pool-Threaded
#  Software
#
# Three-thread:groups!!
# Thread-group:: One    ::Pool1 !and Pool2 ::
#   This thread-group DOWNLOADS and PASSES info to the other groups
#
# Thread-group: Two     ::Pool1 ::
#   This one parses _ONLY_
#
# Thread-group Three:   ::Pool1 ::
#   This one aggrees and DUMPS info
#
##############################################################
##############################################################

#
# Utility function
#
def echo(something, **context):
    print "echo! -> [something] -> {context} -> **&STDOUT"

#
# Walks about a path (directory)
#   Returns: Filtered Content
#    Pass filters through constraints:: 'match_filters' => ? and 'miss_filters'
#  Openbsd "Style" LOL
#
def walk_path(path, **constraints):
    print "walkabout! -> matching! -> [filtered file-info]"
    filtered = []

    match_filters = []
    miss_filters = []

    match_filters= constraints['match_filters']
    miss_filters = constraints['miss_filters']

    # pattern = re.compile(r'.*\.png')
    walked = os.walk(path)
    constraints.update('>os.walk\'ed::{path}'.format(path=path), "Tru-th|True")
    

    #for _S_re-member__((dirpath:0, dirnames:1, filenames:2}}s in os.walk(path):
    for x in walked:
        filtered.append(x[0] + "/" + x[1] + "/" + x[2])

    # filtered # [ lambda x: x not in miss_filters for x in iter(filtered) ]
    # filtered = constraints['match_filters'] # easy patch

    return filtered

#
# Reads out a file and RETURNS FILE content OBJECT
#   LOL that is simply the file in [lines]
#   PASS all needed info in the constraints, please
#
def readout_file(name, **constraints):
    print "readout_file! -> {constraints} -> [File contents ]"
    lines = []
    with open(name) as f:
        for line in f:
            lines.append(line)
    return lines

#
#  Takes what's left of {readout_file} and {DUMPS} it on the disk.. erhmmm.. solidst... erhm...
#   harddrive erhm.... whatever.. "LOCAL" PERSISTENCY "PROVIDER"...
#  LOCAL means LOCALLY ENTWINED, "CONSIDERATIONS"
#
def dump_file(contents, **context):
    print "dump_file! -> filesystem!?"
    local_path = context['dumpfile_location']
    local_filename = context['filename']
    with open(local_filename, 'wb') as f:
        f.write(contents)
        f.flush()

#
# Give me an URL and I Giv you RESPONSE object... LOL REQ/RESP.
# Also, in postguide we update it
#
def download_file(url, **postguide):
    print "download_file! -> response!? -> [postguide] >:D"
    local_filename = url.split('/')[-1]
    postguide.update(filename = local_filename)

    r = requests.get(url) #, stream=True)
    return r

#
# This parses contents..
#
def parse_out(contents, **context):
    print "parse_out! Parsing!?"
    soup = BeautifulSoup(contents)
    targets=soup.findAll('a') #,{'class':'institution'})

    links = []
    for each_target in targets:
        print each_target['href']+","+each_target.string
    return links

#
# Upon PARSE-age EVENT, this gathers the links...
#
def gather_links(links, **context):
    print "gather_links! gather_links"
    pass
 
#    
# Upon :startup: read_out >> config_cat
#
def config_cat(config={}, **context):
    readout_file(
#
# Ha. Ha. MAin functionality... for now this is a SINGLE module, NO PACKAGING. LOL.
#
if __name__ == "__main__":

    constraints =  {'listage': True,
                    'simple': True,
                    'dumpfile_location': 'okcrawler.d/dumpf/',
                    'match_filters': ['something.to.crawl'],
                    'miss_filters': None
                    }

    downloaded = []
    filenames = walk_path(os.curdir, **constraints )
    print "filenames>>", filenames

    for filename in filenames:
        lines = readout_file(filename, **constraints)

        print "bytes>>", lines

        for line in lines:
            response = download_file(line, **constraints)
            links = parse_out(response, **constraints)

    processed = []
    links = [] # `Finally!
    for uri in iter(processed):
        contents = download_file(uri, **constraints)
        links.append(parse_out(contents))
    gather_links(links)

#
# A much needed Borg, this DOES something LOCALLY...
# RAdical DEsign, RAdiCAL iDEAS
#
def os_mkdir_p(directory, *arguments , **options):
    pass

# The Borg in question. Needed for further Expanding of this Story (okcrawling@okcrawler)
# This Borg should work like this... Each state is NOTED and before calling the 'os_*' functions
# It should::
#  1) LOCK all OS resources for everyone in THIS process SPACe
#  2) wait for them processors to stop porcessing
#  3) Do it's dirty bizz, and you know..
#  4|*) Release all locking, and unlock the ADRESS SPACE for '*'
#  yeah it's a HARSH little BORG that needs LOCKS for that on EACH instantation instance
#    e.g when a Borg exemplar is being chosen by the m = Mk(locks = {'locks'...})
#     This file needs to be seen by a Hacker or a seasoned Professional (such as me ;)) OLOL!
class Mk(object):
    __state_funcs = {
        'os_mkdir_p': None,
        'os_touch': None,
        'os_write_out': None,
        'os_read_in': None,
    }
    def __init__(self, first, *arguments, **context):
        # WE certainly DON'T need no stinkin' Sniggletton!!
        self.__dict__ = Mk.__state_funcs
