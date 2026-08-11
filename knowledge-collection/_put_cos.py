import sys, urllib.request

def main():
    local = sys.argv[1]
    url = sys.argv[2]
    with open(local, "rb") as f:
        data = f.read()
    req = urllib.request.Request(url, data=data, method="PUT")
    req.add_header("Content-Type", "text/html")
    req.add_header("Content-Length", str(len(data)))
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            print("HTTP", resp.status, "len", len(data))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        print("HTTPError", e.code, body[:500])
        sys.exit(1)

if __name__ == "__main__":
    main()
