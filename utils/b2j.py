#! /usr/bin/python3

import sys
import bencodepy
import json
import codecs

c=sys.stdin.buffer.read()
bc=bencodepy.Bencode(
	encoding='utf-8',
	encoding_fallback='value'
	)
d=bc.decode(c)
#print(json.dumps(d))
d['info']['pieces'] = codecs.encode(d['info']['pieces'],'base64').decode('utf-8')
#print(d)
print(json.dumps(d))
