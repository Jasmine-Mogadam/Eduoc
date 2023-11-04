from taipy import Gui
from taipy import Config
from taipy import Core

def build_message(name: str):
    return f"Hello {name}!"

input_name_data_node_cfg = Config.configure_data_node(id="input_name")
message_data_node_cfg = Config.configure_data_node(id="message")
build_msg_task_cfg = Config.configure_task("build_msg", build_message, input_name_data_node_cfg, message_data_node_cfg)
scenario_cfg = Config.configure_scenario("scenario", task_configs=[build_msg_task_cfg])

#page = """
# Hello World 🌍 with *Taipy*This is my first Taipy test app.
#And it is running fine!
#"""
page = """
Name: <|{input_name}|input|>
<|submit|button|on_action=submit_scenario|>

Message: <|{message}|text|>
"""

input_name = "Taipy"
message = None


def submit_scenario(state):
    state.scenario.input_name.write(state.input_name)
    state.scenario.submit(wait=True)
    state.message = scenario.message.read()



Gui(page).run(use_reloader=True)  # use_reloader=True if you are in development


if __name__ == "__main__":
    Core().run()