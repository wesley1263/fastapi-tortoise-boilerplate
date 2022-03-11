from tortoise import fields, models


class User(models.Model):
    user_id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    email = fields.CharField(max_length=120, unique=True)
    status = fields.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        table = "user"
        ordering = ["name", "email"]
