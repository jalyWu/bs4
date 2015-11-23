#coding=utf-8

from bs4 import BeautifulSoup

if __name__ == '__main__':
    html_doc = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>

    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

    <p class="story">...</p>
    """
    soup=BeautifulSoup(html_doc,'html.parser')
    #print soup.get_text()
    #print soup.getText
    print soup.head
    print soup.body.b
    print soup.find_all('a')
    head_tag=soup.head
    title_tag=head_tag.contents[0]
    print title_tag
    print title_tag.contents[0]
    for child in title_tag.children:
        print child
    tag_p=soup.p
    print tag_p
    for child in tag_p.children:
        print child
    print '---------------------'
    for child in tag_p.descendants:
        print child
    print title_tag.string
    print head_tag.string
    print '---------------------'
    for string in soup.stripped_strings:
        print string

    print 'here is going up'
    print title_tag.parent
    link=soup.a
    for parent in link.parents:
        if parent is None:
            print parent
        else:
            print parent.name
            
