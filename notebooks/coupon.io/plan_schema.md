### Update Database Schema for Integration with Coupon.io Coupon Service

---

### Problem

When a user adds an item to the shopping cart, there is no provision in the current database schema to store coupon discounts fetched from the Coupon.io coupon service. The goal is to extend the database schema to accommodate the necessary fields for storing coupon discount information.

---

### Analysis

The task requires adding new fields to the `BasketLine` model to store the coupon amount and coupon code. These schema changes should be properly reflected in the Django admin interface and migrations should be created to update the database schema.

---

### Proposed Changes

#### 1. Extending Models with New Fields

**File:** `oscar/apps/basket/models.py`

- Modify the `BasketLine` model to include the following new fields:
  - `coupon_amount`: To store the discount amount provided by the coupon.
  - `coupon_code`: To store the coupon code applied to the item.

#### 2. Updating Model Admin Configuration

**File:** `oscar/apps/basket/admin.py`

- Update the admin model to display and manage the new fields `coupon_amount` and `coupon_code`.

#### 3. Creating Database Migration

**File:** `oscar/apps/basket/migrations/`

- Create a Django migration to add the new fields to the database schema.

---


