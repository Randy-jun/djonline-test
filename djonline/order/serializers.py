from rest_framework import serializers
from order.models import o_order, o_tourist, o_jieji, o_songji

class o_orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = o_order
        fields = '__all__'

class o_touristSerializer(serializers.ModelSerializer):
    class Meta:
        model = o_tourist
        fields = '__all__'

class o_jiejiSerializer(serializers.ModelSerializer):
    class Meta:
        model = o_jieji
        fields = '__all__'

class o_songjiSerializer(serializers.ModelSerializer):
    class Meta:
        model = o_songji
        fields = '__all__'