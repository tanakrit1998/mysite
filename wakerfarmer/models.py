from django.db import models

class Mill(models.Model):
    mid    = models.AutoField(primary_key = True)
    queue  = models.IntegerField(null    = True,blank   = True)
    name   = models.CharField(max_length  = 100)
    price  = models.IntegerField(null     = True,blank   = True)
    sprice = models.IntegerField(null     = True, blank  = True)
    lat    = models.FloatField(null  = True, blank = True)
    lng    = models.FloatField(null  = True, blank = True)
 
    def __str__(self):
        return f'{self.mid} - โรงสี {self.name} คิวที่ {self.queue} ราคาข้าวจ้าว {self.price} ราคข้าวเหนียว  {self.sprice} ละติจูด {self.lat} ลองจิจูด {self.lng}'

class Farmer(models.Model):
    fid        = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length  = 100)
    last_name  = models.CharField(max_length  = 100)
    username   = models.CharField(max_length  = 100)
    password   = models.CharField(max_length  = 100)
    call       = models.IntegerField(null     = True,blank = True)

    def __str__(self):
        return f'{self.fid} ชื่อ {self.first_name} นามสกุล {self.last_name} username: {self.username} password: {self.password} เบอร์โทรศัพท์ {self.call}'


class ScoreLevel(models.Model):
    sid     = models.AutoField(primary_key = True)
    text    = models.CharField(max_length   = 100)
    value   = models.IntegerField()

class Score(models.Model):
    sid     = models.AutoField(primary_key = True)
    level  = models.ForeignKey(ScoreLevel,on_delete=models.CASCADE)
    farmer  = models.ForeignKey(Farmer,on_delete=models.CASCADE)
    mill  = models.ForeignKey(Mill,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.sid} คะแนน {self.score}'

class Status(models.Model):
    sid     = models.AutoField(primary_key = True)
    text    = models.CharField(max_length   = 100) # start, during, done

class Carqueue(models.Model):
    cid    = models.AutoField(primary_key       = True)
    queue  = models.IntegerField(null           = True,blank = True)
    farmer = models.ForeignKey(Farmer,on_delete = models.CASCADE)
    mill   = models.ForeignKey(Mill,on_delete   = models.CASCADE)
    status = models.ForeignKey(Status,on_delete   = models.CASCADE)

    def __str__(self):
        return f'{self.cid} คิวที่ {self.queue}'

class Ownermill(models.Model):
    oid         = models.AutoField(primary_key = True)
    first_name   = models.CharField(max_length = 100)
    last_name    = models.CharField(max_length = 100)
    username     = models.CharField(max_length = 100)
    password     = models.CharField(max_length = 100)
    def __str__(self):
        return f'{self.oid} ชื่อ {self.first_name} นามสกุล {self.last_name} username: {self.username} password: {self.password}'

