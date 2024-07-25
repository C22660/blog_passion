from django.shortcuts import render
from django.core.mail import send_mail


from blog.contacts.forms import CreationContactForm

def send_contact_message(request):
    if request.method == 'POST':
        form = CreationContactForm(request.POST)
        if form.is_valid():
            send_mail(
                f"Message de {form.cleaned_data['contact_email']}",
                f"{form.cleaned_data['content']}",
                None,  # from email
                ['blog-contact@example.com'],  # replace with your email
            )
            form.save()
            return render(request, 'contacts/confirmation_sending.html')
    else:
        form = CreationContactForm()
    
    return render(request, 'contacts/contact_form.html', {'form': form})
