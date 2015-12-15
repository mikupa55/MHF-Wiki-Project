from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    data = ''
    #def handle_starttag(self, tag, attrs):
        #print("Encountered a start tag:", tag)
  #  def handle_endtag(self, tag):
       # print("Encountered an end tag :", tag)
    def handle_data(self, data):
        self.data += data + "\n"


parser = MyHTMLParser()
file = open("tonf.html", 'r')
out = open("tonf.txt", 'w')
for line in file:
    parser.feed(line)

out.write(parser.data)

file.close()
out.close()


