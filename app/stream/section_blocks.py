""" Section blocks """
from wagtail.core.blocks import StructBlock, CharBlock, TextBlock, ChoiceBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.fields import StreamBlock

from wagtail_color_panel.blocks import NativeColorBlock

from stream.settings import cr_settings


# Section Blocks
class SectionBaseBlock(StructBlock):
    """ Section Base Block - Ued by each section """
    # Layout
    section_color_theme = ChoiceBlock(
        required=False,
        choices=cr_settings['SECTION_COLOR_THEME_CHOICES'],
        default=cr_settings['SECTION_COLOR_THEME_CHOICES_DEFAULT'],
        label='Theme',
    )
    section_top_bottom_padding = ChoiceBlock(
        required=False,
        choices=cr_settings['SECTION_TOP_BOTTOM_PADDING_CHOICES'],
        default=cr_settings['SECTION_TOP_BOTTOM_PADDING_CHOICES_DEFAULT'],
        label='Height',
    )
    section_container_width = ChoiceBlock(
        required=False,
        choices=cr_settings['SECTION_CONTAINER_WIDTH_CHOICES'],
        default=cr_settings['SECTION_CONTAINER_WIDTH_CHOICES_DEFAULT'],
        label='Width',
    )
    # Background
    section_background_type = ChoiceBlock(
        required=False,
        choices=cr_settings['SECTION_BACKGROUND_TYPE_CHOICES'],
        default=cr_settings['SECTION_BACKGROUND_TYPE_CHOICES_DEFAULT'],
        label='Background Type',
    )
    section_background_color = NativeColorBlock(
        required=False,
        default='#F37E77',
        label='Color 1',
    )
    section_background_color_2 = NativeColorBlock(
        required=False,
        default='#F37E77',
        label='Color 2',
    )
    section_background_image = ImageChooserBlock(
        required=False,
        label='Image',
    )


class SectionHeadingBlock(StructBlock):
    """ Section Heading Block - Used by each section """
    section_heading = CharBlock(
        required=False,
        max_length=100,
        label='Text',
        default='Awesome Hero Heading',
    )
    section_heading_font_size = ChoiceBlock(
        required=False,
        choices=cr_settings['SECTION_HEADING_FONT_SIZE_CHOICES'],
        default=cr_settings['SECTION_HEADING_FONT_SIZE_CHOICES_DEFAULT'],
        label='Size'
    )
    section_heading_font_weight = ChoiceBlock(
        required=False,
        choices=cr_settings['SECTION_HEADING_FONT_WEIGHT_CHOICES'],
        default=cr_settings['SECTION_HEADING_FONT_WEIGHT_CHOICES_DEFAULT'],
        label='Weight'
    )

    class Meta:
        """ Meta data """
        label = 'Heading'
        template = 'block_sections/section_heading.html'


class SectionSubheadingBlock(StructBlock):
    """ Section Subheading Block - Used by each section """
    section_subheading = CharBlock(
        required=False,
        max_length=100,
        label='Text',
        default='Super Awesome Hero Subheading',
    )
    section_subheading_font_size = ChoiceBlock(
        required=False,
        choices=cr_settings['SECTION_HEADING_FONT_SIZE_CHOICES'],
        default=cr_settings['SECTION_HEADING_FONT_SIZE_CHOICES_DEFAULT'],
        label='Size'
    )
    section_subheading_font_weight = ChoiceBlock(
        required=False,
        choices=cr_settings['SECTION_HEADING_FONT_WEIGHT_CHOICES'],
        default=cr_settings['SECTION_HEADING_FONT_WEIGHT_CHOICES_DEFAULT'],
        label='Weight'
    )

    class Meta:
        """ Meta data """
        label = 'Subheading'
        template = 'block_sections/section_subheading.html'


class SectionDescriptionBlock(StructBlock):
    """ Section Description Block - Used by each section """
    section_description = TextBlock(
        required=False,
        max_length=500,
        label='Description',
        default='The thing we do is better than any other similar thing and this hero panel will convince you of that, just by having a glorious background image.',
        rows=5
    )

    class Meta:
        """ Meta data """
        label = 'Description'
        template = 'block_sections/section_description.html'


# Hero Blocks
class HeroImageBlock(StructBlock):
    """ Seciton image block """
    hero_image = ImageChooserBlock(
        required=False,
        label='Image',
    )
    hero_image_size = ChoiceBlock(
        required=False,
        choices=cr_settings['HERO_IMAGE_SIZE_CHOICES'],
        default=cr_settings['HERO_IMAGE_SIZE_CHOICES_DEFAULT'],
        label='Image size',
    )

    class Meta:
        """ Meta data """
        label = 'Image'
        template = 'block_sections/hero_image.html'


class HeroBaseBlock(SectionBaseBlock):
    """ Hero Base Block - Extends SectionBaseBlock """
    hero_layout = ChoiceBlock(
        required=False,
        choices=cr_settings['HERO_LAYOUT_CHOICES'],
        default=cr_settings['HERO_LAYOUT_CHOICES_DEFAULT'],
        label='Layout',
    )


# Feature Blocks
class FeatureBaseBlock(SectionBaseBlock):
    """ Feature Base Block - Extends SectionBaseBlock """


class FeatureItemBlock(StructBlock):
    """ Feature item block """
    heading = CharBlock(
        required=True,
        max_length=80,
        label='Feature',
        default='Super Awesome Feature',
    )
    description = TextBlock(
        required=True,
        max_length=400,
        label='Description',
        default='The thing we do is better than any other similar thing and this hero panel will convince you of that, just by having a glorious background image.',
    )

    class Meta:
        """ Meta data """
        form_template = 'block_forms/multi_field.html'
        template = 'block_sections/feature_item.html'
        icon = 'tick-inverse'
        label = 'Feature Item'


class FeatureItemsBlock(StructBlock):
    """ Features block """
    feature_layout = ChoiceBlock(
        required=False,
        choices=cr_settings['FEATURE_LAYOUT_CHOICES'],
        default=cr_settings['FEATURE_LAYOUT_CHOICES_DEFAULT'],
        label='Layout',
    )
    feautre_column_count = ChoiceBlock(
        required=False,
        choices=cr_settings['FEATURE_COLUMN_COUNT_CHOICES'],
        default=cr_settings['FEATURE_COLUMN_COUNT_CHOICES_DEFAULT'],
        label='Columns',
    )
    feature_items = StreamBlock(
        [
            ('feature_block', FeatureItemBlock())
        ],
        required=False,
        label="Feature items",
    )

    class Meta:
        template = 'block_sections/feature_items.html'
        label = 'Features'

# class ActionButton(StructBlock):
#     text = CharBlock(
#         required=True,
#         max_length=50,
#         label='Text',
#         # help_text=""
#     )


# class PrimaryButton(StructBlock):
#     text = CharBlock(
#         required=True,
#         max_length=50,
#         label='Text',
#         # help_text=""
#     )


# class CustomButton(StructBlock):
#     text = CharBlock(
#         required=True,
#         max_length=50,
#         label='Text',
#         # help_text=""
#     )


# class ContentBlock(StructBlock):
#     heading = CharBlock(
#         required=False,
#         max_length=80,
#         label='Heading',
#         help_text="Feature name. Keep it short, like 'Free Chat' or 'Secure',",
#         classname='field-col col6'
#     )
#     description = TextBlock(
#         required=False,
#         max_length=400,
#         label='Description',
#         help_text='Write a few lines about this feature',
#         classname='field-col col6'
#     )

#     class Meta:
#         icon = 'tick-inverse'
#         label = 'Content label'


# class PlusBlock(StructBlock):
#     icon = IconChoiceBlock(
#         required=True,
#         label='Icon',
#         help_text='Pick an icon (see https://material.io/tools/icons/) for a bullet point',
#         classname='block_content_field'
#     )
#     more_info_url = URLBlock(
#         required=False,
#         label='URL',
#         help_text='A link to be followed for more information',
#         classname='block_content_field'
#     )
#     color = NativeColorBlock(required=False)

#     class Meta:
#         icon = 'tick-inverse'
#         label = 'Plus label'


# class FeatureBlock(StructBlock):
#     content = ContentBlock()
#     plus = PlusBlock()

#     class Meta:
#         form_template = 'block_forms/multi_field.html'
#         template = 'blocks/feature_item_block.html'
#         icon = 'tick-inverse'
#         label = 'Feature Section'


# class TeamMemberBlock(StructBlock):
#     name = CharBlock(required=True, max_length=80, label='Name')
#     image = ImageChooserBlock(required=True, label='Photo')
#     role = CharBlock(required=True, max_length=80, label='Role / Job Title')
#     biography = TextBlock(required=False, label='Bio')
#     linkedin = URLBlock(required=False, label='LinkedIn Page')
#     twitter = URLBlock(required=False, label='Twitter Page')

#     class Meta:
#         icon = 'user'
#         label = 'Team Member'


# class CarouselImageBlock(StructBlock):
#     image = ImageChooserBlock()
#     heading = CharBlock(required=False, max_length=80,
#                         label='Main text', help_text='Add an image subtitle'),
#     description = TextBlock(required=False, label='Description',
#                             help_text='Add some descriptive information with your image'),
#     more_info_url = URLBlock(required=False, label='Link URL'),

#     class Meta:
#         icon = 'image'
#         label = 'Carousel Image'


# class FaqBlock(StructBlock):
#     question = CharBlock(required=True, max_length=80, label='Question',
#                          help_text="Add a simply worded question, like 'How much will it cost?'")
#     answer = TextBlock(required=True, label='Answer',
#                        help_text='Provide a short answer in no more than a few lines of text')
#     icon = IconChoiceBlock(required=True, label='Icon',
#                            help_text='Pick an icon (see https://material.io/tools/icons/) for a bullet point')
#     more_info_url = URLBlock(required=False, label='URL',
#                              help_text='Add a link to be followed for more information on that question, feature or product')

#     class Meta:
#         icon = 'help'
#         label = 'FAQ'


# class TestimonialBlock(StructBlock):
#     name = CharBlock(required=True, max_length=100, label='Name',
#                      help_text='Name of the person making the recommendation'),
#     role = CharBlock(required=False, max_length=100, label='Role',
#                      help_text='Job title of the person making the recommentation, if any'),
#     organisation = CharBlock(required=False, max_length=100, label='Organisation',
#                              help_text='Name of the organisation the person is part of, if any'),
#     quote = TextBlock(required=True, max_length=100, label='Quote',
#                       help_text='The nice things they have to say')
#     image = ImageChooserBlock(required=False, label='Logo/Picture',
#                               help_text="Add either a company logo or a person's mugshot")
#     stars = ChoiceBlock(required=True, choices=[
#         (None, 'No rating'),
#         (0, '0 Stars'),
#         (1, '1 Star'),
#         (2, '2 Stars'),
#         (3, '3 Stars'),
#         (4, '4 Stars'),
#         (5, '5 Stars')
#     ], icon='pick')

#     class Meta:
#         icon = 'pick'
#         label = 'Testimonial'


# class ProductBlock(StructBlock):
#     heading = CharBlock(required=True, max_length=80, label='Name',
#                         help_text="Name of a product. Keep it short, like 'Mega Kit Pro' or 'Cloud Manager'")
#     description = TextBlock(required=True, max_length=400, label='Description',
#                             help_text='Write a few lines about this product')
#     image = ImageChooserBlock(required=False, label='Image',
#                               help_text='Pick an image to represent this product')
#     more_info_url = URLBlock(required=False, label='URL',
#                              help_text='A link to be followed for more information')

#     class Meta:
#         icon = 'tick-inverse'
#         label = 'Product Overview'
