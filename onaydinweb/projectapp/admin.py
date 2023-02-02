from django.contrib import admin
from .models import Professional_second, Feature, Destlast, Featurepricing

class Professional_secondAdmin(admin.ModelAdmin):
    list_display = ("title","max_proje","fiyati","metin","depolama_alani","ek_bilgi","ek_bilgi2","bilgi2")
class FeatureAdmin(admin.ModelAdmin):
    list_display = ("titlef","metinf")
class DestlastAdmin(admin.ModelAdmin):
    list_display = ("titlel","name_date","photo")
class FeaturepricingAdmin(admin.ModelAdmin):
    list_display = ("ozellik",)

admin.site.register(Professional_second, Professional_secondAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(Destlast, DestlastAdmin)
admin.site.register(Featurepricing, FeaturepricingAdmin)
