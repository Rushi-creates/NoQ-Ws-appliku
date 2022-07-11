import django_filters
from .models import * 

class AccountFilters(django_filters.FilterSet):
    class Meta: 
        model = AuthUser
        fields = '__all__'

class QueueFilters(django_filters.FilterSet):
    class Meta: 
        model = Queue
        fields = '__all__'

class QueueUserFilters(django_filters.FilterSet):
    class Meta: 
        model = QueueUser
        fields = '__all__'


# class GymTrackFilters(django_filters.FilterSet):
#     class Meta: 
#         model = GymTrack
#         fields = '__all__'
# #         # fields = ['recordDate', 'g_uid']

# class AttendanceFilters(django_filters.FilterSet):
#     class Meta: 
#         model = Attendance
#         fields = '__all__'