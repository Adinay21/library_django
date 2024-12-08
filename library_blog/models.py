from django.db import models

class BookModel(models.Model):
    GENRE = (
        ('Ужасы', 'Ужасы'),
        ('Роман', 'Роман'),
        ('Приключения', 'Приключения')
    )
    image = models.ImageField(upload_to="images/", verbose_name="загрузите фото книги")
    title = models.CharField(max_length=100, verbose_name="напишите название книги")
    description = models.TextField(verbose_name="Напишите описание фильма", blank=True)
    price = models.FloatField(verbose_name="укажите цену книги", default=10)
    created_at = models.DateField(auto_now_add=True)
    genre = models.CharField(max_length=100, choices=GENRE, default="Роман")
    time_read = models.TimeField(verbose_name="Укажите длительность аудиокниги", blank=True)
    author = models.CharField(max_length=100, verbose_name="Укажите автора книги", default="А.С.Пушкин")
    audio_book = models.URLField(verbose_name="Укажите ссылку на аудиокнигу")

    class Meta:
        verbose_name = "Книгу"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.title

