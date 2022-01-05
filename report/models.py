from django.db import models
from django.db.models import Manager as GeoManager
from django.contrib.gis.db import models

# Create your models here.

areas = [
	('Aguthi','Aguthi'),('Chinga','Chinga'),('Dedan Kimathi','Dedan Kimathi'),
	('Endarasha/Mwiyogo','Endarasha/Mwiyogo'),('Gakawa','Gakawa'),('Gatarakwa','Gatarakwa'),
	('Gatitu/Muruguru','Gatitu/Muruguru'),('Gikondi','Gikondi'),('Iriani (Mathira)','Iriani (Mathira)'),
	('Iriaini (Othaya)','Iriaini (Othaya)'),('Kabaru','Kabaru'),('Kamakwa/Mukaro','Kamakwa/Mukaro'),
	('Karatina','Karatina'),('Karima','Karima'),('Kiganjo/Mathari','Kiganjo/Mathari'),
	('Kirimukuyu','Kirimukuyu'),('Konyu','Konyu'),('Magutu','Magutu'),
	('Mahiga','Mahiga'),('Mugunda','Mugunda'),('Mukurweini-Central','Mukurweini-Central'),
	('Mukurweini-West','Mukurweini-West'),('Mweiga','Mweiga'),('Narumoru/Kiamathaga','Narumoru/Kiamathaga'),
	('Rugi','Rugi'),('Ruguru','Ruguru'),('Ruringu','Ruringu'),
	('Rware','Rware'),('Thegu','Thegu'),('Wamagana','Wamagana')
	]

class Incidence(models.Model):
	place = models.CharField(max_length=200,choices=areas)
	injuries = models.PositiveIntegerField()
	location = models.PointField(srid=4326)
	date_reported = models.DateTimeField(auto_now_add=True ,null=True)
	objects = GeoManager()

	def __str__(self):
		return self.place
