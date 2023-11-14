from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=200, blank=True,
                                   verbose_name='Описание')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    def __str__(self):
        return f'{self.id}: {self.name}'
    

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE,
                                  verbose_name='ID датчика',
                                  related_name='measurements')
    temperature = models.DecimalField(max_digits=4, decimal_places=1,
                                      verbose_name='Температура')
    created_at = models.DateTimeField(auto_now_add=True, 
                                     verbose_name='Дата и время')
    image = models.ImageField(upload_to='images/', 
                              verbose_name='Изображение', blank=True)
    
    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'

    def __str__(self):
        return f'id: {self.sensor_id}, t = {self.temperature}, \
                дата/время: {self.created_at.strftime("%d/%m/%Y, %H:%M:%S")}'