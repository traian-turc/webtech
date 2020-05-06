from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("log_in", views.log_in, name="log_in"),
    path("menu", views.menu, name="menu"),
    path("help", views.help, name="help"),
    path("register", views.register, name="register"),
    path("register_v", views.register_v, name="register_v"),    
    path("<int:pizza_id>/order_pizza", views.order_pizza, name="order_pizza"),
    path("order_p_v", views.order_p_v, name="order_p_v"),
    path("<int:dinner_id>/order_dinner",views.order_dinner, name="order_dinner"),
    path("order_d_v", views.order_d_v, name="order_d_v"),
    path("<int:salad_id>/order_salad", views.order_salad, name="order_salad"),
    path("order_s_v", views.order_s_v, name="order_s_v"),
    path("<int:pasta_id>/order_pasta", views.order_pasta, name="order_pasta"),
    path("order_ps_v", views.order_ps_v, name="order_ps_v"),
    path("<int:sub_id>/order_sub", views.order_sub, name="order_sub"),
    path("order_sb_v", views.order_sb_v, name="order_sb_v"),
    path("view_order", views.view_order, name="view_order"),
    path("<int:order_id>/complete_order>",views.complete_order, name="complete_order"),
    path("d_order", views.d_order, name="d_order"),  
    path("place_order", views.place_order, name="place_order"),
    path("place_order_v", views.place_order_v, name="place_order_v"),
]