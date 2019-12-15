from django.db import models

class Mill(models.Model):
    mid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField(null=True,blank=True)
    sprice = models.IntegerField(null=True,blank=True)
    score = models.IntegerField(null=True,blank=True)
    lat = models.CharField(max_length=100, default=None)
    lng = models.CharField(max_length=100, default=None)

    def __str__(self):
        return f'{self.mid} - {self.name} โรงสี {self.price} ราคข้าวเหนียว  {self.sprice}  {self.score} '

class Farmer(models.Model):
    fid = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    call = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return f'{self.fid} ชื่อ {self.first_name} นามสกุล {self.last_name} email: {self.email} เบอร์โทรศัพท์ {self.call}'

# class User(models.Model):
#     uid = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     usertype = models.ForeignKey(Usertype, on_delete=models.CASCADE)
#     # usertype = models.ForeignKey(Usertype, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.username} {self.name} {self.usertype}'

