import $ from 'jquery';

import {WysiHTML5Widget} from './widget.js';
export * from './widget.js';

$(function() {
    if (window.ts !== undefined) {
        ts.ajax.register(WysiHTML5Widget.initialize, true);
    } else if (window.bdajax !== undefined) {
        bdajax.register(WysiHTML5Widget.initialize, true);
    } else {
        WysiHTML5Widget.initialize();
    }
});
