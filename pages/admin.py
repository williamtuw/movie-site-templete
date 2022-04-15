from django.contrib import admin
from pages.models import *
from django.contrib.sessions.models import Session
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('id', 'uname','pwd','create_time', 'email', 'vip_expiry_time','is_login')
    list_display_links = ("uname",)
    list_per_page = 10
    search_fields = ("id","uname","email","is_login") #搜索字段
    # list_filter = ("uname","id") #过滤器


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('session_key','session_data','expire_date')
    list_per_page = 10
    list_display_links = ('session_key',)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("title","id","post_time","video_url")
    list_per_page = 20
    search_fields = ("title","id")
    date_hierarchy = "post_time"



#设置admin.site title header
admin.site.site_header = "greenweb-admin"
admin.site.site_title  = "greenweb Resource Management System"

