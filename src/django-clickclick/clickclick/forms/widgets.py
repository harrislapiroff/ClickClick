# http://koensblog.eu/blog/7/multiple-file-upload-django

from django import forms

__all__ = ('MultiFileInput',)

class MultiFileInput(forms.FileInput):
	def render(self, name, value, attrs={}):
		attrs['multiple'] = 'multiple'
		return super(MultiFileInput, self).render(name, None, attrs=attrs)
	def value_from_datadict(self, data, files, name):
		if hasattr(files, 'getlist'):
			return files.getlist(name)
		else:
			return [files.get(name)]