#! /usr/bin/env python3
import os
import re

REPO_DIR="/home/steved/src/aux/torrent/map.git"
NIX_EXPR="/home/steved/src/aux/full"
ATTR_PATH="stdenv"
NIX_CMD="nix --extra-experimental-features nix-command"
DEBUG=False

#os.system("git -C "+REPO_DIR+" pull")

store_hash=re.split("[/-]",os.popen(NIX_CMD + " derivation show -f " + NIX_EXPR + " " + ATTR_PATH + \
	"| jq -r 'first(.[]).outputs.out.path'").read().rstrip())[3]

def dbg(s):
	if DEBUG:
		print(s)

def to_dir(hash):
	return hash[0] + "/" + hash

seen = {}

def proc_hash(hash):
	dbg("processing " + hash)
	if hash in seen:
		return
	seen[hash] = True
	print(REPO_DIR + "/" + to_dir(hash) + ".torrent")
	narinfo=REPO_DIR + "/" + to_dir(hash) + ".narinfo"
	dbg("reading" + narinfo)
	ref_list = dict(map(lambda l: str.split(l, ": "), open(narinfo).read().splitlines()))['References']
	if ref_list == "":
		return
	for ref in ref_list.split(" "):
		dbg("processing ref '"+ref+"'")
		ref_hash=ref.split("-")[0]
		if ref_hash != hash:
			proc_hash(ref_hash)

proc_hash(store_hash)
exit(0)

#       "| jq -r '.|keys[0]'").read().rstrip()

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
