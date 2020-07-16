from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order, OrderUpdate
from math import ceil
import json
from django.views.decorators.csrf import csrf_exempt
from .payment import checksum
MERCHANT_KEY = 'kbzk1DSbJiV_O3p5'
# Create your views here.


def index(request):
    allProds = []
    categoryProds = Product.objects.values('Category', 'id')
    cat = {item['Category'] for item in categoryProds}
    for cats in cat:
        prods = Product.objects.filter(Category=cats)
        n = len(prods)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prods, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def searchMatch(query, item):
    ''' Returntrue only if query matches the item '''
    if query in item.Description.lower() or query in item.Product_name.lower() or query in item.Category.lower():
        return True
    else:
        return False


def search(request):
    query = request.GET.get('search', ' ')
    allProds = []
    categoryProds = Product.objects.values('Category', 'id')
    cat = {item['Category'] for item in categoryProds}
    for cats in cat:
        prodtemp = Product.objects.filter(Category=cats)
        prods = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prods)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prods) != 0:
            allProds.append([prods, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    if len(allProds) != 0 and len(query) <3 :
        params = {'msg': 'please enter valid value'}
    return render(request, 'shop/search.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
        return render(request, 'shop/contact.html', {'thank':thank})
        
    return render(request, 'shop/contact.html')


def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({'status': 'success', 'updates': updates, 'itemsJason': order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status": "noitem"}')
        except Exception as e:
            return HttpResponse('{"status}: "error')

    return render(request, 'shop/tracker.html')


def productview(request, id):
    #Fetch the product using id
    product = Product.objects.filter(id=id)

    return render(request, 'shop/prodview.html', {'product': product[0]})


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        address2 = request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        order = Order(items_json=items_json, name=name, email=email, phone=phone, address=address, address2=address2, city=city, state=state, zip_code=zip_code, amount=amount)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        print(id)
        # return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})
        # request payment gateway to transfer the amount to your account after payment by the user

        data_dict = {

                'MID': 'VMLsKh33374131769871',
                'ORDER_ID': str(id),
                'TXN_AMOUNT': str(amount),
                'CUST_ID': email,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8000/shop/handlerequest/',

        }
        data_dict['CHECKSUMHASH'] = checksum.generate_checksum(data_dict, MERCHANT_KEY)
        return render(request, 'shop/paytm.html', {'paarams_dict':data_dict})
    return render(request, 'shop/checkout.html')

@csrf_exempt
def handlerequest(request):
    # payment gateway will send post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSGH'])
    return render(request, 'shop/paymentstatus.html', {'reaponse ': response_dict})
