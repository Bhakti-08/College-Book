"""djangoProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from djangoProj import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('', include('main.urls'))''
    path('', views.index,name='login'),
    path('logout/', views.logoutPage,name='logout'),
    path('profHome/<str:subID>',views.profHome,name='profHome'),
    path('studentHome/<str:email>',views.studentHome,name='studentHome'),
    path('profRegistrationForm/',views.profRegistrationForm,name='profRegistrationForm'),
    path('studentRegistrationForm/',views.studentRegistrationForm,name='studentRegistrationForm'),
    path('upload_questionBank/<str:subID>',views.upload_questionBank,name='upload_questionBank'),
    path('selectBranch/',views.selectBranch,name='selectBranch'),
    path('selectSubject/<int:branchID>',views.selectSubject,name='selectSubject'),
    path('selectTest/<int:subID>',views.selectTest,name='selectTest'),
    #path('test-subject/',views.test_subject,name='test_subject'), 
    #path('test-question/<int:test_id>',views.test_question,name='test_question'),
    #path('test-question/<int:test_id>/<int:question_id>',views.test_question,name='test_question'),
    #path('test-arranged/',views.test_arranged,name='test_arranged'),
    #path('add-test/',views.add_test,name='add_test'),
    path('addingTest/<str:subID>',views.addingTest,name='addingTest'),    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)