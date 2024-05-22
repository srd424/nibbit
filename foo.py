#! /usr/bin/env python3

import os

REPO_DIR="/home/steved/src/aux/torrent"
NIX_EXPR="/home/steved/src/aux/full"
ATTR_PATH="stdenv"
NIX_CMD="nix --extra-experimental-features nix-command"

os.system("git -C "+REPO_DIR+" pull")

top_drv=os.popen(NIX_CMD + " derivation show -f " + NIX_EXPR + " " + ATTR_PATH + \
	"| jq -r '.|keys[0]'").read().rstrip()
print(top_drv)
#	"| jq -r 'first(.[]).outputs.out.path'").read()

os.system(NIX_CMD + " derivation show -r -f " + NIX_EXPR + " " + ATTR_PATH + \
	"| jq '.\""+top_drv+"\"'")
#close_drv=os.popen(NIX_CMD + " derivation show -f " + NIX_EXPR + " " + ATTR_PATH + \
#	" | 

#print(store_path)

# nix --extra-experimental-features nix-command derivation show -r -f full/ stdenv
