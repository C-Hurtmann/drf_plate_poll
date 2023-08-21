from djoser.serializers import UserCreateSerializer


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = UserCreateSerializer.Meta.fields + ("role",)

    def custom_signup(self, request, user):
        role = self.validated_data.get("role")
        user.role = role
        user.save()
