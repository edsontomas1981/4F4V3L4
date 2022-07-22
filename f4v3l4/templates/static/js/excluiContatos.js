function excContato(idExc) {

    var id = document.getElementById('excluiId');
    var contato = document.getElementById('excluiContato');
    var tipo = document.getElementById('excluiTipo');

    id.value = idExc;
    contato.value = document.getElementById('contato' + idExc).textContent;
    tipo.value = document.getElementById('tipo' + idExc).textContent;
    contato.ariaDisabled = True;
}