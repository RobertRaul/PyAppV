from typing import Any
from django.contrib.auth.views import LoginView


class LoginFormView(LoginView):
    template_name = "login.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['title'] = "Iniciar Sesion"
        return context
    
