from rest_framework.filters import SearchFilter
from django_filters import rest_framework
from .models import Product
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.geos.error import GEOSException
from django.utils.encoding import smart_str
import json
from django.utils.translation import gettext_lazy as _


class CharFilterInFilter(rest_framework.BaseInFilter, rest_framework.CharFilter):
    pass


class ProductFilter(rest_framework.FilterSet):
    company = CharFilterInFilter(field_name='company__name', lookup_expr='in')

    class Meta:
        model = Product
        fields = ['company']


from drf_extra_fields.geo_fields import PointField



class PointField1(PointField):
    EMPTY_VALUES = (None, '', [], (), {})

    def to_internal_value(self, value):
        if value in self.EMPTY_VALUES and not self.required:
            return None

        if isinstance(value, str):
            try:
                value = value.replace("'", '"')
                value = json.loads(value)
            except ValueError:
                self.fail('invalid')

        if value and isinstance(value, dict):
            try:
                latitude = value.get("latitude")
                longitude = value.get("longitude")
                return GEOSGeometry('POINT(%(latitude)s %(longitude)s)' % {
                    "longitude": longitude,
                    "latitude": latitude},
                                    srid=self.srid
                                    )
            except (GEOSException, ValueError):
                self.fail('invalid')
        self.fail('invalid')

    def to_representation(self, value):
        if value is None:
            return value

        if isinstance(value, GEOSGeometry):
            value = {
                "latitude": value.x,
                "longitude": value.y
            }

        if self.str_points:
            value['longitude'] = smart_str(value.pop('longitude'))
            value['latitude'] = smart_str(value.pop('latitude'))
        return value