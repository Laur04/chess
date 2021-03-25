import cv2
import io
import numpy
import PIL

from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect, reverse, get_object_or_404

from .forms import StarterForm
from .models import Run, HarrisCorners

number_of_methods = 1

@login_required
def home(request):
    if request.method == "POST":
        form = StarterForm(request.POST, request.FILES)
        if form.is_valid():
            if int(form.cleaned_data["method"]) in range(0, number_of_methods):
                run = Run.objects.create(
                    submitting_user=request.user,
                    input_image=form.cleaned_data["image"],
                    method=int(form.cleaned_data["method"]),
                    custom_name=form.cleaned_data["custom_name"],
                )

                if form.cleaned_data["method"] == "0":
                    harris_corner_detection(run)
                
                return redirect(reverse("board:results", args=[run.id]))
            else:
                form.add_error("method", "Invalid method")                
    else:
        form = StarterForm()
    return render(request, "board/home.html", context={"form": form})

@login_required
def results(request, run_id):
    run = get_object_or_404(Run, id=run_id)
    context = {"run": run}
    
    output = None

    if run.method == 0:
        output = run.harriscorners_set.all()[0]
        context.update({"run_type": "Harris Corner Detection"})
    
    if output is not None:
        context.update({"output": output})
    
    return render(request, "board/results.html", context=context)

@login_required
def list_runs(request):
    runs = Run.objects.filter(submitting_user=request.user).order_by("time_ran")
    return render(request, "board/list.html", context={"runs": runs})

def harris_corner_detection(run):
    try:
        img_to_input = numpy.float32(PIL.Image.open(run.input_image))
        dst = cv2.dilate(cv2.cornerHarris(numpy.float32(cv2.cvtColor(img_to_input, cv2.COLOR_BGR2GRAY)), 2, 3, .04), None)
        img_to_input[dst > 0.01 * dst.max()] = [255, 0, 0]
        img_to_output = PIL.Image.fromarray(img_to_input.astype(numpy.uint8))
        
        run.successful = True
        run.save()

        hc = HarrisCorners.objects.create(
            run=run,
            output_image=run.input_image
        )
        img_to_output_io = io.BytesIO()
        img_to_output.save(img_to_output_io, format="JPEG")
        hc.output_image.save(
            run.input_image.name.split('/')[-1],
            content=ContentFile(img_to_output_io.getvalue()),
            save=False
        )
        hc.save()
    except:
        run.successful = False
        run.save()
