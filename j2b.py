#! /usr/bin/python3

import sys
import bencodepy
import json
import codecs

j=sys.stdin.buffer.read()
d=(json.loads(j))
bc=bencodepy.Bencode(
	encoding='utf-8',
	encoding_fallback='value'
	)
d['info']['pieces'] = codecs.decode(d['info']['pieces'].encode('utf-8'),'base64')
c=bc.encode(d)
sys.stdout.buffer.write(c)
