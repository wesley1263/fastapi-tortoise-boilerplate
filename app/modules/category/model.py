from tortoise import models, fields


class Category(models.Model):
    category_id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    status = fields.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        table = "category"
        ordering = ["name"]
