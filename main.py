from taipy import Gui
from taipy import Config
from taipy import Core
from os import environ as env

page_1 = """
# ManagMed
<|<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="500" zoomAndPan="magnify" viewBox="0 0 375 374.999991" height="500" preserveAspectRatio="xMidYMid meet" version="1.0"><defs><clipPath id="749ed33b4f"><path d="M 117 183 L 258 183 L 258 347 L 117 347 Z M 117 183 " clip-rule="nonzero"/></clipPath><clipPath id="53b0b963c3"><path d="M 187.5 0 L 375 187.5 L 187.5 375 L 0 187.5 Z M 187.5 0 " clip-rule="nonzero"/></clipPath><clipPath id="136d9d0114"><path d="M 187.5 0 L 375 187.5 L 187.5 375 L 0 187.5 Z M 187.5 0 " clip-rule="nonzero"/></clipPath><clipPath id="35dab84d43"><path d="M 117 28 L 258 28 L 258 186 L 117 186 Z M 117 28 " clip-rule="nonzero"/></clipPath><clipPath id="54e6bd64fc"><path d="M 187.5 0 L 375 187.5 L 187.5 375 L 0 187.5 Z M 187.5 0 " clip-rule="nonzero"/></clipPath><clipPath id="880945a325"><path d="M 187.5 0 L 375 187.5 L 187.5 375 L 0 187.5 Z M 187.5 0 " clip-rule="nonzero"/></clipPath><clipPath id="ee028a128f"><path d="M 127.964844 110.265625 L 156.605469 110.265625 L 156.605469 179.6875 L 127.964844 179.6875 Z M 127.964844 110.265625 " clip-rule="nonzero"/></clipPath><clipPath id="3a6f06fdf2"><path d="M 219.554688 110.265625 L 248.191406 110.265625 L 248.191406 179.6875 L 219.554688 179.6875 Z M 219.554688 110.265625 " clip-rule="nonzero"/></clipPath><clipPath id="850f695fb5"><path d="M 173.175781 67.683594 L 201.816406 67.683594 L 201.816406 179.675781 L 173.175781 179.675781 Z M 173.175781 67.683594 " clip-rule="nonzero"/></clipPath></defs><g clip-path="url(#749ed33b4f)"><g clip-path="url(#53b0b963c3)"><g clip-path="url(#136d9d0114)"><path fill="#004aad" d="M 257.46875 275.9375 L 257.402344 183.628906 L 117.527344 185.652344 L 117.519531 276.113281 L 117.53125 276.113281 C 117.550781 294 124.378906 311.878906 138.019531 325.519531 C 165.34375 352.84375 209.65625 352.84375 236.980469 325.519531 C 250.667969 311.832031 257.496094 293.878906 257.46875 275.9375 Z M 257.46875 275.9375 " fill-opacity="1" fill-rule="nonzero"/></g></g></g><g clip-path="url(#35dab84d43)"><g clip-path="url(#54e6bd64fc)"><g clip-path="url(#880945a325)"><path fill="#96cdec" d="M 257.332031 96.011719 C 256.625 79.09375 249.890625 62.390625 236.980469 49.480469 C 209.652344 22.152344 165.347656 22.152344 138.019531 49.480469 C 125.109375 62.390625 118.375 79.105469 117.671875 96.015625 L 117.527344 96.015625 L 117.527344 185.652344 L 257.402344 183.628906 Z M 257.332031 96.011719 " fill-opacity="1" fill-rule="nonzero"/></g></g></g><g clip-path="url(#ee028a128f)"><path fill="#012656" d="M 156.605469 110.265625 L 156.605469 179.6875 L 127.964844 179.6875 L 127.964844 110.265625 Z M 156.605469 110.265625 " fill-opacity="1" fill-rule="nonzero"/></g><g clip-path="url(#3a6f06fdf2)"><path fill="#012656" d="M 248.191406 110.265625 L 248.191406 179.6875 L 219.554688 179.6875 L 219.554688 110.265625 Z M 248.191406 110.265625 " fill-opacity="1" fill-rule="nonzero"/></g><g clip-path="url(#850f695fb5)"><path fill="#012656" d="M 201.816406 67.683594 L 201.816406 179.675781 L 173.175781 179.675781 L 173.175781 67.683594 Z M 201.816406 67.683594 " fill-opacity="1" fill-rule="nonzero"/></g></svg>|image|>
[Login](http://localhost:3000)
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

if __name__ == "__main__":
    pages = {
        "Login": page_1,
        "Home": page_2,
        "Settings": page_3,
        "Prescriptions": page_4,
        "Help": page_5,
        "Schedule": page_6
    }
    gui = Gui(pages=pages)
    gui.run(dark_mode=True, host="0.0.0.0", port=env.get("PORT", 5000))
    #Core().run()