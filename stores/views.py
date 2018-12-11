from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.http import Http404
from django.http import HttpResponseForbidden
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

from django.forms.models import inlineformset_factory
# from django.forms.models import modelform_factory

from .models import Store
from .models import MenuItem
from .forms import StoreForm, MenuItemFormSet
from events.forms import EventForm


def store_list(request):
    stores = Store.objects.all()
    return render(request, 'stores/store_list.html', {'stores': stores})


def store_detail(request, pk):
    try:
        store = Store.objects.get(pk=pk)
    except Store.DoesNotExist:
        raise Http404
    # 我們在初始化 EventForm 時用了一個新參數 initial，在 form 出現之前先為某個欄位指定初始值。
    # 因為我們要把這個 form post 到 EventCreateView，所以必須用 helper 的 form_action 參數自訂 HTML form tag
    # 中的 action attribute（預設會被 post 到目前的 URL）。
    event_form = EventForm(initial={'store': store}, submit_title='建立活動')
    event_form.helper.form_action = reverse('events:event_create')
    return render(request, 'stores/store_detail.html', {
        'store': store, 'event_form': event_form,
    })


def store_create(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            store = form.save(commit=False)
            if request.user.is_authenticated:
                store.owner = request.user
            store.save()
            return redirect(store.get_absolute_url())
    else:
        form = StoreForm(submit_title='建立')
    return render(request, 'stores/store_create.html', {'form': form})


def store_update(request, pk):
    try:
        store = Store.objects.get(pk=pk)
    except Store.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        form = StoreForm(request.POST, instance=store, submit_title='更新')
        # 用 post data 建立 formset，並在其（與 store form）合法時儲存
        menu_item_formset = MenuItemFormSet(request.POST, instance=store)
        if form.is_valid() and menu_item_formset.is_valid():
            store = form.save()
            menu_item_formset.save()
            return redirect(store.get_absolute_url())
    else:
        form = StoreForm(instance=store, submit_title=None)
        form.helper.form_tag = False
        menu_item_formset = MenuItemFormSet(instance=store)
    # 需要多指定一個 parent_model 參數，Django 才知道要用哪一個 foreign key 建立一對多關聯。
    # 如果有不止一個 foreign key 指向同一個 model,inlineformset_factory 可以接受一個叫 fk_name 的參數，讓你指定欄位名稱。
    # MenuItemFormSet = inlineformset_factory(
    #     parent_model=Store, model=MenuItem, fields=('name', 'price',), extra=3)
        menu_item_formset = MenuItemFormSet(instance=store)
    return render(request, 'stores/store_update.html', {
        'form': form, 'store': store, 'menu_item_formset': menu_item_formset,
    })


@login_required
@require_http_methods(['POST', 'DELETE'])
def store_delete(request, pk):
    try:
        store = Store.objects.get(pk=pk)
    except Store.DoesNotExist:
        raise Http404
    # if (not store.owner or store.owner == request.user or request.user.has_perm('store_delete')):
    #     store.delete()
    #     return redirect('store_list')
    print(request.is_ajax())
    if store.can_user_delete(request.user):
        store.delete()
        if request.is_ajax():

            return HttpResponse()
        return redirect(reverse('stores:store_list'))
    return HttpResponseForbidden()
