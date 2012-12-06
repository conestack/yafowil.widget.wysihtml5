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

                    // options processing
                    options.stylesheets = []; // bootstrap-wysihtml5 tries to load own stylesheets, which fails. so set back anyways.
                    options.stylesheets.push('/++resource++yafowil.widget.wysihtml5/widget.css');
                    if (options.color===true) {
                        // options.stylesheets = [];
                        options.stylesheets.push('/++resource++yafowil.widget.wysihtml5/bootstrap-wysihtml5/lib/css/wysiwyg-color.css');
                    }
                    if (options.justify === true) {

                        $.fn.wysihtml5.defaultOptions.justify = true; // extend defaultOptions

                        options.customTemplates = {
                            justify: function(locale, options) {
                                var size = (options && options.size) ? ' btn-'+options.size : '';
                                return "<li>" +
                                  "<div class='btn-group'>" +
                                      "<a class='btn" + size + "' data-wysihtml5-command='justifyLeft' title='Align left'><i class='icon-align-left'></i></a>" +
                                      "<a class='btn" + size + "' data-wysihtml5-command='justifyCenter' title='Align center'><i class='icon-align-center'></i></a>" +
                                      "<a class='btn" + size + "' data-wysihtml5-command='justifyRight' title='Align right'><i class='icon-align-right'></i></a>" +
                                  "</div>" +
                                "</li>";
                            }
                        };

                        options.parserRules = {
                            classes: {
                                "wysiwyg-text-align-left": 1,
                                "wysiwyg-text-align-center": 1,
                                "wysiwyg-text-align-right": 1
                            }
                        };

                    }

                    // create the editor
                    var editor = elem.wysihtml5('deepExtend', options).data("wysihtml5").editor;

                    // use some extra features
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
