from django.db import models

# Create your models here.

CONTACT_REASONS = (
    ('general_inquiry', 'General Inquiry'),
    ('product_advice', 'Product Advice'),
    ('technical_support', 'Technical Support'),
    ('general_feedback', 'General Feedback'),
)


class Contact(models.Model):
    """ A model for contact submissions """

    class Meta:
        verbose_name_plural = 'Contact Page Submissions'

    reason = models.CharField(
        max_length=120,
        choices=CONTACT_REASONS,
        default='general_enquiry',
        null=False,
        blank=False,
    )
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
    email = models.CharField(
        max_length=90,
        null=False,
        blank=False,
    )
    message = models.TextField(
        max_length=3000,
        null=False,
        blank=False,
    )
    responded = models.BooleanField(default=False)

    def __str__(self):
        return self.name
