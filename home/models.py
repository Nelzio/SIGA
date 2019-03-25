from django.db import models


class Endereco(models.Model):
    cidade = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    quarteirao = models.PositiveIntegerField()
    casa = models.PositiveIntegerField()
    avenida = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.bairro


class Contacto(models.Model):
    telefone = models.CharField(max_length=9)
    alternativo = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    def __str__(self):
        return self.email


class Disciplina(models.Model):
    nome = models.CharField(max_length=20)


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    regime = models.BooleanField()
    mensalidade_vocacional = models.DecimalField(max_digits=6, decimal_places=2)
    mensalidade_regular = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nome


class Estudante(models.Model):
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    contacto = models.ForeignKey(Contacto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=20)
    dataNasc = models.DateField()
    doc_type = models.CharField(max_length=20)
    num_doc = models.CharField(max_length=20)

    @classmethod
    def create(cls, endereco, contacto, nome, dataNasc, doc_type, num_doc):
        estudante = cls(
            endereco=endereco,
            contacto=contacto,
            nome=nome,
            dataNasc=dataNasc,
            doc_type=doc_type,
            num_doc=num_doc
        )
        return estudante

    def __str__(self):
        return self.nome


class Matricula(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    regime = models.CharField(max_length=10)
    data = models.DateTimeField(auto_now=True)

    @classmethod
    def create(cls, estudante, curso, regime):
        matricula = cls(
            estudante=estudante,
            curso=curso,
            regime=regime
        )
        return matricula


class Inscricao(models.Model):
    matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE)
    semestre = models.PositiveIntegerField(default=1)
    data = models.DateTimeField(auto_now=True)

    @classmethod
    def create(cls, matricula, semestre):
        inscricao = cls(
            matricula=matricula,
            semestre=semestre
        )
        return inscricao


class Mensalidade(models.Model):
    inscricao = models.ForeignKey(Inscricao, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now=True)

    @classmethod
    def create(cls, inscricao):
        mensalidade = cls(inscricao=inscricao)
        return mensalidade
