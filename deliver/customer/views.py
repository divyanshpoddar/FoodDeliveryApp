import json

from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail
from .models import MenuItem, Category, OrderModel


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')


class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')


class Order(View):
    def get(self, request, *args, **kwargs):
        # get every item from each category
        drinks = MenuItem.objects.filter(category__name__contains='Drinks')
        starters = MenuItem.objects.filter(category__name__contains='Starters')
        dishes = MenuItem.objects.filter(category__name__contains='Dishes')
        desert = MenuItem.objects.filter(category__name__contains='Desert')

        # pass into context
        context = {
            'drinks': drinks,
            'starters': starters,
            'dishes': dishes,
            'desert': desert,
        }

        # render the template
        return render(request, 'customer/order.html', context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        hostel = request.POST.get('hostel')
        block = request.POST.get('block')
        room = request.POST.get('room')

        order_items = {
            'items': []
        }

        items = request.POST.getlist('items[]')

        for item in items:
            menu_item = MenuItem.objects.get(pk=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price
            }

            order_items['items'].append(item_data)

        price = 0
        item_ids = []

        for order_item in order_items['items']:
            price += order_item['price']
            item_ids.append(order_item['id'])

        order = OrderModel.objects.create(
            price=price,
            name=name,
            email=email,
            hostel=hostel,
            block=block,
            room=room
        )
        order.items.add(*item_ids)

        body = ('Thank you for ordering! Your food is being prepared and will be delivered soon!\n'
                f'Your total is : {price}\n')

        send_mail(
            'Thanks for Ordering',
            body,
            'example@gmail.com',
            [email],
            fail_silently=False
        )

        context = {
            'items': order_items['items'],
            'price': price
        }

        return redirect('order-confirmation', pk=order.pk)


class OrderConfirmation(View):
    def get(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)

        context = {
            'pk': order.pk,
            'items': order.items.all(),
            'price': order.price
        }

        return render(request, 'customer/order_confirmation.html', context)

    def post(self, request, pk, *args, **kwargs):
        data = json.loads(request.body)

        if data['isPaid']:
            order = OrderModel.objects.get(pk=pk)
            order.is_paid = True
            order.save()

        return redirect('payment-confirmation')

class OrderPayConfirmation(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/order_pay_confirmation.html')

class Menu(View):
    def get(self, request, *args, **kwargs):
        menu_items = MenuItem.objects.all()

        context = {
            'menu_items': menu_items
        }

        return render(request, 'customer/menu.html', context)

class MenuSearch(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get("q")

        menu_items = MenuItem.objects.filter(
            Q(name__icontains=query) |
            Q(price__icontains=query) |
            Q(description__icontains=query)
        )

        context = {
            'menu_items': menu_items
        }

        return render(request, 'customer/menu.html', context)