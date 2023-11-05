from taipy import Gui
from taipy import Config
from taipy import Core
import perscription
import help
import schedule
import home
import setting
from taipy.gui import Markdown

page_1 = """
<h3 class="h5">ManagMed</h3>
<|navbar|>
<|toggle|theme|class_name=sidebar|>
<|submit|button|on_action=submit_scenario|>
"""
#page 2 is home

#page 3 is Settings
# page 4 is Perscription

#page 5 is Help

#page 6 is Schedule

#content = 
input_name = ""
input_password = ""
#message = ""


def submit_scenario(state):
    state.scenario.input_name.write(state.input_name)
    state.scenario.submit(wait=True)
    state.message = state.scenario.message.read()

if __name__ == "__main__":
    #"""<|sidebar|Inside the container|>"""
    pages = {
        "Login": page_1,
        "Home": home.page_2,
        "Settings": setting.page_3,
        "Perscriptions": perscription.page_4,
        "Help": help.page_5,
        "Scheduele": schedule.page_6
    }
    gui = Gui(pages=pages)
    gui.run(stylekit=False)
    stylekit = {
        "color_primary": "#BADA55",
        "color_secondary": "#O0FFE",
    }
    gui.run(stylekit=stylekit)
    gui.run(dark_mode=True)
    #Core().run()