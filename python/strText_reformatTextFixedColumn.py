In [39]: %paste
s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

## -- End pasted text --

In [40]: import textwrap

In [41]: print(textwrap.fill(s, 70))
Look into my eyes, look into my eyes, the eyes, the eyes, the eyes,
not around the eyes, don't look around the eyes, look into my eyes,
you're under.

In [42]: print(textwrap.fill(s, 40))
Look into my eyes, look into my eyes,
the eyes, the eyes, the eyes, not around
the eyes, don't look around the eyes,
look into my eyes, you're under.

In [43]: print(textwrap.fill(s, 40, initial_indent='  '))
  Look into my eyes, look into my eyes,
the eyes, the eyes, the eyes, not around
the eyes, don't look around the eyes,
look into my eyes, you're under.

In [44]: print(textwrap.fill(s, 40, subsequent_indent=' '))
Look into my eyes, look into my eyes,
 the eyes, the eyes, the eyes, not
 around the eyes, don't look around the
 eyes, look into my eyes, you're under.

In [45]: import os

In [47]: os.get_terminal_size().columns
Out[47]: 80
