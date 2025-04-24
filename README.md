# ***GreenPredenergy:*** **Predicción de viabilidad de proyectos de energia renovable en Colombia**


## **Descripcion** 🚀
Debido a la posición geográfica, Colombia es un país con mucho potencial de desarrollar proyectos de energía renovable, sin embargo, los esfuerzos del gobierno se ven mermados por la gran desconexión del territorio. Es por esta razón que este proyecto se enfoca en traer la atención a estos lugares, con el fin de ser considerados como fuertes candidatos para invertir en su infrasestructura energética y así fortalecer el desarrollo regional del país.

A través del análisis de datos energéticos y meteorológicos, de los municipios, este modelo evalua y predice la viabilidad de un proyecto de energía renovable. Con la información que brinda este algoritmo de _machine learning_ los inversores y los gobiernos locales tienen la oportunidad de evaluar y reducir los costos de un proyecto de energía solar o eólica. 

## **Características del proyecto** hammer: 
Nuestro modelo trabaja con datos abierto del gobierno de Colombia. 

## **Una evaluación directa de la viabilidad:**
* Introduce el municipio
* Califica las condiciones del clima para un proyecto renovable

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


## **¿Qué es el proyecto?** 🤔
Este proyecto tiene como objetivo desarrollar un modelo de predicción que evalúe la viabilidad de proyectos de energía renovable en Colombia. Utilizando técnicas de análisis de datos y aprendizaje automático, se busca identificar factores clave que influyen en el éxito de estos proyectos, como la ubicación geográfica, las condiciones climáticas.

## **¿Por qué es importante?** 👆
La transición energética es crucial para Colombia, un país que busca aumentar su capacidad de generación a partir de fuentes renovables. Con una capacidad instalada en crecimiento y un compromiso gubernamental hacia la sostenibilidad, este proyecto es relevante para facilitar la toma de decisiones informadas sobre inversiones en energía renovable. Al predecir la viabilidad de proyectos, se pueden optimizar recursos, minimizar riesgos y contribuir a la lucha contra el cambio climático.

## **¿Cómo se llevó a cabo?** 📑📉
Etapas del proyecto:

* Recolección de Datos: Se recopilaron datos relevantes sobre proyectos existentes, condiciones ambientales y políticas energéticas.
* Análisis Exploratorio: Se realizó un análisis exploratorio para entender las relaciones entre variables y se prepararon los datos para modelado.
* Desarrollo del Modelo: Se emplearon algoritmos de aprendizaje automático para crear un modelo predictivo que evalúa la viabilidad de nuevos proyectos.
* Validación y Evaluación: Se valido el modelo utilizando métricas adecuadas para asegurar su precisión y confiabilidad.
* Implementación: Finalmente, se desarrolló una interfaz que permite a los interesados evaluar nuevos proyectos utilizando el modelo.










## **Autores** 😊

* **Monica Garcia**
* **Juan Pablo Cardenas**
* **Juan Pablo Quevedo**
* **Hildebrando Vargas**
* **Jonathan Gutierrez**
* **Mary Luz Ceballosl**