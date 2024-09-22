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


def analyze(archivo):

	samplingFrequency, signalData = wavfile.read(archivo)
	y, sr = librosa.load(archivo)
	n_fft = 2048								
	n_mels = 128

	# Preparando la señal
	fsonido, sonido = waves.read(archivo)
	sonido = sonido[:,0].copy()

	n = len(sonido)
	normalizado = []

	for x in range(0,n):
		normalizado.append(sonido[x]/30000)

	# ABSULUTO
	Absoluto = []

	for x in range(0,n):
		Absoluto.append(abs(normalizado[x]))

	n= len(normalizado)
	norm = np.array([])
	norm = normalizado

	# CARACTERÍSTICAS EN TIEMPO  Energía y RMS

	N = len(Absoluto)
	energyt = 0
	for x in range(0,N):
		plus = (Absoluto[x])**2
		energyt = energyt + plus

	RMSx = math.sqrt(energyt/(N**2))

	RMSx_T = RMSx	
	Energy_T = energyt

	#CARACTERISTICAS EN LA FRECUENCIA
	n = len(norm)
	frec = np.fft.fftfreq(n)
	mascara = frec > 0 

	#señal 
	fft_valores = np.fft.fft(norm)
	ab1 = (1/n)*np.abs(fft_valores)

	# Centroide Espectral
	CCentroide = np.sum(frec[mascara]*ab1[mascara])/np.sum(ab1[mascara])

	mel = librosa.filters.mel(sr=sr, n_fft=n_fft, n_mels=n_mels)

	abi = ab1[mascara]

	def functionHl(frecuencia):
		Hl = 0
		frecuencia = frecuencia
		f = []
		idxs_to_plot = [0, 9, 49, 99, 127]
		for i in idxs_to_plot:
			f = mel[i]
			for x in range(0,len(f)):
				if x+1 == frecuencia:
					Hl = f[x]
					break
			if Hl != 0:
				break
		return(Hl)

	N = len(frec[mascara])
	freci = frec[mascara]

	AnchoBanda = 1030
	FrstSuma = 0
	for x in range(0,AnchoBanda):	 
		Hl = functionHl(x)
		plus = abi[x]*Hl
		FrstSuma = FrstSuma + plus

	FrstSuma = math.log10(FrstSuma)

	N = len(freci)
	DCT = 0
	for x in range(0,N):
		plus = (freci[x] *math.cos(3.1416/(N*(x+0.5))))*FrstSuma
		DCT = DCT + plus	

	MFCC_T = abs(DCT)


	print('******************time******************')
	print('RMSx =', RMSx_T)
	print('Energy = ', Energy_T)
	print('******************frequencies******************')
	print('MFCC = ', MFCC_T)
	print('Centroide = ', CCentroide)


	def prediction(proof):

		# prueba Sr BURNS dieciOCHO  NEW
		RMSxPRUEBA = proof[0]
		EnergiaPRUEBA =  proof[1]
		MFCCPRUEBA = proof[2]
		CentroidePRUEBA = proof[3]

		####################### INSERTAR CONSULTA A  JSON #####################
		#BART -> cero RMSx > pixeles ;   energia > Varianza    ;     MFCC > A1   ;  Centroide > A2"""
		# RMSxBart = [4113, 4268, 3883, 3592, 3894, 4213, 4491, 4612, 4278, 4696, 3924, 3924, 3955, 4231, 3969]
		# EnergiaBart = [512.8444405624948, 284.58144211433523, 326.1945706371191, 1625.7354863514036, 929.6193932355931, 664.2818361768308, 585.937158862396, 297.4820672755625, 377.4424720578566, 206.2094500247737, 492.17220142494875, 442.59640831758026, 553.2598758092217, 466.51679151586546, 1341.3623437499996]
		# MFCCBart = [62.560853218292664, 64.98187510298237, 57.239473329438724, 41.617984092032536, 56.12539133300379, 62.11709282643539, 69.00942195059842, 69.6628918947258, 67.34297997273775, 72.91900717506253, 58.115759672853095, 60.33081681870609, 60.31396515825582, 62.11522041971869, 58.2580625833221]
		# CentroideBart = [12.730493266825446, 12.522656121272037, 14.299570095417847, 18.136131457930766, 16.334876196467892, 13.878278584160936, 10.135337557482886, 9.661618658158451, 11.191374945700206, 10.393729684387123, 13.758444554292305, 13.38396321095283, 13.230425860183646, 10.936727632229362, 15.372459144085441]

		RMSxBart = [0.00018329979767715355, 0.00018116778731912137, 0.00019118560279751624, 0.00019653234778635963, 0.00017730695929158208, 0.00021073382228239306, 0.000154655408770606, 0.00023091444947967546, 0.000184514277545585, 0.00019458089800099447, 0.00018371397917486086, 0.00033997637292114673, 0.00018274902949877274, 0.00016620746189279677, 0.00026255838504634586]
		EnergiaBart = [1947.6974765757207, 1523.1761522233764, 1304.6770520577008, 1361.9095070478259, 1351.7660422968488, 996.0018650954887, 743.0500131810958, 1141.3389003289465, 556.6867312877805, 630.2914417655624, 756.9654728110764, 885.9916221344104, 856.3370160488621, 858.2006812177403, 1147.6059424199682]
		MFCCBart = [121374.94708254383, 111531.56376956026, 100748.32774782703, 96911.49496421714, 104572.74206885681, 79943.21245762288, 85808.04655545321, 78949.92949946548, 61112.25157966995, 65380.39484413915, 73020.88915689105, 46603.80946342153, 75966.17350572492, 91296.3240916312, 68409.36608085265]
		CentroideBart = [0.04470434886146516, 0.040506359735379145, 0.08463694844175307, 0.07599770024017719, 0.07430384241924926, 0.07808903442947589, 0.10071504664531884, 0.07688713800039153, 0.08491011148694834, 0.09305062679080346, 0.06226242391034769, 0.1001643498476496, 0.0970422805194362, 0.07517853237359384, 0.06713780897240625]

		
		# HOMERO -> uno  RMSx > pixeles ;   energia > Varianza    ;     MFCC > A1   ;  Centroide > A2
		# RMSxHomero = [3296, 1739, 3221, 3121, 2187, 1887, 1635, 1798, 1579, 2467, 2023, 2216, 2426, 3153, 1977]
		# EnergiaHomero = [2134.1388888888882, 2666.6703601108034, 1155.0571525577204, 997.5991709183688, 4579.591220850479, 5040.705621301775, 2182.27734375, 3521.734375, 3.1358024691358026, 2299.374755859375, 2123.8732638888896, 678.9165023011179, 1323.311120366514, 1362.5042735042712, 6266.6336]
		# MFCCHomero = [42.36320196527809, 17.62683683098908, 39.863538998487094, 44.95461286118726, 26.49642744798454, 24.783175302206445, 16.43036893901946, 20.38676433140101, 13.681675878907713, 39.31492383049476, 25.921598585958446, 27.876391198190507, 30.054000209709553, 41.25660959570994, 20.98406207402747]
		# CentroideHomero = [8.02139037433155, 8.2011414191345, 12.852199703410776, 11.406701718120404, 7.081442202549469, 9.779580281310386, 8.045731661648617, 11.236312706900943, 4.006950373732381, 9.223475486451266, 8.547536661723512, 9.79643194176066, 9.275902874518792, 11.421680971853982, 3.9357989184978805]

		RMSxHomero = [0.00031406356771222316, 0.00024116512146829075, 0.00027152829798202067, 0.00020199980000117104, 0.00014579748509562754, 0.0001817476147970546, 0.00024471518143457223, 0.0001834712645669919, 0.000243908315862514, 0.0002552642765396076, 0.0002504575474573831, 0.0002042555613213597, 0.0003055392564060554, 0.00015006175197009977, 0.0001848485998771762]
		EnergiaHomero = [923.6313175111222, 1622.818533287854, 939.6958399666279, 2456.7787327791825, 2998.059335513808, 2179.9780677847716, 1343.1158925166867, 2530.433805531163, 789.5109779944112, 1818.1137209802027, 1120.1835319378467, 1417.4008978333247, 1874.343610000006793, 1317.9033826955708, 1234.5400324734194]
		MFCCHomero = [39757.73016175888, 77509.06536193876, 51566.85776865138, 130324.4491023485, 214881.2126227047, 126974.76575988851, 72243.94671776603, 145044.0087896247, 57000.65506598271, 79959.42181153351, 58908.199172700784, 87960.17864583364, 63432.95974211959, 122588.9224250274, 90877.74907554741]
		CentroideHomero = [0.050093302827707915, 0.04240378872718643, 0.033645475624829356, 0.04208578963313535, 0.04930338833454074, 0.03630975716823465, 0.04124970865715199, 0.03780383209005141, 0.041457113544353406, 0.04178148137042915, 0.0404961732646661, 0.057479957417729065, 0.036605016046618914, 0.05683204391172659, 0.04833459866081245]

		# LISA -> dos  RMSx > pixeles ;   energia > Varianza    ;     MFCC > A1   ;  Centroide > A2
		# RMSxLISA = [3438, 3823, 3628, 2981, 3170, 3194, 3124, 3794, 2834, 3874, 3168, 2985, 3057, 3382, 3564]
		# EnergiaLISA = [407.8350634371399, 279.3059573002753, 292.3225806451613, 603.109375, 332.5144888888888, 518.9954086317721, 525.9620761451514, 335.8983214587611, 211.42512783053326, 265.9180203686559, 551.5246876859014, 229.9631469315815, 236.2674072604642, 312.5070888468808, 313.21338002656677]
		# MFCCLisa = [60.57422969187675, 60.76708758369658, 59.574364505160354, 55.093695232103535, 50.40144400005992, 57.74315073623032, 57.27317665033928, 58.574499318443955, 48.42418250722749, 63.69927650204467, 54.59750745217873, 51.487439895744394, 51.706511481597985, 58.55952006471038, 54.51512155664405]
		# CentroideLisa = [10.081037762698662, 11.056561662097995, 9.867583396995162, 8.29288934825267, 8.611198490091224, 8.482002426639104, 8.053221288515406, 13.6910379124912, 7.397878937671325, 11.386105244236733, 6.515975374106862, 8.596219236357644, 7.826660075795024, 10.773828247876692, 12.088257762998248]
		
		RMSxLISA = [0.00011873432080843139, 0.0001342310390142828, 0.0001888507392910021, 0.0002457785119012098, 0.00022005592871048667, 0.00019499392105066005, 0.00020845845466839545, 0.00023907311029266153, 0.00014058170102509648, 0.00017409194755541976, 0.0002638645276383354, 0.00017999177740239355, 0.0001715015670900869, 0.000264956814764859, 0.00014349708983740384]
		EnergiaLISA = [592.7854119555408, 927.9900382666177, 1619.891003933503, 450.9364128677889, 1069.4254773699643, 775.8727042022073, 1051.021313425493, 1444.5234428511128, 868.7710129777586, 953.9020174977557, 683.3825438055663, 980.3116954832941, 949.92723726988, 510.1743102366901, 312.8662383666862]
		MFCCLisa = [108826.88664782482, 134371.8597978798, 110507.59049797419, 38047.0347431434, 73943.87457537751, 69566.11332683297, 72440.66052927791, 84666.0077656647, 116253.35416971991, 98389.33799997905, 47109.920802017165, 92757.11821604084, 86941.3606406817, 43089.20977235213, 64076.92501155543]
		CentroideLisa = [0.054084918828252816, 0.0519328015560478, 0.05752194770535806, 0.05306387770770755, 0.05549995006887041, 0.062030216406721066, 0.04830303802001077, 0.045113835343235514, 0.07563252838811675, 0.05940953017032936, 0.05790825841719239, 0.053686729655184964, 0.056140822579464525, 0.06180497510291182, 0.08165087024258533]

		# MARCH -> tres RMSx > pixeles ;   energia > Varianza    ;     MFCC > A1   ;  Centroide > A2
		# RMSxMARCH = [3788, 4247, 3813, 3329, 2726, 2852, 3007, 4144, 3672, 3779, 3086, 3251, 3953, 3519, 3760]
		# EnergiaMARCH = [152.12596183441062, 380.2167570153061, 308.7646484375, 734.7601666336046, 598.9576331360945, 654.7752525252525, 367.04470742932284, 107.19454056132261, 111.81422042725053, 209.09215219976218, 341.12437499999993, 297.98109374999984, 161.54827880859375, 151.95612188365666, 145.54093651249642]
		# MFCCMarch = [60.67721206129511, 67.62196857352566, 65.84318219266316, 59.78594646414716, 53.346739765424886, 55.256594616456205, 57.1121496727033, 64.35087403945535, 60.813897751614014, 61.946703815215926, 59.78781887086385, 59.88892883356551, 56.316376818106924, 59.10813523270271, 59.07817672523555]
		# CentroideMarch = [11.378615617369942, 9.114875896882817, 6.894201530879732, 6.9410116987971655, 4.928174478347489, 5.092946269416857, 5.645306250842583, 12.726748453392052, 9.264668434218606, 10.818766009077427, 5.444958732155964, 6.901691157746521, 13.430773378870265, 10.46862595305502, 9.891924684312228]
		RMSxMARCH = [8.024098471134326e-05, 7.691658436506191e-05, 0.00010432839537212521, 0.00014382371820042796, 0.00016594222992145203, 0.0001699753205904926, 0.00017341405109816847, 0.00014566783628784777, 0.00017548215949991496, 0.00021865229802625643, 0.00018015279437190196, 0.0001389128814305196, 0.00015711131182467877, 0.0001946260588496545, 0.00018307418881187898]
		EnergiaMARCH = [486.2087779945012, 441.00308825224647, 329.35473253889126, 1661.2546006824366, 543.9243020766224, 1284.0409538910696, 971.2314174944028, 1313.8318904588978, 871.1172428198894, 1088.8188771144678, 893.1243872477048, 1065.73770910451, 817.7753993087605, 836.5393131443782, 598.5151852510904]
		MFCCMarch = [151032.72506868505, 156505.28354748437, 90636.88259024186, 147400.54661993947, 64375.003515113094, 101740.3276196617, 86215.82642857944, 125085.27938168094, 87074.28353095936, 75744.04630851124, 85849.75106735347, 115669.89161403352, 92604.42032694971, 72285.32497916897, 62268.61038135746]
		CentroideMarch = [0.04514438141360031, 0.04889282405687871, 0.04567338759136619, 0.047812114334660594, 0.035738424355574686, 0.04276456281842144, 0.04269963600908998, 0.045171916432901575, 0.04097111779115785, 0.04717531018665366, 0.03702338996269164, 0.043400826769119924, 0.039260095078003106, 0.03819061079749126, 0.04240758555401088]

		# BURNS -> cuatro RMSx > pixeles ;   energia > Varianza    ;     MFCC > A1   ;  Centroide > A2
		# RMSxSrBURNS = [3009, 3320, 3386, 2943, 3153, 2675, 2742, 3318, 3035, 3870, 3167, 3335, 3054, 3185, 3801]
		# EnergiaSrBURNS = [2060.707429322814, 2185.3012048192772, 1761.367687617942, 1721.2460547910612, 2213.6866448542523, 1668.6278659611992, 1366.5528007346186, 1867.5436628745395, 1151.21, 541.3556632653057, 1671.4410666666663, 2259.1376133786844, 2558.123858320338, 387.63959262688337, 822.5998891966759]
		# MFCCSrBurns = [43.32187420422714, 42.557932263814614, 40.78101828966881, 36.15991851285969, 47.12098743240612, 38.59779205799967, 37.26838328914454, 44.48838358872961, 41.89322787938705, 48.28749681690858, 46.18478407405743, 40.88025584565377, 46.317724950942946, 42.32013661079405, 45.70357554786621]
		# CentroideSrBurns = [9.949969292529847, 12.576955916056262, 15.408034871702691, 11.97216854656301, 10.601566829940532, 11.393594871103522, 15.833071196392996, 12.573211102622867, 14.286463248400965, 15.657064965023443, 13.820233975943319, 16.379813957668627, 11.4085741248371, 12.648107371290763, 14.34638026333528]
		RMSxSrBURNS = [0.00027545321886987887, 0.0002443592459102337, 0.00029328973903772307, 0.00019579621638780067, 0.00023547241814242135, 0.00028151113826582313, 0.00033138530196992667, 0.0002165495542055594, 0.0002337163079640073, 0.00023146620720850336, 0.00025263314728577997, 0.0002965476520191653, 0.00017670200217919174, 0.00027052786645989597, 0.0003250040012045291]
		EnergiaSrBURNS = [1746.551401734617, 2618.1987497331925, 2113.127562307925, 1215.3389722211316, 2656.3925132221607, 2032.0094546002215, 1428.373655538964, 2692.441129210988, 1116.1018277566743, 1920.6206160867985, 3776.565967257659, 1075.564362003366, 2976.168303744433, 2066.0744906890545, 1727.7915247145138]
		MFCCSrBurns = [67046.45629813893, 100001.32960732405, 77697.27927316152, 85605.90700074518, 112829.0468244683, 72469.03616686462, 52718.11256536594, 113904.52210234755, 61867.44427485746, 84081.98779403983, 108800.05448513637, 49493.2857139087, 165187.55741895913, 78783.19361836811, 62589.81007078671]
		CentroideSrBurns = [0.08228177113692889, 0.08467104789890423, 0.06767709471664524, 0.07563207949236266, 0.06227825536891714, 0.07394139375601905, 0.08186796921827849, 0.07738082233910842, 0.08164217853985663, 0.07377244428289663, 0.07633175842073599, 0.09461267298963054, 0.06861959472674121, 0.08142781782303486, 0.08392860571403778]

		########### ------ BRAIN ------

		########### ------ BRAIN ------


		####################### INSERTAR CONSULTA A  JSON #####################


		long_finger = len(RMSxBart)
		num_personas = 5
		LabelNombres = ["Bart","Homero","Lisa","March","SrBurns"]

		string_s_rms = [RMSxBart,RMSxHomero,RMSxLISA,RMSxMARCH,RMSxSrBURNS]
		string_s_energia = [EnergiaBart,EnergiaHomero,EnergiaLISA,EnergiaMARCH,EnergiaSrBURNS]
		string_s_mfcc = [MFCCBart,MFCCHomero,MFCCLisa,MFCCMarch,MFCCSrBurns]
		string_s_centroide = [CentroideBart,CentroideHomero,CentroideLisa,CentroideMarch,CentroideSrBurns] 


		# pre-procesamiento de los datos para su analisis: normalización

		def apendizar(string_s,string_s_prueba):
			resultado = []
			longitud = len(string_s)
			for i in range(0,longitud):	
				#consulta de operación por ID
				aux = string_s[i]
				longitud_aux = len(aux)
				#### En Y: Energía
				for j in range(0,longitud_aux):
					resultado.append(aux[j])

			resultado.append(string_s_prueba)

			return resultado

		entrenamiento_Tiempo_X = apendizar(string_s_rms,RMSxPRUEBA)
		max1 = max(entrenamiento_Tiempo_X)

		entrenamiento_Tiempo_Y = apendizar(string_s_energia,EnergiaPRUEBA)
		max2 = max(entrenamiento_Tiempo_Y)

		entrenamiento_Frecuencia_X = apendizar(string_s_mfcc,MFCCPRUEBA)
		max3 = max(entrenamiento_Frecuencia_X)

		entrenamiento_Frecuencia_Y = apendizar(string_s_centroide,CentroidePRUEBA)
		max4 = max(entrenamiento_Frecuencia_Y)

		cnt1 = 1/(max1/100)
		cnt2 = 1/(max2/100)
		cnt3 = 1/(max3/100)
		cnt4 = 1/(max4/100)

		# aplicando la normalizacion

		def aplicando_norm(cnt,string):
			for x in range(0,len(string)):
				string[x] = cnt*string[x]
			return string


		####################### INSERTAR CONSULTA A PERSONAJE POR JSON #####################

		# for i in range(0,num_personas):
		# 	RMS = aplicando_norm(cnt1,RMS)
		# 	Energia = aplicando_norm(cnt2,Energia)
		# 	MFCC = aplicando_norm(cnt3,MFCC)
		# 	Centroide = aplicando_norm(cnt4,Centroide)


		RMSxBart = aplicando_norm(cnt1,RMSxBart)
		EnergiaBart = aplicando_norm(cnt2,EnergiaBart)
		MFCCBart = aplicando_norm(cnt3,MFCCBart)
		CentroideBart = aplicando_norm(cnt4,CentroideBart)

		RMSxHomero = aplicando_norm(cnt1,RMSxHomero)
		EnergiaHomero = aplicando_norm(cnt2,EnergiaHomero)
		MFCCHomero = aplicando_norm(cnt3,MFCCHomero)
		CentroideHomero = aplicando_norm(cnt4,CentroideHomero)


		RMSxLISA = aplicando_norm(cnt1,RMSxLISA)
		EnergiaLISA = aplicando_norm(cnt2,EnergiaLISA)
		MFCCLisa = aplicando_norm(cnt3,MFCCLisa)
		CentroideLisa = aplicando_norm(cnt4,CentroideLisa)


		RMSxLISA = aplicando_norm(cnt1,RMSxLISA)
		EnergiaLISA = aplicando_norm(cnt2,EnergiaLISA)
		MFCCLisa = aplicando_norm(cnt3,MFCCLisa)
		CentroideLisa = aplicando_norm(cnt4,CentroideLisa)

		RMSxMARCH = aplicando_norm(cnt1,RMSxMARCH)
		EnergiaMARCH = aplicando_norm(cnt2,EnergiaMARCH)
		MFCCMarch = aplicando_norm(cnt3,MFCCMarch)
		CentroideMarch = aplicando_norm(cnt4,CentroideMarch)


		RMSxSrBURNS = aplicando_norm(cnt1,RMSxSrBURNS)
		EnergiaSrBURNS = aplicando_norm(cnt2,EnergiaSrBURNS)
		MFCCSrBurns = aplicando_norm(cnt3,MFCCSrBurns)
		CentroideSrBurns = aplicando_norm(cnt4,CentroideSrBurns)



		RMSxPRUEBA = cnt1*RMSxPRUEBA
		EnergiaPRUEBA = cnt2*EnergiaPRUEBA
		MFCCPRUEBA = cnt3*MFCCPRUEBA
		CentroidePRUEBA = cnt4*CentroidePRUEBA








		##############################################################################
		##############################################################################

		def distEuclidiana(instancia11,instancia12,instancia21,instancia22): 
			dE = 0
			contador = 0
			dE = (instancia11 - instancia12)**2 + (instancia21 - instancia22)**2
			return math.sqrt(dE)


		def distancia(Energía,RMS,xPrueba,yPrueba):	
			distancia = []
			longitud = len(Energía)
			for x in range(0,longitud): # para la tongitud total 15*5
				Y2 = Energía[x]
				Y1 = yPrueba
				X2 = RMS[x]
				X1 = xPrueba
				distancia.append(distEuclidiana(Y2,Y1,X2,X1))
			return distancia

		####################################################################			FUNCIONES


			
		def minimosLocales(distancia,Energia,RMS,cnt,k):
			pasos = len(Energia)
			cadenaDePuntos = []
			puntosRMS = []
			puntosEnergia = []
			puntosLabel = []
			label = 0
			longitud = len(distancia)
			maximo = max(distancia)
			cadena = []
			num_perso = round(longitud/cnt)
			cnt = cnt-1
			
			for x in range(0,num_perso):
				cadena.append((cnt*(x+1))+x)
			long_cadena = len(cadena)
			## buscando los 8 minimos = "k"
			for x in range(0,k):
				
				label = 0
				minimo = min(distancia)
				
				for xy in range(0,longitud): # para la tongitud total 15*5 BUSCANDO MIN
					if minimo == distancia[xy]:
						cadenaDePuntos.append(distancia[xy])
						puntosRMS.append(RMS[xy])
						puntosEnergia.append(Energia[xy])
						puntosLabel.append(label)
						distancia[xy] = 100*maximo
						break
					
					for l in range(0,long_cadena):
						aux = cadena[l]
						if xy == aux:
							label = label + 1

			resultado = [cadenaDePuntos, puntosRMS, puntosEnergia,puntosLabel]
			return resultado


		def contadorDeEtiquetas(puntos, numPersonajes):
			etiquetasTotal = []
			lon = len(puntos)
			for x in range(0,numPersonajes):
				cnt = 0 
				for y in range(0,lon):
					if  puntos[y] == x :
						cnt = cnt + 1
				etiquetasTotal.append(cnt)
			return etiquetasTotal

		def suma(t):

			u = len(t)
			sumatoria = 0
			for j in range(0,u):
				sumatoria += t[j]
			return sumatoria

		######   Midiendo confiabilidad en los datos " representandolo con grado de similitud = correlación "
		######   esto con el hecho de que entre más consistencia, coherencia y estabilidad entre los resultados en el análisis en el T y F
		######   podremos confiar más en los resultados "asumiendo" un comportamiento lineal entre estos dos resultados por lo que haremos
		######   el calculo de r = correlación; en este caso correlación de Pearson

		##fórmula  r = (n*sum(xy)-sum(x)*sum(y))/sqrt((n*sum(x^2)-sum(x)^2)*(n*sum(y^2)-sum(y)^2))
			


		def correlacionDePearon(x,y):
			x_dato = x
			y_dato = y
			x_cuadrada_sumatoria = 0
			y_cuadrada_sumatoria = 0
			xy_sumatoria = 0
			x_sumatoria = 0
			y_sumatoria = 0
			# operando correlación
			n = len(x_dato)

			for j in range(0,n):
				x_cuadrada_sumatoria = (x_dato[j])**2 + x_cuadrada_sumatoria
				y_cuadrada_sumatoria = (y_dato[j])**2 + y_cuadrada_sumatoria
				xy_sumatoria = ((x_dato[j])*(y_dato[j])) + xy_sumatoria
				x_sumatoria = x_dato[j] + x_sumatoria
				y_sumatoria = y_dato[j] + y_sumatoria

			ri = ( (n*xy_sumatoria) - (x_sumatoria*y_sumatoria) ) / ( ( ((n*x_cuadrada_sumatoria)-(x_sumatoria**2))*((n*y_cuadrada_sumatoria)-(y_sumatoria**2)) )**0.5)
			return abs(ri) #aplicando absoluto para que el rango de r quede en [0,1]

						# DESCRIPCÓN DE RANGOS: [0,0.4]   correlación MALA
						#						  (0.4,0.7] correlación REGULAR
						#						  (0.7,1]   correlación BUENA 
		#####################################################################################
		#####################################################################################



		def concatenar(strings):
			result = []
			for i in range(0,len(strings)):
				aux = strings[i]
				for j in range(0,len(aux)):
					result.append(aux[j])
			return result

		############## TOTAL TIEMPO ############
		# creando un array de todas las cadenas
		RMSTotal = concatenar(string_s_rms)
		EnergiaTotal = concatenar(string_s_energia)

		############## TOTAL  FRECUENCIA   ############
		CentroideTotal = concatenar(string_s_centroide)
		MFCCTotal = concatenar(string_s_mfcc)


		datos = len(MFCCTotal)
		INICIOdeK = int(round(datos*0.10)) # TOMANDO DEL 10% DEL TOTAL DE DATOS EN EL ANÁLISIS
		FINALdeKMAX = int(round(datos*0.20)) # TOMANDO AL 20% DEL TOTAL DE DATOS EN EL ANÁLISIS

		print("INICIOdeK ", INICIOdeK)
		print("FINALdeKMAX", FINALdeKMAX)

		cadenaCorrelaciones = []	  ### CALCULANDO LA MEJOR CORRELACIÓN DE LOS DATOS   ###

		for iteraciones in range(INICIOdeK,FINALdeKMAX):

			k = iteraciones
			

			distanciaTotal = distancia(EnergiaTotal,RMSTotal,RMSxPRUEBA,EnergiaPRUEBA)
			print("DISTANCIA TOOOOTAL")
			print(distanciaTotal)

			resultado = minimosLocales(distanciaTotal,EnergiaTotal,RMSTotal,long_finger,k)

			tresPuntosTotal = resultado[0]
			puntosRMSTotal = resultado[1]
			puntosEnergiaTotal = resultado[2]
			puntosLabelTimepo = resultado[3]

			#print("ETIQUETAS tiempo ", puntosLabelTimepo)

			distanciaTotalFrec = distancia(MFCCTotal,CentroideTotal,CentroidePRUEBA,MFCCPRUEBA)

			resultadoFrec = minimosLocales(distanciaTotalFrec,MFCCTotal,CentroideTotal,long_finger,k)

			tresPuntosTotalFrec = resultadoFrec[0]
			puntosCentroideTotal = resultadoFrec[1]
			puntosMFCCTotal = resultadoFrec[2]
			puntosLabelFrecuencia = resultadoFrec[3]

			#print("ETIQUETAS frecuencia ", puntosLabelFrecuencia)

			puntosLabel = puntosLabelTimepo + puntosLabelFrecuencia


			LabelTiempo = contadorDeEtiquetas(puntosLabelTimepo,num_personas)
			LabelFrecuencia = contadorDeEtiquetas(puntosLabelFrecuencia,num_personas)
			print("LABEL TIEMPO")
			print(LabelTiempo)
			print("LABEL FRECUENCIA")
			print(LabelFrecuencia)
			
			LabelTotal = contadorDeEtiquetas(puntosLabel,num_personas) # 5 = num. de personajes

			correlacion_R = correlacionDePearon(LabelTiempo,LabelFrecuencia) # 5 = num. de personajes PUEDO HACERLO COMO N = 5 arriba en fin asi lo dejo

			cadenaCorrelaciones.append(correlacion_R)

		print("correlaciones MAX ", cadenaCorrelaciones)

		cadenaCorrelaciones2 = cadenaCorrelaciones

		Nk = int(round(len(cadenaCorrelaciones2)/2))

		cadenaCorrelaciones1 = cadenaCorrelaciones[0:Nk]

		mejorCorrelación1 = max(cadenaCorrelaciones1)
		mejorCorrelación2 = max(cadenaCorrelaciones2)

		print("1     ",mejorCorrelación1)
		print("2     ",mejorCorrelación2)

		if mejorCorrelación2 >= mejorCorrelación1 + 0.1: ## estamos buscando que realmente exista una diferencia notable sino basta con tomar los 15 primeros puntos
			cadenaCorrelaciones = cadenaCorrelaciones2
			mejorCorrelación = mejorCorrelación2
		else:
			cadenaCorrelaciones = cadenaCorrelaciones1
			mejorCorrelación = mejorCorrelación1	

		cadenaCorrelaciones = cadenaCorrelaciones2
		mejorCorrelación = mejorCorrelación2

		print("correlaciones  ", cadenaCorrelaciones)

		######### 2da ETAPA ##############


		# buscando K(correlación)
		Nn = len(cadenaCorrelaciones)

		for j in range(0,Nn):
			if mejorCorrelación == cadenaCorrelaciones[j]:
				break

		k = j + INICIOdeK
		i = k  # llamado de plot legend

		print("K como mejor opcion: ", k)

		Porcentaje = (k*100)/datos 

		print("Porcentaje de los datos tomados para pronostico: ", Porcentaje)

		distanciaTotal = distancia(EnergiaTotal,RMSTotal,RMSxPRUEBA,EnergiaPRUEBA)

		resultado = minimosLocales(distanciaTotal,EnergiaTotal,RMSTotal,long_finger,k)

		tresPuntosTotal = resultado[0]
		puntosRMSTotal = resultado[1]
		puntosEnergiaTotal = resultado[2]
		puntosLabelTimepo = resultado[3]


		distanciaTotalFrec = distancia(MFCCTotal,CentroideTotal,CentroidePRUEBA,MFCCPRUEBA)

		resultadoFrec = minimosLocales(distanciaTotalFrec,MFCCTotal,CentroideTotal,long_finger,k)

		tresPuntosTotalFrec = resultadoFrec[0]
		puntosCentroideTotal = resultadoFrec[1]
		puntosMFCCTotal = resultadoFrec[2]
		puntosLabelFrecuencia = resultadoFrec[3]

		#print("ETIQUETAS frecuencia ", puntosLabelFrecuencia)

		puntosLabel = puntosLabelTimepo + puntosLabelFrecuencia

		LabelTiempo = contadorDeEtiquetas(puntosLabelTimepo,num_personas)
		LabelFrecuencia = contadorDeEtiquetas(puntosLabelFrecuencia,num_personas)

		LabelTotal = contadorDeEtiquetas(puntosLabel,num_personas) # 5 = num. de personajes
		print("lab4l T", LabelTiempo)
		print("lab4l F", LabelFrecuencia)
		correlacion_R = correlacionDePearon(LabelTiempo,LabelFrecuencia) # 5 = num. de personajes PUEDO HACERLO COMO N = 5 arriba en fin asi lo dejo
		print("correlacion como mejor opcion de K: ", correlacion_R)


		explode = np.zeros((num_personas,), dtype=int)
		Max = max(LabelTotal)
		Len = len(LabelTotal)
		for x in range(0,Len):
			if Max == LabelTotal[x]:
				break
		explode[x] = 1


		result =  LabelNombres[x]
  
		print("esto es lo que veo?:", result)

		data = { "resultado": result}
		json_data = json.dumps(data)

		return data

	# print('******************time******************')
	# print('RMSx =', RMSx_T)
	# print('Energy = ', Energy_T)
	# print('******************frequencies******************')
	# print('MFCC = ', MFCC_T)
	# print('Centroide = ', CCentroide)

		# RMSxPRUEBA = proof[0]
		# EnergiaPRUEBA =  proof[1]
		# MFCCPRUEBA = proof[2]
		# CentroidePRUEBA = proof[3]

	resultado = prediction([RMSx_T, Energy_T, MFCC_T, CCentroide])

	print(resultado)

	return resultado



##----- ejecución GRAL

# archivo='media/CincoHomero.wav'

# solucion = analyze(archivo)

# print("esto es lo que sale de analyze::::",solucion)
