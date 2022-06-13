function limpaCampos(){
    document.getElementById('contato').value=("");
    document.getElementById('tipo').value=("Telefone");
}

function insereNaTabela(){

    var tipo = document.getElementById('tipo').value;
    var contato= document.getElementById('contato').value;
    var usuario = document.getElementById('usuario').value;
    var corpoTabela = document.querySelector('tbody');

    var tr= document.createElement('tr');
    var tdContato= document.createElement('td');
    var tdTipo= document.createElement('td');

    tdTipo.textContent = tipo;
    tdContato.textContent = contato;

    tr.appendChild(tdTipo);
    tr.appendChild(tdContato);
    corpoTabela.appendChild(tr);
    limpaCampos();
}

