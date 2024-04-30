import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df = pd.read_csv(link, sep=',')
dfdrop = df.drop(['continent'], axis=1)
tab1, tab2, tab3 = st.tabs(["DataFrame Complet", "HeatMap", "Filtre"])
with tab1: 
    st.write('DataFrame Complet')
    st.dataframe(df)
    
with tab2:    
    st.write('HeatMap de correlation')
    viz_correlation = sns.heatmap(dfdrop.corr(), 
                                    center=0,
                                    cmap = sns.color_palette("vlag", as_cmap=True)
                                    )

    st.pyplot(viz_correlation.figure)

with tab3:
    continent = st.sidebar.multiselect(
        "Quel continent souhaitez-vous? :warning: :warning: Ce filtre ne fonctionne que dans l'onglet Filtre ",
        options=df.sort_values(by="continent",ascending=False).continent.unique(),
        #default=df["startYear"].unique(),
        default=None

    )


    df_selection = df.query(
        "continent == @continent"
    )
    if df_selection.empty:
        st.error(" :warning: En l'absence de résultat, merci de choisir un continent.")
        st.stop() # This will halt the app from further execution.

    st.dataframe(df_selection)
