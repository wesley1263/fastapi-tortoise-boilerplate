from tortoise import fields, models


class Category(models.Model):
    category_id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100, unique=True)
    status = fields.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        table = "category"
        ordering = ["name"]
