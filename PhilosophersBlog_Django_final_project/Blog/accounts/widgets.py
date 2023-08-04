from django.forms import ClearableFileInput


# A widget to remove the 'Currently', 'Change' and 'Clear' elements for the image upload
class ClearRedundantImageFieldsWidget(ClearableFileInput):

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['url'] = value.url if value else ''
        context['widget']['is_initial'] = not bool(value)
        return context
