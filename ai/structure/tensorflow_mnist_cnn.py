from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import numpy as np

from layers import conv_layer, max_pool_2x2, full_layer

DATA_DIR = '.'
MINIBATCH_SIZE = 50
STEPS = 5000


mnist = input_data.read_data_sets(DATA_DIR, one_hot=True)

x = tf.placeholder(tf.float32, shape=[None, 784])
y_ = tf.placeholder(tf.float32, shape=[None, 10])

x_image = tf.reshape(x, [-1, 28, 28, 1])
conv1 = conv_layer(x_image, shape=[5, 5, 1, 32])
conv1_pool = max_pool_2x2(conv1)

conv2 = conv_layer(conv1_pool, shape=[5, 5, 32, 64])
conv2_pool = max_pool_2x2(conv2)

conv2_flat = tf.reshape(conv2_pool, [-1, 7*7*64])
full_1 = tf.nn.relu(full_layer(conv2_flat, 1024))

keep_prob = tf.placeholder(tf.float32)
full1_drop = tf.nn.dropout(full_1, keep_prob=keep_prob)

y_conv = full_layer(full1_drop, 10)

cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=y_conv, labels=y_))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for i in range(STEPS):
        batch = mnist.train.next_batch(MINIBATCH_SIZE)

        if i % 100 == 0:
            train_accuracy = sess.run(accuracy, feed_dict={x: batch[0], y_: batch[1],
                                                           keep_prob: 1.0})
            print("step {}, training accuracy {}".format(i, train_accuracy))

        sess.run(train_step, feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})

    X = mnist.test.images.reshape(10, 1000, 784)
    Y = mnist.test.labels.reshape(10, 1000, 10)
    test_accuracy = np.mean(
        [sess.run(accuracy, feed_dict={x: X[i], y_: Y[i], keep_prob: 1.0}) for i in range(10)])

print("test accuracy: {}".format(test_accuracy))

'''
Extracting .\train-images-idx3-ubyte.gz
Extracting .\train-labels-idx1-ubyte.gz
Extracting .\t10k-images-idx3-ubyte.gz
Extracting .\t10k-labels-idx1-ubyte.gz
2017-12-05 10:31:00.559063: I C:\tf_jenkins\home\workspace\rel-win\M\windows\PY\35\tensorflow\core\platform\cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX AVX2
step 0, training accuracy 0.05999999865889549
step 100, training accuracy 0.8399999737739563
step 200, training accuracy 0.8799999952316284
step 300, training accuracy 0.9800000190734863
step 400, training accuracy 0.9599999785423279
step 500, training accuracy 0.9800000190734863
step 600, training accuracy 0.9599999785423279
step 700, training accuracy 1.0
step 800, training accuracy 0.9399999976158142
step 900, training accuracy 0.9200000166893005
step 1000, training accuracy 0.9599999785423279
step 1100, training accuracy 0.9800000190734863
step 1200, training accuracy 0.9800000190734863
step 1300, training accuracy 0.9800000190734863
step 1400, training accuracy 0.9599999785423279
step 1500, training accuracy 0.9399999976158142
step 1600, training accuracy 0.9800000190734863
step 1700, training accuracy 0.9800000190734863
step 1800, training accuracy 0.9399999976158142
step 1900, training accuracy 0.9599999785423279
step 2000, training accuracy 0.9200000166893005
step 2100, training accuracy 1.0
step 2200, training accuracy 1.0
step 2300, training accuracy 1.0
step 2400, training accuracy 1.0
step 2500, training accuracy 1.0
step 2600, training accuracy 0.9800000190734863
step 2700, training accuracy 1.0
step 2800, training accuracy 0.9599999785423279
step 2900, training accuracy 1.0
step 3000, training accuracy 0.9399999976158142
step 3100, training accuracy 0.9800000190734863
step 3200, training accuracy 0.9800000190734863
step 3300, training accuracy 1.0
step 3400, training accuracy 1.0
step 3500, training accuracy 1.0
step 3600, training accuracy 0.9800000190734863
step 3700, training accuracy 1.0
step 3800, training accuracy 0.9800000190734863
step 3900, training accuracy 0.9800000190734863
step 4000, training accuracy 1.0
step 4100, training accuracy 1.0
step 4200, training accuracy 0.9800000190734863
step 4300, training accuracy 1.0
step 4400, training accuracy 1.0
step 4500, training accuracy 0.9599999785423279
step 4600, training accuracy 0.9599999785423279
step 4700, training accuracy 1.0
step 4800, training accuracy 1.0
step 4900, training accuracy 0.9599999785423279
test accuracy: 0.9875999689102173
'''
