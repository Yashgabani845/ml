import tensorflow as tf
# tensors are nothing but vectors of any dimension 
# 0 D - scaler 
# 1 D - simple 1d array 
# Each tensor has a data type and a shape.
# Data Types Include: float32, int32, string and others.
# Shape: Represents the dimension of data.
string = tf.Variable("this is a string", tf.string) 
number = tf.Variable(324, tf.int16)
floating = tf.Variable(3.567, tf.float64)

#rank of the tensor is same as dimension
rank1_tensor = tf.Variable(["Test"], tf.string) 
rank2_tensor = tf.Variable([["test", "ok"], ["test", "yes"]], tf.string)
print(tf.rank(rank2_tensor))
tf.rank(rank1_tensor)

#shape : number of elements in each dimension 
#reshape : 
tensor1 = tf.ones([1,2,3])  # tf.ones() creates a shape [1,2,3] tensor full of ones
tensor2 = tf.reshape(tensor1, [2,3,1])  # reshape existing data to shape [2,3,1]
tensor3 = tf.reshape(tensor2, [3, -1])  # -1 tells the tensor to calculate the size of the dimension in that place
                                        # this will reshape the tensor to [3,3]
                                                                             
# The numer of elements in the reshaped tensor MUST match the number in the original
print(tensor1)
print(tensor2)
print(tensor3)
# Notice the changes in shape