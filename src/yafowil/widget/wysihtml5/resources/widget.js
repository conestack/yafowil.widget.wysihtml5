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

                    extra_keys = ['focus', 'resize'];

                    var elem = $(this);
                    var options = elem.data();

                    function make_options_extra(options, extra_keys) {
                        // cleanup api options object and move out extra options
                        var options_extra = {};
                        for (i=0;i<extra_keys.length;i++) {
                            key = extra_keys[i];
                            options_extra[key] = options[key];
                        delete options[key];
                        }
                        return options_extra;
                    }
                    options_extra = make_options_extra(options, extra_keys);

                    if (options.stylesheets === undefined) { options.stylesheets = []; }
                    if (options.color===true) {
                        options.stylesheets.push('/++resource++yafowil.widget.wysihtml5/bootstrap-wysihtml5/lib/css/wysiwyg-color.css');
                    }
                    var editor = elem.wysihtml5(options).data("wysihtml5").editor;

                    if (options_extra.focus === true) {
                        editor.on("load", function() {
                            editor.focus();
                        });
                    }
                    if (options_extra.resize === true) {
                        var wysihtml5_resize_iframe = function() {
                            editor.composer.iframe.style.height = editor.composer.element.scrollHeight + "px";
                        };
                        editor.observe("load", function () {
                            editor.composer.element.addEventListener("keyup", wysihtml5_resize_iframe, false);
                            editor.composer.element.addEventListener("blur", wysihtml5_resize_iframe, false);
                            editor.composer.element.addEventListener("focus", wysihtml5_resize_iframe, false);
                        });
                    }
                });

            }
        }
    });



})(jQuery);
