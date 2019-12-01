import streamlit as st
from pandas import *
from batch_fitting_class import *
import matplotlib.backends.backend_pdf
import matplotlib.pyplot as plt
import altair as alt

###This will read in the entire excel
ss = read_excel("DMSP_dosage.xlsx", sheetname = "substrate_forpy")
# #st.write(ss)

#times
dtimes = array(ss['T'])
a1 = array(ss['A_2090'])
a1sd = array(ss['A_2090_sd'])

# put in dictionary
cont_2090 = {'htimes':dtimes,'hms':a1,'hss':a1sd} # pack data into a dictionary
model = ['aff','mum','delth'] # the class is setup so that you can choose a list of parameters and it will automatically determine which model structure to use
pmod = all_mods(cont_2090,model) # setup the object for this sample dataset and the specific model

# plot 
f1,ax1 = plt.subplots()
pmod.plot_data(ax1)
# pmod.do_fitting(ax1) # this function will do the fitting and also plot the best fits to the axes (not sure if this is best)
pmod.double_labels(ax1) # automatically add axes labels with appropriate scales

# st.pyplot(plt)





def main():
    df = load_data()
    page = st.sidebar.selectbox("SELECT A PAGE", ["Homepage","Predator Free Growth Curve page"," Predator-Prey Growth curve page"])

    if page == "Homepage":
    	st.title("tHE APP : mikroDyno.")
        st.markdown(" ### Welcome to mikroDyno, a simple app to fit dynamic models to laboratory growth curves.")
        st.markdown(" #### Do you want to work with:")
        st.write("a) Growth curves (without a predator)?")
        st.markdown("b) Growth curves with a host preyed upon by a virus or a pathogenic bacteria?")
        st.markdown(" ### Please select a page on the dashboard on the left?")


    elif page == "Predator Free Growth Curve page":
    	st.pyplot(plt)
        st.markdown('# Which type of mechanism do you think might be important in explaining these dynamics?')
        st.markdown('a)Nutrient limitation')
        st.markdown('b)Cellular damage (e.g. due to toxins)')
        if st.button(" RUN Model"):
        	st.write("do sth")

	elif page == "Predator-Prey Growth curve page":
		st.markdown("Here is the data (plot of data)")
        st.markdown('# Which type of mechanism do you think might be important in explaining these dynamics?')
        st.markdown('a)Host-nutrient limitation')
        st.markdown('b)Decay of the predator')
    	Inf_states = st.radio("How many infection states do you want to account for?",('One', 'Two', 'Three'))
    	if Inf_states== 'One':
    		st.write("print equation one.")
    	else:
    		st.write("do nothing.")
    
    

@st.cache
def load_data():
    df = ss
    return df


