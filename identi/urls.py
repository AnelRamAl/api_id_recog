# from rest_framework import routers
# from .api  import MaterApiViewSet   
# #aqui se definen las urls por ahora usaremos las del frame work 

# router = routers.DefaultRouter()

# router.register('api/ident',MaterApiViewSet,'ident')

# urlpatterns = router.urls


from rest_framework import routers
from .api  import MaterApiViewSet   
from django.urls import path
# from .views import AudioAnalysisView
from .views import respuesta

router = routers.DefaultRouter()

router.register('api/ident',MaterApiViewSet,'ident')

urlpatterns = router.urls

urlpatterns = router.urls + [
    path('upload/', respuesta)
]
