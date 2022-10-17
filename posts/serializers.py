from rest_framework import serializers
from posts.models import Post, Vote


class PostSerializer(serializers.ModelSerializer):
    user_score = serializers.SerializerMethodField('get_user_score')

    def get_user_score(self, model):
        user = self.context.get('request').user
        vote = Vote.objects.filter(post=model, voter=user.id)
        if vote:
            vote = vote[0].vote
        else:
            vote = None
        return vote

    score = serializers.FloatField()

    class Meta:
        model = Post
        fields = ['title', 'body', 'score', 'user_score']


class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'body']


class VoteSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        request = self.context.get("request")
        user = request.user
        post = self.context.get("post")
        attrs.update({
            'voter': user,
            'post': post,
        })
        return super().validate(attrs)

    def create(self, validated_data):
        if Vote.objects.filter(voter=validated_data.get('voter'), post=validated_data.get('post')).exists():
            vote = validated_data.pop('vote')
            instance = Vote.objects.get(**validated_data)
            instance.vote = vote
            instance.save()
        else:
            instance = Vote.objects.create(**validated_data)
        return instance

    class Meta:
        model = Vote
        fields = ['vote']
