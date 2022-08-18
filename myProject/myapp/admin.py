from django.contrib import admin
from .models import UserDetails,DonateContact, Donation,Contact,Message

# Register your models here.


admin.site.register(UserDetails)
admin.site.register(DonateContact)
admin.site.register(Donation)
admin.site.register(Contact)
admin.site.register(Message)


