from .models import identif
from rest_framework import viewsets, permissions, status
from .serializers import identifSerializer
from rest_framework.response import Response
from .testing import analyze
from django.http import JsonResponse
import json


class MaterApiViewSet(viewsets.ModelViewSet):
    queryset = identif.objects.all()  
    permission_classes = [permissions.AllowAny] #cuando ya se tenga que autenticar el ususario la linea de codigo queda como:  permission_classes = [permissions.IsAuthenticated]  
    serializer_class = identifSerializer
    # return Response('holaaaaaaaa')
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        # Obtener el último registro insertado
        last_inserted_instance = identif.objects.latest('id')
        
        # Procesar el archivo y obtener la solución
        # Acceder al campo 'file' del último registro y procesarlo
        solucion = self.process_file(last_inserted_instance.file)

        # Actualizar el campo 'result' en el modelo con la solución obtenida
        last_inserted_instance.result = solucion
        last_inserted_instance.save()

        # Incluir 'solucion' en la respuesta
        response_data = solucion 
        # {
        #     'serializer_data': serializer.data,
        #     'solucion': solucion
        # }
        
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def process_file(self, file):
        # Aquí va tu lógica personalizada para procesar el archivo
        #-- archivo='media/CatorceHomero_ZVVaGRt.wav'
        # Suponiendo que 'archivo' es una instancia de FieldFile
        ruta_archivo = file.path
        ruta_archivo_str = str(ruta_archivo)
        solucion = analyze(ruta_archivo_str)
        # print(f"Procesando el archivo TXT: {archivo}")
        # print(f"Tipo de variable 'archivo': {type(archivo)}")
        # print(f"Procesando el archivo PORC: {file}")
        # print(f"Tipo de variable 'file': {type(file)}")
        print(f"Análisis ressultadooo: {solucion}")
        return solucion

        # nos quedamos en que el resultado se despliegue en una url
        