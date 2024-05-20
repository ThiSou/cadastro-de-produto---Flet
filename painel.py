import flet as ft 
import sistema as adm

def main(page : ft.Page):
    
    def salvar_informacoes(e):
        produto = {
            "Nome_produto": nome_produto.value,
            "Quantidade_produto": quantidade_produto.value,
            "Preço_produto": peso.value,
            "Marca_produto": marca_produto.value
        }
        adm.gerenciador.cadastrar_produto(produto["Nome_produto"],produto["Quantidade_produto"],produto["Peso_produto"],produto["Marca_produto"])
        

    def buscar_produto(e):
        produtos = adm.gerenciador.buscar_produto(produto_busca.value)
        print(produtos)
        # print('-=-'*5)
        # lista_produtos.controls.append(ft.Text(f"-=--=--=--=--=--=-\nNome: {produtos[0]}\nMarca: {produtos[3]}\nPeso:{produtos[4]}\nQuantidade no estoque: {produtos[1]}\nPreço: R${produtos[2]}\n-=--=--=--=--=--=-"))
        
        # lista_produtos.update()


    display = ft.Container(
        col=12,
        width=500,
        bgcolor=ft.colors.BLACK26,
        padding=ft.padding.all(20),
        content=ft.Column(
            aspect_ratio=12/18,
            controls=[
                nome_produto := ft.TextField(
                    label="Nome do produto",
                    hint_text="ex: Arroz",
                ),
                ft.ResponsiveRow(
                    controls=[
                        quantidade_produto := ft.TextField(
                            col=4,
                            label="Quantidade"
                        ),
                        peso := ft.TextField(
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
                            text="Submeter",
                            on_click=salvar_informacoes
                        )
                    ]
                ),

                ft.Container(
                    content=ft.Column(
                        controls=[
                            produto_busca := ft.TextField(
                                label="Produto",
                                hint_text=("Busque aqui o produto que você procura")
                            ),
                            ft.ElevatedButton(
                                col=12,
                                text="Buscar item",
                                on_click=buscar_produto
                            ),
                            lista_produtos := ft.ListView(
                                col=12,
                                spacing=10,
                                padding=20,
                                auto_scroll=True
                            )
                        ],
                    )
                )
            ]
        )
    )

    page.add(display)

if __name__ == "__main__":
    ft.app(target=main)