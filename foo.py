#! /usr/bin/env python3

import os
import json

REPO_DIR="/home/steved/src/aux/torrent/map.git"
NIX_EXPR="/home/steved/src/aux/full"
ATTR_PATH="stdenv"
NIX_CMD="nix --extra-experimental-features nix-command"

#os.system("git -C "+REPO_DIR+" pull")

top_drv_name=os.popen(NIX_CMD + " derivation show -f " + NIX_EXPR + " " + ATTR_PATH + \
       "| jq -r '.|keys[0]'").read().rstrip()

j=os.popen(NIX_CMD + " derivation show -r -f " + \
	NIX_EXPR + " " + ATTR_PATH).read()
#print(j)
#exit(0)

close_drv=json.loads(j)

def proc_drv(drv):
#	print(drv['inputDrvs'])
	for idrv, outs in drv['inputDrvs'].items():
		for out in outs:
			print(idrv+" - "+out)
#		print(repr(id))
#		for out in id:
#			print(out)

proc_drv(close_drv[top_drv_name])



#print(deriv)
#
#print(top_drv)
##	"| jq -r 'first(.[]).outputs.out.path'").read()
#
#os.system(NIX_CMD + " derivation show -r -f " + NIX_EXPR + " " + ATTR_PATH + \
#	"| jq '.\""+top_drv+"\"'")
##close_drv=os.popen(NIX_CMD + " derivation show -f " + NIX_EXPR + " " + ATTR_PATH + \
##	" | 
#
##print(store_path)
#
## nix --extra-experimental-features nix-command derivation show -r -f full/ stdenv
