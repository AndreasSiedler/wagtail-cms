from wagtail.core.blocks import StructBlock, CharBlock, TextBlock, URLBlock, ChoiceBlock
from wagtail.images.blocks import ImageChooserBlock
from .material_icons import IconChoiceBlock


class FeatureBlock(StructBlock):
    heading = CharBlock(
        required=True,
        max_length=80,
        label='Feature',
        help_text="Feature name. Keep it short, like 'Free Chat' or 'Secure',",
        classname='block_content_field'
    )
    description = TextBlock(
        required=True,
        max_length=400,
        label='Description',
        help_text='Write a few lines about this feature',
        classname='block_content_field'
    )
    icon = IconChoiceBlock(
        required=True,
        label='Icon',
        help_text='Pick an icon (see https://material.io/tools/icons/) for a bullet point',
        classname='block_content_field'
    )
    more_info_url = URLBlock(
        required=False, 
        label='URL',
        help_text='A link to be followed for more information',
        classname='block_content_field'
    )

    class Meta:
        icon = 'tick-inverse'
        label = 'Add Feature'


class TeamMemberBlock(StructBlock):
    name = CharBlock(required=True, max_length=80, label='Name')
    image = ImageChooserBlock(required=True, label='Photo')
    role = CharBlock(required=True, max_length=80, label='Role / Job Title')
    biography = TextBlock(required=False, label='Bio')
    linkedin = URLBlock(required=False, label='LinkedIn Page')
    twitter = URLBlock(required=False, label='Twitter Page')

    class Meta:
        icon = 'user'
        label = 'Team Member'


class CarouselImageBlock(StructBlock):
    image = ImageChooserBlock()
    heading = CharBlock(required=False, max_length=80,
                        label='Main text', help_text='Add an image subtitle'),
    description = TextBlock(required=False, label='Description',
                            help_text='Add some descriptive information with your image'),
    more_info_url = URLBlock(required=False, label='Link URL'),

    class Meta:
        icon = 'image'
        label = 'Carousel Image'


class FaqBlock(StructBlock):
    question = CharBlock(required=True, max_length=80, label='Question',
                         help_text="Add a simply worded question, like 'How much will it cost?'")
    answer = TextBlock(required=True, label='Answer',
                       help_text='Provide a short answer in no more than a few lines of text')
    icon = IconChoiceBlock(required=True, label='Icon',
                           help_text='Pick an icon (see https://material.io/tools/icons/) for a bullet point')
    more_info_url = URLBlock(required=False, label='URL',
                             help_text='Add a link to be followed for more information on that question, feature or product')

    class Meta:
        icon = 'help'
        label = 'FAQ'


class TestimonialBlock(StructBlock):
    name = CharBlock(required=True, max_length=100, label='Name',
                     help_text='Name of the person making the recommendation'),
    role = CharBlock(required=False, max_length=100, label='Role',
                     help_text='Job title of the person making the recommentation, if any'),
    organisation = CharBlock(required=False, max_length=100, label='Organisation',
                             help_text='Name of the organisation the person is part of, if any'),
    quote = TextBlock(required=True, max_length=100, label='Quote',
                      help_text='The nice things they have to say')
    image = ImageChooserBlock(required=False, label='Logo/Picture',
                              help_text="Add either a company logo or a person's mugshot")
    stars = ChoiceBlock(required=True, choices=[
        (None, 'No rating'),
        (0, '0 Stars'),
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars')
    ], icon='pick')

    class Meta:
        icon = 'pick'
        label = 'Testimonial'


class ProductBlock(StructBlock):
    heading = CharBlock(required=True, max_length=80, label='Name',
                        help_text="Name of a product. Keep it short, like 'Mega Kit Pro' or 'Cloud Manager'")
    description = TextBlock(required=True, max_length=400, label='Description',
                            help_text='Write a few lines about this product')
    image = ImageChooserBlock(required=False, label='Image',
                              help_text='Pick an image to represent this product')
    more_info_url = URLBlock(required=False, label='URL',
                             help_text='A link to be followed for more information')

    class Meta:
        icon = 'tick-inverse'
        label = 'Product Overview'
