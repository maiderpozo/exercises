import re


def collect_links(string):
    return re.findall(r'<a href="(.*)">', string)

print(collect_links('''<a href="a">fdf</a>
        
        <a href="b">qff</a>
        
        <a href="abc">dfdg</a>
        
        <a href="fiop">fdghh</a>'''))