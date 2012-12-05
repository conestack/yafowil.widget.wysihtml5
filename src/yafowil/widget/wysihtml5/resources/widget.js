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

                $('textarea.wysihtml5', context).each(function(event) {

                    var elem = $(this);
                    var options = elem.data();
                    if (options.stylesheets === undefined) { options.stylesheets = []; }
                    options.stylesheets.push('/++resource++yafowil.widget.wysihtml5/bootstrap-wysihtml5/lib/css/wysiwyg-color.css');
                    var editor = elem.wysihtml5(options);

                    /*
                    var editor = elem.wysihtml5(options).data("wysihtml5").editor;

                    var wysihtml5_resize_iframe = function() {
                        editor.composer.iframe.style.height = editor.composer.element.scrollHeight + "px";
                    };
                    editor.observe("load", function () {
                        editor.composer.element.addEventListener("keyup", wysihtml5_resize_iframe, false);
                        editor.composer.element.addEventListener("blur", wysihtml5_resize_iframe, false);
                        editor.composer.element.addEventListener("focus", wysihtml5_resize_iframe, false);
                    });
                    */
                });

            }
        }
    });



})(jQuery);
