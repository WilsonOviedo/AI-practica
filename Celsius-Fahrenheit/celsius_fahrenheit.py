#Codigo general
#Si quieres ver como lo programamos, revisa el video donde lo explico
#todo desde cero: https://youtu.be/iX_on3VxZzk
#Fuente https://colab.research.google.com/drive/1od-bZmep_qM3c1eIDuS3OQH1h-eGu2CD?usp=sharing

import tensorflow as tf
import numpy as np

celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1])
oculta2 = tf.keras.layers.Dense(units=3)
salida = tf.keras.layers.Dense(units=1)
modelo = tf.keras.Sequential([oculta1, oculta2, salida])

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.01),
    loss='mean_squared_error'
)

print("Comenzando entrenamiento...")
historial = modelo.fit(celsius, fahrenheit, epochs=300, verbose=False)
print("Modelo entrenado!")

resultado = round(float( modelo.predict([100.0])))
print("Prediccion: 100 grados celsius son " + str(resultado) + " fahrenheit!")

#Exportar el modelo en formato h5
#modelo.save('celsius_a_fahrenheit.h5')