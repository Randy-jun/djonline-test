from rest_framework import serializers
from acct.models import Agency_t, Line_Price_t, Ref_Price_t, Application_t, Tourist_t, Settlement_t

class Agency_tSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency_t
        fields = '__all__'
        depth = 1#解决嵌套问题，depth=1确保外键能正确序列化。


class Line_Price_tSerializer(serializers.ModelSerializer):
    class Meta:
        model = Line_Price_t
        fields = '__all__'
        depth = 1

class Ref_Price_tSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ref_Price_t
        fields = '__all__'
        depth = 1

class Application_tSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Application_t
        fields = '__all__'
        depth = 1

class Tourist_tSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tourist_t
        fields = '__all__'
        depth = 1

class Settlement_tSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settlement_t
        fields = '__all__'
        depth = 1