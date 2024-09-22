from django.http import JsonResponse
# import testing
from .testing import analyze
import json

def respuesta(request):
    archivo='media/CatorceLisa.wav'
    solucion = analyze(archivo)
    print('esta sol:::::::::',solucion)
    return JsonResponse(solucion)


# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import identif
# from .serializers import identifSerializer

# # import testing  # Importa tu script de análisis

# # class AudioAnalysisView(APIView):
# #     def post(self, request, *args, **kwargs):
# #         serializer = identifSerializer(data=request.data)
# #         if serializer.is_valid():
# #             audio_file = serializer.validated_data['data']
            
# #             # Llama al script de análisis y obtén el resultado
# #             result = testing.analyze(audio_file)
            
# #             # Crea una instancia de identif y guarda los datos
# #             identif_instance = serializer.save(result=result)
            
# #             # Devuelve una respuesta con el resultado numérico
# #             return Response({'result': result}, status=status.HTTP_200_OK)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # from django.shortcuts import render

# # # Create your views here.
# # # marterapi/views.py
# # # myapp/views.py
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.views import APIView
# # from .models import Masteapi
# # from .serializers import MasterapiSerializer
# import os
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# # import testing

# # class AudioAnalysisView(APIView):
# #     def post(self, request, *args, **kwargs):
# #         serializer = identifSerializer(data=request.data )
# #         if serializer.is_valid():
# #             audio_file = serializer.validated_data['data']
# #             # data = serializer.validated_data['data']
# #             try:
# #                 # Guardar el archivo temporalmente
# #                 temp_file_path = 'temp_audio_file.wav'
# #                 with open(temp_file_path, 'wb') as f:
# #                     for chunk in audio_file.chunks():
# #                         f.write(chunk)

# #                 # Llamar al script de análisis
# #                 result = self.process_audio(temp_file_path)
                
# #                 # Eliminar el archivo temporal
# #                 os.remove(temp_file_path)
                
# #                 # Guardar el archivo y el resultado en la base de datos
# #                 audio_instance = serializer.save(result=result)
                
# #                 return Response({'result': result}, status=status.HTTP_201_CREATED)
# #             except Exception as e:
# #                 return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #     def process_audio(self, file_path):
# #         # Aquí llamamos a tu script de análisis
# #         import testing  # Asegúrate de importar tu script correctamente
# #         print(f"Processing audio file at: {file_path}")  # Debugging line
# #         result = testing.analyze(file_path)
# #         print(f"Analysis result: {result}")  # Debugging line
# #         # result = 42.0  # Valor de ejemplo

# #         return result


# class AudioAnalysisView(APIView):

#     def post(self, request, *args, **kwargs):
#         serializer = identifSerializer(data=request.data)
#         if serializer.is_valid():
#             audio_file = serializer.save()

#             # Llamada al script de análisis
#             result = self.run_analysis(audio_file.file.path)
            
#             # Guarda el resultado en la base de datos
#             audio_file.result = result
#             audio_file.save()
            
#             response_data = serializer.data
#             response_data['result'] = result
            
#             return Response(response_data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def run_analysis(self, file_path):
#         # Llama al script de análisis y captura el resultado
#         import testing
#         result = testing.analyze(file_path)
#         return result.stdout