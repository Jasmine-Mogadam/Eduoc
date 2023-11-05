from taipy import Gui
from taipy import Config
from taipy import Core
#from taipy.gui import Markdown

#<|{content}|image|label=|on_action=function_name|>
page_1 = """
<|navbar|>
<h3 class="h5">ManagMed</h3>
<|button|>
<|submit|button|on_action=submit_scenario|>


"""

page_2 = """
<|navbar|>
<h3>testing something</h3>

"""
page_3 = """
<|navbar|>
<h3>testing something</h3>

"""
page_4 = """
<|navbar|>
<h3>testing something</h3>

"""
page_5 = """
<|navbar|>
<h3>testing something</h3>

"""
page_6 = """
<|navbar|>
<h3>testing something</h3>

"""
#content = 
input_name = ""
input_password = ""
#message = ""


def submit_scenario(state):
    state.scenario.input_name.write(state.input_name)
    state.scenario.submit(wait=True)
    state.message = state.scenario.message.read()

if __name__ == "__main__":
    pages = {
        "Login": page_1,
        "Home": page_2,
        "Settings": page_3,
        "Perscriptions": page_4,
        "Help": page_5,
        "Scheduele": page_6
    }
    gui = Gui(pages=pages)
    gui.run(dark_mode=True)
    #Core().run()