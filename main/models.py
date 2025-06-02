from django.db import models
from django.urls import reverse_lazy, reverse

# Create your models here.


class Net(models.Model):
    name = models.CharField(verbose_name="Назва", max_length=500)
    c_name = models.CharField(default='net', editable=False)
    description = models.TextField(verbose_name="Опис", max_length=5000, blank=True, null=True)
    price_m = models.IntegerField(verbose_name="Ціна за метр")
    price = models.IntegerField(verbose_name='Ціна за встановлення')
    image = models.ImageField(verbose_name='Фото', upload_to='main/nets/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(self.c_name, args=[self.id])

    class Meta:
        verbose_name = 'Москітна сітка'
        verbose_name_plural = 'Москітні сітки'


class Fabric(models.Model):
    name = models.CharField(verbose_name='Назва',max_length=500)
    c_name = models.CharField(default='fabric', editable=False)
    description = models.TextField(verbose_name='Опис', max_length=5000, blank=True, null=True)
    price_m = models.IntegerField(verbose_name='Ціна за метр')
    image = models.ImageField(verbose_name='Фото', upload_to='main/fabrics/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(self.c_name, args=[self.id])

    class Meta:
        verbose_name = 'Тканина'
        verbose_name_plural = 'Тканини'


class Rolet(models.Model):
    name = models.CharField(verbose_name='Назва', max_length=500)
    c_name = models.CharField(default='rolet', editable=False)
    description = models.TextField(verbose_name='Опис', max_length=5000, blank=True, null=True)
    price_m = models.IntegerField(verbose_name='Ціна за метр', default=0)
    price = models.IntegerField(verbose_name='Ціна')
    fabric = models.ManyToManyField(Fabric, verbose_name='Доступні тканини')
    image = models.ImageField(verbose_name='Фото', upload_to='main/rolets/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(self.c_name, args=[self.id])

    class Meta:
        verbose_name = 'Ролет'
        verbose_name_plural = 'Ролети'


class Worker(models.Model):
    name = models.CharField(verbose_name="Ім'я", max_length=200)
    photo = models.ImageField(verbose_name='Фото', upload_to='main/workers')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Працівник'
        verbose_name_plural = 'Працівники'


class WorkerImage(models.Model):
    work_picture = models.ImageField(verbose_name='Фото', upload_to='main/workers_work')
    worker = models.ForeignKey(Worker, verbose_name='Працівник', on_delete=models.CASCADE)

    def __str__(self):
        return self.work_picture.url

    class Meta:
        verbose_name = 'Фото роботи'
        verbose_name_plural = 'Фото роботи'


class WindowType(models.Model):
    name = models.CharField(verbose_name='Назва', max_length=1000)
    price = models.IntegerField(verbose_name='Ціна')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип вікна'
        verbose_name_plural = 'Типи вікон'


class WindowColour(models.Model):
    name = models.CharField(verbose_name='Назва', max_length=1000)
    price = models.IntegerField(verbose_name='Ціна')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Колір вікна'
        verbose_name_plural = 'Кольори вікон'
