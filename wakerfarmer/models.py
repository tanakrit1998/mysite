from django.db import models


class Mill(models.Model):
    Millname = models.CharField(max_length=100)
    price = models.IntegerField()
    score = models.IntegerField()

    def _str_(self):
        return f'{self.Millname} โรงสี {self.price} ราคา {self.score} คะแนน'