from .views import adUsuario, carlsjr, carro, choclo, coronta, cotonito, cuarto, datosperson, duna,factura,adPedidos,adVentas,crearcuenta, formulario, guardar_compra, menu, quinto, robin, salir, segundo, tarjeta, tercero
from django.urls import include, path
from  .import views
urlpatterns = [
    path('adPedidos/',adPedidos,name='adPedidos'),
    path('adUsuario/',adUsuario,name='adUsuario'),
    path('salir/',salir,name='salir'),
    path('adVentas/',adVentas,name='adVentas'),
    path('factura/',factura,name='factura'),
    path('crearcuenta/', crearcuenta, name= 'crearcuenta'),
    path('',menu,name='menu'),
    path('carlsjr/',carlsjr,name='carlsjr'),
    path('carro/',carro,name='carro'),
    path('choclo/',choclo,name='choclo'),
    path('coronta/',coronta,name='coronta'),
    path('cotonito/',cotonito,name='cotonito'),
    path('cuarto/',cuarto,name='cuarto'),
    path('datosperson/',datosperson,name='datosperson'),
    path('duna/',duna,name='duna'),
    path('formulario/',formulario,name='formulario'),
    path('quinto/',quinto,name='quinto'),
    path('robin/',robin,name='robin'),
    path('segundo/',segundo,name='segundo'),
    path('tarjeta/',tarjeta,name='tarjeta'),
    path('tercero/',tercero,name='tercero'),
    path('guardar_compra/',guardar_compra,name='guardar_compra'),
    
    path('adProductos/',views.adProductos,name='adProductos'),
    path('agregarproducto/',views.agregarproducto,name='agregarproducto'),
    path('editarproducto/<int:id>/', views.editarproducto, name='editarproducto'),
    path('eliminarproducto/<int:id>/', views.eliminarproducto, name='eliminarproducto'),
] 