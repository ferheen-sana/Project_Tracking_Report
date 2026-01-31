from django.urls import path
from . import views

app_name = 'tracker'
urlpatterns = [
    path('', views.project_list, name='list'),
    path('project/add/', views.project_create, name='add'),
    path('project/<int:pk>/edit/', views.project_edit, name='edit'),
    path('project/<int:pk>/delete/', views.project_delete, name='delete'),
    path('export/csv/', views.export_csv, name='export_csv'),
    path('export/excel/', views.export_excel, name='export_excel'),
    path('api/stats/', views.stats_json, name='stats_json'),
    path('project/update-aircraft/<int:pk>/<str:aircraft>/', views.update_aircraft, name='update_aircraft'),
    path('export/csv/', views.export_csv, name='export_csv'),
    path('export/excel/', views.export_excel, name='export_excel'),
    path('export/pdf/', views.export_pdf, name='export_pdf'),

]
