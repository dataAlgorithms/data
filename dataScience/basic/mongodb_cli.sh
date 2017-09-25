1. start mongo
./mongodb/bin/mongod --dbpath mongodb/data/db &

2. operation on mongo
mongo agile_data_science

> db.my_collection.insert({"name": "Russell Jurney"});
> db.my_collection.find({"name": "Russell Jurney"});
> db.executives.find()
