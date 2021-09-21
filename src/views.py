import json
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from src.models import Data

@login_required
def file(request):
    data = Data.objects.all()
    if request.method == 'POST':
        file = request.FILES['file']
        print(file)
        file_type = str(file).split(".")[-1]
        if file_type != 'json':
            messages.add_message(request, messages.ERROR, "file type " +
                                 str(file_type) + " not supported")
            return render(request, 'src/file.html', {'data': data})
        try:
            decoded_file = file.read().decode('utf-8')
            json_decode = json.loads(decoded_file)
        except Exception as e:
            messages.add_message(request, messages.ERROR, "Inconsistent json data: \n" + str(e)[0:50])
            return render(request, 'src/file.html', {'data': data})
        for data in json_decode:
            try:
                Data.objects.create(userId=data['userId'], title=data['title'],
                                    body=data['body'])
            except Exception as e:
                messages.add_message(request, messages.ERROR, "Inconsistent json data: \n" + str(e)[0:50])
                break

        data = Data.objects.all()
        return render(request, 'src/file.html', {'data': data})
    return render(request, 'src/file.html', {'data': data})
