import codecs

def python_codecs_demo():
    testStrUnicode = u"中文测试Unicode字符串"
    print("testStrUnicode=%s" % testStrUnicode)
    testStrUtf8 = testStrUnicode.encode("UTF-8")
    testStrGbk = testStrUnicode.encode("GBK")

    outputFilename = "outputFileUtf.txt"

    print("------------1.Utf-8 write and read---------------")
    print("---(1) Write Utf-8 string into file ---")
    # 'a+': read, write, append
    # 'w': clear before, then write
    outputFp = codecs.open(outputFilename, 'wb')
    outputFp.write(testStrUtf8)
    outputFp.flush()
    outputFp.close()
    print('---(2) read out previously written Utf-8 content---')
    readoutFp = codecs.open(outputFilename, 'r', 'UTF-8')
    #here already is unicode, for we have pass utf-8 to codecs.open
    readOutStrUnicodeFromUtf8 = readoutFp.read()
    readoutFp.close()
    print("readOutStrUnicodeFromUtf8=%s" % readOutStrUnicodeFromUtf8)

    outputFilename = "outputFileGbk.txt"

    print("---------2.Gbk write and read --------")
    print("---(1) write Gbk string into file---")
    # 'a+': read, write, append
    # 'w': clear before, then write
    outputFp = codecs.open(outputFilename, 'wb')
    outputFp.write(testStrGbk)
    outputFp.flush()
    outputFp.close()
    print("---(2) read out previously written Gbk content---")
    readoutFp = codecs.open(outputFilename, 'r', 'GBK')
    readOutStrUnicodeFromGbk = readoutFp.read()
    readoutFp.close()
    print("readOutStrUnicodeFromGbk=%s" % readOutStrUnicodeFromGbk)

'''
testStrUnicode=中文测试Unicode字符串
------------1.Utf-8 write and read---------------
---(1) Write Utf-8 string into file ---
<class 'bytes'>
---(2) read out previously written Utf-8 content---
readOutStrUnicodeFromUtf8=中文测试Unicode字符串
---------2.Gbk write and read --------
---(1) write Gbk string into file---
---(2) read out previously written Gbk content---
readOutStrUnicodeFromGbk=中文测试Unicode字符串
'''
if __name__ == "__main__":
    python_codecs_demo()
