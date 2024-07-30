from django.db import models

# 모델링 & 스키마 정의
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # *auto_now_add = True : 실제로 작성한 시점을 자동으로 입력
    # *auto_now : 수정된 시간 정보를 자동으로 반영


