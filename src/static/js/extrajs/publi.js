function get_publications(ini, out){
  $.ajax({
    url: "get/"+ini+'/'+out+"/",
    dataType: "json",
    success: function(respuesta){
      if (respuesta.publicaciones.length == 0) {
        var texto = "<div class='box box-danger'><div class='box-body'>"
        texto += " <h4 align='center'> No se encontraron resultados <h4></div> </div>"
      } else{
        var texto = "";
        $.each(respuesta.publicaciones, function(index, item){
          texto += "<div class='col-md-6'>";
          texto += "<div class='box box-primary' style='height:350px;'>";
          texto += "<div class='box-header'>";
          texto += "<div class='box-title'>" + item.titulo + "</div></div>";
          texto += "<div class='box-body'><p>" + item.parrafo + "</p><img style='height:200px;display:block;margin:0 auto 0 auto;' src='../media/"+item.foto+" '></div></div></div>";
        })
      };
      document.getElementById('pub').innerHTML = texto;
      

    }
  });
}
