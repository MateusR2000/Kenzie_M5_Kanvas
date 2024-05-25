from rest_framework import serializers
from .models import Account
from rest_framework.validators import UniqueValidator

class AccountSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "id",
            "username",
            "email",
            "password",
            "is_superuser"
        ]

        extra_kwargs = {"password": {"write_only": True}}

    email = serializers.EmailField(validators=[
        UniqueValidator(Account.objects.all(), "user with this email already exists.")
        ],
    )

    is_superuser = serializers.BooleanField(default=False, allow_null=True)
    
    def create(self, validated_data: dict) -> Account:
        if validated_data.get("is_superuser"):
            account = Account.objects.create_superuser(**validated_data)
        else:
            account = Account.objects.create_user(**validated_data)
        
        return account