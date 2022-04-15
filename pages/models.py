from django.db import models
from django.utils.html import format_html


# Create your models here.

# uname pwd id email create_time vip_expiry


class User(models.Model):
    uname = models.CharField(max_length=20, unique=True)
    pwd = models.CharField(max_length=16)
    email = models.CharField(max_length=32)
    create_time = models.DateField(auto_now_add=True)
    # 有效时间戳-15e8 以此判断 是不是vip
    vip_expiry = models.IntegerField()
    # 0 root  1 normal
    user_type = models.SmallIntegerField(default=1)
    is_login = models.BooleanField(default=False)

    def __str__(self):
        return self.uname

    #自定义 显示字段 定义函数 返回html显示内容 加入list_display
    def vip_expiry_time(self):
        import time
        color = "green"
        if time.time() > float(self.vip_expiry) + 15e8:
            color = "red"
        return format_html(
            "<span style='color:{};'>{}</span>",
            color,
            self.vip_expiry,
        )

class Video(models.Model):
    post_time = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=128)
    img_link = models.CharField(max_length=256)
    video_url = models.CharField(max_length=256)

    def __str__(self):
        return self.title[:12]


