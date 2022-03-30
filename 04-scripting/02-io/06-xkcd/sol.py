

from urllib import request


url = 'https://xkcd.com/info.0.json'
r = request.get(url, allow_redirects=True)

open('download.ico', 'wb').write(r.content)