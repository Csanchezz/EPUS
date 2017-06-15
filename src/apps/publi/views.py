from django.shortcuts import render, get_object_or_404
from apps.publi.models import *
from apps.publi.forms import *
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from braces.views import LoginRequiredMixin, GroupRequiredMixin
from django.urls import reverse_lazy

class CreatePost(LoginRequiredMixin, GroupRequiredMixin, CreateView):
	group_required = [u"u_valle", ]
	model = Publicacion
	form_class = FormPublicacion
	template_name = "publi/crear_publi.html"
	success_url = reverse_lazy('view_post')
	


class ViewPost(LoginRequiredMixin, GroupRequiredMixin, ListView):
	group_required = [u"u_valle", ]
	model = Publicacion
	template_name = 'publi/view_publi.html'
	#if ind is None:
	#	ind = 1

	#if ind == 1:
	#	ini=0
	#else:
	#	inicio = ind-1
	#	iniq = inicio*4
	#	ini = iniq-1
	
	#out= ind*4

	#def get_context_data(self, **kwargs):
	 #   context = super(ViewPost, self).get_context_data(**kwargs)

	  #  return context

	#def count(self, ini, out):
	#	lista= Publicacion.objects.all()
	#	lista_q=lista.reverse()
	#	return

class EditPost(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
	group_required = [u"u_valle", ]
	model = Publicacion
	form_class = FormPublicacion
	pk_url_kwarg = 'post_pk'
	template_name = "publi/edit_publi.html"
	success_url = reverse_lazy('view_private_post')


def publico(request):
	latest_publications_list = Publicacion.objects.all().order_by('id')
	latest_list = latest_publications_list.reverse()


	final_list= latest_list[0:4]
	indice=[]
	for i in range(1,21):
		indice.append(i*4)

	template = 'publi/ver_publi.html'
	context = {
	'indice': indice,
	'list' : final_list,
	}
	return render(request, template, context)

#def error(request):
#	word= "Error en esto"
#	template = 'publi/error.html'
#	context = {
#	'word' : word,
#	}
#	return render(request, template, context)

def get_publications(request, ini, out):
	latest_publications_list = Publicacion.objects.all().order_by('id')
	latest_list = latest_publications_list.reverse()
    
    lista_vacia = []
    for salida in lista_entrada:
        lista_vacia.append({'id':salida.id, 'tecnico':str(salida.salida.tecnico), 'fecha': str(salida.salida.fecha), 'equipo':str(salida.equipo), 'cantidad': salida.cantidad})
    
    return HttpResponse(
            json.dumps({
                "tablainf": lista_vacia, 
                })
            )
