from django.shortcuts import render

from rest_framework import generics, viewsets, filters
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .models import *

from drf_multiple_model.views import ObjectMultipleModelAPIView

from django.db.models import Q


class ComViewSet(viewsets.ModelViewSet):
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated,)

	queryset = com_1968.objects.all().order_by('Libelle_de_commune')
	serializer_class = COM_1968Serializer


def search_filter(queryset, request, *args, **kwargs):
	search = request.query_params['search']

	return queryset.filter(Q(Libelle_de_commune = search) | Q(Departement_en_geographie_2018 = search))

class PopulationCommune(ObjectMultipleModelAPIView):
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated,) 
	
	pagination_class = None

	def get_querylist(self):
		filter_backends = (filters.SearchFilter,)
		search_fields = ['Libelle_de_commune', 'Departement_en_geographie_2018']

		search = self.request.query_params['search']

		querylist = [
			{
				'queryset': com_1968.objects.all(),
				'serializer_class': COM_1968Serializer,
				'label': '1968',
				'filter_fn': search_filter
			},
			{
				'queryset': com_1975.objects.all(),
				'serializer_class': COM_1975Serializer,
				'label': '1975',
				'filter_fn': search_filter
			},
			{
				'queryset': com_1982.objects.all(),
				'serializer_class': COM_1982Serializer,
				'label': '1982',
				'filter_fn': search_filter
			},
			{
				'queryset': com_1990.objects.all(),
				'serializer_class': COM_1990Serializer,
				'label': '1990',
				'filter_fn': search_filter
			},
			{
				'queryset': com_1999.objects.all(),
				'serializer_class': COM_1999Serializer,
				'label': '1999',
				'filter_fn': search_filter
			},
			{
				'queryset': com_2006.objects.all(),
				'serializer_class': COM_2006Serializer,
				'label': '2006',
				'filter_fn': search_filter
			},
			{
				'queryset': com_2011.objects.all(),
				'serializer_class': COM_2011Serializer,
				'label': '2011',
				'filter_fn': search_filter
			},
			{
				'queryset': com_2016.objects.all(),
				'serializer_class': COM_2016Serializer,
				'label': '2016',
				'filter_fn': search_filter
			},
		]

		return querylist








