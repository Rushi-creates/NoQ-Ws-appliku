# from time import sleep
from channels.generic.websocket import JsonWebsocketConsumer
from asgiref.sync import async_to_sync




#! create diff class, for diff sockets crud ( separate them using links in routing)
class QueueLiveData(JsonWebsocketConsumer):
    def connect(self):
        self.group_name = "queueUser_liveData"



        #@ add channel to group
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,            #! add here the group name
            self.channel_name    #! get the client channel name using self.channel_name and pass it here
        ) 


        ## to send something to a particular channel only ( real time ) , NOT to whole group
        ## can be used for sending notifications ( just add celery or cron jobs)
        # async_to_sync(self.channel_layer.send)(
        # self.channel_name,     #Todo : pass group name here
        # {
        #     'type' : 'particular.liveData',
        #     'message' : 'particular msg'   #Todo : pass message here
        #     }
        # )

        
        self.accept()



 # ---------------------------------------------------------------------------- #
 #    ! the content received from client, will already be decoded from json     #
 # ---------------------------------------------------------------------------- #

    def receive_json(self, content, **kwargs):

        # content = 'queueUserWs'
        # self.group_name = content
        print('received content', content)
        self.send_json(content)


    
    # def particular_liveData(self,event):
    #     print(event['message'])
    #     self.send_json(event['message'])


          # #! to send something to client , when msg is added to group ( from above)
    def queueUser_liveData(self,event):
        print('group name is ', self.group_name)
        print('channel layer  is ' ,self.channel_layer)
        print('channel name is ' ,self.channel_name)
        print('Event is ' , event)
        self.send_json(event['message'])  # send data to client based on what queue's id he sends in content
        


    def disconnect(self, code):        
        # we can also call this from consumer
        #! to remove client channel from group, when disconnected
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )











# # ---------------------------------------------------------------------------- #
# #                         !      your number ws                                #
# # ---------------------------------------------------------------------------- #

# #! create diff class, for diff sockets crud ( separate them using links in routing)
# class YourNumberWs(JsonWebsocketConsumer):
#     def connect(self):

#         # to send something to a particular channel only ( real time ) , NOT to whole group
#         # can be used for sending notifications ( just add celery or cron jobs)
#         async_to_sync(self.channel_layer.send)(
#         self.channel_name,     #Todo : pass group name here
#         {
#             'type' : 'yourNumber.ws',
#             'message' : 'your number is after x people'   #Todo : pass message here
#             }
#         )

        
#         self.accept()



#     def receive_json(self, content, **kwargs):
#         print('received content', content)
#         self.send_json(content)


    
#     def yourNumber_ws(self,event):
#         print(event['message'])
#         self.send_json(event['message'])



#     def disconnect(self, code):        
#       print('disconnected and code is', code)





# # i guess this one is better for notifications
# # note make it async ( as this only works for one client now)
# # will work for only one client, if contains some func, which needs await( such as for loop,etc)
# # ---------------------------------------------------------------------------- #
# #                         !      your number ws                                #
# # ---------------------------------------------------------------------------- #

# #! create diff class, for diff sockets crud ( separate them using links in routing)
# class ScheduledNotificationWs(JsonWebsocketConsumer):
#     def connect(self):

#         self.accept()
    
#         # add here cron jobs / celery to send scheduled tasks
#         for i in range(20):
#             self.send_json({'notification':f'Some message {i}'})
#             sleep(1)
        



#     def receive_json(self, content, **kwargs):
#         self.send_json(content)


#     def disconnect(self, code):        
#       print('disconnected and code is', code)

