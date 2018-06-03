awk '/'href=\"'/' index.html | awk -F "/" '{print $3}' | awk '/'cisco'/' | awk '/.com$/' | sort -u | nslookup  | awk '/^Address: / { print $2}' | awk '!/:/'
