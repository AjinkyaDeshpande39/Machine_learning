# Machine_learning

            neuclear stability
            


My project has built a model which helps you predict whether an element exists or not based on its atomic number and atomic mass number.

In this project i have collected atomic number and atomic mass number of all elements in periodic table and also addel some hypothetical
non existing elements in training set.

training example : [atomic size , atomic mass]

Each of the training example is labelled as 1 : if element exists an 0: if element doesnt exists

X = training set 236x2
Y = labels 236x1

Data is stored in "New Text Document.txt"

"keras_practice.py" runs python code which -1)extracts data
                                            2)stores them in numpy array
                                            3)build a neural network                       ......
                                                                                           ......{ with the help of tensorflow.keras }
                                            4)predicts output with 98% training accuracy   ......
                                            
