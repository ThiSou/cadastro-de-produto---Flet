import flet as ft 
import sistema as adm

def main(page : ft.Page):
    page.scroll = ft.ScrollMode.AUTO
    page.theme_mode = ft.ThemeMode.DARK
    
    def cadastrar_produto(e):
        
        produto = {
            "Nome_produto": nome_produto.value,
            "Quantidade_produto": quantidade_produto.value,
            "Preço_produto": preco.value,
            "Marca_produto": marca_produto.value
        }

        adm.gerenciador.cadastrar_produto(produto["Nome_produto"],produto["Quantidade_produto"],produto["Preço_produto"],produto["Marca_produto"])

        nome_produto.value = ""
        quantidade_produto.value = ""
        preco.value = ""
        marca_produto.value = ""
        page.update()
        

    def buscar_produto(e):
        produtos = adm.gerenciador.buscar_produto(buscar_item.value)
        print(produtos)
        lista_produtos.clean()

        if produtos != None:
            lista_produtos.controls.append(ft.Text(f"Nome: {produtos[0]}\nQuantidade no estoque: {produtos[1]}\nPreço: {produtos[2]}\nMarca: {produtos[3]}"))
        else:
            lista_produtos.controls.append(ft.Text(f"Erro 404: Produto não encontrado"))

        buscar_item.value = ""
        lista_produtos.update()
        buscar_item.update()


    barra_pesquisa = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    "Barra de pesquisa"
                ),
                ft.Divider(color=ft.colors.WHITE70,thickness=2),
                buscar_item := ft.TextField(
                    label="Busque aqui o produto desejado",
                    hint_text="ex: Óleo de girassol"
                ),
                ft.ResponsiveRow(
                    controls=[
                        ft.ElevatedButton(
                            col=12,
                            text="Buscar",
                            on_click=buscar_produto
                        ),
                    ]
                ),
                ft.Divider(color=ft.colors.WHITE70,thickness=2),                
                lista_produtos := ft.ListView(
                    col=12,
                    spacing=10,
                    padding=20,
                    auto_scroll=True
                ),
                ft.Divider(color=ft.colors.WHITE70,thickness=2),

            ]
        )
    )


    painel_cadastro = ft.Container(
        col=12,
        content=ft.Column(
            controls=[
                ft.Text(
                    "Cadastro de produto",
                ),

                ft.Divider(
                    color=ft.colors.WHITE70,
                    thickness=2
                ),

                nome_produto := ft.TextField(
                    col=4,
                    label="Nome do produto",
                    hint_text="ex: Arroz"
                ), 

                ft.ResponsiveRow(
                    controls=[
                        quantidade_produto := ft.TextField(
                            col=4,
                            label="Quant."
                        ),
                        preco := ft.TextField(
                            col=4,
                            label="Preço"
                        ),
                        marca_produto := ft.TextField(
                            col=4,
                            label="Marca"
                        )
                    ]
                ),
                ft.ResponsiveRow(
                    controls=[
                        ft.ElevatedButton(
                            col=12,
                            text="Cadastrar",
                            on_click=cadastrar_produto
                        )
                    ]
                ),
            ]
        )
    )


    display = ft.Container(
        col=12,
        width=500,
        bgcolor=ft.colors.BLACK26,
        padding=ft.padding.all(20),
        content=ft.Column(
            aspect_ratio=15/18,
            controls=[
                painel_cadastro,
                barra_pesquisa
            ]
        )
    )

    page.add(display)

if __name__ == "__main__":
    ft.app(target=main)