from django.db import models
import os 
from django.conf import settings 


class Post(models.Model):
    user_id = models.CharField(max_length=30)
    passwd = models.CharField(max_length=50)
    titles = models.CharField(max_length=50)
    contents = models.TextField()
    # 첨부이미지 : null을 허용하는 컬럼으로 생성하고, 작성시 입력이 없어도 된다는 의미
    mainphoto = models.ImageField(blank=True, null=True)


    def __str__(self):
        return self.titles

    def delete(self, *args, **kwargs):
        if self.mainphoto:
            print("이미지 삭제")
            print(settings.MEDIA_ROOT, self.mainphoto.path)
            # 여기서 이미지 삭제
            os.remove(os.path.join(settings.MEDIA_ROOT, self.mainphoto.path)) 
        super(Post, self).delete(*args, **kwargs)