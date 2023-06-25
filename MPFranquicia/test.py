from django.test import TestCase
from faker import Faker
from MusicPro.models import Producto

from django.core.files.uploadedfile import SimpleUploadedFile
from faker import Faker
from PIL import Image
from io import BytesIO

class ProductoTestCase(TestCase):

    def test_carga_1000_productos(self):
        fake = Faker()
        cantidad = 1000

        image = Image.new('RGB', (200, 200))
        file_name = fake.file_name(extension='jpg')
        image_io = BytesIO()
        image.save(image_io, 'JPEG')
        image_file = SimpleUploadedFile(file_name, image_io.getvalue(), content_type='image/jpeg')
        
        for _ in range(cantidad):
            producto = Producto.objects.create(
                nombre=fake.name(),
                precio=fake.random_int(min=1, max=100),
                descripcion=fake.text(),
                imagen=None,
                cantidad=fake.random_int(min=0, max=100)
            )
        
        cantidad_productos = Producto.objects.count()
        self.assertEqual(cantidad_productos, cantidad)

    def test_carga_10000_productos(self):
        fake = Faker()
        cantidad = 10000

        image = Image.new('RGB', (200, 200))
        file_name = fake.file_name(extension='jpg')
        image_io = BytesIO()
        image.save(image_io, 'JPEG')
        image_file = SimpleUploadedFile(file_name, image_io.getvalue(), content_type='image/jpeg')
        
        for _ in range(cantidad):
            producto = Producto.objects.create(
                nombre=fake.name(),
                precio=fake.random_int(min=1, max=100),
                descripcion=fake.text(),
                imagen=None,
                cantidad=fake.random_int(min=0, max=100)
            )
        
        cantidad_productos = Producto.objects.count()
        self.assertEqual(cantidad_productos, cantidad)
    
    def test_carga_100000_productos(self):
        fake = Faker()
        cantidad = 100000

        image = Image.new('RGB', (200, 200))
        file_name = fake.file_name(extension='jpg')
        image_io = BytesIO()
        image.save(image_io, 'JPEG')
        image_file = SimpleUploadedFile(file_name, image_io.getvalue(), content_type='image/jpeg')
        
        for _ in range(cantidad):
            producto = Producto.objects.create(
                nombre=fake.name(),
                precio=fake.random_int(min=1, max=100),
                descripcion=fake.text(),
                imagen=None,
                cantidad=fake.random_int(min=0, max=100)
            )
        
        cantidad_productos = Producto.objects.count()
        self.assertEqual(cantidad_productos, cantidad)