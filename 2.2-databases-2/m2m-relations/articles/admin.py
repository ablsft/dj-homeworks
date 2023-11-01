from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_count = 0
        for form in self.forms:
            if not form.cleaned_data:
                continue
            if form.cleaned_data['is_main']:
                main_count += 1

        if main_count == 0:
            raise ValidationError('Укажите основной раздел')
        elif main_count > 1:
            raise ValidationError('Основным может быть только один раздел')
        
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 3


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        ScopeInline,
    ]
    exclude = ['scopes']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
