from rest_framework import serializers
 
from .models import Category,Product,Variation

class VariationSerializer(serializers.ModelSerializer):
	class Meta:
		model=Variation
		fields=[
			'id',
			'title',
			'price',
		]

class ProductUpdateDetailSerializer(serializers.ModelSerializer):
	image=serializers.SerializerMethodField()
	variation_set=VariationSerializer(many=True,read_only=True)
	class Meta:
		model=Product
		fields=[
			'id',
			'title',
			'description',
			'price',
			'image',
			'variation_set'
		]
	def get_image(self,obj):
		try:
			return obj.productimage_set.first().image.url
		except:
			return None

	def create(self, validated_data):
		print(validated_data)
		product=Product.objects.create(**validated_data)
		return product

	def create(self, instance,validated_data):
		instance.title=validated_data['title']
		instance.save()
		return instance

class ProductDetailSerializer(serializers.ModelSerializer):
	image=serializers.SerializerMethodField()
	# variation_set=VariationSerializer(many=True,read_only=True)
	class Meta:
		model=Product
		fields=[
			'id',
			'title',
			'description',
			'price',
			'image',
			'variation_set'
		]
	def get_image(self,obj):
		return obj.productimage_set.first().image.url


class ProductSerializer(serializers.ModelSerializer):
	url=serializers.HyperlinkedIdentityField(view_name='products_detail_api')
	image=serializers.SerializerMethodField()
	variation_set=VariationSerializer(many=True,read_only=True)
	class Meta:
		model=Product
		fields=[
			'id',
			'url',
			'title',
			'image',
			'variation_set'
		]
	def get_image(self,obj):
		try:
			return obj.productimage_set.first().image.url
		except:
			return None
			
		


class CategorySerializer(serializers.ModelSerializer):
	url=serializers.HyperlinkedIdentityField(view_name='category_detail_api')
	product_set=ProductSerializer(many=True)
	class Meta:
		model=Category
		fields=[
		'id',
		'url',
		'title',
		'product_set',
		# 'default_category'

		]