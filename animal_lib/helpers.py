from django.core.exceptions import PermissionDenied
from django.http import HttpResponseBadRequest
from django.views.generic import View
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from functools import wraps

def paginate_data(qs, page_size, page, paginated_type, **kwargs):
    """Helper function to turn many querysets into paginated results at
dispose of our GRAPHQL endpoint"""
    pass

def ajax_required(func):
    """A decorate that validates ajax requests"""
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest()

        return func(request, *args, **kwargs)
    return wrapper

class AuthorRequiredMixin(View):
    """Mixin to validate that the loggedin user is the creator
    of the object to be edited or updated."""
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)
