from rest_framework import serializers

from .models import *

class COM_1968Serializer(serializers.ModelSerializer):
	class Meta:
		model = com_1968
		fields = ("__all__")
		

class COM_1975Serializer(serializers.ModelSerializer):
	class Meta:
		model = com_1975
		fields = ("__all__")


class COM_1982Serializer(serializers.ModelSerializer):
	class Meta:
		model = com_1982
		fields = ("__all__")


class COM_1990Serializer(serializers.ModelSerializer):
	class Meta:
		model = com_1990
		fields = ("__all__")


class COM_1999Serializer(serializers.ModelSerializer):
	class Meta:
		model = com_1999
		fields = ("__all__")


class COM_2006Serializer(serializers.ModelSerializer):
	class Meta:
		model = com_2006
		fields = ("__all__")


class COM_2011Serializer(serializers.ModelSerializer):
	class Meta:
		model = com_2011
		fields = ("__all__")


class COM_2016Serializer(serializers.ModelSerializer):
	class Meta:
		model = com_2016
		fields = ("__all__")