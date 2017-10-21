# Print filename of unknown origin
# use this convention to avoid error
def bad_filename(filename):
    return repr(filename)[1:-1]

try:
    print(filename)
except UnicodeEncodeError:
    print(bad_filename(filename))

# Re-encode the value in some way
def bad_filename(filename):
    temp = filename.encode(sys.getfilesystemencoding(), 
              errors='surrogateescape')
    return temp.decode('latin-1')
