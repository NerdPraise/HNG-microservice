"""PageTester URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.documentation import include_docs_urls
from landingPageTester import views as LPT_views
from django.urls import path, re_path

schema_view = get_schema_view(
    openapi.Info(
        title='Landing Page Tester',
        default_version='v1',
        description='Microservice for Testing Landing Pages',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email='contact@snippets.local'),
        license=openapi.License(name='BSD License')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
	path('v1/', include('landingPageTester.urls')),
    # path('', LPT_views.index, name='index'),
    # path('add_page/', LPT_views.add_page, name='add_page'),
    # path('get_status/', LPT_views.get_status, name='get_status'),
    # path('landingpagetester/', LPT_views.TestPage, name='testPage'),
    # path('delete_page/<int:pk>/', LPT_views.delete_page, name='delete_page'),
    # path('manage/<int:pk>/', LPT_views.manage, name='manage'),
	# path('edit_url/', LPT_views.edit_url, name='edit_url'),
	# path('get_url/<int:pk>/', LPT_views.get_url, name='get_url'),
    # path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^v1/documentation(?P<format>\.json)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', include_docs_urls(title='Landing Page Tester', description=
    """Microservice for Testing Various Landing Pages.Testing is simple,
    register below in the /v1/register/ or using httpie using the command http post then go to /api-token-auth below to get your token or alternatively
    via the Command line  '/api-token-auth/ username=   password= ' using httpie via the command http post.Testing can be done here 
    or via a testing tool like Postman or via the Command Line using httpie.
    If testing via Postman add your Token to the header Key = Authorization,Value = Token <your token>.
    If testing using httpie always add 'Authorization: Token <your token>' after each end point.
    To test here go to Authentication in the side bar ,click on token. Fill in the Bearer field with 'Token' then the API key field with your generated token.
    You are good to go.
    """
    ,permission_classes=(permissions.AllowAny,)))
]
