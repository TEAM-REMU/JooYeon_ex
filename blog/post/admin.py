from django.contrib import admin
from .models import * # 모든 모델을 불러옵니다.

admin.site.register(Blog)
admin.site.register(Comment)