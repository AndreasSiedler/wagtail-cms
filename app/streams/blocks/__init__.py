from .base import HashBlock, SectionBlock  # noqa
from .blocks import (
    FeatureBlock,
    FeatureSectionBlock,
    ProductBlock,
    ProductSectionBlock,
    TeamMemberBlock,
    TeamSectionBlock,
    CarouselImageBlock,
    CarouselSectionBlock,
    CustomSectionBlock,
    FaqBlock,
    FaqSectionBlock,
    TestimonialBlock,
    TestimonialSectionBlock,
    IconChoiceBlock
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
section_blocks = [
    # ('hero_section', HeroSectionBlock()),
    ('feature_section', FeatureSectionBlock()),
    ('carousel_section', CarouselSectionBlock()),
    ('feature_block', FeatureSectionBlock()),
    ('faq_section', FaqSectionBlock()),
    ('product_section', ProductSectionBlock()),
    ('team_section', TeamSectionBlock()),
    ('testimonial_section', TestimonialSectionBlock()),
    ('custom_section', CustomSectionBlock()),
]