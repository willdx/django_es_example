from elasticsearch_dsl import Q
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django_es_example.users.elastic_models import ElasticUser


@api_view(('GET',))
def searchUser(request):
    page = int(request.GET.get('page', default=0))
    limit = int(request.GET.get('limit', default=10))
    query_str = request.GET.get('keyword', default='')
    u = ElasticUser()
    s = u.search()
    query_obj = Q("multi_match",
                  query=query_str,
                  fields=['username', 'description'])
    q = s.query(query_obj)[limit * page: limit * page + limit]
    dsl = q.to_dict()
    data = q.execute().to_dict()
    return Response(dict(dsl=dsl, result=data), status=status.HTTP_200_OK)
