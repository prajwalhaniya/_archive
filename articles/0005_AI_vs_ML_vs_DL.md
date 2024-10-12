# AI vs ML vs DL | What is the difference?

Original reference: https://cloud.google.com/discover/deep-learning-vs-machine-learning

Artificial intelligence is a large and complicated field with an extended ecosystem of terms, phrases, and concepts that can be intimidating when bandied about by technologists and other experts. Artificial intelligence is often used in popular culture as a catch-all word to mean any type of smart machine. In reality, artificial intelligence, machine learning, and deep learning are distinct terms with subtle differences.

To learn more about how artificial intelligence and machine learning can help your business, read more about [Google Cloud’s AI and ML products and solutions here](https://cloud.google.com/products/ai).

**New customers get up to $300 in free credits** to try Vertex AI and other Google Cloud products.

[Get started for free](https://console.cloud.google.com/freetrial?redirectPath=/vertex-ai/)[Learn about Vertex AI](https://cloud.google.com/vertex-ai)

# Deep learning vs machine learning vs artificial intelligence

Machine learning is a subset of artificial intelligence. In turn, deep learning is a subset of machine learning. Essentially, all deep learning is machine learning, and all machine learning is artificial intelligence, but not all artificial intelligence is machine learning.

## What is deep learning?

Deep learning is a subset of machine learning that uses artificial neural networks to process and analyze information. Neural networks are composed of computational nodes that are layered within deep learning algorithms. Each layer contains an input layer, an output layer, and a hidden layer. The neural network is fed training data which helps the algorithm learn and improve accuracy. When a neural network is composed of three or more layers it is said to be “deep,” thus deep learning.

Deep learning algorithms are inspired by the workings of the human brain and are used for analysis of data with a logical structure. Deep learning is used in many of the tasks we think of as AI today, including image and speech recognition, object detection, and natural language processing. Deep learning can make non-linear, complex correlations within datasets though requires more training data and computational resources than machine learning.

Some common types of neural networks used for deep learning include:

**Feedforward neural networks (FF)** are one of the oldest forms of neural networks, with data flowing one way through layers of artificial neurons until the output is achieved.

**Recurrent neural networks (RNN)** differ from feedforward neural networks in that they typically use time series data or data that involves sequences. Recurrent neural networks have “memory” of what happened in the previous layer as contingent to the output of the current layer.

**Long/short term memory (LSTM)** is an advanced form of RNN that can use memory to “remember” what happened in previous layers.

**Convolutional neural networks (CNN)** include some of the most common neural networks in modern artificial intelligence and use several distinct layers (a convolutional layer, then a pooling layer) that filter different parts of an image before putting it back together (in the fully connected layer).

**Generative adversarial networks (GAN)** involve two neural networks (a “generator” and a “discriminator") that compete against each other in a game that ultimately improves the accuracy of the output.

## What is machine learning?

Machine learning is a subset of artificial intelligence that enables a system to autonomously learn and improve without being explicitly programmed. Machine learning algorithms work by recognizing patterns and data and making predictions when new data is inputted into the system.

In broad strokes, three kinds of models are often used in machine learning: supervised, unsupervised, and reinforcement.

### Supervised learning

Supervised learning is a machine learning model that uses labeled training data (structured data) to map a specific input to an output. In supervised learning, the output is known (such as recognizing a picture of an apple) and the model is trained on data of the known output. In simple terms, to train the algorithm to recognize pictures of apples, feed it pictures labeled as apples.

The most common supervised learning algorithms used today include:

- Linear regression
- Polynomial regression
- K-nearest neighbors
- Naive Bayes
- Polynomial regression
- Decision trees

### Unsupervised learning

Unsupervised learning is a machine learning model that uses unlabeled data (unstructured data) to learn patterns. Unlike supervised learning, the output is not known ahead of time. Rather, the algorithm learns *from* the data without human input (thus, unsupervised) and categorizes it into groups based on attributes. For instance, if the algorithm is given pictures of apples and bananas, it will work by itself to categorize which picture is an apple and which is a banana. Unsupervised learning is good at descriptive modeling and pattern matching.

The most common unsupervised learning algorithms used today include:

- Fuzzy means
- K-means clustering
- Hierarchical clustering
- Principal component analysis
- Partial least squares

A mixed approach machine learning called semi-supervised learning is also often employed, where only some of the data is labeled. In semi-supervised learning, the algorithm must figure out how to organize and structure the data to achieve a known result. For instance, the machine learning model is told that the end result is an apple, but only some of the training data is labeled as an apple.

### Reinforcement learning

Reinforcement learning is a machine learning model that can be described as “learn by doing” through a series of trial and error experiments. An “agent” learns to perform a defined task through a feedback loop until its performance is within a desirable range. The agent receives positive reinforcement when it performs the task well and negative reinforcement when it performs poorly. An example of reinforcement learning is when Google researchers taught a reinforcement learning algorithm to play the game Go. The model had no prior knowledge of the rules of Go and simply moved pieces at random and “learned” the best results as the algorithm was trained, to the point that the machine learning model could beat a human player at the game.

## What is artificial intelligence?

Artificial intelligence is a field of science concerned with building computers and machines that can reason, learn, and act in such a way that would normally require human intelligence or that involves data whose scale exceeds what humans can analyze. AI is a large field that includes many disciplines including computer science, data and analytics, software engineering, and even philosophy.

At the business level, AI is a set of technologies that has many use cases, including data analytics, predictions and forecasting, natural language processing, recommendations, machine automation, intelligent data retrieval, and more.

## Artificial intelligence vs machine learning vs deep learning

Artificial intelligence, machine learning, and deep learning are often used synonymously when discussing all things AI. While the terms are correlated, they are not interchangeable.

Whereas AI is a broad field, machine learning is an application of AI that allows machines to learn without being specifically programmed. Machine learning is more explicitly used as a means to extract knowledge from data through simpler methods such as decision trees or linear regression, while deep learning uses the more advanced methods found in artificial neural networks.

Deep learning requires less human intervention, as features of a dataset are extracted automatically, versus simpler machine learning techniques that often require an engineer to manually identify features and classifiers of the data and adjust the algorithm accordingly. Essentially, deep learning can learn from its own errors while machine learning needs a human to intervene.

Deep learning also requires much more data than machine learning, which in turn requires significantly more computational power. Machine learning can typically be done with servers running CPUs, while deep learning often requires more robust chips such as GPUs.