from django.shortcuts import render



from .models import Smell
from .forms import SmellForm


def smell_map(request):
    """
    においマップを表示し、データ登録フォームも表示するビュー。
    """
    if request.method == 'POST':
        form = SmellForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SmellForm()
    smells = Smell.objects.all()
    smell_data = [
        {
            'name': s.name,
            'description': s.description,
            'lat': s.latitude,
            'lng': s.longitude,
            'intensity': s.intensity
        } for s in smells
    ]
    import json
    return render(request, 'mapping/smell_map.html', {
        'smell_data': json.dumps(smell_data, ensure_ascii=False),
        'form': form
    })

