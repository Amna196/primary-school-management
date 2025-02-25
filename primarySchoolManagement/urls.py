"""
URL configuration for primarySchoolManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


# schema_view = get_schema_view(
#     openapi.Info(
#         title="Your API Title",
#         default_version='v1',
#         description="Your API Description",
#         # ... other info

#         # Security definition inside openapi.Info
#         securityDefinitions={  # Note the "s" here
#             "Bearer": {  # Simpler name
#             "type": "apiKey",
#             "name": "Authorization",  # Must be "Authorization"
#             "in": "header"
#             }
#         },
#     ),
#     public=True,  # Set to False for production
#     permission_classes=(permissions.AllowAny,),  # Or your custom permission class for production
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Homework.urls')),

     # Swagger/Redoc URLs (These are the new additions)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
