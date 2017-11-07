'''
cat pred.xml

<?xml version="1.0"?>
<stop>
    <id>14791</id>
    <nm>Clark &amp; Balmoral</nm>
    <sri>
        <rt>22</rt>
        <d>North Bound</d>
        <dd>North Bound</dd>
    </sri>
    <cr>22</cr>
    <pre>
        <pt>5 MIN</pt>
        <fd>Howard</fd>
        <v>1378</v>
        <rn>22</rn>
    </pre>
    <pre>
        <pt>15 MIN</pt>
        <fd>Howard</fd>
        <v>1867</v>
        <rn>22</rn>
    </pre>
</stop>
'''

# read the xml
from xml.etree.ElementTree import parse, Element

doc = parse('pred.xml')
root = doc.getroot()
print(roow)

# remove a few elements
root.remove(root.find('sci'))
root.remove(root.find('cr'))

# insert a new element after <nm>...</nm>
index = root.getchildren().index(root.find('nm'))
print('index', index)

e = Element('spam')
e.text = 'This is a test'
root.indert(inex+1, e)

# write back to a file
doc.write('newpred.xml', xml_declaration=True)

'''
<?xml version='1.0' encoding='us-ascii'?>
<stop>
    <id>14791</id>
    <nm>Clark &amp; Balmoral</nm>
    <spam>This is a test</spam><pre>
        <pt>5 MIN</pt>
        <fd>Howard</fd>
        <v>1378</v>
        <rn>22</rn>
    </pre>
    <pre>
        <pt>15 MIN</pt>
        <fd>Howard</fd>
        <v>1867</v>
        <rn>22</rn>
    </pre>
</stop>
'''
