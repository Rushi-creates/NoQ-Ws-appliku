from django.urls import path
from . import views

urlpatterns = [

    # returns acc if acc already exists in DB
    # adds acc in DB , and return added acc ( if acc doesnt exists in DB)
    path('account/loginOrRegister/', views.loginOrRegister),

    path('account/login/', views.loginAccount),  # return true/false ( after checking if account exists)

    #!  ACCOUNTS -register paths 
    path('account/', views.getAllAccounts),
    path('account/<int:id>/', views.getSingleAccount),
    path('account/register/', views.registerAccount),  #add
    path('account/resetAccount/<int:id>/', views.resetAccount),  #update , (use for reset password)
    path('account/delete/<int:id>/', views.deleteAccount),    #delete

    #! MEMBER PROFILE DATA paths ( here uid prop is setted as primary key)
    path('memberProfile/', views.getMemberProfile),
    path('memberProfile/<int:id>/', views.getSingleMemberProfile),
    path('memberProfile/add/', views.addMemberProfile),
    path('memberProfile/update/<int:id>/', views.updateMemberProfile),
    path('memberProfile/delete/<int:id>/', views.deleteMemberProfile),


   
    #! GYM TRACK  paths ( here uid prop id setted as Foreign key)
    path('queue/', views.getQueue),
    path('queue/<int:id>/', views.getSingleQueue),
    path('queue/add/', views.addQueue),
    path('queue/update/<int:id>/', views.updateQueue),
    path('queue/delete/<int:id>/', views.deleteQueue),
    path('queue/deleteByUid/<int:uid>/', views.deleteQueueByUid), # delete by uid ( dont need now as uid=id)
    

    #! Queue user websockets  paths ( here uid prop id setted as Foreign key)
    path('queueUserWs/', views.getQueueUserWs),
    path('queueUserWs/add/', views.addQueueUserWs),
    path('queueUserWs/update/<int:id>/', views.updateQueueUserWs),
    path('queueUserWs/delete/<int:id>/', views.deleteQueueUserWs),

    
    #! GYM TRACK  paths ( here uid prop id setted as Foreign key)
    path('queueUser/', views.getQueueUser),
    path('queueUser/<int:id>/', views.getSingleQueueUser),
    path('queueUser/add/', views.addQueueUser),
    path('queueUser/update/<int:id>/', views.updateQueueUser),
    path('queueUser/delete/<int:id>/', views.deleteQueueUser),
    path('queueUser/deleteByUid/<int:uid>/', views.deleteQueueUserByUid), # delete by uid ( dont need now as uid=id)


#     #! ATTENDANCE  paths ( here uid prop id setted as Foreign key)
#     path('attendance/', views.getAttendance),
#     path('attendance/<int:id>/', views.getSingleAttendance),
#     path('attendance/add/', views.addAttendance),
#     path('attendance/update/<int:id>/', views.updateAttendance),
#     path('attendance/delete/<int:id>/', views.deleteAttendance),
#     path('attendance/deleteByUid/<int:uid>/', views.deleteAttendanceByUid), # delete by uid ( dont need now as uid=id)

]










