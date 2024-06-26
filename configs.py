# Hides Streamlit's excessive UI
remove_st_ui = """
<style>
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
</style>
"""

# Removes the anchors next to titles
no_anchors = """""" # Broken right now =(

# Removes the user settings menu
hide_settings = """
<style>div[data-testid="stToolbar"] { display: none;}</style>
"""

# Hides the 'made with streamlit' message when hosting
hide_made_with_s = """
            <style>
            [data-testid="stToolbar"] {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            </style>
            """