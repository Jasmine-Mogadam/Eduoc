from taipy import Gui
from taipy import Config
from taipy import Core

def build_message(name: str):
    return f"Hello {name}!"

input_name_data_node_cfg = Config.configure_data_node(id="input_name")
message_data_node_cfg = Config.configure_data_node(id="message")
build_msg_task_cfg = Config.configure_task("build_msg", build_message, input_name_data_node_cfg, message_data_node_cfg)
scenario_cfg = Config.configure_scenario("scenario", task_configs=[build_msg_task_cfg])
from taipy.gui import Markdown

page_1 = """
<h3 class="h5">ManagMed</h3>
<|{content}|image|label=|on_action=function_name|>

<|submit|button|on_action=submit_scenario|>

"""

page_2 = """
<h3>testing something</h3>

"""
#content = 
input_name = ""
input_password = ""
#message = ""


def submit_scenario(state):
    state.scenario.input_name.write(state.input_name)
    state.scenario.submit(wait=True)
    state.message = scenario.message.read()



Gui(page_1).run(use_reloader=True)  # use_reloader=True if you are in development
Gui(page_2).run(use_reloader=True)

if __name__ == "__main__":
    Core().run()