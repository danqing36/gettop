from behave import given, when, then


@given('Open gettop page')
def open_gettop_page(context):
    context.app.main_page.open_main_page()

@given('Open gettop orderby {order_name} page')
def open_gettop_sort_page(context, order_name):
    suffix = '/shop/?orderby='+order_name
    context.app.header.open_product_sort_page(suffix)

@when('Click on {category_name} category')
def click_on_category(context, category_name):
    if category_name=='accessories':
        category_name='airpods'
    context.app.header.click_category(category_name)


@when('Select sort method {sort_method}')
def select_sort_method(context, sort_method):
    context.app.product_list.select_sort(sort_method)


@then('verify products order by {sort_method}')
def verify_sort_result(context, sort_method):
    price_list=[]
    context.app.product_list.get_product_list(price_list)
    print(price_list)
    if 'low to high' in sort_method:
        after_sort = sorted(price_list)
    elif 'high to low' in sort_method:
        after_sort = sorted(price_list, reverse=True)
    assert price_list == after_sort, f'Product sort by wrong order'


@then('verify products sort by {suffix} {sort_method}')
def verify_all_products_sort(context, suffix, sort_method):
    price_list=[]
    context.app.product_list.get_product_list(price_list)
    open_next_page(context, suffix)
    context.app.product_list.get_product_list(price_list)
    if 'low to high' in sort_method:
        after_sort = sorted(price_list)
    elif 'high to low' in sort_method:
        after_sort = sorted(price_list, reverse=True)
    assert price_list == after_sort, f'Product sort by wrong order'



def open_next_page(context, suffix):
    suffix = '/shop/page/2/?orderby='+suffix
    context.app.header.open_product_sort_page(suffix)
