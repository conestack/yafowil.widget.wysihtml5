/*
 * yafowil wysihtml5 widget
 *
 * Optional: bdajax
 */

if (typeof(window.yafowil) == "undefined") yafowil = {};

(function($) {

    $(document).ready(function() {
        // initial binding
        yafowil.wysihtml5.binder();

        // add after ajax binding if bdajax present
        if (typeof(window.bdajax) != "undefined") {
            $.extend(bdajax.binders, {
                wysihtml5_binder: yafowil.wysihtml5.binder
            });
        }
    });

    $.extend(yafowil, {

        wysihtml5: {

            binder: function(context) {
                var resource_base = '/++resource++yafowil.widget.wysihtml5';
                var color_css = resource_base
                              + '/bootstrap3-wysihtml5/wysiwyg-color.css';
                $('textarea.wysihtml5', context).each(function(event) {
                    var elem = $(this);
                    // most options are taken from data attributes
                    elem.wysihtml5({stylesheets: [color_css]});
                });
            }
        }
    });

})(jQuery);
