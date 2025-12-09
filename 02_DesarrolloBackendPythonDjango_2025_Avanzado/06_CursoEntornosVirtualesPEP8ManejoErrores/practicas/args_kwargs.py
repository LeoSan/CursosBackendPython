"""Explicaciones y ejemplos de *args y **kwargs."""


def ejemplo_args(api_key, *args):
    print(f"api_key: {api_key}")
    print(f"args: {args}")
    print(f"type args: {type(args)}")
    print("====")


ejemplo_args("API_KEY_VALUE", "Este", "parametro", "acá")
ejemplo_args("API_KEY_VALUE", "Hola", "Mundo")


def ejemplo_kwargs(**kwargs):
    print(f"kwargs: {type(kwargs)}")
    print(f"kwargs: {kwargs}")
    print("======")


ejemplo_kwargs(
    api_key="DEMO",
    query="Noticias de Python",
    timeout=30,
    retries=3,
)
ejemplo_kwargs(
    api_key="DEMO_GUARDIAN",
    section="Sports",
    from_date="2020-10-20",
    timeout=30,
    retries=3,
)