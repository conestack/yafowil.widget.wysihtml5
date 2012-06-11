/* 
 * yafowil wysihtml5 widget
 * 
 * Optional: bdajax
 */

if (typeof(window['yafowil']) == "undefined") yafowil = {};

(function($) {

    $(document).ready(function() {
        // initial binding
        yafowil.wysihtml5.binder();
        
        // add after ajax binding if bdajax present
        if (typeof(window['bdajax']) != "undefined") {
            $.extend(bdajax.binders, {
                wysihtml5_binder: yafowil.wysihtml5.binder
            });
        }
    });
    
    $.extend(yafowil, {
        
        wysihtml5: {
            
            binder: function(context) {

                var editor = new wysihtml5.Editor("textarea.wysihtml5", {
                    parserRules:  wysihtml5ParserRules,
                    toolbar:      null,
                    autoLink:     true,
                    parser:       wysihtml5.dom.parse || Prototype.K,
                    composerClassName: "wysihtml5-editor",
                    bodyClassName:     "wysihtml5-supported",
                    allowObjectResizing:  true,
                    supportTouchDevices:  true
                });
                var wysihtml5_resize_iframe = function() {
                    editor.composer.iframe.style.height = editor.composer.element.scrollHeight + "px";
                };
                editor.observe("load", function () {
                    editor.composer.element.addEventListener("keyup", wysihtml5_resize_iframe, false);
                    editor.composer.element.addEventListener("blur", wysihtml5_resize_iframe, false);
                    editor.composer.element.addEventListener("focus", wysihtml5_resize_iframe, false);
                });

            }
        }
    });



})(jQuery);
