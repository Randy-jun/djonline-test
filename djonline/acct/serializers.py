from rest_framework import serializers
from acct.models import Agency_t

class Agency_tSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency_t
        fields =('name','remark')