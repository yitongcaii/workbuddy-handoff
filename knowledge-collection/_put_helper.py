# -*- coding: utf-8 -*-
import sys, urllib.request, os

def put(url, path):
    data = open(path, 'rb').read()
    req = urllib.request.Request(url, data=data, method='PUT')
    req.add_header('Content-Type', 'text/html')
    req.add_header('Content-Length', str(len(data)))
    try:
        resp = urllib.request.urlopen(req, timeout=120)
        print('PUT status:', resp.status, 'bytes:', len(data))
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', 'replace')
        print('PUT HTTPError:', e.code, body[:500])

if __name__ == '__main__':
    put(sys.argv[1], sys.argv[2])
