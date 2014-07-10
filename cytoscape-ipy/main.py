import uuid
import json
import os

def init_ipynb():
    from IPython.core.display import display, HTML

    path = os.path.abspath(os.path.dirname(__file__)) + '/init_ipy.js'
    html = open(path).read()
    return display(HTML(html))

def plot(nodes=None, edges=None):
    from jinja2 import Template
    from IPython.core.display import display, HTML

    if nodes==None:
        nodes = [
            { 'data': { 'id': 'a' } },
            { 'data': { 'id': 'b' } },
            { 'data': { 'id': 'c' } },
            { 'data': { 'id': 'd' } },
            { 'data': { 'id': 'e' } }
        ]

    if edges==None:
        edges = [
            { 'data': { 'id': 'a', 'weight': 1, 'source': 'a', 'target': 'e' } },
            { 'data': { 'id': 'ab', 'weight': 3, 'source': 'a', 'target': 'b' } },
            { 'data': { 'id': 'be', 'weight': 4, 'source': 'b', 'target': 'e' } },
            { 'data': { 'id': 'bc', 'weight': 5, 'source': 'b', 'target': 'c' } },
            { 'data': { 'id': 'ce', 'weight': 6, 'source': 'c', 'target': 'e' } },
            { 'data': { 'id': 'cd', 'weight': 2, 'source': 'c', 'target': 'd' } },
            { 'data': { 'id': 'de', 'weight': 7, 'source': 'd', 'target': 'e' } }
        ]

    path = os.path.abspath(os.path.dirname(__file__)) + '/template.html'
    template = Template(open(path).read())
    html = template.render(nodes=json.dumps(nodes), edges = json.dumps(edges), uuid="cy" + str(uuid.uuid4()))
    return display(HTML(html))


