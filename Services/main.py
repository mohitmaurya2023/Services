import streamlit as st

from streamlit_option_menu import option_menu

import about, account, home, trending, your_posts

st.set_page_config(
    page_title = "Services",
)

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function,
        })

    def run():

        with st.sidebar:
            # st.info('👤 ' + st.session_state.username )
        
            app = option_menu(
                menu_title = "Services",
                options = ["Home", "Account", "About", "Trending", "Your Posts"],
                icons = ['house-fill', 'info-circle-fill', 'person-circle', 'trophy-fill','chat-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important", "background-color": "black"
                },
                "icon": {"color": "white", "font-size": "23px"},
                "nav-link": {"color":"white", "font-size": "20px", "text-align": "left", "margin":"0px"},
                "nav-link-selected": {"background-color": "#02ab21"},}
            )
        
        if app== 'Home':
            home.app()
        if app == 'Account':
            account.app()
        if app == 'Trending':
            trending.app()
        if app == 'About':
            about.app()
        if app == 'Your Posts':
            your_posts.app()
    
    run()