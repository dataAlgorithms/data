#!/usr/bin/env python


import codecs, json

def write_json_file(obj, path):
    '''Dump an object and write it out as Json to a file.'''
    f = codecs.open(path, 'w', 'utf-8')
    f.write(json.dumps(obj, ensure_ascii=False))
    f.close()

def write_json_lines_file(ary_of_objects, path):
    '''Dump a list of objects out as a Json lines file.'''
    f = codecs.open(path, 'w', 'utf-8')
    for row_object in ary_of_objects:
        json_record = json.dumps(row_object, ensure_ascii=False)
        f.write(json_record + "\n")
    f.close()

def read_json_file(path):
    '''Turn a normal Json files into an object.'''
    text = codecs.open(path, 'r', 'utf-8').read()
    return json.loads(text)

def read_json_lines_file(path):
    '''Turn a josn file into an arry of objects'''
    ary = []
    f = codecs.open(path, "r", "utf-8")
    for line in f:
        record = json.loads(line.rstrip("\n|\r"))
        ary.append(record)
    return ary

def main():
    ary_of_objects = [
        {'name': 'Russell Jurney', 'title': 'CEO'},
        {'name': 'Muhammad Imran', 'title': 'VP of Marketing'},
        {'name': 'Fe Mata', 'title': 'Chief Marketing Officer'},
    ]

    path = "/tmp/test.jsonl"

    write_json_lines_file(ary_of_objects, path)
    print(json.dumps(read_json_lines_file(path), indent=1))

'''
[
 {
  "name": "Russell Jurney",
  "title": "CEO"
 },
 {
  "name": "Muhammad Imran",
  "title": "VP of Marketing"
 },
 {
  "name": "Fe Mata",
  "title": "Chief Marketing Officer"
 }
]
'''
if __name__ == "__main__":
    main()
