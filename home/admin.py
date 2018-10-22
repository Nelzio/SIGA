from django.contrib import admin
from . import models


admin.site.register(models.Curso)
admin.site.register(models.Estudante)
admin.site.register(models.Contacto)
admin.site.register(models.Disciplina)
admin.site.register(models.Endereco)
admin.site.register(models.Matricula)
admin.site.register(models.Inscricao)
admin.site.register(models.Mensalidade)

