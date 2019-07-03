from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EncryptForm, DecryptForm
from .models import AllData
import random
import string
import ast
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    return render(request, 'home/home.html')

def encrypt(request):
    form = EncryptForm()
    if request.method == "POST":
        form = EncryptForm(request.POST)
        if form.is_valid():
            try:
                pswdLen = len(request.POST.get("finder"))
                i = 0
                d = {}
                while i <= 255:
                    letters = string.ascii_lowercase + string.digits
                    code =  ''.join(random.choice(letters) for i in range(pswdLen))
                    d.update({i:code})
                    
                    i += 1
                inputText = request.POST.get("decText")
                text = ""
                for i in inputText:
                    ascii_of_i = ord(i)
                    for key, value in d.items():
                        if key == ascii_of_i:
                            text += value
                query = AllData(
                    finder = request.POST.get("finder"),
                    keys = str(d),
                    encText = text
                )
                query.save()
                i = 0
                device_width = request.POST.get("device_width")
                device_width = int(device_width)
                device_width = int(device_width/11)
                try:
                    x = text
                    y = ""
                    i = 0
                    while i < len(x):
                        if i%device_width == 0 and i != 0:
                            y += x[i]+" "
                            i += 1
                        else:
                            y += x[i]
                            i += 1
                    subject = 'From EncryptionFog'
                    message = 'Someone used EncryptionFog'
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = ['your email..',]
                    try:
                        send_mail( subject, message, email_from, recipient_list)
                    except:
                        pass
                    messages.success(request, "Your text is encrypted")
                    return render(request, 'home/encrypted.html', {'result': y})
                except:
                    messages.success(request, 'Something went wrong try after some time.')
                    return redirect('/encrypt')
            except:
                messages.warning(request, 'Something went wrong try after some time.')
                return redirect('/encrypt')
    return render(request, 'home/encrypt.html', {'form': form})

def decrypt(request):
    form = DecryptForm()
    if request.method == "POST":
        form = DecryptForm(request.POST)
        if form.is_valid():
            try:
                encText = str(request.POST.get("encText"))
                encText = encText.replace(" ", "")
                encText = encText.replace("\n", "")
                q = AllData.objects.filter(finder = request.POST.get("finder"), encText=encText).first()
                
                d = ast.literal_eval(q.keys)
                finderLen = len(request.POST.get("finder")) 
                encTextLen = len(encText)

                i = 0
                data = ""
                while i <= encTextLen:
                    encText_parts = encText[i : i + finderLen]
                    for key,val in d.items():
                        if val == encText_parts:
                            data += chr(key)
                    i += finderLen

                messages.success(request, "Your decrypted text:")
                messages.success(request, "----------xxx----------")
                messages.success(request, data)
                messages.success(request, "----------xxx----------")
                return redirect('/decrypted')
            except:
                messages.warning(request, 'Incorrect password or text.')
                return redirect('/decrypt')
        else:
            messages.success(request, "Incorrect password or text")
            return redirect('/decrypt')
    return render(request, 'home/decrypt.html', {'form': form})

def encrypted(request):
    return render(request, 'home/encrypted.html')

def decrypted(request):
    return render(request, 'home/decrypted.html')
