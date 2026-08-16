# -*- coding: utf-8 -*-
# 乐享上传第2步：HTTP PUT 文件本体到预签名 URL（urllib，Windows 原生路径）
import sys, urllib.request

def put(url, path):
    data = open(path, 'rb').read()
    req = urllib.request.Request(url, data=data, method='PUT')
    req.add_header('Content-Type', 'text/html')
    req.add_header('Content-Length', str(len(data)))
    with urllib.request.urlopen(req, timeout=120) as r:
        code = r.getcode()
    print('PUT', path, '-> HTTP', code, 'bytes', len(data))

if __name__ == '__main__':
    put(sys.argv[1], sys.argv[2])
