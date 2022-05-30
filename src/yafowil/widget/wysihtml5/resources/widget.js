var yafowil_wysihtml5 = (function (exports, $) {
    'use strict';

    class WysiHTML5Widget {
        static initialize(context) {
            let resource_base = '/++resource++yafowil-wysihtml5';
            let color_css = resource_base + '/bootstrap3-wysihtml5/wysiwyg-color.css';
            $('textarea.wysihtml5', context).each(function() {
                new WysiHTML5Widget($(this), color_css);
            });
        }
        constructor(elem, color_css) {
            elem.data('yafowil-wysihtml5', this);
            this.elem = elem;
            this.elem.wysihtml5({stylesheets: [color_css]});
        }
    }

    $(function() {
        if (window.ts !== undefined) {
            ts.ajax.register(WysiHTML5Widget.initialize, true);
        } else if (window.bdajax !== undefined) {
            bdajax.register(WysiHTML5Widget.initialize, true);
        } else {
            WysiHTML5Widget.initialize();
        }
    });

    exports.WysiHTML5Widget = WysiHTML5Widget;

    Object.defineProperty(exports, '__esModule', { value: true });


    window.yafowil = window.yafowil || {};
    window.yafowil.wysihtml5 = exports;


    return exports;

})({}, jQuery);
