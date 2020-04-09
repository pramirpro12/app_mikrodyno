## In order to run mikrodyno.py, you need to have all the files read_all_data.py , batch_fitting_class.py and mikrodyno.py in the same folder.
import streamlit as st
from pandas import *
#import read_all_data
from read_all_data import *
from batch_fitting_class import *
import matplotlib.backends.backend_pdf
import matplotlib.pyplot as plt
import altair as alt

def main():
#creating a dashboard where we have Homepage, Predator Free Growth Curve page and Predator-Prey Growth curve page.

    page = st.sidebar.selectbox("SELECT A PAGE", [
                                "Homepage", "Predator Free Growth Curve page", "Predator-Prey Growth curve page"])

    if page == "Homepage":
        st.title("tHE APP : mikroDyno.")
        st.markdown(
            " ### Welcome to mikroDyno, a simple app to fit dynamic models to laboratory growth curves.")
        st.markdown(" #### Do you want to work with:")
        st.write("a) Growth curves (without a predator)?")
        st.markdown(
            "b) Growth curves with a host preyed upon by a virus or a pathogenic bacteria?")
        st.markdown(" ### Please select a page on the dashboard on the left?")

    elif page == "Predator Free Growth Curve page":
    	st.markdown(
            '# Which type of mechanism do you think might be important in explaining these dynamics?')
        st.markdown('a)Nutrient limitation')
        st.markdown('b)Cellular damage (e.g. due to toxins)')
        st.markdown("How many parameters do you want to account for? ")
        st.markdown('One= (aff) or Three = (aff, mum,delth)')
        #creating click buttons with data and model fit depending on different number of parameters for the model
        # for Preditor free growth curve

        num_param = st.radio( "Please chose the number of parameters to observe the model fit to the laboratory growth curves?", ('One', 'Three'))
        if num_param =='One':
            model = ['aff']
            pmod = all_mods(cont_a2090, model)
            f1, ax1 = plt.subplots(1)
            pmod.plot_data(ax1)
            pmod.do_fitting(ax1) 
            pmod.double_labels(ax1)
            st.pyplot(plt)
        elif num_param =='Three':
        	model = ['aff', 'mum', 'delth']
        	pmod = all_mods(cont_a2090, model)
        	f2, ax2 = plt.subplots(1)
        	pmod.plot_data(ax2)
        	pmod.do_fitting(ax2) 
        	pmod.double_labels(ax2)
        	st.pyplot(plt)
        

    elif page == "Predator-Prey Growth curve page":
         st.markdown("Here is the data (plot of data)")
         st.markdown(
            '# Which type of mechanism do you think might be important in explaining these dynamics?')
         st.markdown('a)Host-nutrient limitation')
         st.markdown('b)Decay of the predator')
         st.markdown("How many parameters do you want to account for? ")
         st.markdown('One= (aff) or Five = (mum, phi,beta,deltv,lambda)')
         Inf_states = st.radio(
            "How many infection states do you want to account for?", ('one', 'five'))

         if Inf_states == 'one':
         	model = ['aff']
         	pmod = all_mods(inf_379bac, model)
         	f3, ax3 = plt.subplots(2)
         	pmod.plot_data(ax3)
         	pmod.do_fitting(ax3)
         	pmod.double_labels(ax3)
         	st.pyplot(plt)
         elif Inf_states =='five':
         	model = ['mum', 'phi', 'beta', 'deltv', 'lambd']
         	pmod = all_mods(inf_379bac, model)
         	f4, ax4 = plt.subplots(2)
         	pmod.plot_data(ax4)
         	pmod.do_fitting(ax4)
         	pmod.double_labels(ax4)
         	st.pyplot(plt)

@st.cache
def load_data():
    df = ss
    return df

main()
