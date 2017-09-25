1. start elaticsearch
./elasticsearch/bin/elasticsearch -Des.insecure.allow.root=true &

2. use elaticsearch
//xput
curl -XPUT 'localhost:9200/agile_data_science?pretty' \
-H 'Content-Type: application/json' -d'
{
"settings" : {
"index" : {
"number_of_shards" : 1,
"number_of_replicas" : 1
}
}
} '

curl -XPUT 'localhost:9200/agile_data_science/test/1?pretty' \
-H 'Content-Type: application/json' -d'
{
"name" : "Russell Jurney","message" : "trying out Elasticsearch"
}'
Which

//xget
curl -XGET 'localhost:9200/agile_data_science/_search?q=name:Russell&pretty'

