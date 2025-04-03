import streamlit as st

# title
st.title("Calculator")

# normal text
st.markdown('Wecome to my first web calculator!')

# to make 2 columns
c1, c2 = st.columns(2)

# to input  numbers
fnum = c1.number_input('First number', value =  0)
snum = c2.number_input('Second number', value = 0)

# list of operations to perform
options = ['Addition', 'Substraction', 'Multiplication', 'Division']

# make a radio options box
choice = st.radio('Select options', options)

# button on which after clicking an action becomes
button = st.button('Calculate')

result = 0
# actions to occur
if button:
    if choice == 'Addition':
        result = fnum + snum
    if choice == 'Substraction':
        result = fnum - snum
    if choice == 'Multiplication':
        result = fnum * snum
    if choice == 'Division':
        result = fnum / snum

# success is green color, warning is yellow color, of box
st.success(f"Result: {result}")