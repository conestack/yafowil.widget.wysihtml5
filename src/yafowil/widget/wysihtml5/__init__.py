import os

def register():
    import widget

def get_resource_dir():
    return os.path.join(os.path.dirname(__file__), 'resources')

def get_js(thirdparty=True):
    js = list()
    if thirdparty:
        js.append('bootstrap-wysihtml5/jscripts/tiny_mce/tiny_mce.js')
    js.append('wysihtml5/dist/wysihtml5-0.3.0.min.js')
    js.append('wysihtml5/dist/wysihtml5-0.3.0.min.js')
    js.append('widget.js')
    return js

def get_css(thirdparty=True):
    return list()
