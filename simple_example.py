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
    
    # elif page == "Homepage":
    # 	st.title("tHE APP : mikroDyno.")
    #     st.markdown(" ### Welcome to mikroDyno, a simple app to fit dynamic models to laboratory growth curves.")
    #     st.markdown(" #### Do you want to work with:")
    #     st.write("a) Growth curves (without a predator)?")
    #     st.markdown("b) Growth curves with a host preyed upon by a virus or a pathogenic bacteria?")
    #     st.markdown(" ### Please select a page on the dashboard on the left?")

   	
        
       

        # x_axis = st.selectbox("Choose a variable for the x-axis", df.columns, index=3)
        # y_axis = st.selectbox("Choose a variable for the y-axis", df.columns, index=4)
        # visualize_data(df, x_axis, y_axis)


@st.cache
def load_data():
    df = ss
    return df

def visualize_data(df, x_axis, y_axis):
    graph = alt.Chart(df).mark_circle(size=60).encode(
        x=x_axis,
        y=y_axis,
        color='Origin',
        tooltip=['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
    ).interactive()

    st.write(graph)

if __name__ == "__main__":
    main()




# import plotly.express as px

# data = {"x": [1, 2, 3, 4], "y": [2, 4, 6, 8]}

# st.selectbox("Select x", options=["A", "B"])
# st.selectbox("Select y", options=["A", "B"])
# dataframe = pd.DataFrame(data)
# fig = px.scatter(dataframe, x="x", y="x", title="Plot 1", height=400)
# st.plotly_chart(fig, height=400)
# st.slider("Select min and max", min_value=1, max_value=10, value=[1, 4])


# df = pd.read_csv("https://github.com/MaartenGr/boardgame/raw/master/files/boardgame_new.csv").head()
# st.write(df)

# # from vega_datasets import data
# # import streamlit as st
# # import altair as alt