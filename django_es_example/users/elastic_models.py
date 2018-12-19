from elasticsearch_dsl import DocType, Text, Date
from elasticsearch_dsl.connections import connections

from config.settings.base import env

elasticsearch_host = env.str('ES_DOMAIN', 'http://127.0.0.1:9200')
print("elasticsearch_host:{}".format(elasticsearch_host))
connections.create_connection(hosts=elasticsearch_host, sniff_on_start=True)


class ElasticUser(DocType):
    username = Text()
    first_name = Text()
    last_name = Text()
    address = Text()
    birthday = Date()
    description = Text()

    class Meta:
        index = 'elastic_user'
