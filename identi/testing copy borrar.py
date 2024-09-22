from code import interact
import cv2
import cv2 as cv
import matplotlib.pyplot as plt
import scipy 
from scipy.fftpack import fft2, ifft2, fft
import numpy as np
import math
import pandas as pd
import json
import random
import os
import json


import numpy as np
import math
import scipy.io.wavfile as waves
import matplotlib.pyplot as plt
import scipy.fftpack as fourier
from scipy.io import wavfile
import librosa
import librosa.display
import json


# creando un sistema de intentos para el sistema que descubre es un for 
iteracion_i = 1
# regla No j = no hay cajas solo gaussianas no existe el no absoluto
valor = 0.0001
result = 1

valori= 0
X = 1


while result == 1 :
	operación = (iteracion_i*valor) + valori**X
	if operación < 0 : # aqui se define el WOW que es el wow define el WOW  parametrizalo para detectarlo e.g. en redes 
						# sociales el wow es un alto view,, likes y seguidores
						# el wow en musica puede ser un integrante en especial ya que hay muchos que cantan bien 
						# pero ademas te ves bien? ademas eres joven? ademas es buena tu musica? 
		result = 100 # you got it now deep in 
	else: 
		result = 1 # always try again just change the value of valor ITERACIONES SIN CASTIGO PARAN HASTA ENCONTRAR RESULTADOS 
					# solo cambian parametros de valor y estructura/forma	nos movemos a traves de las gausianas
		iteracion_i + 1
		valor = 0.00002 # we are a infinite gaussian
		valori = valori +1		# cambio de estructura
		if iteracion_i > 1000: 	# estre al loop de la locura? hacer un cambio fuerte en la estructura
			x = x+1
   
	iteracion_i = iteracion_i +1

  
			