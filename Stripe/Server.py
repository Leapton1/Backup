#! /usr/bin/env python3.6

"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""
import os
from flask import Flask, redirect, request, render_template

import stripe
# This is a public sample test API key.
# Don’t submit any personally identifiable information in requests made with this key.
# Sign in to see your own test API key embedded in code samples.
stripe.api_key = 'sk_test_51LiJHALtzQmkfLaVAFSdHTULRgaFeYuH7nehxxRJhX7ONTlN19jWeVa1TAO10lUUWiRyqAvAPlnkEr4LKLb12esh00xPgJlyRx'

app = Flask(__name__,
            static_url_path='',
            static_folder='public')

YOUR_DOMAIN = 'http://127.0.0.1:4242'

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1LiKubLtzQmkfLaVAlWmVO3j',
                    'quantity': 1,
                },
                {
                    'price': 'price_1LiKubLtzQmkfLaVAlWmVO3j',
                    'quantity': 2,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success',
            cancel_url=YOUR_DOMAIN + '/cancel',
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)

@app.route('/', methods=['GET'])
def create_checkout():
    return render_template('checkout.html')

@app.route('/success', methods=['GET'])
def create_success():
    return render_template('success.html')

@app.route('/cancel', methods=['GET'])
def create_cancel():
    return render_template('cancel.html')


if __name__ == '__main__':
    app.run(port=4242)