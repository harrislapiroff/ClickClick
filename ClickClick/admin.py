from django.contrib import admin
from clickclick.models import Photo, PhotoSet


class PhotoInline(admin.StackedInline):
	model = Photo
	sortable_field_name = "index"
	extra = 0


class PhotoSetAdmin(admin.ModelAdmin):
	inlines = (PhotoInline,)
	prepopulated_fields = {'slug': ('title',)}


class PhotoAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}


admin.site.register(Photo, PhotoAdmin)
admin.site.register(PhotoSet, PhotoSetAdmin)