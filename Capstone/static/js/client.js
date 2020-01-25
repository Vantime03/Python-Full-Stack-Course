const stripe = Stripe('');

let checkoutButton = document.querySelector('#checkout-button');
checkoutButton.addEventListener('click', function () {
  console.log("***********************");
  stripe.redirectToCheckout({
    items: [{
      // Define the product and SKU in the Dashboard first, and use the SKU
      // ID in your client-side code.
      sku: 'sku_123',
      quantity: 1

    }],
    sessionId: '{{CHECKOUT_SESSION_ID}}',
    successUrl: 'https://www.example.com/success',
    cancelUrl: 'https://www.example.com/cancel'
  });
});

