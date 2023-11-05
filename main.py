from taipy import Gui
from taipy import Config
from taipy import Core

page_1 = """
<h3 class="h5">ManagMed</h3>
<|{content}|image|label=|on_action=function_name|>

<|submit|button|on_action=submit_scenario|>

"""

page_2 = """
<h3>testing something</h3>

"""

def submit_scenario(state):
    state.scenario.input_name.write(state.input_name)
    state.scenario.submit(wait=True)
    state.message = state.scenario.message.read()



Gui(page_1).run(use_reloader=True)  # use_reloader=True if you are in development
Gui(page_2).run(use_reloader=True)

if __name__ == "__main__":
    Core().run()