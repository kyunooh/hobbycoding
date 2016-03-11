from django.conf import settings
from django.db import models
from django.utils import timezone


class Meetup(models.Model):
    # 관계
    # TODO: related_name이 뭐지
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'주최자', related_name='my_meetup')
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name=u'관심', blank=True, related_name='liked_meetup')

    # 정보
    title = models.CharField(u'제목', max_length=200)
    desc = models.TextField(u'설명')
    image_file = models.ImageField(u'썸네일', upload_to='%Y/%m/%d')
    created_date = models.DateTimeField(
        u'생성일', default=timezone.now)
    modified_date = models.DateTimeField(
        u'수정일', blank=True, null=True)

    def modify(self):
        self.modified_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
