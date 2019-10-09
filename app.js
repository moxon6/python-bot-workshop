editor = window.ace.edit("editor")
editor.setTheme("ace/theme/solarized_dark")
editor.session.setMode("ace/mode/python")
editor.focus()
editor.scrollToRow(0)
editor.gotoLine(0)
editor.setOptions({
    'enableLiveAutocompletion': true,
    'highlightActiveLine': false,
    'highlightSelectedWord': true
})