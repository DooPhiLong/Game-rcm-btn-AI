import streamlit as st
import pandas as pd
import textwrap
import random

@st.cache_data(persist=True)
def getdata():
    df = pd.read_csv('game_rcm_data.csv')
    return df

df = getdata()

# Sidebar
st.sidebar.markdown('<strong><span style="color: #8B2500;font-size: 26px;"> Game recommendation</span></strong>',unsafe_allow_html=True)
st.sidebar.image('pexels-pixabay-275033.jpg', use_column_width=True)
st.sidebar.markdown('<strong><span style="color: #EE4000;font-size: 26px;">:slot_machine: Choose your game !!!</span></strong>',unsafe_allow_html=True)
ph = st.sidebar.empty()
selected_game = ph.selectbox('Select one of games '
                             'from the menu: (you can type it as well)',
                             [''] + df['game_name'].to_list(), key='default',
                             format_func=lambda x: 'Select a game' if x == '' else x)

if selected_game:

    # DF query
    cluter = df[df["game_name"] == selected_game]["cluster"].tolist()
    matches = df[df["cluster"] == cluter[0]].reset_index(drop=True)
    topic = matches["Topic"].tolist()[0]

    #st.markdown("# The recommended games for {} with topic {} are:".format(selected_game, topic ))
    markdown_text = f"""
        <h1 >
            The recommended games for <span style="color:#DC143C;">{selected_game}</span> with topic <span style="color:#DC143C;">{topic}</span>
                    </h1>
                    """
    # Hiển thị chuỗi markdown với HTML và CSS
    st.markdown(markdown_text, unsafe_allow_html=True)

    
    def switch_case(topic):
        switch = {
            "Exploration & Adventure ": "adventure_game.mp4",
            "Fight in teams & gun battle": "gun_battle_game.mp4",
            "Clothes & fashion": "clothes.mp4",
            "Sport": "sport.mp4",
            "IQ test & puzzle": "puzzle.mp4",
            "Jump-scare & horror": "horror.mp4",
            "Multiplayer online battle arena": "MOBA.mp4"
        }
        return switch.get(topic)
    

    st.video(switch_case(topic))

    


    for idx, row in matches.iterrows():
        st.markdown('### {} - {}'.format(str(idx + 1), row['game_name']))
        #st.markdown('{}'.format(row['plots']))
        st.markdown('{} [Detail]({})'.format(row['plots'],row['link'] ))

else:

        st.markdown('# Game recommendation :video_game:')
        st.text('')
        st.markdown('> _You have  just finished an amazing game, and would like '
                    'to get recommendations for similar games?_')
        st.text('')
        st.markdown("This app lets you select a game from the dropdown menu and you'll get five "
                    'recommendations that are the closest to your game according to the gameplay and/or plot.')
        st.text('')
        st.warning(':point_left: Select a game from the dropdown menu!')
        
        
        
        
        
        
        
        
        
        
        
        
        
        