from rest_framework import serializers
from .models import Room

class roomSerializer(serializers.ModelSerializer):
  class Meta:
    model=Room
    fields=('id','host','votes_to_skip','guest_can_pause','created_at')