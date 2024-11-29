from django.db import models
from django.conf import settings

class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscriptions')
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='subscriptions')

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user} подписан на {self.course}"

class Course(models.Model):
    """
    Модель курса
    """
    title = models.CharField(max_length=255, verbose_name="Название курса")
    preview = models.ImageField(upload_to='courses/', blank=True, null=True, verbose_name="Превью")
    description = models.TextField(verbose_name="Описание")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='owned_courses',  # Уникальный related_name для курсов
        verbose_name="Владелец"
    )

    def __str__(self):
        return self.title


class Lesson(models.Model):
    """
    Модель урока
    """
    title = models.CharField(max_length=255, verbose_name="Название урока")
    description = models.TextField(verbose_name="Описание")
    preview = models.ImageField(upload_to='lessons/', blank=True, null=True, verbose_name="Превью")
    video_url = models.URLField(verbose_name="Ссылка на видео")
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='lessons',
        verbose_name="Курс"
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='owned_lessons',  # Уникальный related_name для уроков
        verbose_name="Владелец"
    )

    def __str__(self):
        return self.title
