from io import BytesIO

from django.core.files.base import ContentFile
from PIL import Image


def compress_image_field(instance, field_name, max_size=(1800, 1800), quality=82):
    image_field = getattr(instance, field_name, None)
    if not image_field:
        return

    try:
        image = Image.open(image_field)
    except Exception:
        return

    image.thumbnail(max_size)
    if image.mode in ("RGBA", "P"):
        image = image.convert("RGB")

    buffer = BytesIO()
    image.save(buffer, format="JPEG", optimize=True, quality=quality)
    base_name = image_field.name.rsplit("/", 1)[-1].rsplit(".", 1)[0]
    image_field.save(f"{base_name}.jpg", ContentFile(buffer.getvalue()), save=False)
