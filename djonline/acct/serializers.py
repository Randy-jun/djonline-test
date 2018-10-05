from rest_framework import serializers
from acct.models import Agency_t, Line_Price_t, Ref_Price_t,Application_t,Tourist_t,Settlement_t

class Agency_tSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency_t
        fields =('id','name','remark','localname')


class Line_Price_tSerializer(serializers.ModelSerializer):
    class Meta:
        model = Line_Price_t
        fields = '__all__'

class Ref_Price_tSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ref_Price_t
        fields = '__all__'

class Application_tSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application_t
        fields = '__all__'

class Tourist_tSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tourist_t
        fields = '__all__'

class Settlement_tSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settlement_t
        fields = '__all__'