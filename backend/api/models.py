from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    """Blog / project news updates."""
    title = models.CharField(max_length=255, verbose_name='Başlık')
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    content = models.TextField(verbose_name='İçerik')
    image = models.ImageField(
        upload_to='posts/', blank=True, null=True, verbose_name='Görsel'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Yazı'
        verbose_name_plural = 'Yazılar'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Resource(models.Model):
    """Downloadable PDF guides and legal frameworks."""
    CATEGORY_CHOICES = [
        ('guide', 'Rehber'),
        ('framework', 'Çerçeve Program'),
        ('report', 'Rapor'),
        ('other', 'Diğer'),
    ]

    title = models.CharField(max_length=255, verbose_name='Başlık')
    description = models.TextField(verbose_name='Açıklama')
    file = models.FileField(upload_to='resources/', verbose_name='Dosya')
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default='guide',
        verbose_name='Kategori'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Kaynak'
        verbose_name_plural = 'Kaynaklar'

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    """Researchers and scholars involved in the project."""
    name = models.CharField(max_length=150, verbose_name='Ad Soyad')
    title = models.CharField(
        max_length=200, verbose_name='Unvan',
        help_text='Örn: Prof. Dr., Araş. Gör.'
    )
    bio = models.TextField(blank=True, verbose_name='Biyografi')
    photo = models.ImageField(
        upload_to='team/', blank=True, null=True, verbose_name='Fotoğraf'
    )
    university = models.CharField(
        max_length=200, blank=True, verbose_name='Üniversite'
    )
    order = models.PositiveIntegerField(
        default=0, verbose_name='Sıralama',
        help_text='Küçük sayı önce görünür.'
    )

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Ekip Üyesi'
        verbose_name_plural = 'Ekip Üyeleri'

    def __str__(self):
        return f"{self.title} {self.name}"


class ContactMessage(models.Model):
    """Messages sent from the frontend contact form."""
    name = models.CharField(max_length=150, verbose_name='Ad Soyad')
    email = models.EmailField(verbose_name='E-posta')
    subject = models.CharField(max_length=255, verbose_name='Konu')
    message = models.TextField(verbose_name='Mesaj')
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False, verbose_name='Okundu')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'İletişim Mesajı'
        verbose_name_plural = 'İletişim Mesajları'

    def __str__(self):
        return f"{self.name} – {self.subject}"
