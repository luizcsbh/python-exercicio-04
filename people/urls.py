from django.urls import path

from .views import people_views as pv

urlpatterns = [
    # /people/
    path('', pv.home, name="index"),
    #/people/listar
    path('listar', pv.listar, name="listar"),
    # /people/detalar/1/
    path('detalhar/<int:id_pessoa>/', pv.detalhar, name="detalhar"),
    # /people/excluir/1/
    path('excluir/<int:id_pessoa>/', pv.excluir, name="excluir"),
    # /people/cadastro
    path('cadastro', pv.cadastro, name="cadastro"),
    # cadatro Departamento
    path('cadastro_departamento', pv.cadastro_departamento, name="cadastro_departamento"),
    #cadastro Cargo
    path('cadastro_cargo/', pv.cadastro_cargo, name="cadastro_cargo"),
    # /people/cadastrar
    path('cadastrar', pv.cadastrar, name="cadastrar"),
    # query filto por idade
    path('queryfilterage/', pv.queryfilterage, name="queryfilterage"),
    # query filto por data de nascimento
	path('queryfilterdateofbirth/', pv.queryfilterdateofbirth, name="queryfilterdateofbirth"),
    # query filto pelos primeiros registros
	path('queryfirstrecords/', pv.queryfirstrecords, name="queryfirstrecords"),
    # query filto por nome
	path('queryfiltername/', pv.queryfiltername, name="queryfiltername"),
    # cadastrar Departamento
    path('cadastrar_departamento/', pv.cadastrar_departamento, name="cadastrar_departamento"),
	# Listar Departamento
    path('listar_departamento/', pv.listar_departamento, name="listar_departamento"),
	# Excluir Departamento
    path('excluir_departamento/<int:id_departamento>/', pv.excluir_departamento, name="excluir_departamento"),
	# Detalhar Departamento
    path('detalhar_departamento/<int:id_departamento>/', pv.detalhar_departamento, name="detalhar_departamento"),
	# Editar Departamento
    path('editar_departamento/<int:id_departamento>/', pv.editar_departamento, name="editar_departamento"),
	# Edit Departamento
    path('edit_departamento/', pv.edit_departamento, name="edit_departamento"),
	# Cadastrar Cargo
    path('cadastrar_cargo/', pv.cadastrar_cargo, name="cadastrar_cargo"),
	# Listar Cargo
    path('listar_cargo/', pv.listar_cargo, name="listar_cargo"),
	#Ecluir Cargo
    path('excluir_cargo/<int:id_cargo>/', pv.excluir_cargo, name="excluir_cargo"),
	# Editar Cargo
    path('editar_cargo/<int:id_cargo>/', pv.editar_cargo, name="editar_cargo"),
	# Edit Cargo
    path('edit_cargo/', pv.edit_cargo, name="edit_cargo"),
	#Detalhar Cargo
    path('detalhar_cargo/<int:id_cargo>/', pv.detalhar_cargo, name="detalhar_cargo")
]

