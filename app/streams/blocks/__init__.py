from .base import HashBlock  # noqa
from .blocks import (
    FeatureBlock,
    ProductBlock,
    TeamMemberBlock,
    CarouselImageBlock,
    FaqBlock,
    TestimonialBlock,
    IconChoiceBlock,
    HeroSectionChooserBlock,
)  # noqa
# noqa avoids "unused imports in __init__.py" error when using flake8

# Simply add this to any existing list of streamfield blocks in a content panel to enable creation of sections
blocks = [
    ('feature_block', FeatureBlock()),
    ('product_block', ProductBlock()),
    ('team_member_block', TeamMemberBlock()),
    ('carousel_image_block', CarouselImageBlock()),
    ('faq_block', FaqBlock()),
    ('testimonial_block', TestimonialBlock()),
    ('icon_choice_block', IconChoiceBlock()),
]