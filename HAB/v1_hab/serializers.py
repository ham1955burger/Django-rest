# from rest_framework import serializers
# from v1_hab.models import HouseholdAccountBook, STATE_CHOICES, CATEGORY_CHOICES
# from django.utils import timezone
#
# class HouseholdAccountBookSerializer(serializers.Serializer):
#     pk = serializers.IntegerField(read_only=True)
#     date = serializers.DateField(default=timezone.now)
#     price = serializers.IntegerField()
#     state = serializers.ChoiceField(choices=STATE_CHOICES)
#     category = serializers.ChoiceField(choices=CATEGORY_CHOICES, default='default')
#     priority = serializers.IntegerField(default=0)
#     memo = serializers.CharField(allow_blank=True, max_length=100)
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return HouseholdAccountBook.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.date = validated_data.get('date', instance.date)
#         instance.price = validated_data.get('price', instance.price)
#         instance.state = validated_data.get('state', instance.state)
#         instance.category = validated_data.get('category', instance.category)
#         instance.priority = validated_data.get('priority', instance.priority)
#         instance.memo = validated_data.get('memo', instance.memo)
#         instance.save()
#         return instance
