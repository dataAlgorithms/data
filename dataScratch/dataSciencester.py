# users initial definition
users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]

# frinednships initial definition
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# to define user friends
for user in users:
    user["friends"] = []

# Intial user friends
for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

# Check the average number of connections
def number_of_friends(user):
    return len(user["friends"])

# total connections
total_connections = sum(number_of_friends(user) for user in users)
print 'total_connections:', total_connections

# avg connections
num_users = len(users)
avg_connections = total_connections / float(num_users)
print 'avg_connections:', avg_connections

# create a list (user_id, number_of_friends)
num_friends_by_id = [(user["id"],number_of_friends(user)) for user in users]
sorted_num_friends_by_id = sorted(num_friends_by_id,
                                  key=lambda (user_id, num_friends): num_friends,
                                  reverse=True)
print 'sorted_num_friends_by_id:', sorted_num_friends_by_id 

def friends_of_friend_ids_bad(user):
    # foaf is short for friend of a friend
    return [foaf["id"]
             for friend in user["friends"]
               for foaf in friend["friends"]]

print "friends_of_friends_ids_bad:", friends_of_friend_ids_bad(users[0])

from collections import Counter

def not_the_same(user, other_user):

    """two users are not the same if they have different ids"""
    return user["id"] != other_user["id"]

def not_friends(user, other_user):
    """other_user is not a friend if he's not in user["friends"];
    that is, if he's not_the_same as all the people in u ser["friends"]"""
    return all(not_the_same(friend, other_user) 
                 for friend in user["friends"])

def friends_of_friend_ids(user):
    return Counter(foaf["id"]
            for friend in user["friends"]
            for foaf in friend["friends"]
            if not_the_same(user, foaf)
            and not_friends(user, foaf))

print "friends_of_friend_ids:", friends_of_friend_ids(users[3])

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

def data_scientists_who_like(target_interest):
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]

from collections import defaultdict

user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

def most_common_interests_with(user):
    return Counter(interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"])
    
print 'most_common_interests_with:', most_common_interests_with(users[0])

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
    (48000, 0.7), (76000, 6),
    (69000, 6.5), (76000, 7.5),
    (60000, 2.5), (83000, 10),
    (48000, 1.9), (63000, 4.2)
]

salary_by_tenure = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

average_salary_by_tenure = {
    tenure: sum(salaries) / float(len(salaries))
    for tenure, salaries in salary_by_tenure.items()
}

print 'average_salary_by_tenure:', average_salary_by_tenure 

def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"

salary_by_tenure_bucket = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

average_salary_by_bucket = {
    tenure_bucket: sum(salaries) / float(len(salaries))
    for tenure_bucket, salaries in salary_by_tenure_bucket.iteritems()
}

print 'average_salary_by_bucket:', average_salary_by_bucket 

def predict_paid_or_unpaid(years_experience):
    if years_experience < 3.0:
        return "paid"
    elif years_experience < 8.5:
        return "unpaid"
    else:
        return "paid"
    
words_and_counts = Counter(word
                   for user, interest in interests
                   for word in interest.lower().split())

for word, count in words_and_counts.most_common():
    if count > 1:
        print word, count
        
"""
total_connections: 24
avg_connections: 2.4
sorted_num_friends_by_id: [(1, 3), (2, 3), (3, 3), (5, 3), (8, 3), (0, 2), (4, 2), (6, 2), (7, 2), (9, 1)]
friends_of_friends_ids_bad: [0, 2, 3, 0, 1, 3]
friends_of_friend_ids: Counter({0: 2, 5: 1})
most_common_interests_with: Counter({9: 3, 1: 2, 8: 1, 5: 1})
average_salary_by_tenure: {6.5: 69000.0, 7.5: 76000.0, 6: 76000.0, 10: 83000.0, 8.1: 88000.0, 4.2: 63000.0, 8.7: 83000.0, 0.7: 48000.0, 1.9: 48000.0, 2.5: 60000.0}
average_salary_by_bucket: {'more than five': 79166.66666666667, 'between two and five': 61500.0, 'less than two': 48000.0}
learning 3
java 3
python 3
big 3
data 3
hbase 2
regression 2
cassandra 2
statistics 2
probability 2
hadoop 2
networks 2
machine 2
neural 2
scikit-learn 2
r 2
"""
