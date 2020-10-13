function insertar(input, str) {
    let startPos = input.selectionStart;
    let endPos = input.selectionEnd;
    let pparte = input.value.slice(0, startPos);
    let sparte = input.value.slice(endPos);
    input.focus();
    input.value = pparte + str + sparte;
    input.selectionStart = startPos + 1;
    input.selectionEnd = startPos + 1;
}

function atajo(event) {
    widget = event.target;
    // alt + y
    if (event.altKey && event.keyCode == 89) {
        insertar(widget, "ỹ");
    }
}

var inputBox = document.getElementById("search-box");
btn = document.getElementById("btn-y");

btn.addEventListener("click", function(){insertar(inputBox, "ỹ")}, false);
inputBox.addEventListener("keydown", atajo, false);
