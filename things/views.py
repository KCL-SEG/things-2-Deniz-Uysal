from django.shortcuts import render
# views.py
from django.shortcuts import render
from .forms import ThingForm

def home(request):
    if request.method == 'POST':
        form = ThingForm(request.POST)
        if form.is_valid():
            form.save()  # Save the valid form data
            # Redirect or do something else after successful form submission
            # Example: return redirect('success_url')
    else:
        form = ThingForm()

    return render(request, 'home.html', {'form': form})
