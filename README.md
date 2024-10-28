# ***GreenPredenergy:*** **Predicción de viabilidad de proyectos de energia renovable en Colombia**
### Proyecto Final - TalentoTech 2024

> El proyecto fue realizado en el marco del curso de AI-ML TalentoTech

## **Descripcion** 🚀
Debido a la posición geográfica, Colombia es un país con mucho potencial de desarrollar proyectos de energía renovable, sin embargo, los esfuerzos del gobierno se ven mermados por la gran desconexión del territorio. Es por esta razón que este proyecto se enfoca en traer la atención a estos lugares, con el fin de ser considerados como fuertes candidatos para invertir en su infrasestructura energética y así fortalecer el desarrollo regional del país.

A través del análisis de datos energéticos y meteorológicos, de los municipios, este modelo evalua y predice la viabilidad de un proyecto de energía renovable. Con la información que brinda este algoritmo de _machine learning_ los inversores y los gobiernos locales tienen la oportunidad de evaluar y reducir los costos de un proyecto de energía solar o eólica. 

## **Características del proyecto** :hammer: 
Nuestro modelo trabaja con datos abierto del gobierno de Colombia. Introduce el municipio y recibe:

*Una evaluación directa de la viabilidad

## **Tecnologías** 📗
Se utilizan las siguientes tecnologias para el desarrollo del proyecto:

* [ Python ](https://www.python.org/) -- <img height="20" src="https://cdn.simpleicons.org/python?viewbox=auto" />
* [Jupyter](https://jupyter.org/) -- <img height="20" src="https://cdn.simpleicons.org/jupyter?viewbox=auto" />
* [Pandas](https://pandas.pydata.org/) -- <img height="20" src="https://cdn.simpleicons.org/pandas?viewbox=auto" />
* [Numpy](https://numpy.org/) -- <img height="20" src="https://cdn.simpleicons.org/numpy?viewbox=auto" />
* [Scikit-learn](https://scikit-learn.org/stable/) -- <img height="20" src="https://cdn.simpleicons.org/scikitlearn?viewbox=auto" />
* [github](https://github.com) -- <img height="20" src="https://cdn.simpleicons.org/github?viewbox=auto" />
* [seaborn](https://seaborn.pydata.org/) -- <img height="20" src="https://seaborn.pydata.org/_images/logo-mark-lightbg.svg?viewbox=auto" />
* [flask](https://flask.palletsprojects.com/en/2.0.x/) -- <img height="20" src="https://cdn.simpleicons.org/flask?viewbox=auto" />

## **Autores** 😊

* **Monica Garcia**
* **Juan Pablo Cardenas**
* **Juan Pablo Quevedo**
* **Hildebrando Vargas**
* **Jonathan Gutierrez**
* **Mary Luz Ceballosl**

## **Tareas**  ✒️

 - [Importar librerías necesarias](# Importar librerías necesarias)
 2. Cargar los Datos
 3. Explore y visualice los datos para obtener información.
 4. Prepare los datos para los algoritmos de machine learning.
 5. Generación de Estadísticas Descriptivas
 6. Visualización de datos utilizando gráficos de barras, histogramas y gráficos de dispersión
 7. Identificación y manejo de valores atípicos y tendencias en los datos
 8. Uso de técnicas como imputación de la media, mediana y regresión para completar datos faltantes.
 9. Eliminación de registros con datos faltantes o imputación de valores categóricos.
 10. Cálculo de la correlación entre variables.
 11. Aplicación de técnicas de reducción de dimensionalidad para reducir la dimensionalidad de los datos.
 12. Aplicación de PCA para reducir la dimensionalidad de datasets
 13. Aplicación de técnicas de regresión para predecir valores de variables.
 14. Ajusta tu modelo.
 15. Presente su solución.
 16. Inicie, supervise y mantenga su sistema.


## **Importar librerías necesarias** <a name="Importar librerías necesarias"></a>

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.linear_model import
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, auc, roc_curve, roc_auc_score
from sklearn.impute import KNNImputer
from sklearn.preprocessing import RobustScaler
from sodapy
import pickle
```
## *Pandas:* 
Biblioteca de Python diseñada que trabaja con datos tabulares, es decir, datos organizados en filas y columnas, Proporciona estructuras de datos como DataFrames, facilita la manipulación y análisis de datos.
## *NumPy:*
Biblioteca que proporciona soporte para arreglos multidimensionales y funciones matemáticas de alto rendimiento. Utilizada en la ciencia de datos, análisis numérico y computación científica.
## *Matplotlib:* 
Biblioteca de Python que crea visualizaciones estáticas, animadas e interactivas en Python. Es utilizada en la ciencia de datos, análisis de datos y visualización. Se usa para representar datos numéricos en forma gráfica.
## *Seaborn:* 
Biblioteca de visualización de datos con  interfaz de alto nivel para crear gráficos estadísticos, simplifica la creación de gráficos complejos, incluyendo temas y paletas de colores que mejoran la estética de las visualizaciones.
## *Sklearn:*
Las librerías de Scikit-learn en Google Colab ofrecen herramientas clave para el aprendizaje automático: train_test_split divide los datos en conjuntos de entrenamiento y prueba; KFold y cross_val_score facilitan la validación cruzada; los clasificadores MultinomialNB, GaussianNB y BernoulliNB implementan Naive Bayes; funciones como classification_report y accuracy_score evalúan el rendimiento del modelo; KNNImputer imputa valores faltantes usando K-Nearest Neighbors, y RobustScaler normaliza características de manera robusta frente a outliers.
## *SodaPy:*
La biblioteca  permite interactuar con la API de datos abiertos de Socrata. Facilita la consulta y obtención de conjuntos de datos públicos en formatos como JSON o CSV, lo que es útil en Google Colab para analizar datos de interés público sin necesidad de descargarlos manualmente.
## *Pickle:*
Se utiliza en Google Colab, permite serializar y deserializar objetos de Python. Esto es para guardar modelos de aprendizaje automático y estructuras de datos en archivos, facilitando su almacenamiento y carga posterior sin necesidad de regenerarlos, optimizando así el tiempo y los recursos en proyectos de análisis y machine learning.





