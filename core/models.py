from django.db import models

# Create your models here.
class AuthUser(models.Model):
    email = models.CharField(max_length=20,default="no value")
    password = models.CharField(max_length=20,default="no value")  
    isAdmin = models.BooleanField(default=False)
    isAdminVerified = models.BooleanField(default=False) # to turn to true by superAdmin

    class Meta:
        ordering = ['id']

#! using OneToOneField , coz one account can have only profile ( user can create one rowObj of this class )
class MemberProfile(models.Model):
    name = models.CharField(max_length=40,default="no value")
    bio = models.CharField(max_length=20,default="no value")
    gender = models.CharField(max_length=20,default="no value")
    age = models.IntegerField(default=1)
    address = models.CharField(max_length=100,default="no value")
    mobileNum =  models.IntegerField(default=1)
    dob = models.IntegerField(default=1)
    lockerNum = models.IntegerField(default=1)
    reg_no = models.IntegerField(default=1)
    membership_no = models.IntegerField(default=1)
    package = models.CharField(max_length=20,default="no value")
    startDate = models.IntegerField(default=1)
    period = models.IntegerField(default=1)
    endDate = models.IntegerField(default=1)
    isApproved = models.BooleanField(default=False)  # bool to be approved by admin
    m_uid = models.OneToOneField(AuthUser , on_delete=models.CASCADE, related_name='muid', primary_key=True) # uid setted as pk


#! just a normal db table
class Queue(models.Model):
    acc_uid = models.ForeignKey(AuthUser,blank=True, null=True, on_delete=models.CASCADE,related_name='authUser_in_queue_uid') # filter search by ui
    # acc_uid = models.ForeignKey(AuthUser,blank=True,default=0, on_delete=models.CASCADE, related_name='authUser_in_queue_uid') # filter search by ui
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=80)
    isOpen = models.BooleanField(default=False)  # bool to open/close queues on holidays etc

    class Meta:
        ordering = ['id']

#! using filter method , coz one account can have multiple objects of this class
class QueueUser(models.Model):
    q_uid = models.ForeignKey(Queue,blank=True, null=True, on_delete=models.CASCADE, related_name='queue_in_queueUser_uid') 
    acc_uid = models.ForeignKey(AuthUser,blank=True, null=True,on_delete=models.CASCADE, related_name='authUser_in_queueUser_uid') 
    q_name = models.CharField(max_length=80,default='no value')
    acc_name = models.CharField(max_length=80,default='no value')
    shop_name = models.CharField(max_length=80,default='no value')
    recordTime = models.CharField(max_length=20)   # filter search, of time when user was added to queue
    qrCode_id = models.IntegerField(default=0)

    class Meta:
        ordering = ['id']


# #! using filter method , coz one account can have multiple objects of this class
# class GymTrack(models.Model):
#     g_uid = models.ForeignKey(AuthUser , on_delete=models.CASCADE, related_name='guid') # filter search by ui
#     recordDate = models.CharField(max_length=20)   # filter search , by date to separate monthly track
#     weight = models.IntegerField(default=0)
#     height = models.IntegerField(default=0)
#     neck = models.IntegerField(default=0)
#     shoulder = models.IntegerField(default=0)
#     chest = models.IntegerField(default=0)
#     upperArm = models.IntegerField(default=0)
#     forearm = models.IntegerField(default=0)
#     upperAbdomen = models.IntegerField(default=0)
#     lowerAbdomen = models.IntegerField(default=0)
#     waist = models.IntegerField(default=0)
#     hips = models.IntegerField(default=0)
#     thighs = models.IntegerField(default=0)
#     calf = models.IntegerField(default=1)


# class Attendance(models.Model):
#     a_uid = models.ForeignKey(AuthUser , on_delete=models.CASCADE, related_name='auid') # filter search by ui
#     recordDate = models.CharField(max_length=20)   # filter search , by date to separate monthly track
#     profileName = models.CharField(max_length=40, default='no name')




