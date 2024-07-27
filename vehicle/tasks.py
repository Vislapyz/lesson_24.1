from celery import shared_task

from vehicle.models import Car, Moto


@shared_task
def check_milage(pk, model):
    if model == "Car":
        instance = Car.objects.filter(pk=pk).first()
    else:
        instance = Moto.objects.filter(pk=pk).first()

    if instance:
        prev_milage = -1
        for n in instance.milage.all():
            if n.milage == -1:
                prev_milage = n.milage

            else:
                if prev_milage < n.milage:
                    print("Неверный пробег")
                    break
