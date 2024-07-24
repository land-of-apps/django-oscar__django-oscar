### Integrate Coupon.io Coupon Service with Shopping Cart

---

### Problem

When a user adds an item to the shopping cart, there is no integration with the Coupon.io coupon service to fetch and store coupon discounts. The goal is to integrate a web service call to Coupon.io's REST API upon item addition to the cart, store the fetched discount data, and reflect it in the user interface.

---

### Analysis

To implement this feature, the following steps should be performed:

1. **Make Web Service Call**: When an item is added to the shopping cart, a web service call should be made to the Coupon.io REST API using the product ID and currency. The API returns a coupon data object containing the discount amount and coupon code.
   
2. **Store Data Association**: Upon receiving the coupon data, an association should be created in the database between the cart item and the coupon information.

3. **Reflect in UI**: Update the user interface to show the applied coupon discount for the item in the shopping cart.

---

### Proposed Changes

#### 1. Making the Web Service Call

**File:** `oscar/apps/basket/views.py`

- In the function that handles adding items to the cart, add logic to make a call to Coupon.io REST API using the `requests` library.
- Extract the required information (`product_id` and `currency`) from the cart item.
- Handle the response data to capture the discount amount and coupon code.

#### 2. Associating Coupon Data with Cart Item

**File:** `oscar/apps/basket/models.py`

- Modify the `BasketLine` model to include fields for coupon amount and coupon code.
- Ensure these fields are populated with the appropriate data when an item is added to the cart.

#### 3. Adding Coupon Data to the Database

**File:** `oscar/apps/basket/models.py`

- Update the `BasketLine` model to store the newly added coupon data fields.
- Create a migration to reflect these model changes in the database.

**File:** `oscar/apps/basket/admin.py`

- Update the admin configuration to manage the new fields `coupon_amount` and `coupon_code`.

#### 4. Reflecting Changes in the User Interface

**File:** `oscar/templates/basket/partials/line.html`

- Update the template to display the coupon discount amount along with the item details in the shopping cart.
- Ensure the UI elements correctly show the coupon code and discount in the specified currency.

#### 5. Testing

**File:** `oscar/tests/integration/basket/tests.py`

- Add tests to check the full integration of the coupon functionality.
- Test the web service call, model updates, and UI display to ensure all elements are integrated correctly.

---

### Detailed Steps for Implementation

1. **oscar/apps/basket/views.py** 
   - Locate the function where items are added to the cart.
   - Import the `requests` library.
   - After adding the item, but before saving, make a GET request to `https://coupon.io/:product_id?currency`.
   - Extract the `discount_amount` and `coupon_code` from the JSON response.

2. **oscar/apps/basket/models.py**
   - Add fields for `coupon_amount` and `coupon_code` in the `BasketLine` model.
   - Update the model's `save` method to handle the new fields appropriately.

3. **oscar/apps/basket/admin.py**
   - Register the `coupon_amount` and `coupon_code` fields in the admin model display.

4. **oscar/templates/basket/partials/line.html**
   - Modify the template to include the new coupon discount amount and code.
   - Add conditional checks to ensure the fields are displayed only when applicable.

5. **oscar/tests/integration/basket/tests.py**
   - Create new tests or update existing ones to confirm the integration of the coupon fetching logic.
   - Validate that the discount is reflected in the UI and stored correctly in the database.

By following these steps, the integration with the Coupon.io coupon service will be complete, providing a seamless user experience reflecting coupon discounts in the shopping cart.