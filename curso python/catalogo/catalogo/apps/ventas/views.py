# vistas de la aplicacion ventas
from django.shortcuts import render_to_response
from django.template import RequestContext
from catalogo.apps.ventas.forms import add_product_form
from catalogo.apps.ventas.models import Producto
from catalogo.apps.ventas.forms import add_marca_form
from catalogo.apps.ventas.models import Marca
from catalogo.apps.ventas.forms import add_categoria_form
from catalogo.apps.ventas.models import Categoria
from django.http import HttpResponseRedirect


def add_product_view(request):
	info = "inicializando"
	if request.method == "POST":
		formulario = add_product_form(request.POST, request.FILES)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.status = True
			add.save()
			formulario.save_m2m()
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect ('/producto/%s' %add.id)
	else:
		formulario = add_product_form()
	ctx = { 'form': formulario, 'informacion':info}
	return render_to_response('ventas/add_producto.html', ctx,context_instance = RequestContext(request))


def add_marca_view(request):
	info = "inicializando"
	if request.method == "POST":
		formulario = add_marca_form(request.POST, request.FILES)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.status = True
			add.save()
			formulario.save_m2m()
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect ('/marca/%s' %add.id)
	else:
		formulario = add_marca_form()
	ctx = { 'form': formulario, 'informacion':info}
	return render_to_response('ventas/add_marca.html', ctx,context_instance = RequestContext(request))

def add_categoria_view(request):
	info = "inicializando"
	if request.method == "POST":
		formulario = add_categoria_form(request.POST, request.FILES)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.status = True
			add.save()
			formulario.save_m2m()
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect ('/categoria/%s' %add.id)
	else:
		formulario = add_categoria_form()
	ctx = { 'form': formulario, 'informacion':info}
	return render_to_response('ventas/add_categoria.html', ctx,context_instance = RequestContext(request))

def edit_product_view(request, id_prod):
	info = ""
	prod = Producto.objects.get(pk = id_prod)
	if request.method == "POST":
		formulario = add_product_form(request.POST, request.FILES, instance= prod)
		if formulario.is_valid():
			edit_prod = formulario.save(commit = False)
			formulario.save_m2m()
			edit_prod.status = True
			edit_prod.save()
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect ('/producto/%s'% edit_prod.id)
	else:
		formulario = add_product_form(instance = prod)
	ctx = { 'form': formulario, 'informacion':info}
	return render_to_response('ventas/edit_producto.html', ctx,context_instance = RequestContext(request))

def del_product_view(request, id_prod):
	info = "inicializando"
	try:
		prod = Producto.objects.get(pk = id_prod)
		prod.delete()
		info = "Producto Eliminado Correctamente"
		return HttpResponseRedirect('/productos/')
	except:
		info = "Producto no se puede Eliminar"
		#return  render_to_response('home/productos.html', context_instance = RequestContext(request))
		return HttpResponseRedirect('/productos/')









