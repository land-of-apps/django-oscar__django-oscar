### Checklist for Implemented Changes

#### 1. Extending Models with New Fields
- **[x]** Modify the `BasketLine` model to include the following new fields:
  - **[x]** `coupon_amount`: To store the discount amount provided by the coupon.
  - **[x]** `coupon_code`: To store the coupon code applied to the item.

#### 2. Updating Model Admin Configuration
- **[  ]** Update the admin model to display and manage the new fields `coupon_amount` and `coupon_code`.

#### 3. Creating Database Migration
- **[  ]** Create a Django migration to add the new fields to the database schema.

#### **Extra Implemented Items**
- **Add `__str__` method to represent `Line` model using `coupon_code`**: This was implemented but not planned.
