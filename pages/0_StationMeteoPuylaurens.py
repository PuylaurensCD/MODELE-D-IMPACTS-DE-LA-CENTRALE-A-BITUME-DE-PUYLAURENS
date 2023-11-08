# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any

import numpy as np

import streamlit as st
from streamlit.hello.utils import show_code
import pandas as pd
import datetime
import matplotlib.pyplot as plt

meteo = pd.read_csv('./DATA/METEO/meteo_puylaurens.csv', sep=';', skiprows=3)
date = pd.to_datetime(meteo.iloc[:, 0], format="%d/%m/%y")

def data_explore() -> None:

    # set time series
    start_date = st.sidebar.date_input('Début de période', date[0]+datetime.timedelta(days=5))
    end_date = st.sidebar.date_input('Fin de période', date[len(date)-1])

    filtre = (date>= pd.to_datetime(start_date)) & (date<= pd.to_datetime(end_date))
    meteo_slice = meteo[filtre]
    header = meteo.columns[1:]
    st.dataframe(meteo_slice)

    choice = ['Température (°C)', 'Précipitation (mm) & Humidité (%)', 'Pression (hPa)', 'Vitesse des vents (m/s)', 'Rose des vents', 'Propagation des particules']

    to_plot = st.sidebar.selectbox("Quelle(s) donnée(s) afficher ?", choice)

    if to_plot == 'Température (°C)':
        fig, ax = plt.subplots()
        ax.plot(date[filtre], meteo_slice['Temp_Moy '], c='k')
        ax.plot(date[filtre], meteo_slice['T_MEAN'], c='k') 
        ax.fill_between(date[filtre], meteo_slice['T_LOW'], meteo_slice['T_HIGH'], color='gray', alpha=.5, linewidth=0)
        ax.fill_between(date[filtre], meteo_slice['Temp_Min'], meteo_slice['Temp_Max'], color='gray', alpha=.5, linewidth=0)
        ax.set_xlabel("Date")
        ax.set_ylabel(to_plot)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
        st.pyplot(fig)

    elif to_plot == 'Précipitation (mm) & Humidité (%)':
        fig, ax = plt.subplots()
        ax2 = ax.twinx()
        ax.bar(date[filtre], meteo_slice['RAIN'], color='dodgerblue', alpha=0.5, edgecolor=None, width=datetime.timedelta(days=1))
        ax.bar(date[filtre], meteo_slice['Precipitation [mm]'], color='dodgerblue', alpha=0.5, edgecolor=None, width=datetime.timedelta(days=1))
        ax2.fill_between(date[filtre], meteo_slice['Humidite_Min [%]'], meteo_slice['Humidite_Max [%]'], color='gray', alpha=.5, linewidth=0)
        ax.plot(date[filtre], meteo_slice['Humidite_Moy [%]'], c='k') 
        ax.set_xlabel("Date")
        ax.set_ylabel(to_plot.split('&')[0])
        ax2.set_ylabel(to_plot.split('&')[1])
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
        st.pyplot(fig)

    elif to_plot == 'Pression (hPa)':
        fig, ax = plt.subplots()
        ax.fill_between(date[filtre], meteo_slice['Pression_Min [hPa]'], meteo_slice['Pression_Max [hPa]'], color='gray', alpha=.5, linewidth=0)
        ax.set_xlabel("Date")
        ax.set_ylabel(to_plot)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
        st.pyplot(fig)

    elif to_plot == 'Vitesse des vents (m/s)':
        fig, ax = plt.subplots()
        ax.fill_between(date[filtre], meteo_slice[header[20]]/3.6, meteo_slice[header[18]]/3.6, color='gray', alpha=.5, linewidth=0)
        ax.plot(date[filtre], meteo_slice[header[19]]/3.6, c='k')
        ax.fill_between(date[filtre], meteo_slice[header[20]]/3.6, meteo_slice['HIGH']/3.6, color='gray', alpha=.5, linewidth=0)
        ax.plot(date[filtre], meteo_slice['AVG_WIND_SPEED']/3.6, c='k')        
        ax.set_xlabel("Date")
        ax.set_ylabel(to_plot)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
        st.pyplot(fig)

    elif to_plot == 'Rose des vents':
        v = meteo_slice[header[19]]/3.6
        vmax = meteo_slice[header[18]]/3.6
        vdir = meteo_slice['DOM_DIR']
        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
        ax.set_theta_direction('clockwise')
        ax.set_theta_zero_location('N')
        v1 = vdir[v <2]
        v2 = vdir[(v <3) & (v >=2)]
        v3 = vdir[(v <5) & (v >=3)]
        v4 = vdir[(v <6) & (v >=5)]
        v5 = vdir[v >=6]
        n1, bins = np.histogram(v1[~np.isnan(v1)], range=(0, 360), bins=36)
        n2, _ = np.histogram(v2[~np.isnan(v2)], range=(0, 360), bins=36)
        n3, _ = np.histogram(v3[~np.isnan(v3)], range=(0, 360), bins=36)
        n4, _ = np.histogram(v4[~np.isnan(v4)], range=(0, 360), bins=36)
        n5, _ = np.histogram(v5[~np.isnan(v5)], range=(0, 360), bins=36)  
        ins = np.asarray([[b, b] for b in bins[1:]]).flatten()
        bins = np.concatenate([[bins[0]], ins])
        n1 = np.repeat(n1, 2)
        n2 = np.repeat(n2, 2)
        n3 = np.repeat(n3, 2)
        n4 = np.repeat(n4, 2)
        n5 = np.repeat(n5, 2)
        n1 = np.insert(n1, len(n1), n1[0])
        n2 = np.insert(n2, len(n2), n2[0])
        n3 = np.insert(n3, len(n3), n3[0])
        n4 = np.insert(n4, len(n4), n4[0])
        n5 = np.insert(n5, len(n5), n5[0])
        dct_color = {'< 2 m/s':'navy', '[2, 3[ m/s':'dodgerblue', '[3, 5[ m/s':'mediumseagreen', '[5, 6[ m/s':'gold', '>= 6 m/s':'crimson'}                                    
        n = np.asarray([n1, n2, n3, n4, n5])
        ax.stackplot(np.radians(bins), 100*n/np.sum(n), labels=['< 2 m/s', '[2, 3[ m/s', '[3, 5[ m/s', '[5, 6[ m/s', '>= 6 m/s'], 
                 colors = [dct_color.get(l, '#9b59b6') for l in ['< 2 m/s', '[2, 3[ m/s', '[3, 5[ m/s', '[5, 6[ m/s', '>= 6 m/s']])
        ax.set_xticklabels(['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'])
        ax.legend()
        ax.set_title('Rose des vents - vitesses moyennes journalières (m/s)')
        st.pyplot(fig)

        fig2, ax2 = plt.subplots(subplot_kw={'projection': 'polar'})
        ax2.set_theta_direction('clockwise')
        ax2.set_theta_zero_location('N')
        v1 = vdir[vmax <2]
        v2 = vdir[(vmax <3) & (vmax >=2)]
        v3 = vdir[(vmax <5) & (vmax >=3)]
        v4 = vdir[(vmax <6) & (vmax >=5)]
        v5 = vdir[vmax >=6]
        n1, bins = np.histogram(v1[~np.isnan(v1)], range=(0, 360), bins=36)
        n2, _ = np.histogram(v2[~np.isnan(v2)], range=(0, 360), bins=36)
        n3, _ = np.histogram(v3[~np.isnan(v3)], range=(0, 360), bins=36)
        n4, _ = np.histogram(v4[~np.isnan(v4)], range=(0, 360), bins=36)
        n5, _ = np.histogram(v5[~np.isnan(v5)], range=(0, 360), bins=36)  
        ins = np.asarray([[b, b] for b in bins[1:]]).flatten()
        bins = np.concatenate([[bins[0]], ins])
        n1 = np.repeat(n1, 2)
        n2 = np.repeat(n2, 2)
        n3 = np.repeat(n3, 2)
        n4 = np.repeat(n4, 2)
        n5 = np.repeat(n5, 2)
        n1 = np.insert(n1, len(n1), n1[0])
        n2 = np.insert(n2, len(n2), n2[0])
        n3 = np.insert(n3, len(n3), n3[0])
        n4 = np.insert(n4, len(n4), n4[0])
        n5 = np.insert(n5, len(n5), n5[0])
        dct_color = {'< 2 m/s':'navy', '[2, 3[ m/s':'dodgerblue', '[3, 5[ m/s':'mediumseagreen', '[5, 6[ m/s':'gold', '>= 6 m/s':'crimson'}                                    
        n = np.asarray([n1, n2, n3, n4, n5])
        ax2.stackplot(np.radians(bins), 100*n/np.sum(n), labels=['< 2 m/s', '[2, 3[ m/s', '[3, 5[ m/s', '[5, 6[ m/s', '>= 6 m/s'], 
                 colors = [dct_color.get(l, '#9b59b6') for l in ['< 2 m/s', '[2, 3[ m/s', '[3, 5[ m/s', '[5, 6[ m/s', '>= 6 m/s']])
        ax2.set_xticklabels(['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'])
        ax2.legend()
        ax2.set_title('Rose des vents - vitesses maximales journalières (m/s)')
        st.pyplot(fig2)

    elif to_plot == 'Propagation des particules':
        st.markdown("""
                    Supposons que nous représentions le déplacement moyen d'une particule par jour sur la plage temporelle choisis.
                    \n Cet outil permet de voir à quelle vitesse et dans quelle direction cette particule se déplace (Nord en haut).
                    """)
        v = meteo_slice[header[19]]/3.6
        vdir = meteo_slice['DOM_DIR']
        fig3, ax3 = plt.subplots()
        v = v.to_numpy()
        time = st.sidebar.slider("Choisir un temps après émission (seconde)", value=1., min_value=0.1, max_value=10., step=0.1)
        u_vent_unit = np.asarray([np.sin(vdir*np.pi/180), np.cos(vdir*np.pi/180)]).T*-1
        u_vent = u_vent_unit*v[:, np.newaxis]*time
        cmap= plt.get_cmap('jet')
        cvv = v/np.nanmax(v)
        for dx, dy, c in zip(u_vent[:, 0], u_vent[:, 1], cvv):
            c = cmap(c)
            ax3.annotate("", xytext=(dx,dy),xy=(dx+0.001*dx,dy+0.001*dy), 
            arrowprops=dict(arrowstyle="->", color=c), size = 10, alpha=0.6)
        ax3.scatter(0, 0, c='k', s=100)
        ax3.set_facecolor('xkcd:gray')
        ax3.set_aspect('equal')
        ax3.grid()
        ax3.set_xlim(-7, 7)
        ax3.set_ylim(-7, 7)
        ax3.set_xlabel(f"Position en abcisse d'une particule \n {time}s après son émission à l'origine (m)")
        ax3.set_ylabel(f"Position en ordonnée d'une particule \n {time}s après son émission à l'origine (m)")
        st.pyplot(fig3)


    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    st.button("Re-run")


st.set_page_config(page_title="Les données", page_icon="📹")
st.markdown("# Les données de la station météo de Puylaurens")
st.sidebar.header("Les données")
st.markdown(
    """
    Cette page permet d'explorer et de configurer les données d'entrées.
    
    La météo : historique enregistré à cette [station](https://puylaurens.payrastre.fr).
    
    Il est possible de sélectionner une période de début et de fin dans le panneau latéral.
    """
)

data_explore()
