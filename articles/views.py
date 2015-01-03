from django.shortcuts import render_to_response

def template_view(request):

  template_name = "index.html"
  return render_to_response(template_name)
