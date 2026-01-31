from django.contrib import admin
from .models import Project
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id','project_name','status','aircraft','start_date','end_date')
    list_filter = ('status','aircraft')
    search_fields = ('project_name','brief')
