from sklearn.neural_network import MLPClassifier
from sklearn import datasets

iris = datasets.load_iris()
entradas = iris.data
saidas = iris.target

# tol = tolerancia
# verbose = mostrar o erro
# max_iter = epocas
redeNeural = MLPClassifier(verbose=True,
                           max_iter=2000,
                           tol=0.00001,
                           activation='logistic')
redeNeural.fit(entradas, saidas) 

# fazer uma previsão
redeNeural.predict([[5, 7.2, 5.1, 2.2]])

