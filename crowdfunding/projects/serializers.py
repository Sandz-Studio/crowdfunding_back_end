from rest_framework import serializers
from .models import Project, Pledge

class PledgeSerializer(serializers.ModelSerializer):
    # Check this is correct for the pledge serializer
    supporter = serializers.SerializerMethodField()
    class Meta:
        model = Pledge
        fields = '__all__'

    def get_supporter(self, obj):
        if obj.anonymous:  # i.e. if anonymous = true
            return None
        else:
            return obj.supporter.username
    
    # Is this correct to update pledge??
    def update(self, instance, validated_data):
        instance.anonymous = validated_data.get('anonymous', instance.anonymous)
        # Add other fields as needed
        instance.save()
        return instance

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)
    

class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    
    class Meta:
        model = Project
        fields = '__all__'

class ProjectDetailSerializer(ProjectSerializer):
    # Serialiser added for total sum of pledges for a project
    total_amount = serializers.ReadOnlyField()
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance