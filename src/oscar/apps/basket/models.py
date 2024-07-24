# Path: src/oscar/apps/basket/models.py
from oscar.apps.basket.abstract_models import (
    AbstractBasket,
    AbstractLine,
    AbstractLineAttribute,
)
from django.db import models
from oscar.core.loading import is_model_registered

__all__ = [
    "InvalidBasketLineError",
]


class InvalidBasketLineError(Exception):
    pass


if not is_model_registered("basket", "Basket"):

    class Basket(AbstractBasket):
        pass

    __all__.append("Basket")


if not is_model_registered("basket", "Line"):

    class Line(AbstractLine):
        coupon_amount = models.DecimalField(
            "Coupon Amount", max_digits=12, decimal_places=2, default=0
        )
        coupon_code = models.CharField(
            "Coupon Code", max_length=255, blank=True, null=True
        )

        def __str__(self):
            return self.coupon_code or "No Coupon"

        pass

    __all__.append("Line")


if not is_model_registered("basket", "LineAttribute"):

    class LineAttribute(AbstractLineAttribute):
        pass

    __all__.append("LineAttribute")
