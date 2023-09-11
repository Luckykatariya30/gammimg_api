from django.contrib import admin
from .models import *
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','task_code','task_number','task_name','video_link']
    search_fields = ['task_name']
admin.site.register(Tasks, TaskAdmin)

class LevelAdmin(admin.ModelAdmin):
    list_display = ['id','level_number','level_code','level_name','discount','price','game']
    search_fields = ['level_number',]
admin.site.register(Level, LevelAdmin)


class GamesAdmin(admin.ModelAdmin):
    list_display = ['id','game_name','membership_price','age_group',]
admin.site.register(Games,GamesAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display= ['id','name','contact','email','gender','parent_contact','school_name','class_semester','is_captain','join_date','updated']
    search_fields = ['name',]
admin.site.register(Student, StudentAdmin)