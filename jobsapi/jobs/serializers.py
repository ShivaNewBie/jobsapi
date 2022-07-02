from rest_framework import serializers

from .models import JobOffer
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOffer
        fields = "__all__"



# class JobSerializer(serializers.Serializer):
#     company_name = serializers.CharField(max_length=250)
#     company_email = serializers.EmailField(max_length=250)
#     job_title = serializers.CharField(max_length=250) 
#     job_description = serializers.CharField(max_length=250)
#     salary = serializers.IntegerField()
#     city = serializers.CharField(max_length=250)
#     state = serializers.CharField(max_length=250)
#     created_at = serializers.DateTimeField(read_only=True)
#     available = serializers.BooleanField(default=True)

#     def create(self,validated_data):
#         print(validated_data)
#         return JobOffer.objects.create(**validated_data)

#     def update(self,instance,validated_data):
#         instance.company_name = validated_data.get('company name', instance.company_name)
#         instance.company_email = validated_data.get('company email', instance.company_email)
#         instance.job_title = validated_data.get('job title', instance.job_title)
#         instance.job_description = validated_data.get('job description', instance.description)
#         instance.salary = validated_data.get('salary', instance.salary)
#         instance.city = validated_data.get('city', instance.city)
#         instance.state = validated_data.get('state', instance.state)
#         instance.save()
#         return instance    

#     def validate(self,data):
#         #check description and title are different
#         if data['title'] == data['job_description']:
#             raise serializers.ValidationError('Title and description must be different from one another')
#         return data 

#     def validate_title(self,value):
#         if len(value) < 60:
#             raise serializers.ValidationError('Title should be at least 60 characters long')
#         return value