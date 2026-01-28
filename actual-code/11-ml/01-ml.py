hours = [1, 2, 3, 4, 5]
scores = [50, 90, 20, 95, 10]  # 85

from matplotlib import pyplot as plt
plt.scatter(hours, scores)
plt.show()

from sklearn.linear_model import LinearRegression

# create a model
model = LinearRegression()

# fit the model to data
model.fit([[h] for h in hours], scores)  # y = mx + c

import numpy as np
# make a prediction
prediction = model.predict(np.array([[6]]))
print(prediction)

# ### Path 1: “I want to understand ML properly”

# * NumPy (arrays)
# * pandas (cleaning data)
# * scikit-learn (classic models)
# https://www.manning.com/books/build-a-large-language-model-from-scratch


### Path 2: “I want to build AI things”
# * APIs (OpenAI, etc.)
# * Prompting as an engineering task
# * Automation + decision support

