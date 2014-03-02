from django.contrib import admin
from clickclick.models import Photo, PhotoSet


class PhotoInline(admin.StackedInline):
	model = Photo
	extra = 0
	readonly_fields = ('upload_time', 'last_updated_time', '_order')
	fields = (('title', 'slug', 'owner'), ('image', 'caption',), ('upload_time', 'last_updated_time', '_order',),)
	prepopulated_fields = {'slug': ('title',)}


class PhotoSetAdmin(admin.ModelAdmin):
	inlines = (PhotoInline,)
	prepopulated_fields = {'slug': ('title',)}


class PhotoAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}


admin.site.register(Photo, PhotoAdmin)
admin.site.register(PhotoSet, PhotoSetAdmin)