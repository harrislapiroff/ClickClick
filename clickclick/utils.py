from django.core.urlresolvers import reverse
from django.utils.functional import lazy

# reverse_lazy is, as of this writing, in Django dev, but for now we'll import it from here.
reverse_lazy = lazy(reverse, str)