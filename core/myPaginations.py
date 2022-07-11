from rest_framework.pagination import PageNumberPagination


class MyCustomPagination(PageNumberPagination):
    # page_size=100  #to define from backend, ( never set page_size to big or else slow)
    #!( but if we have commented above line, we have COMPULSORY pass ?records=7 in URL)
    page_query_param='pagenum'  # to serach from link use this ?page=2
    page_size_query_param = 'pagesize'
    ordering = 'id'
    # last_page_strings='end'    #! to fetch last page of paginations

