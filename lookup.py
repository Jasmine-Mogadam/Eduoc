from taipy import Gui
from taipy.gui import Markdown

page_7="""
<|layout|columns=1fr auto 1fr|class_name=container align_columns_center|
<|part|class_name=pt_half pb_half|
<|Taipy App|text|height=30px|width=30px|>
|>
<|part|class_name=align_item_stretch|
<|navbar|lov={[("p1", "Page 1"), ("p2", "Page 2")]}|class_name=fullheight|>
|>
<|part|class_name=text_right|
<|toggle|theme|class_name=relative nolabel|>
|>
|>
"""
