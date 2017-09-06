# User lambda to sort 
class User:
    def __init__(self, user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)

In [3]: users = [User(23), User(3), User(99)]

In [4]: print(users)
[User(23), User(3), User(99)]

In [5]: print(sorted(users, key=lambda u: u.user_id))
[User(3), User(23), User(99)]

# Use attrgetter to sort
In [6]: from  operator import attrgetter

In [7]: sorted(users, key=attrgetter('user_id'))
Out[7]: [User(3), User(23), User(99)]

In [10]: min(users, key=attrgetter('user_id'))
Out[10]: User(3)

In [11]: max(users, key=attrgetter('user_id'))
Out[11]: User(99)

In [12]:

//for multi attr
by_name = sorted(users, key=attrgetter('last_name', 'first_name'))
