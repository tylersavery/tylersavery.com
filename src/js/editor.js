import * as ace from 'brace'

import 'brace/mode/javascript'
import 'brace/mode/python'
import 'brace/mode/css'
import 'brace/theme/monokai'

export function initEditor() {

    document.querySelectorAll('.editor').forEach(function(container) {

        const language = container.getAttribute('data-language');
    
        const editor = ace.edit(container);
        editor.getSession().setMode(`ace/mode/${language}`);
        editor.setTheme("ace/theme/monokai");
        editor.setShowPrintMargin(false);
        editor.setReadOnly(true);
        editor.setFontSize(16);
        editor.getSession().setUseWrapMode(false);

        var lineHeight = editor.renderer.lineHeight;
        const doc = editor.getSession().getDocument();
        container.style.height = lineHeight * doc.getLength() + "px";
        editor.resize();
    
    });
}


