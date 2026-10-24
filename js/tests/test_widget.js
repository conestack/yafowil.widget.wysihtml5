import $ from 'jquery';
import { WysiHTML5Widget } from '../src/widget.js';

QUnit.module('WysiHTML5Widget', (hooks) => {
    let container, calls;

    hooks.beforeEach(() => {
        container = $('<div />').appendTo('body');
        calls = [];
        // mock bootstrap3-wysihtml5 jQuery plugin
        $.fn.wysihtml5 = function (options) {
            calls.push([this, options]);
            return this;
        };
    });
    hooks.afterEach(() => {
        container.remove();
        delete $.fn.wysihtml5;
    });

    QUnit.test('initialize', (assert) => {
        const el = $('<textarea class="wysihtml5" />').appendTo(container);
        const other = $('<textarea class="other" />').appendTo(container);
        WysiHTML5Widget.initialize(container);

        const wid = el.data('yafowil-wysihtml5');
        assert.true(wid instanceof WysiHTML5Widget);
        assert.true(wid.elem.is(el));
        assert.strictEqual(other.data('yafowil-wysihtml5'), undefined);
        assert.strictEqual(calls.length, 1);
        assert.true(calls[0][0].is(el));
        assert.deepEqual(calls[0][1], {
            stylesheets: ['/++resource++yafowil-wysihtml5/bootstrap3-wysihtml5/wysiwyg-color.css'],
        });
    });

    QUnit.test('initialize respects context', (assert) => {
        const el = $('<textarea class="wysihtml5" />').appendTo(container);
        WysiHTML5Widget.initialize($('<div />'));
        assert.strictEqual(el.data('yafowil-wysihtml5'), undefined);
        assert.strictEqual(calls.length, 0);
    });
});
