import urllib.request
from lxml import etree


def gakki_photos():
    url = 'http://acfun.cn/a/ac3581658'
    pathToDownload = "/Users/Editor_kn/Documents/My Pictures/gakki/"
    with urllib.request.urlopen(url) as response:
        html = response.read()
        tree = etree.HTML(html)
        nodes = tree.xpath("//div[@id='area-player']/p/img")
        for i,n in enumerate(nodes):
            img_src = n.attrib["src"]
            fileName = 'gakki'+' '+str(i+1)
            urllib.request.urlretrieve(img_src, pathToDownload+fileName)

if __name__ == '__main__':
    gakki_photos()
