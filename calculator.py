import streamlit as st
import numpy as np

#App title
st.set_page_config(page_title="Grailed Fee Calculator")
st.header('Grailed Fee Calculator :dollar:')
#App Description
st.caption("An app designed to calculate Grailed's commission and payment processing fees.")

#whether or not user is shipping domestically or internationally
shipping = st.radio('Select your shipping destination: ', ('Domestic', 'International'), horizontal = True)

#input asking users to type price with a mim value of 0
selling_price = st.number_input('Enter selling price:', min_value = 0)

calc = st.button('Calculate')

#logic for calculation
if (shipping == 'Domestic' and calc):
	grailed_fee = np.round(0.09 * selling_price, 2)
	st.error("Commission Fees: ${}".format(grailed_fee) + " :rage:")
	paypal_fee  = np.round((selling_price * 0.0349) + .49, 2)
	st.error("Payment Processing Fees: ${}".format(paypal_fee) + " :rage:")
	after_fees =  np.round(selling_price - (grailed_fee + paypal_fee), 2) 
	st.success('After fees, your adjusted selling price is ${}'.format(after_fees) + " :moneybag:")
elif (shipping == 'International' and calc):
	grailed_fee = np.round(0.09 * selling_price, 2)
	st.error("Commission Fees: ${}".format(grailed_fee) + " :rage:")
	paypal_fee  = np.round((selling_price * 0.0499) + .49, 2)
	st.error("Payment Processing Fees: ${}".format(paypal_fee) + " :rage:")
	after_fees =  np.round(selling_price - (grailed_fee + paypal_fee), 2)
	st.success('After fees, your adjusted selling price is ${}'.format(after_fees) + " :moneybag:")



