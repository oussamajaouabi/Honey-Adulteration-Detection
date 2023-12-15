import pandas as pd
import pickle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('adulteration_dataset_26_08_2021.csv')

c = df.shape[1]

X = df.values[:, 4:c-2]
y = df.values[:, c-1]

# Convertir le type de la variable y de OBJECT à INT.
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.25)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(Xtrain, ytrain)

pickle.dump(knn, open('model.pkl', 'wb'))
