from django.shortcuts import render
from .utils import get_value, get_direction

def home(request):
    questions  = 32
    x_vals = []
    y_vals = []
    if request.method == 'POST':
        for i in range(1, questions + 1):
            var = "question" + str(i)
            ans = request.POST.get(var)
            val = get_value(ans)
            direction = get_direction(ans)

            if direction == "xy":
                x_vals.append(val)
                y_vals.append(val)
            elif direction == "x":
                x_vals.append(val)
            else:
                y_vals.append(val)

        x_sum  = sum(x_vals)
        y_sum  = sum(y_vals)
        cor = (x_sum, y_sum)

        print(x_vals, y_vals, cor)

    return render(request, 'home/home.html')
