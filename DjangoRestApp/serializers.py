from rest_framework import serializers
from DjangoRestApp.models import Post

class PostSerializers(serializers.HyperlinkedmodelSerializers):
    class meta:
        model=Post
        fields=["post_title", "post_descripations"]