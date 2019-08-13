from django_hstore.dict import HStoreDict
from rest_framework import serializers


class HStoreField(serializers.Field):

    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        return HStoreDict(data)