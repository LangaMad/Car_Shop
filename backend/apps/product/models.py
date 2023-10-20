from PIL import Image
from django.db import models


# Create your models here.
TRANSMISSION_CHOICE = (
    ('Автомат','Автомат'),
    ("Механика","Механика"),
    ("Вариатор","Вариатор")
)
ENGINE_CHOICE = (
    ('Дизель','Дизель'),
    ("Гибрид","Гибрид"),
    ("Бензин","Бензин"),
    ("Электро","Электро"),
    ("Газ","Газ")
)
VILE_SIDE_CHOICE = (
    ('Леворульный','Леворульный'),
    ("Праворульный","Праворульный")
)
CONDITION_CHOICE = (
    ("Новое","Новое"),
    ("Старое","Старое"),
    ("Идеальное","Идеальное"),
    ("Аварийное","Аварийное")
)
class Car(models.Model):
    name = models.CharField("Название машины",max_length=100)
    age = models.DateTimeField("Год выпуска")
    # photo = models.ImageField("Фото", upload_to='media/')
    color = models.CharField("Цвет машины",max_length=100)
    transmission = models.CharField("Выбор трансмиссии", choices=TRANSMISSION_CHOICE,
            default='Механика',max_length=10)
    price = models.DecimalField('Цена',decimal_places=2,max_digits=10)
    engine = models.CharField('Вид двигателя', choices=ENGINE_CHOICE,
                              default="Бензин",max_length=50)
    volume = models.DecimalField("Обьем двигателя",decimal_places=2,
                                 max_digits=10)
    vile_side = models.CharField("Расположение руля", choices=VILE_SIDE_CHOICE,
                                 default="Леворульный",max_length=50)
    mileage = models.DecimalField("Пробег",decimal_places=2,
                                  max_digits=10)
    condition = models.CharField("Состояние", choices=CONDITION_CHOICE,
                                 default="Нет",max_length=50)

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'


    def __str__(self):
        return self.name
class CarImage(models.Model):
    car = models.ForeignKey(Car,on_delete=models.CASCADE,related_name='photos')
    photo = models.ImageField(upload_to="media/")

    def save(self, *args, **kwargs):
        super(CarImage, self).save(*args, **kwargs)
        img = Image.open(self.photo.path)
        if img.height > 1125 or img.width > 1125:
            img.thumbnail((1125, 1125))
        img.save(self.photo.path, quality=70, optimize=True)

    class Meta:
        verbose_name = 'Фото машины'
        verbose_name_plural = 'Фото машин'




