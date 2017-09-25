1. start
kafka/bin/zookeeper-server-start.sh kafka/config/zookeeper.properties
kafka/bin/kafka-server-start.sh kafka/config/server.properties

2. Topics, console producer, and console consumer
Kafka messages are grouped into topics, so we need to create one before we can send messages
through Kafka:
$ kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 \
--replication-factor 1 --partitions 1 --topic test
Created topic "test".

We can see the topic we created with the list topics command:
$ kafka/bin/kafka-topics.sh --list --zookeeper localhost:2181
test

Now we can use the “console producer” to type some messages in manually, and send them to the
test topic. Enter this command:
kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test

Then type in a simple JSON message and press Return (there will be no output, so hit Ctrl-C to exit
once you’re done):
{"message": "Hello, World!"}

Now we can play back the test topic from the beginning, and see our message. Once again, hit Ctrl-C to exit:
$ kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 \
--topic test --from-beginning
{"message": "Hello, World!"}
^CProcessed a total of 1 messages

