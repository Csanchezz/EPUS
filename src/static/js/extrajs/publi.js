function get_publications(ini, out){
  $.ajax({
    url: tecnico+"/"+ini+'/'+out+"/",
    dataType: "json",
    success: function(respuesta){
      if (respuesta.tablainf.length == 0) {
        var texto = "<div class='box box-danger'><div class='box-body'>"
        texto += " <h4 align='center'> No se encontraron resultados <h4></div> </div>"
      } else{
        var texto = "<div class='box box-success'><table class='table table-hover table-striped'>";
        texto += "<thead>";
        texto += "<tr>";
        texto += "<th>No. Salida</th>";
        texto += "<th>Técnico</th>";
        texto += "<th>Fecha</th>";
        texto += "<th>Equipo</th>";
        texto += "<th>Cantidad</th>";
        texto += "</tr>";
        texto += "</thead>";
        $.each(respuesta.tablainf, function(index, item){
          texto += "<tr><td>" + item.id + "</td><td>"+ item.tecnico + "</td><td>"+ item.fecha + "</td><td>" + item.equipo +"</td><td>" + item.cantidad +"</td></tr>";
        })
        texto += "</table></div>";
      };
      document.getElementById('informe').innerHTML = texto;
      

    }
  });
}
