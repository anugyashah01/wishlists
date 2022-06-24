"""
Test Factory to make fake objects for testing
"""
import factory
from factory.fuzzy import FuzzyChoice
from service.models import Wishlist


class WishlistFactory(factory.Factory):
    """Creates fake Wishlists"""

    class Meta:  # pylint: disable=too-few-public-methods
        """Maps factory to data model"""

        model = Wishlist

    id = factory.Sequence(lambda n: n)
    name = factory.Faker("name")
    available = FuzzyChoice(choices=[True, False])
