# Import necessary libraries
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# Load and preprocess the MNIST dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Reshape the images to fit the neural network (28x28 -> 784) and normalize
train_images = train_images.reshape((60000, 28 * 28)).astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28)).astype('float32') / 255

# Convert labels to categorical (one-hot encoding)
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# Build the neural network model
model = models.Sequential()

# Add layers: Input layer with 784 neurons, hidden layer, and output layer
model.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))  # First hidden layer with 512 neurons
model.add(layers.Dropout(0.2))  # Add dropout to prevent overfitting
model.add(layers.Dense(256, activation='relu'))  # Second hidden layer with 256 neurons
model.add(layers.Dense(10, activation='softmax'))  # Output layer with 10 neurons (one for each class)

# Compile the model
model.compile(optimizer='adam', 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])

# Train the model
model.fit(train_images, train_labels, epochs=10, batch_size=128, validation_split=0.2)

# Evaluate the model on the test data
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f'Test accuracy: {test_acc}')
