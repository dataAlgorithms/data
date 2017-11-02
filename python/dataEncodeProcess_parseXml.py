#coding=utf-8

'''
<?xml version="1.0"?>
<rss version="2.0" xmlns:dc="http://purl.org/dc/elements/1.1/">
<channel>
<title>Planet Python</title>
<link>http://planet.python.org/</link>
<language>en</language>
<description>Planet Python - http://planet.python.org/</description>
<item>
<title>Steve Holden: Python for Data Analysis</title>
<guid>http://holdenweb.blogspot.com/...-data-analysis.html</guid>
<link>http://holdenweb.blogspot.com/...-data-analysis.html</link>
<description>...</description>
<pubDate>Mon, 19 Nov 2012 02:13:51 +0000</pubDate>
</item>
<item>
184 | Chapter 6: Data Encoding and Processing<title>Vasudev Ram: The Python Data model (for v2 and v3)</title>
<guid>http://jugad2.blogspot.com/...-data-model.html</guid>
<link>http://jugad2.blogspot.com/...-data-model.html</link>
<description>...</description>
<pubDate>Sun, 18 Nov 2012 22:06:47 +0000</pubDate>
</item>
<item>
<title>Python Diary: Been playing around with Object Databases</title>
<guid>http://www.pythondiary.com/...-object-databases.html</guid>
<link>http://www.pythondiary.com/...-object-databases.html</link>
<description>...</description>
<pubDate>Sun, 18 Nov 2012 20:40:29 +0000</pubDate>
</item>
...
</channel>
</rss>
'''
from urllib.request import urlopen
from xml.etree.ElementTree import parse

# Download the RSS feed and parse it
u = urlopen("http://planetpython.org/rss20.xml")
doc = parse(u)

# Extract and output tags of interest
for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')

    print(title)
    print(date)
    print(link)
    print()

'''
output:

D:\Python34\python.exe D:/dataviz/dataEncodeProcess_parseXml.py
Anarcat: October 2017 report: LTS, feed2exec beta, pandoc filters, git mediawiki
Thu, 02 Nov 2017 16:12:08 +0000
https://anarc.at/blog/2017-11-02-free-software-activities-october-2017/

PyCharm: PyCharm 2017.3 EAP 8
Thu, 02 Nov 2017 15:11:39 +0000
http://feedproxy.google.com/~r/Pycharm/~3/g09ZZ1BKTY8/

Continuum Analytics Blog: AnacondaCON 2018: Anaconda Opens Registration and Call for Speakers for Second Annual User Conference
Thu, 02 Nov 2017 14:12:42 +0000
https://www.anaconda.com/blog/news/anacondacon-2018-anaconda-opens-registration-and-call-for-speakers-for-second-annual-user-conference/

Python Software Foundation: Eric Floehr, Community Service Award 3rd Quarter 2017 Recipient
Thu, 02 Nov 2017 10:31:52 +0000
http://feedproxy.google.com/~r/PythonSoftwareFoundationNews/~3/qBj_8ISlUfM/eric-floehr-community-service-award-3rd.html

Python Bytes: #50 Bundling , shipping, and protecting Python applications
Thu, 02 Nov 2017 08:00:00 +0000
https://pythonbytes.fm/episodes/show/50/bundling-shipping-and-protecting-python-applications

Django Weblog: Django bugfix release: 1.11.7
Thu, 02 Nov 2017 01:39:45 +0000
https://www.djangoproject.com/weblog/2017/nov/01/bugfix-release/

Enthought: Webinar: Machine Learning Mastery Workshop: An Exclusive Peek “Under the Hood” of Enthought Training
Wed, 01 Nov 2017 19:01:02 +0000
http://blog.enthought.com/training/machine-learning-mastery-workshop-an-exclusive-peek-under-the-hood-of-enthought-training/

PyCharm: Webinar Recording: “GraphQL in the Python World” with Nafiul Islam
Wed, 01 Nov 2017 14:05:18 +0000
http://feedproxy.google.com/~r/Pycharm/~3/-efxJE05Hwk/

PyPy Development
Wed, 01 Nov 2017 11:49:54 +0000
http://feedproxy.google.com/~r/PyPyStatusBlog/~3/QD4P1Z312G4/cape-of-good-hope-for-pypy-hello-from.html

Full Stack Python: DevOps, Continuous Delivery... and You
Wed, 01 Nov 2017 04:00:00 +0000
https://www.fullstackpython.com/devops-continuous-delivery-you.html

NumFOCUS: NumFOCUS welcomes Jim Weiss, Events Coordinator
Tue, 31 Oct 2017 21:08:14 +0000
https://www.numfocus.org/blog/numfocus-welcomes-jim-weiss-events-coordinator/

Stack Abuse: Download Files with Python
Tue, 31 Oct 2017 19:44:31 +0000
http://stackabuse.com/download-files-with-python/

Mike Driscoll: Python 3: Variable Annotations
Tue, 31 Oct 2017 17:15:18 +0000
http://www.blog.pythonlibrary.org/2017/10/31/python-3-variable-annotations/

PyCharm: PyCharm 2017.2.4 is out now
Tue, 31 Oct 2017 13:57:10 +0000
http://feedproxy.google.com/~r/Pycharm/~3/wv142W0fdio/

The Digital Cat: A game of tokens: solution - Part 3
Tue, 31 Oct 2017 12:00:00 +0000
http://blog.thedigitalcatonline.com/blog/2017/10/31/a-game-of-tokens-solution-part-3/

The Digital Cat: A game of tokens: write an interpreter in Python with TDD - Part 3
Tue, 31 Oct 2017 11:00:00 +0000
http://blog.thedigitalcatonline.com/blog/2017/10/31/a-game-of-tokens-write-an-interpreter-in-python-with-tdd-part-3/

Weekly Python Chat: Writing Docs with Sphinx
Mon, 30 Oct 2017 20:30:00 +0000
https://www.crowdcast.io/e/sphinx

Tryton News: New Tryton release 4.6
Mon, 30 Oct 2017 18:00:00 +0000
http://www.tryton.org/posts/new-tryton-release-46.html

Continuum Analytics Blog: Getting Started with GPU Computing in Anaconda
Mon, 30 Oct 2017 16:56:42 +0000
https://www.anaconda.com/blog/developer-blog/getting-started-with-gpu-computing-in-anaconda/

Stack Abuse: Modified Preorder Tree Traversal in Django
Mon, 30 Oct 2017 16:15:12 +0000
http://stackabuse.com/modified-preorder-tree-traversal-in-django/

Doug Hellmann: tempfile — Temporary File System Objects — PyMOTW 3
Mon, 30 Oct 2017 13:00:34 +0000
http://feeds.doughellmann.com/~r/doughellmann/python/~3/4nqGfgTfvL8/

Will Kahn-Greene: Markus v1.0 released! Better metrics API for Python projects.
Mon, 30 Oct 2017 13:00:00 +0000
http://bluesock.org/~willkg/blog/dev/markus_1_0.html

Mike Driscoll: Educative Python 101 / 201 Courses on Sale
Mon, 30 Oct 2017 12:55:02 +0000
http://www.blog.pythonlibrary.org/2017/10/30/educative-python-101-201-courses-on-sale/

Mike Driscoll: PyDev of the Week: Matthew Makai
Mon, 30 Oct 2017 12:30:12 +0000
http://www.blog.pythonlibrary.org/2017/10/30/pydev-of-the-week-matthew-makai/

PyPy Development: How to make your code 80 times faster
Mon, 30 Oct 2017 11:15:59 +0000
http://feedproxy.google.com/~r/PyPyStatusBlog/~3/nxgk9LMY-NU/how-to-make-your-code-80-times-faster.html


Process finished with exit code 0

'''
