from django.db import models



class Farmer(models.Model):
    fid        = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length  = 100)
    last_name  = models.CharField(max_length  = 100)
    username   = models.CharField(max_length  = 100, unique=True)
    password   = models.CharField(max_length  = 100)
    call       = models.IntegerField(null     = True,blank = True)

    def __str__(self):
        return f'{self.fid} ชื่อ {self.first_name} นามสกุล {self.last_name} username: {self.username} password: {self.password} เบอร์โทรศัพท์ {self.call}'

class Ownermill(models.Model):
    oid         = models.AutoField(primary_key = True)
    first_name   = models.CharField(max_length = 100)
    last_name    = models.CharField(max_length = 100)
    username     = models.CharField(max_length = 100, unique=True)
    password     = models.CharField(max_length = 100)
   
    def __str__(self):
        return f'{self.oid} ชื่อ {self.first_name} นามสกุล {self.last_name} username: {self.username} password: {self.password} '        


class Mill(models.Model):
    mid    = models.AutoField(primary_key = True)
    name   = models.CharField(max_length  = 100)
    lat       = models.FloatField(null    = True, blank = True, unique=True)
    lng       = models.FloatField(null    = True, blank = True, unique=True)
    ownermill = models.ForeignKey(Ownermill,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return f'{self.mid} - โรงสี - {self.name}  - ละติจูด - {self.lat} ลองจิจูด - {self.lng} เจ้าของโรงสี {self.ownermill}'


class Queue(models.Model):
    qid       = models.AutoField(primary_key = True)
    mill      = models.ForeignKey(Mill,on_delete=models.CASCADE,default=1)
    farmer    = models.ForeignKey(Farmer,on_delete=models.CASCADE,default=1)
    queue     = models.IntegerField(null     = True, blank = True)

    def __str__(self):
        return f'{self.qid} - คิวที่ {self.queue} - ชื่อชาวนา {self.farmer} - โรงสี {self.mill} '

class Price(models.Model):
    pid    = models.AutoField(primary_key = True)
    mill   = models.ForeignKey(Mill,on_delete=models.CASCADE,default=1)
    farmer = models.ForeignKey(Farmer,on_delete=models.CASCADE,default=1)
    price  = models.IntegerField(null     = True, blank = True)
    sprice = models.IntegerField(null     = True, blank = True)

    def __str__(self):
        return f'{self.pid} - ราคาข้าวหอมมะลิ {self.price} -ราคาข้าวเหนียว {self.sprice} ชื่อ {self.farmer} - โรงสี - {self.mill}'





# class Map(models.Model):
#     lid       = models.AutoField(primary_key = True)
#     ownermill = models.ForeignKey(Ownermill,on_delete=models.CASCADE,default=1)
#     lat       = models.FloatField(null    = True, blank = True, unique=True)
#     lng       = models.FloatField(null    = True, blank = True, unique=True)

#     def __str__(self):
#         return f'{self.lid}  ละติจูด {self.lat}  ลองจิจูด {self.lng} ชื่อ {self.ownermill}'


