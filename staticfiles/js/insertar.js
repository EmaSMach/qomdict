function insertar() {
    let input = document.getElementById("searchin");
    let startPos = input.selectionStart;
    let endPos = input.selectionEnd;
    let contenido = input.value;
    let pparte = contenido.slice(0, startPos);
    let sparte = contenido.slice(endPos);
    const ychar = "ỹ";
    let fullStr = pparte + ychar + sparte;
    input.focus();
    input.value = fullStr;
    input.selectionStart = startPos + 1;
    input.selectionEnd = startPos + 1;
}


function teclado(event) {
    widget = event.target;
    if (event.altKey && event.keyCode == 89) {
        insertar();
    }
}

var inputBox = inp = document.getElementById("searchin");
btn = document.getElementById("btn-y");

btn.addEventListener("click", insertar, false);
inputBox.addEventListener("keydown", teclado, false);
