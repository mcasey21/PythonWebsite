import streamlit as st

st.set_page_config(page_title="GCD Calculator", page_icon="🧮")
st.sidebar.header("GCD Calculator")
st.title("GCD Calculator")

"""
# GCD CALCULATOR
formula: a = q(b) + r
"""

num1 = st.number_input("Enter num1")
num2 = st.number_input("Enter num2")

if num1 == num2:
    st.write(F"# GCD: {num1}")

elif num1 and num2:
    r_list = []

    if num1 > num2:
        a = num1            
        b = num2
    else:
        a = num2
        b = num1

        q = a//b
        r = a - (q*b)

        r_list.append(r)

        if r_list[0] == 0:
            st.write(F"# GCD: {b}")

        else:

            st.write(F"{a} = {q}({b}) + {r}")

            while r != 0:
                if r != 0:
                    a = b
                    b = r
                
                q = a//b
                r = a - (q*b)

                r_list.append(r)

                st.write(F"{a} = {q}({b}) + {r}")

            if r == 0:
                st.write(F"# GCD: {r_list[-2]}")

