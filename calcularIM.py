

import customtkinter as ctk
from click import clear


def calc_IMC():
    if entry_peso and entry_altura.get () != "":  
        peso = float (entry_peso.get ())
        altura= float (entry_altura.get ())

        imc = peso / (altura * altura)

        # janela do segundo label que mostra o IMC
        root2 = ctk.CTkToplevel()
        root2.geometry('500x150+10+10')
        root2.title('calcular IMC')
        root2.resizable(False,False)

        # label que mostra o resultado do IMC
        end_calc = ctk.CTkLabel(root2,
            text=(f'IMC: {round(imc,2)}' ),
            font=('monospace', 20, 'bold'),
            text_color='blue',
        )
        end_calc.pack(padx=10, pady=10)


        # Obter estado
        estado = ''
        if imc < 17:
            estado = 'Muito abaixo do peso'
        elif imc >= 17 and imc < 18.5:
            estado = 'Abaixo do peso'
        elif imc >= 18.5 and imc < 25:
            estado = 'Peso normal'
        elif imc >= 25 and imc <30:
            estado = 'Acima do peso'
        elif imc >= 30 and imc < 35:
            estado = 'Obesidade I'
        elif imc >= 35 and imc < 40:
            estado = 'Obesidade II'
        elif imc >= 40:
            estado = 'Obesidade iii'
            

        # mostrar o estado fisico da pessoa
        mostrar_estado = ctk.CTkLabel(root2,
                text=(f'{estado}'),
                font=('monospace', 20, 'bold'),
         )
        mostrar_estado.pack(padx=10, pady=10)


        # Botao para sair do label que mostra o IMC 
        btn_sair =ctk.CTkButton (root2,
            text = 'SAIR',
            width= 200, height= 30,
            font= ("monospace", 25, 'bold'),
            text_color= '#ffffff',
            fg_color= '#4169E1',
            corner_radius=30,
            hover_color = '#0000CD',
            command= root2.destroy
        )
        btn_sair.pack(padx=10, pady=5)


ctk.set_appearance_mode('light')

# JA TA criando o freme
root = ctk.CTk()
root.geometry('500x300+500+100')
root.title('Calcular IMC')
root.resizable(False,False)

# label tituloJANELA  
lbl_titulo = ctk.CTkLabel(root,
    text=('Calcular IMC'),
    font=('monospace', 25),
    text_color='blue'
    )
lbl_titulo.pack(padx=10, pady=10)

# Caixa de entrada [Entry box]
entry_peso = ctk.CTkEntry(root,
	placeholder_text=('peso'),
	width=200, height=40,
	font=("Monospace", 25, 'bold'),
    corner_radius=10,
	placeholder_text_color=('black'),
	text_color='#000000'
    )
entry_peso.pack(padx=10, pady=20)

# Caixa de entrada 2 [Entry box]
entry_altura = ctk.CTkEntry(root,
	placeholder_text=('altura'),
	width=200, height=40,
	font=("Monospace", 25, 'bold'),
    corner_radius=10,
	placeholder_text_color=('black'),
	text_color='#000000'
    )
entry_altura.pack(padx=10, pady=20)

# botao para enviar a conta
btn_enviar =ctk.CTkButton (root,
    text = 'Enviar',
    width= 200, height= 30,
    font= ("monospace", 25, 'bold'),
    text_color= '#ffffff',
    fg_color= '#4169E1',
    corner_radius=30,
    hover_color = '#0000CD',
    command= calc_IMC
)
btn_enviar.pack(padx=10, pady=20)


clear()
root.mainloop()