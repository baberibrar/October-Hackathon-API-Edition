from rest_framework import serializers
from .models import Companies, Advocates


class AdvocatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advocates
        fields = '__all__'


class CompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = '__all__'
