from django.db import models

class Mill(models.Model):
    mid    = models.AutoField(primary_key = True)
    name   = models.CharField(max_length  = 100)
    price  = models.IntegerField(null     = True,blank   = True)
    sprice = models.IntegerField(null     = True, blank  = True)
    lat    = models.CharField(max_length  = 100, default = None)
    lng    = models.CharField(max_length  = 100, default = None)
    #score  = models.ForeignKey(Score,on_delete=models.CASCADE)
    #queue  = models.ForeignKey(Carqueue,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.mid} - โรงสี {self.name} ราคาข้าวจ้าว {self.price} ราคข้าวเหนียว  {self.sprice} คะแนน {self.score} คิวรถ {self.queue}'

class Farmer(models.Model):
    fid        = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length  = 100)
    last_name  = models.CharField(max_length  = 100)
    email      = models.CharField(max_length  = 100)
    call       = models.IntegerField(null     = True,blank = True)

    def __str__(self):
        return f'{self.fid} ชื่อ {self.first_name} นามสกุล {self.last_name} email: {self.email} เบอร์โทรศัพท์ {self.call}'


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
    def __str__(self):
        return f'{self.oid} ชื่อ {self.first_name} นามสกุล {self.last_name}'

