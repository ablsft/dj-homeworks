from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django_filters import rest_framework as filters
from django.db.models import Q
from django.db import IntegrityError

from advertisements.models import Advertisement, Favourites
from advertisements.serializers import AdvertisementSerializer
from advertisements.filters import AdvertisementFilter
from advertisements.permissions import IsOwner


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    serializer_class = AdvertisementSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = AdvertisementFilter
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get_queryset(self):
        return Advertisement.objects.exclude(
            Q(status='DRAFT'), ~Q(creator=self.request.user.id))

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action == "create":
            return [IsAuthenticated()]
        if self.action in ["update", "partial_update", "destroy"] \
                and not self.request.user.is_staff:
            return [IsAuthenticated(), IsOwner()]
        if self.action in ["favourites", "add_to_favourites"]:
            return [IsAuthenticated()]
        return []

    @action(detail=True, methods=['post'])
    def add_to_favourites(self, request, pk):
        advertisement = self.get_object()

        if self.request.user == advertisement.creator:
            return Response({"detail": "You are not allowed to add your own \
                             advertisement to favourites"},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            fav_entry = Favourites(user=self.request.user,
                                   advertisement=advertisement)
            fav_entry.save()
            return Response({'status': f'Advertisement #{pk} successfully \
                            added to favourites'})

        except IntegrityError:
            return Response({"detail": "This advertisement is already \
                             in favourites"},
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def favourites(self, request, *args, **kwargs):
        queryset = Advertisement.objects.filter(
                            favourites__user=self.request.user.id)
        serializer = AdvertisementSerializer(queryset, many=True)
        return Response(serializer.data)
