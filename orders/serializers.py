from rest_framework.serializers import Serializers
from .models import Cart , CartDetail , Order , OrderDetail

class CartDetailSerializer(Serializers.modelSerializers):
  class Meta:
    model = CartDetail
    fields = '__all__'

class CartSerializer(Serializers.modelSerializer):
  cart_detail = CartDetailSerializer(many=True)
  class Meta:
    model = Cart
    fields = '__all__'


