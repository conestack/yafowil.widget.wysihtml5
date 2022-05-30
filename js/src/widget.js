import $ from 'jquery';

export class WysiHTML5Widget {

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
