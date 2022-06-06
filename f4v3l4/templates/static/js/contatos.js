var lista = []
function limpaCampos(){
    document.getElementById('contato').value=("");
    document.getElementById('tipo').value=("Telefone");
}

function insereNaTabela(){

    var lista = []
    var tipo = document.getElementById('tipo').value;
    var contato= document.getElementById('contato').value;
    
    var corpoTabela = document.querySelector('tbody');

    var tr= document.createElement('tr');
    var tdContato= document.createElement('td');
    var tdTipo= document.createElement('td');
    
    tdTipo.textContent = tipo;
    tdContato.textContent = contato;
    
    tr.appendChild(tdTipo);
    tr.appendChild(tdContato);
    corpoTabela.appendChild(tr);
    lista.push(tipo)
    console.log(lista)
    limpaCampos();
}