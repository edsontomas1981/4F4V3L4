function excContato(idExc){
    
    var id = document.getElementById('excluiId');
    var contato = document.getElementById('excluiContato');
    var tipo = document.getElementById('excluiTipo');

    var tdContato = document.getElementById('tdContato');
    var tdTipo = document.getElementById('tdTipo');

    id.value = idExc;
    contato.value = document.getElementById('contato'+idExc).textContent;
    tipo.value = document.getElementById('tipo'+idExc).textContent;
    contato.ariaDisabled = True;
    tipo.ariaDisabled = True;
        //var excTipo = document.getElementById(varAltTipo)
        ///var excContato = document.getElementById(varAltCont)
        //var excluiTipoContato = document.getElementById('excluiTipoContato')
        //var excluiContato = document.getElementById('excluiContato')
        //var idExcluiContato = document.getElementById("idExcluiContato")
        //excluiContato.value = excContato.textContent
        //excluiContato.value = excContato.textContent
        //idExcluiContato.value = id

    }
