from rest_framework import serializers
from acct.models import Agency_t, Line_Price_t, Ref_Price_t

class Agency_tSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency_t
        fields =('id','name','remark')


class Line_Price_tSerializer(serializers.ModelSerializer):
    class Meta:
        model = Line_Price_t
        fields = '__all__'

class Ref_Price_tSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ref_Price_t
        fields = '__all__'