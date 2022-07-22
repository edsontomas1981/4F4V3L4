function excluiProposta(id) {
    proposta = document.getElementById('excluir')
    proposta.value = id
}

function alteraProposta(id) {
    let valor = "valor" + id
    let obs = "observacao" + id
    let datIni = "datIni" + id
    let prazo = "prazo" + id
    console.log(valor, obs, datIni, prazo)
    proposta = document.getElementById('excluir')
    proposta.value = id
}