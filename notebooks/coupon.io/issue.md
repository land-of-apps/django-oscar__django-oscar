# Integrate with Coupon.io coupon service

When a user adds an item to the shopping cart, integrate a web service call to Coupon.io coupon service.

The coupon service provides a REST API https://coupon.io/:product_id?currency that returns a Coupon data object.

The data object includes a discount quantity in the specified currency, and a coupon code.

On receiving this data, store a data association in the database between the item that's being added to the
shopping cart, and the coupon amonut.

Reflect this change in the user interface.

