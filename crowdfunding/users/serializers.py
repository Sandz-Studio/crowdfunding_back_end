# from projects.serializers import PledgeSerializer, ProjectSerializer
from rest_framework import serializers
from .models import CustomUser
# from users.serializers import CustomUserSerializer

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
    
# class CustomUserDetail(CustomUserSerializer):
#     # below based on ProjectSerializer approach for owner
#     pledges = PledgeSerializer(many=True, source="supporter_pledges", required=False)
#     projects = ProjectSerializer(many=True, source="owner_projects", required=False)

#     class Meta:
#         model = CustomUser
#         fields = (
#             "id",
#             "username",
#             "email",
#             "is_active",
#             "bio",
#             "avatar",
#             "comments",
#             "pledges",
#             "projects",
#         )
#         read_only_fields = ["id", "comments", "pledges", "projects"]
        
    # def create(self, validated_data):
    #     user = CustomUser.objects.create(
    #         first_name = validated_data['first_name'],
    #         last_name = validated_data['last_name'],
    #         date_of_birth = validated_data['date_of_birth'],
    #         profile_picture = validated_data['profile_picture'],
    #         bio = validated_data['bio'],
    #         username = validated_data['username'],
    #         email = validated_data['email'],
    #     )