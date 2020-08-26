from django.db import models

from wagtail.core.models import Page, PageManager, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    PageChooserPanel,
    InlinePanel
    )
from wagtailmetadata.models import MetadataPageMixin
from wagtail.search import index
from modelcluster.fields import ParentalKey


# Create your models here.
class Store(Page, MetadataPageMixin):
    intro = RichTextField(blank=True)
    parent_page_types = [
        "home.HomePage",
    ]
    subpage_types = [
        "shop.Product",
    ]

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        InlinePanel(
            "related_articles",
            heading="Products",
            help_text="Select one or more products",
        ),
    ]


class Product(Page, MetadataPageMixin):
    description = RichTextField()
    content_panels = Page.content_panels + [
        FieldPanel('description')
    ]
    related_store = ParentalKey('shop.Store', on_delete=models.SET_NULL, null=True, related_name='related_products')

    # Search index configuration
    search_fields = Page.search_fields + [
        index.SearchField('description'),
    ]
    parent_page_types = [
        "shop.Store",
    ]
    subpage_types = []


class StoreArticle(Orderable):
    store = ParentalKey(
        "shop.Store",
        null=True,
        on_delete=models.CASCADE,
        related_name="related_articles",
    )
    product = models.ForeignKey(
        Product, null=True, on_delete=models.CASCADE, related_name="+"
    )

    panels = [PageChooserPanel("product")]


class ProductManager(PageManager):
    """ Cutom manager for Products """
