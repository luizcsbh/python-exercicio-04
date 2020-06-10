from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from datetime import datetime
from ..models import Pessoa, Endereco, Departamento, Cargo

# Create your views here.
@require_http_methods(["GET", "POST"])
def home(request):
    return HttpResponse("Ola, requisição feita com sucesso!")

@csrf_exempt
@require_http_methods(["GET", "POST"])
def listar(request):
    result = Pessoa.objects.all()
    template = loader.get_template('listar.html')
    context = {
        'lista': result,
    }
    return HttpResponse(template.render(context, request))

def detalhar(request, id_pessoa):
    pessoa = Pessoa.objects.get(id = id_pessoa)
    context = {'pessoa': pessoa}
    return render( request, 'detalhar.html', context)

#queryfilterage
def queryfilterage(request):
	pessoa = Pessoa.objects.filter(idade = 40)
	context = {'pessoa': pessoa}
	return render(request, 'detalhar.html', context)

#queryfilterdateofbirth
def queryfilterdateofbirth(request):
	pessoa = Pessoa.objects.filter(data_nascimento = '1980-01-01')
	context = {'pessoa': pessoa}
	return render(request, 'detalhar.html', context)

#queryfilterfirstrecords
def queryfirstrecords(request):
	result = Pessoa.objects.all()[:3]
	template = loader.get_template('listar.html')
	context = {
		'lista' : result,
	}
	return HttpResponse(template.render(context, request))

#queryfiltername
def queryfiltername(request):
	pessoa = Pessoa.objects.get(nome__contains='Luiz')
	context = {'pessoa': pessoa}
	return render(request, 'detalhar.html', context)


def excluir(request, id_pessoa):
    try:
        pessoa = Pessoa.objects.get(id = id_pessoa)
        pessoa.delete()
        return HttpResponse (f"Registro: {pessoa.nome} de (id={pessoa.id}) foi excluído com sucesso.")
    except ObjectDoesNotExist:
        return HttpResponse("Pessoa não encontrada")

def cadastro(request):
    genero = ['Masculino','Feminino','Binário','Não informado']
    template = loader.get_template('cadastrar.html')
    context = {
        'genero': genero,
    }
    return HttpResponse(template.render(context, request))

def editar(request, id_pessoa):
    	pessoa = Pessoa.objects.get(id=id_pessoa)
	context = {'pessoa':pessoa}
	return render(request, 'editar.html', context)

@csrf_exempt
@require_http_methods(["POST","GET"])
def edit(request):
	p = Pessoa.objects.edit(
			request.POST['id'],
			request.POST['nome'],
			request.POST['idade'],
			request.POST['cpf'])
	return HttpResponse(f"{p} alterado com sucesso")

def cadastro_departamento(request):
    template = loader.get_template('cadastrar_departamento.html')
	context = {
	}
	return HttpResponse(template.render(context, request))

def cadastro_cargo(request):
	template = loader.get_template('cadastrar_cargo.html')
	context = {
	}
	return HttpResponse(template.render(context, request))

def cadastrar(request):
    dataNascimento = datetime.strptime(request.POST['dataNascimento'], "%d/%m/%Y").date()
	p = Pessoa.objects.nova(
			request.POST['nome'],
			request.POST['idade'],
			dataNascimento,
			request.POST['cpf'],
			request.POST['logradouro'],
			request.POST['numero'],
			request.POST['bairro'],
			request.POST['cep'])

	return HttpResponse(f"{p} cadastrado com sucesso")

@csrf_exempt
@require_http_methods(["POST","GET"])
def listar_departamento(request):
	result = departamento.objects.all()
	template = loader.get_template('listar_departamento.html')
	context = {
		'lista' : result,
	}
	return HttpResponse(template.render(context, request))

def detalhar_departamento(request, id_departamento):
	departamento = departamento.objects.get(id=id_departamento)
	context = {'departamento':departamento}
	return render(request, 'detalhe_departamento.html', context)

def excluir_departamento(request, id_departamento):
	try:
		departamento = departamento.objects.get(id=id_departamento)
		departamento.delete()		
		return HttpResponse(f"Excluiu {departamento.descricao} (id={departamento.id})")
	except ObjectDoesNotExist:
		return HttpResponse("departamento não encontrado")

def editar_departamento(request, id_departamento):
	departamento = departamento.objects.get(id=id_departamento)
	context = {'departamento':departamento}
	return render(request, 'editar_departamento.html', context)

@csrf_exempt
@require_http_methods(["POST","GET"])
def edit_departamento(request):
	s = departamento.objects.get(id=request.POST['id'])
	s.descricao = request.POST['descricao']
	s.save()
	return HttpResponse(f"{s.descricao} alterado com sucesso")

def cadastrar_cargo(request):
	c = Cargo(
		descricao=request.POST['descricao'], 
		cbo=request.POST['cbo'])
	c.save()
	return HttpResponse(f"{c.descricao} cadastrado com sucesso")

def listar_cargo(request):
	result = Cargo.objects.all()
	template = loader.get_template('listar_cargo.html')
	context = {
		'lista' : result,
	}
	return HttpResponse(template.render(context, request))

def detalhar_cargo(request, id_cargo):
	cargo = Cargo.objects.get(id=id_cargo)
	context = {'cargo':cargo}
	return render(request, 'detalhe_cargo.html', context)

def excluir_cargo(request, id_cargo):
	try:
		cargo = Cargo.objects.get(id=id_cargo)
		cargo.delete()		
		return HttpResponse(f"Excluiu {cargo.descricao} (id={cargo.id})")
	except ObjectDoesNotExist:
		return HttpResponse("Cargo não encontrado")

def editar_cargo(request, id_cargo):
	cargo = Cargo.objects.get(id=id_cargo)
	context = {'cargo':cargo}
	return render(request, 'editar_cargo.html', context)

@csrf_exempt
@require_http_methods(["POST","GET"])
def edit_cargo(request):
	c = Cargo.objects.get(id=request.POST['id'])
	c.descricao = request.POST['descricao']
	c.cbo = request.POST['cbo']
	c.save()
	return HttpResponse(f"{c.descricao} alterado com sucesso")
