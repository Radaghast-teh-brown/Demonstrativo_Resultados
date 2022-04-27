from ctypes import alignment
import tkinter as tk
from tkinter import *
from prettytable import PrettyTable

from click import command 

janela = tk.Tk()
janela.geometry("700x700") 
janela.title("Teste")  
janela.resizable(False, False)
janela.configure(bg = "#FFCC99")

vetor_informacoes = []
vetor_ativo_circulante = []
vetor_ativo_nao_circulante = []
vetor_passivo_circulante = []
vetor_passivo_nao_circulante = []
vetor_patrimonio = []



l1 = tk.Label(janela, font=('Helvetica', 14, 'bold'), text="Bem-vindo ao seu gerador de Balanço Patrimonial", bg = "#FFCC99" )
l1.place(relx = 0.07, rely = 0.02, relheight=0.1, relwidth=0.9) 
l2 = tk.Label(janela, font=('Helvetica', 14, 'bold'), text="Escolha uma opção abaixo", bg = "#FFCC99" )
l2.place(relx = 0.07, rely = 0.1, relheight=0.1, relwidth=0.9) 

b0 = tk.Button(janela, text='Cadastrar Informações', bg = "#994c00", command=lambda:definir_informacoes())
b0.place(relx = 0.35, rely = 0.2, relheight=0.1, relwidth=0.35) 
b1 = tk.Button(janela, text='Ativo circulante e não circulante', bg = "#994c00", command=lambda:ativo())
b1.place(relx = 0.35, rely = 0.35, relheight=0.1, relwidth=0.35) 
b2 = tk.Button(janela, text='Passivo circulante e não circulante', bg = "#994c00", command=lambda:passivo())
b2.place(relx = 0.35, rely = 0.5, relheight=0.1, relwidth=0.35) 
b3 = tk.Button(janela, text='Gerar relatório', bg = "#994c00", command=lambda:relatorio())
b3.place(relx = 0.35, rely = 0.65, relheight=0.1, relwidth=0.35) 

def definir_informacoes():

    janela_filha=Toplevel(janela) # Página filha
    janela_filha.geometry("800x650") 
    janela_filha.resizable(0,0)
    janela_filha.title("Cadastrar informações")
    janela_filha.configure(bg = "#B2FF66")

    def pegar_informacoes():
        nome = nome_entrada.get()
        endereco = endereco_entrada.get()
        razao_social = razao_social_entrada.get()
        cnpj = cnpj_entrada.get()
        cep = cep_entrada.get()
        vetor_informacoes.append(["Nome",nome])
        vetor_informacoes.append(["Endereço",endereco])
        vetor_informacoes.append(["Razão social",razao_social])
        vetor_informacoes.append(["CNPJ",cnpj])
        vetor_informacoes.append(["CEP",cep])
        print(vetor_informacoes)

    my_str1 = tk.StringVar()
    l1 = tk.Label(janela_filha,  textvariable=my_str1 )
    l1.grid(row=1,column=2) 

    titulo = tk.Label(janela_filha, font=('Helvetica', 14, 'bold'), text="Preencha os campos abaixos", bg = "#B2FF66")
    titulo.place(relx = 0.05, rely = 0.05, relheight=0.1, relwidth=0.9)

    b2 = tk.Button(janela_filha, text=' Fechar Tudo', bg = "#808080", command=janela.destroy)
    b2.place(relx = 0.35, rely = 0.9, relwidth=0.12 , relheight = 0.05)
    b3 = tk.Button(janela_filha, text=' Fechar Atual',  bg = "#808080", command=janela_filha.destroy)
    b3.place(relx = 0.50, rely = 0.9, relwidth=0.12 , relheight = 0.05)

    b4 = tk.Button(janela_filha, text='Adicionar Informações',  bg = "#808080", command=pegar_informacoes)
    b4.place(relx = 0.38, rely = 0.6, relwidth=0.25 , relheight = 0.05)
    

    nome = tk.Label(janela_filha, text = "Nome completo", fg = "White", bg = "#006600")
    nome.place(relx = 0.3, rely = 0.2, relheight=0.05, relwidth=0.2)
 

    endereco = tk.Label(janela_filha, text = "Endereço", fg = "White", bg = "#006600")
    endereco.place(relx = 0.3, rely = 0.28, relheight=0.05, relwidth=0.2)

    razao_social = tk.Label(janela_filha, text = "Razão Social", fg = "White", bg = "#006600")
    razao_social.place(relx = 0.3, rely = 0.36, relheight=0.05, relwidth=0.2)

    cnpj = tk.Label(janela_filha, text = "CNPJ", fg = "White", bg = "#006600")
    cnpj.place(relx = 0.3, rely = 0.44, relheight=0.05, relwidth=0.2)

    
    cep = tk.Label(janela_filha, text = "CEP", fg = "White", bg = "#006600")
    cep.place(relx = 0.3, rely = 0.52, relheight=0.05, relwidth=0.2)


    nome_entrada = tk.Entry(janela_filha, bg = "LightBlue")
    nome_entrada.place(relx = 0.53, rely = 0.2, relheight = 0.05, relwidth = 0.2)

    endereco_entrada = tk.Entry(janela_filha, bg = "LightBlue")
    endereco_entrada.place(relx = 0.53, rely = 0.28, relheight = 0.05, relwidth = 0.2)

    razao_social_entrada = tk.Entry(janela_filha, bg = "LightBlue")
    razao_social_entrada.place(relx = 0.53, rely = 0.36, relheight = 0.05, relwidth = 0.2)

    cnpj_entrada = tk.Entry(janela_filha, bg = "LightBlue")
    cnpj_entrada.place(relx = 0.53, rely = 0.44, relheight = 0.05, relwidth = 0.2)

    cep_entrada = tk.Entry(janela_filha, bg = "LightBlue")
    cep_entrada.place(relx = 0.53, rely = 0.52, relheight = 0.05, relwidth = 0.2)





def ativo():
    janela_filha=Toplevel(janela) # Página filha
    janela_filha.geometry("700x700") 
    janela_filha.resizable(0,0)
    janela_filha.title("Ativo circulante e não circulante")
    janela_filha.configure(bg = "#00BFFF")

    def pegar_ativo_ciruclante():
        caixa = caixa_entrada.get()
        aplicacao = aplicacaoLP_entrada.get()
        contas = contas_entrada.get()
        estoque = estoque_entrada.get()
        vetor_ativo_circulante.append(["Caixa",caixa])
        vetor_ativo_circulante.append(["Aplicação", aplicacao])
        vetor_ativo_circulante.append(["Contas",contas])
        vetor_ativo_circulante.append(["Estoque",estoque])

        novo1, novo2, novo3 = "",'',''
        novo1valor, novo2valor, novo3valor = 0,0,0

        lista_novo =[[novo1, novo1valor], [novo2, novo2valor],[novo3, novo3valor] ]
        lista_novo[0][0] = novo1_ativo_circulante_nome_entrada.get()
        lista_novo[0][1]= novo1_ativo_circulante_valor_entrada.get()
        lista_novo[1][0] = novo2_ativo_circulante_nome_entrada.get()
        lista_novo[1][1] = novo2_ativo_circulante_valor_entrada.get()
        lista_novo[2][0]= novo3_ativo_circulante_nome_entrada.get()
        lista_novo[2][1] = novo3_ativo_circulante_valor_entrada.get()

        for i in range(3):
            if lista_novo[i][0] != '' and lista_novo[i][1] != 0:
                vetor_ativo_circulante.append([lista_novo[i][0],lista_novo[i][1]])
        print(vetor_ativo_circulante)

    def pegar_ativo_nao_circulante():
        participacao = participacao_entrada.get()
        aplicacao = aplicacao_entrada.get()
        imoveis = imoveis_entrada.get()
        moveis = moveis_entrada.get()
        equipamentos = equipamentos_entrada.get()
        veiculos = veiculos_entrada.get()
        marcas = marcas_entrada.get()
        direitos = direitos_entrada.get()
        software = software_entrada.get()

        vetor_ativo_nao_circulante.append(["Participação/Empresas",participacao])
        vetor_ativo_nao_circulante.append(["Aplicação financeira", aplicacao])
        vetor_ativo_nao_circulante.append(["Imoveis", imoveis])
        vetor_ativo_nao_circulante.append(["Móveis",moveis])
        vetor_ativo_nao_circulante.append(["Equipamentos",equipamentos])
        vetor_ativo_nao_circulante.append(["Veículos",veiculos])
        vetor_ativo_nao_circulante.append(["Marcas", marcas])
        vetor_ativo_nao_circulante.append(["Direitos",direitos])
        vetor_ativo_nao_circulante.append(["Software",software])

        novo1, novo2, novo3 = "",'',''
        novo1valor, novo2valor, novo3valor = 0,0,0

        lista_novo =[[novo1, novo1valor], [novo2, novo2valor],[novo3, novo3valor] ]
        lista_novo[0][0] = novo1_ativo_circulante_nao_nome_entrada.get()
        lista_novo[0][1]= novo1_ativo_circulante_nao_valor_entrada.get()
        lista_novo[1][0] = novo2_ativo_circulante_nao_nome_entrada.get()
        lista_novo[1][1] = novo2_ativo_circulante_nao_valor_entrada.get()
        lista_novo[2][0]= novo3_ativo_circulante_nao_nome_entrada.get()
        lista_novo[2][1] = novo3_ativo_circulante_nao_valor_entrada.get()

        for i in range(3):
            if lista_novo[i][0] != '' and lista_novo[i][1] != 0:
                vetor_ativo_nao_circulante.append([lista_novo[i][0],lista_novo[i][1]])
                

        print(vetor_ativo_nao_circulante)


    my_str1 = tk.StringVar()
    l1 = tk.Label(janela_filha,  textvariable=my_str1 )
    l1.grid(row=1,column=2) 

    titulo = tk.Label(janela_filha, font=('Helvetica', 14, 'bold'), text="Ativo circulante e não circulante", bg = "#00BFFF")
    titulo.place(relx = 0.05, rely = 0.01, relheight=0.1, relwidth=0.9)

    b2 = tk.Button(janela_filha, text=' Fechar Tudo', bg = "#808080", command=janela.destroy)
    b2.place(relx = 0.35, rely = 0.9, relwidth=0.12 , relheight = 0.05)
    b3 = tk.Button(janela_filha, text=' Fechar Atual',  bg = "#808080", command=janela_filha.destroy)
    b3.place(relx = 0.50, rely = 0.9, relwidth=0.12 , relheight = 0.05)

    b4 = tk.Button(janela_filha, text='Adicionar Ativo Circulante',  bg = "#808080", command=pegar_ativo_ciruclante)
    b4.place(relx = 0.73, rely = 0.78, relwidth=0.25 , relheight = 0.05)

    b5 = tk.Button(janela_filha, text='Adicionar Ativo  Não Circulante',  bg = "#808080", command= pegar_ativo_nao_circulante)
    b5.place(relx = 0.73, rely = 0.84, relwidth=0.25 , relheight = 0.05)

     ####################### Ativo Circulante ############################

    ativo_circulante = Label(janela_filha, text = "Ativo Circulante", fg = "white", bg = "navy")
    ativo_circulante.place(relx = 0.05, rely = 0.1, relwidth=0.2 , relheight = 0.05)

    valor = Label(janela_filha, text = "Valor (R$)", fg = "white", bg = "navy")
    valor.place(relx = 0.28, rely = 0.1, relwidth=0.2, relheight = 0.05)

    caixa = Label(janela_filha, text = "Caixa", fg = "white" , bg = "RoyalBlue")
    caixa.place(relx = 0.05, rely = 0.2, relwidth=0.2, relheight = 0.05)

    aplicacaoLP = Label(janela_filha, text = "Aplicação LP", fg = "white",bg = "RoyalBlue")
    aplicacaoLP.place(relx = 0.05, rely = 0.26, relwidth=0.2, relheight = 0.05)

    contas = Label(janela_filha, text = "Contas a Receber",fg = "white", bg = "RoyalBlue")
    contas.place(relx = 0.05, rely = 0.32, relwidth=0.2, relheight = 0.05)

    estoque = Label(janela_filha, text = "Estoque", fg = "white", bg = "RoyalBlue")
    estoque.place(relx = 0.05, rely = 0.38, relwidth=0.2, relheight = 0.05)

 ####################### Acrescentar ativo circulante ############################

    novo1_ativo_circulante = Label(janela_filha, text = "Acrescentar Ativo circulante", fg = "white", bg = "#2B26C1")
    novo1_ativo_circulante.place(relx = 0.05, rely = 0.46, relwidth=0.43, relheight = 0.03)
    
    texto_info = Label(janela_filha, text = "Nome", fg = "white", bg = "#2B26C1")
    texto_info.place(relx = 0.13, rely = 0.50)

    valor_info = Label(janela_filha, text = "Valor", fg = "white", bg = "#2B26C1" )
    valor_info.place(relx = 0.35, rely = 0.50)

    novo1_ativo_circulante_nome_entrada = Entry(janela_filha, bg = "LightBlue")
    novo1_ativo_circulante_nome_entrada.place(relx = 0.05, rely = 0.54, relwidth=0.2, relheight = 0.03)

    novo1_ativo_circulante_valor_entrada = Entry(janela_filha, bg = "LightBlue")
    novo1_ativo_circulante_valor_entrada.place(relx = 0.28, rely = 0.54, relwidth=0.2, relheight = 0.03)

    novo2_ativo_circulante_nome_entrada = Entry(janela_filha, bg = "LightBlue")
    novo2_ativo_circulante_nome_entrada.place(relx = 0.05, rely = 0.58, relwidth=0.2, relheight = 0.03)

    novo2_ativo_circulante_valor_entrada = Entry(janela_filha,  bg = "LightBlue")
    novo2_ativo_circulante_valor_entrada.place(relx = 0.28, rely = 0.58, relwidth=0.2, relheight = 0.03)

    novo3_ativo_circulante_nome_entrada = Entry(janela_filha,  bg = "LightBlue")
    novo3_ativo_circulante_nome_entrada.place(relx = 0.05, rely = 0.62, relwidth=0.2, relheight = 0.03)

    novo3_ativo_circulante_valor_entrada = Entry(janela_filha,  bg = "LightBlue")
    novo3_ativo_circulante_valor_entrada.place(relx = 0.28, rely = 0.62, relwidth=0.2, relheight = 0.03)

#############################################################################################################

    caixa_entrada = Entry(janela_filha,  bg = "LightBlue")
    caixa_entrada.place(relx = 0.28, rely = 0.2, relwidth=0.2, relheight = 0.05)

    aplicacaoLP_entrada = Entry(janela_filha, bg = "LightBlue")
    aplicacaoLP_entrada.place(relx = 0.28, rely = 0.26, relwidth=0.2, relheight = 0.05)

    contas_entrada = Entry(janela_filha, bg = "LightBlue")
    contas_entrada.place(relx = 0.28, rely = 0.32, relwidth=0.2, relheight = 0.05)

    estoque_entrada = Entry(janela_filha, bg = "LightBlue")
    estoque_entrada.place(relx = 0.28, rely = 0.38, relwidth=0.2, relheight = 0.05)

    
    ################################# Ativo Não-Circulante ####################################

        

    ativo_nao_circulante = Label(janela_filha, text = "Ativo Não-Circulante", fg = "white", bg = "navy")
    ativo_nao_circulante.place(relx = 0.55, rely = 0.1, relwidth=0.2 , relheight = 0.05)

    valor = Label(janela_filha, text = "Valor (R$)", fg = "white", bg = "navy")
    valor.place(relx = 0.78, rely = 0.1, relwidth=0.2, relheight = 0.05)

    participacao = Label(janela_filha, text = "Participação/Empresas", fg = "white", bg = "RoyalBlue")
    participacao.place(relx = 0.55, rely = 0.2, relwidth=0.2, relheight = 0.05)

    aplicacao = Label(janela_filha, text = "Aplicação Financeira",fg = "white", bg = "RoyalBlue")
    aplicacao.place(relx = 0.55, rely = 0.26, relwidth=0.2, relheight = 0.05)
    
    imoveis = Label(janela_filha, text = "Imóveis", fg = "white", bg = "RoyalBlue")
    imoveis.place(relx = 0.55, rely = 0.32, relwidth=0.2, relheight = 0.05)

    moveis = Label(janela_filha, text = "Móveis", fg = "white", bg = "RoyalBlue")
    moveis.place(relx = 0.55, rely = 0.38, relwidth=0.2, relheight = 0.05)

    equipamentos = Label(janela_filha, text = "Equipamentos", fg = "white", bg = "RoyalBlue")
    equipamentos.place(relx = 0.55, rely = 0.44, relwidth=0.2, relheight = 0.05)

    veiculos = Label(janela_filha, text = "Veiculos", fg = "white", bg = "RoyalBlue")
    veiculos.place(relx = 0.55, rely = 0.50, relwidth=0.2, relheight = 0.05)

    marcas = Label(janela_filha, text = "Marcas/Patentes", fg = "white", bg = "RoyalBlue")
    marcas.place(relx = 0.55, rely = 0.56, relwidth=0.2, relheight = 0.05)

    direitos = Label(janela_filha, text = "Direitos/Patentes", fg = "white", bg = "RoyalBlue")
    direitos.place(relx = 0.55, rely = 0.62, relwidth=0.2, relheight = 0.05)

    software = Label(janela_filha, text = "Software", fg = "white", bg = "RoyalBlue")
    software.place(relx = 0.55, rely = 0.68, relwidth=0.2, relheight = 0.05)

    


    ####################### Acrescentar ativo  nao circulante ############################

    novo1_ativo_circulante = Label(janela_filha, text = "Acrescentar Ativo  nao circulante", fg = "white", bg = "#2B26C1")
    novo1_ativo_circulante.place(relx = 0.05, rely = 0.68, relwidth=0.43, relheight = 0.03)
    
    texto_info = Label(janela_filha, text = "Nome", fg = "white", bg ="#2B26C1" )
    texto_info.place(relx = 0.13, rely = 0.72)

    valor_info = Label(janela_filha, text = "Valor", fg = "white", bg = "#2B26C1" )
    valor_info.place(relx = 0.35, rely = 0.72)

    novo1_ativo_circulante_nao_nome_entrada = Entry(janela_filha, bg = "LightBlue")
    novo1_ativo_circulante_nao_nome_entrada.place(relx = 0.05, rely = 0.76, relwidth=0.2, relheight = 0.03)

    novo1_ativo_circulante_nao_valor_entrada = Entry(janela_filha, bg = "LightBlue")
    novo1_ativo_circulante_nao_valor_entrada.place(relx = 0.28, rely = 0.76, relwidth=0.2, relheight = 0.03)

    novo2_ativo_circulante_nao_nome_entrada = Entry(janela_filha, bg = "LightBlue")
    novo2_ativo_circulante_nao_nome_entrada.place(relx = 0.05, rely = 0.80, relwidth=0.2, relheight = 0.03)

    novo2_ativo_circulante_nao_valor_entrada = Entry(janela_filha,  bg = "LightBlue")
    novo2_ativo_circulante_nao_valor_entrada.place(relx = 0.28, rely = 0.80, relwidth=0.2, relheight = 0.03)

    novo3_ativo_circulante_nao_nome_entrada = Entry(janela_filha,  bg = "LightBlue")
    novo3_ativo_circulante_nao_nome_entrada.place(relx = 0.05, rely = 0.84, relwidth=0.2, relheight = 0.03)

    novo3_ativo_circulante_nao_valor_entrada = Entry(janela_filha,  bg = "LightBlue")
    novo3_ativo_circulante_nao_valor_entrada.place(relx = 0.28, rely = 0.84, relwidth=0.2, relheight = 0.03)


 #########################################Entry##########################################
    participacao_entrada = Entry(janela_filha, bg = "LightBlue")
    participacao_entrada.place(relx = 0.78, rely = 0.2, relwidth=0.2, relheight = 0.05)

    aplicacao_entrada = Entry(janela_filha, bg = "LightBlue")
    aplicacao_entrada.place(relx = 0.78, rely = 0.26, relwidth=0.2, relheight = 0.05)

    imoveis_entrada = Entry(janela_filha, bg = "LightBlue")
    imoveis_entrada.place(relx = 0.78, rely = 0.32, relwidth=0.2, relheight = 0.05)

    moveis_entrada = Entry(janela_filha, bg = "LightBlue")
    moveis_entrada.place(relx = 0.78, rely = 0.38, relwidth=0.2, relheight = 0.05)

    equipamentos_entrada = Entry(janela_filha, bg = "LightBlue")
    equipamentos_entrada.place(relx = 0.78, rely = 0.44, relwidth=0.2, relheight = 0.05)

    veiculos_entrada = Entry(janela_filha, bg = "LightBlue")
    veiculos_entrada.place(relx = 0.78, rely = 0.50, relwidth=0.2, relheight = 0.05)

    marcas_entrada = Entry(janela_filha, bg = "LightBlue")
    marcas_entrada.place(relx = 0.78, rely = 0.56, relwidth=0.2, relheight = 0.05)

    direitos_entrada = Entry(janela_filha, bg = "LightBlue")
    direitos_entrada.place(relx = 0.78, rely = 0.62, relwidth=0.2, relheight = 0.05)

    software_entrada = Entry(janela_filha, bg = "LightBlue")
    software_entrada.place(relx = 0.78, rely = 0.68, relwidth=0.2, relheight = 0.05)

    




def passivo():
    janela_filha=Toplevel(janela) # Página filha
    janela_filha.geometry("750x700") 
    janela_filha.resizable(0,0)
    janela_filha.title("Passivo circulante e não circulante")
    janela_filha.configure(bg = "#FF9999")



    def pegar_passivo_ciruclante():
    
        salario = salario_entrada.get()
        impostos = impostos_entrada.get()
        contas_fornecedores = contas_fornecedores_entrada.get()
        contas_pagar = contas_pagar_entrada.get()
        emprestimos = emprestimo_entrada.get()
        obrigacoe = obrigacao_entrada.get()

        vetor_passivo_circulante.append(["Salario",salario])
        vetor_passivo_circulante.append(["Impostos",impostos])
        vetor_passivo_circulante.append(["Contas fornecedores", contas_fornecedores])
        vetor_passivo_circulante.append(["Contas a pagar", contas_pagar])
        vetor_passivo_circulante.append(["Empréstimos", emprestimos])
        vetor_passivo_circulante.append(["Obrigações",obrigacoe])

        novo1, novo2, novo3 = "",'',''
        novo1valor, novo2valor, novo3valor = 0,0,0

        lista_novo =[[novo1, novo1valor], [novo2, novo2valor],[novo3, novo3valor] ]
        lista_novo[0][0] = novo1_passivo_circulante_nome_entrada.get()
        lista_novo[0][1]= novo1_passivo_circulante_valor_entrada.get()
        lista_novo[1][0] = novo2_passivo_circulante_nome_entrada.get()
        lista_novo[1][1] = novo2_passivo_circulante_valor_entrada.get()
        lista_novo[2][0]= novo3_passivo_circulante_nome_entrada.get()
        lista_novo[2][1] = novo3_passivo_circulante_valor_entrada.get()

        for i in range(3):
            if lista_novo[i][0] != '' and lista_novo[i][1] != 0:
                vetor_passivo_circulante.append([lista_novo[i][0],lista_novo[i][1]])
        print(vetor_passivo_circulante)

    def pegar_passivo_nao_circulante():
        titulos = titulos_entrada.get()
        finaceamentos = finaceamentos_entrada.get()
        vetor_passivo_nao_circulante.append(["Títulos a pagar",titulos])
        vetor_passivo_nao_circulante.append(["Financeamentos",finaceamentos])

        novo1, novo2, novo3 = "",'',''
        novo1valor, novo2valor, novo3valor = 0,0,0

        lista_novo =[[novo1, novo1valor], [novo2, novo2valor],[novo3, novo3valor] ]
        lista_novo[0][0] = novo1_passivo_nao_circulante_nome_entrada.get()
        lista_novo[0][1]= novo1_passivo_nao_circulante_valor_entrada.get()
        lista_novo[1][0] = novo2_passivo_nao_circulante_nome_entrada.get()
        lista_novo[1][1] = novo2_passivo_nao_circulante_valor_entrada.get()
        lista_novo[2][0]= novo3_passivo_nao_circulante_nome_entrada.get()
        lista_novo[2][1] = novo3_passivo_nao_circulante_valor_entrada.get()

        for i in range(3):
            if lista_novo[i][0] != '' and lista_novo[i][1] != 0:
                vetor_passivo_nao_circulante.append([lista_novo[i][0],lista_novo[i][1]])
                

        print(vetor_passivo_nao_circulante)
    
    def pegar_patrimonio():
        capital = capital_proprio_entrada.get()
        reservas = reservas_entrada.get()
        reservas_lucro = reservas_lucro_entrada.get()

        vetor_patrimonio.append(["Capital próprio",capital])
        vetor_patrimonio.append(["Reservas de capital",reservas])
        vetor_patrimonio.append(["Reservas de lucro",reservas_lucro])

        novo1, novo2, novo3 = "",'',''
        novo1valor, novo2valor, novo3valor = 0,0,0

        lista_novo =[[novo1, novo1valor], [novo2, novo2valor],[novo3, novo3valor] ]
        lista_novo[0][0] = novo1_patrimonio_nome_entrada.get()
        lista_novo[0][1] = novo1_patrimonio_valor_entrada.get()
        lista_novo[1][0] = novo2_patrimonio_nome_entrada.get()
        lista_novo[1][1] = novo2_patrimonio_valor_entrada.get()
        lista_novo[2][0] = novo3_patrimonio_nome_entrada.get()
        lista_novo[2][1] = novo3_patrimonio_valor_entrada.get()

        for i in range(3):
            if lista_novo[i][0] != '' and lista_novo[i][1] != 0:
                vetor_patrimonio.append([lista_novo[i][0],lista_novo[i][1]])
                

        print(vetor_patrimonio)



    my_str1 = tk.StringVar()
    l1 = tk.Label(janela_filha,  textvariable=my_str1 )
    l1.grid(row=1,column=2) 

    titulo = tk.Label(janela_filha, font=('Helvetica', 14, 'bold'), text="Passivo circulante, não circulante e patrimônio", bg = "#FF9999")
    titulo.place(relx = 0.05, rely = 0.01, relheight=0.1, relwidth=0.9)

    b2 = tk.Button(janela_filha, text=' Fechar Tudo', bg = "#808080", command=janela.destroy)
    b2.place(relx = 0.35, rely = 0.9, relwidth=0.12 , relheight = 0.05)
    b3 = tk.Button(janela_filha, text=' Fechar Atual',  bg = "#808080", command=janela_filha.destroy)
    b3.place(relx = 0.50, rely = 0.9, relwidth=0.12 , relheight = 0.05)

    b4 = tk.Button(janela_filha, text='Adicionar Passivo Circulante',  bg = "#808080", command= pegar_passivo_ciruclante)
    b4.place(relx = 0.05, rely = 0.8, relwidth=0.25 , relheight = 0.05)

    b5 = tk.Button(janela_filha, text='Adicionar Passivo Não Circulante',  bg = "#808080", command = pegar_passivo_nao_circulante)
    b5.place(relx = 0.4, rely = 0.8, relwidth=0.25 , relheight = 0.05)
    
    b6 = tk.Button(janela_filha, text='Adicionar Patrimônio',  bg = "#808080", command = pegar_patrimonio)
    b6.place(relx = 0.72, rely = 0.8, relwidth=0.25 , relheight = 0.05)


   

     ####################### Passivo Circulante ############################

    passivo_circulante = Label(janela_filha, text = "Passivo Circulante", fg = "white", bg = "#FF3333")
    passivo_circulante.place(relx = 0.02, rely = 0.1, relwidth=0.15 , relheight = 0.05)

    valor = Label(janela_filha, text = "Valor (R$)", fg = "white", bg = "#FF3333")
    valor.place(relx = 0.18, rely = 0.1, relwidth=0.15, relheight = 0.05)

    salario = Label(janela_filha, text = "Salários", fg = "white", bg = "#FF6666")
    salario.place(relx = 0.02, rely = 0.2, relwidth=0.15, relheight = 0.05)

    impostos = Label(janela_filha, text = "Impostos", fg = "white", bg = "#FF6666")
    impostos.place(relx = 0.02, rely = 0.26, relwidth=0.15, relheight = 0.05)

    contas_fornecedores = Label(janela_filha, text = "Contas/fornecedores",  fg = "white",bg = "#FF6666")
    contas_fornecedores.place(relx = 0.02, rely = 0.32, relwidth=0.15, relheight = 0.05)

    contas_pagar = Label(janela_filha, text = "Contas a pagar", fg = "white", bg = "#FF6666")
    contas_pagar.place(relx = 0.02, rely = 0.38, relwidth=0.15, relheight = 0.05)

    emprestimo = Label(janela_filha, text = "Empréstimo",fg = "white", bg = "#FF6666")
    emprestimo.place(relx = 0.02, rely = 0.44, relwidth=0.15, relheight = 0.05)

    obrigacoe = Label(janela_filha, text = "Obrigações trabalhistas", fg = "white", bg = "#FF6666")
    obrigacoe.place(relx = 0.02, rely = 0.50, relwidth=0.15, relheight = 0.05)



    salario_entrada = Entry(janela_filha, bg = "LightBlue")
    salario_entrada.place(relx = 0.18, rely = 0.2, relwidth=0.15, relheight = 0.05)

    impostos_entrada = Entry(janela_filha, bg = "LightBlue")
    impostos_entrada.place(relx = 0.18, rely = 0.26, relwidth=0.15, relheight = 0.05)

    contas_fornecedores_entrada = Entry(janela_filha, bg = "LightBlue")
    contas_fornecedores_entrada.place(relx = 0.18, rely = 0.32, relwidth=0.15, relheight = 0.05)

    contas_pagar_entrada = Entry(janela_filha, bg = "LightBlue")
    contas_pagar_entrada.place(relx = 0.18, rely = 0.38, relwidth=0.15, relheight = 0.05)

    emprestimo_entrada = Entry(janela_filha, bg = "LightBlue")
    emprestimo_entrada.place(relx = 0.18, rely = 0.44, relwidth=0.15, relheight = 0.05)

    obrigacao_entrada = Entry(janela_filha, bg = "LightBlue")
    obrigacao_entrada.place(relx = 0.18, rely = 0.50, relwidth=0.15, relheight = 0.05)

    ####################### Acrescentar passivo circulante ############################

    novo1_passivo_circulante = Label(janela_filha, text = "Acrescentar Passivo Circulante", fg = "white", bg = "#D2042D")
    novo1_passivo_circulante.place(relx = 0.02, rely = 0.58, relwidth=0.31, relheight = 0.03)
    
    texto_info = Label(janela_filha, text = "Nome", fg = "white", bg = "#D2042D")
    texto_info.place(relx = 0.08, rely = 0.62)

    valor_info = Label(janela_filha, text = "Valor", fg = "white", bg = "#D2042D" )
    valor_info.place(relx = 0.25, rely = 0.62)

    novo1_passivo_circulante_nome_entrada = Entry(janela_filha, bg = "LightBlue")
    novo1_passivo_circulante_nome_entrada.place(relx = 0.02, rely = 0.66, relwidth=0.15, relheight = 0.03)

    novo1_passivo_circulante_valor_entrada = Entry(janela_filha, bg = "LightBlue")
    novo1_passivo_circulante_valor_entrada.place(relx = 0.2, rely = 0.66, relwidth=0.13, relheight = 0.03)

    novo2_passivo_circulante_nome_entrada = Entry(janela_filha, bg = "LightBlue")
    novo2_passivo_circulante_nome_entrada.place(relx = 0.02, rely = 0.70, relwidth=0.15, relheight = 0.03)

    novo2_passivo_circulante_valor_entrada = Entry(janela_filha,  bg = "LightBlue")
    novo2_passivo_circulante_valor_entrada.place(relx = 0.2, rely = 0.70, relwidth=0.13, relheight = 0.03)

    novo3_passivo_circulante_nome_entrada = Entry(janela_filha,  bg = "LightBlue")
    novo3_passivo_circulante_nome_entrada.place(relx = 0.02, rely = 0.74, relwidth=0.15, relheight = 0.03)

    novo3_passivo_circulante_valor_entrada = Entry(janela_filha,  bg = "LightBlue")
    novo3_passivo_circulante_valor_entrada.place(relx = 0.2, rely = 0.74, relwidth=0.13, relheight = 0.03)

#############################################################################################################

    

       ####################### Passivo  Não - Circulante ############################

    passivo_circulante = Label(janela_filha, text = "Passivo Não Circulante", fg = "white", bg = "#FF3333")
    passivo_circulante.place(relx = 0.36, rely = 0.1, relwidth=0.17 , relheight = 0.05)

    valor = Label(janela_filha, text = "Valor (R$)", fg = "white", bg = "#FF3333")
    valor.place(relx = 0.54, rely = 0.1, relwidth=0.15, relheight = 0.05)


    titulos = Label(janela_filha, text = "Títulos a pagar", fg = "white", bg = "#FF6666")
    titulos.place(relx = 0.36, rely = 0.2, relwidth=0.17, relheight = 0.05)

    finaceamentos = Label(janela_filha, text = "Financeamentos", fg = "white", bg = "#FF6666")
    finaceamentos.place(relx = 0.36, rely = 0.26, relwidth=0.17, relheight = 0.05)


    titulos_entrada = Entry(janela_filha, bg = "LightBlue")
    titulos_entrada.place(relx = 0.54, rely = 0.2, relwidth=0.15, relheight = 0.05)

    finaceamentos_entrada = Entry(janela_filha, bg = "LightBlue")
    finaceamentos_entrada.place(relx = 0.54, rely = 0.26, relwidth=0.15, relheight = 0.05)

    
    ####################### Acrescentar passivo nao circulante ############################

    novo1_passivo_circulante = Label(janela_filha, text = "Acrescentar Passivo Não Circulante", fg = "white", bg = "#D2042D")
    novo1_passivo_circulante.place(relx = 0.38, rely = 0.58, relwidth=0.31, relheight = 0.03)
    
    texto_info = Label(janela_filha, text = "Nome", fg = "white", bg = "#D2042D")
    texto_info.place(relx = 0.42, rely = 0.62)

    valor_info = Label(janela_filha, text = "Valor", fg = "white", bg = "#D2042D")
    valor_info.place(relx = 0.57, rely = 0.62)

    novo1_passivo_nao_circulante_nome_entrada = Entry(janela_filha, bg = "LightBlue")
    novo1_passivo_nao_circulante_nome_entrada.place(relx = 0.38, rely = 0.66, relwidth=0.15, relheight = 0.03)

    novo1_passivo_nao_circulante_valor_entrada = Entry(janela_filha, bg = "LightBlue")
    novo1_passivo_nao_circulante_valor_entrada.place(relx = 0.55, rely = 0.66, relwidth=0.13, relheight = 0.03)

    novo2_passivo_nao_circulante_nome_entrada = Entry(janela_filha, bg = "LightBlue")
    novo2_passivo_nao_circulante_nome_entrada.place(relx = 0.38, rely = 0.70, relwidth=0.15, relheight = 0.03)

    novo2_passivo_nao_circulante_valor_entrada = Entry(janela_filha,  bg = "LightBlue")
    novo2_passivo_nao_circulante_valor_entrada.place(relx = 0.55, rely = 0.70, relwidth=0.13, relheight = 0.03)

    novo3_passivo_nao_circulante_nome_entrada = Entry(janela_filha,  bg = "LightBlue")
    novo3_passivo_nao_circulante_nome_entrada.place(relx = 0.38, rely = 0.74, relwidth=0.15, relheight = 0.03)

    novo3_passivo_nao_circulante_valor_entrada = Entry(janela_filha,  bg = "LightBlue")
    novo3_passivo_nao_circulante_valor_entrada.place(relx = 0.55, rely = 0.74, relwidth=0.13, relheight = 0.03)
   

     ####################### Patrimonios ############################

    passivo_circulante = Label(janela_filha, text = "Patrimônio líquido", fg = "white", bg = "#FF3333")
    passivo_circulante.place(relx = 0.71, rely = 0.1, relwidth=0.13 , relheight = 0.05)

    valor = Label(janela_filha, text = "Valor (R$)", fg = "white", bg = "#FF3333")
    valor.place(relx = 0.85, rely = 0.1, relwidth=0.13, relheight = 0.05)


    capital_proprio = Label(janela_filha, text = "Capital próprio", fg = "white", bg = "#FF6666")
    capital_proprio.place(relx = 0.71, rely = 0.2, relwidth=0.13, relheight = 0.05)

    reservas = Label(janela_filha, text = "Reservas de capital", fg = "white", bg = "#FF6666")
    reservas.place(relx = 0.71, rely = 0.26, relwidth=0.13, relheight = 0.05)

    reservas_lucro = Label(janela_filha, text = "Reservas de lucro", fg = "white", bg = "#FF6666")
    reservas_lucro.place(relx = 0.71, rely = 0.32, relwidth=0.13, relheight = 0.05)

    

    capital_proprio_entrada = Entry(janela_filha, fg = "black", bg = "LightBlue")
    capital_proprio_entrada.place(relx = 0.85, rely = 0.2, relwidth=0.13, relheight = 0.05)

    reservas_entrada = Entry(janela_filha, fg = "black", bg = "LightBlue")
    reservas_entrada.place(relx = 0.85, rely = 0.26, relwidth=0.13, relheight = 0.05)

    reservas_lucro_entrada = Entry(janela_filha, fg = "black", bg = "LightBlue")
    reservas_lucro_entrada.place(relx = 0.85, rely = 0.32, relwidth=0.13, relheight = 0.05)

     
    ####################### Acrescentar patrimonio ############################

    novo1_passivo_circulante = Label(janela_filha, text = "Acrescentar Patrimônio", fg = "white", bg ="#D2042D")
    novo1_passivo_circulante.place(relx = 0.72, rely = 0.58, relwidth=0.27, relheight = 0.03)
    
    texto_info = Label(janela_filha, text = "Nome", fg = "white", bg = "#D2042D")
    texto_info.place(relx = 0.76, rely = 0.62)

    valor_info = Label(janela_filha, text = "Valor", fg = "white", bg = "#D2042D" )
    valor_info.place(relx = 0.90, rely = 0.62)

    novo1_patrimonio_nome_entrada = Entry(janela_filha, bg = "LightBlue")
    novo1_patrimonio_nome_entrada.place(relx = 0.72, rely = 0.66, relwidth=0.13, relheight = 0.03)

    novo1_patrimonio_valor_entrada = Entry(janela_filha, bg = "LightBlue")
    novo1_patrimonio_valor_entrada.place(relx = 0.86, rely = 0.66, relwidth=0.13, relheight = 0.03)

    novo2_patrimonio_nome_entrada = Entry(janela_filha, bg = "LightBlue")
    novo2_patrimonio_nome_entrada.place(relx = 0.72, rely = 0.70, relwidth=0.13, relheight = 0.03)

    novo2_patrimonio_valor_entrada = Entry(janela_filha,  bg = "LightBlue")
    novo2_patrimonio_valor_entrada.place(relx = 0.86, rely = 0.70, relwidth=0.13, relheight = 0.03)

    novo3_patrimonio_nome_entrada = Entry(janela_filha,  bg = "LightBlue")
    novo3_patrimonio_nome_entrada.place(relx = 0.72, rely = 0.74, relwidth=0.13, relheight = 0.03)

    novo3_patrimonio_valor_entrada = Entry(janela_filha,  bg = "LightBlue")
    novo3_patrimonio_valor_entrada.place(relx = 0.86, rely = 0.74, relwidth=0.13, relheight = 0.03)




    

def relatorio():
    janela_filha=Toplevel(janela) # Página filha
    janela_filha.geometry("900x650") 
    janela_filha.title("Relatório final")
    janela_filha.configure(bg = "#FFCC99")
    janela_filha.resizable(1, 1)

    ############################################################
    tabela = PrettyTable()

    tabela_ativo = PrettyTable()
    tabela_ativo.title = "Ativo Circulante"

    lista_nomes_ativo_circulante = [i[0] for i in vetor_ativo_circulante]
    while len(lista_nomes_ativo_circulante) < 13:
        lista_nomes_ativo_circulante.append("-")

    tabela_ativo.add_column("Nome",lista_nomes_ativo_circulante)

    lista_valores_ativo_circulante = [i[1] for i in vetor_ativo_circulante]
    while len(lista_valores_ativo_circulante) <13:
        lista_valores_ativo_circulante.append("-")

    tabela_ativo.add_column("Valores",lista_valores_ativo_circulante)
    
    #############################################################
    tabela_ativo_nao = PrettyTable()
    tabela_ativo_nao.title = "Ativo Não Circulante"

    lista_nomes_ativo_nao_circulante = [i[0] for i in vetor_ativo_nao_circulante]
    while len(lista_nomes_ativo_nao_circulante) < 13:
        lista_nomes_ativo_nao_circulante.append("-")
    tabela_ativo_nao.add_column("Nome",lista_nomes_ativo_nao_circulante)
    lista_valores_ativo_nao_circulante = [i[1] for i in vetor_ativo_nao_circulante]
    while len(lista_valores_ativo_nao_circulante) < 13:
        lista_valores_ativo_nao_circulante.append("-")
    tabela_ativo_nao.add_column("Valores",lista_valores_ativo_nao_circulante)
    
    #########################################################
    tabela_passivo = PrettyTable()
    tabela_passivo.title = "Passivo Circulante"

    lista_nomes_passivo_circulante = [i[0] for i in vetor_passivo_circulante]
    while len(lista_nomes_passivo_circulante) < 13:
        lista_nomes_passivo_circulante.append("-")
    tabela_passivo.add_column("Nome",lista_nomes_passivo_circulante)
    lista_valores_passivo_circulante = [i[1] for i in vetor_passivo_circulante]
    while len(lista_valores_passivo_circulante) < 13:
        lista_valores_passivo_circulante.append("-")
    tabela_passivo.add_column("Valores",lista_valores_passivo_circulante)
    
    
    ########################################################
    tabela_passivo_nao = PrettyTable()
    tabela_passivo_nao.title = "Passivo Circulante"

    lista_nomes_passivo_nao_circulante = [i[0] for i in vetor_passivo_nao_circulante]
    while len(lista_nomes_passivo_nao_circulante) < 13:
        lista_nomes_passivo_nao_circulante.append("-")
    tabela_passivo_nao.add_column("Nome",lista_nomes_passivo_nao_circulante)
    lista_valores_passivo_nao_circulante = [i[1] for i in vetor_passivo_nao_circulante]
    while len(lista_valores_passivo_nao_circulante) < 13:
        lista_valores_passivo_nao_circulante.append("-")
    tabela_passivo_nao.add_column("Valores",lista_valores_passivo_nao_circulante)

    ###############################################################
    
    lista_nomes_patrimonio = [i[0] for i in vetor_patrimonio]
    while len(lista_nomes_patrimonio) < 13:
        lista_nomes_patrimonio.append("-")

    lista_valores_patrimonio = [i[1] for i in vetor_patrimonio]
    while len(lista_valores_patrimonio) < 13:
        lista_valores_patrimonio.append("-")
    
    
    ########################################################
    
    tabela.add_column("Ativo Circulante",lista_nomes_ativo_circulante)
    tabela.add_column("Valores",lista_valores_ativo_circulante)
    tabela.add_column("Ativo N/ Circulante",lista_nomes_ativo_nao_circulante)
    tabela.add_column("Valores",lista_valores_ativo_nao_circulante)
   


    tabelaN = PrettyTable()
    tabelaN.add_column("Passivo Circulante", lista_nomes_passivo_circulante)
    tabelaN.add_column("Valores", lista_valores_passivo_circulante)
    tabelaN.add_column("Passivo N/ Circulente",lista_nomes_passivo_nao_circulante)
    tabelaN.add_column("Valores",lista_valores_passivo_nao_circulante)
    tabelaN.add_column("Patrimonio",lista_nomes_patrimonio)
    tabelaN.add_column("Valores",lista_valores_patrimonio)

    tabelaFinal = PrettyTable()
    somaAtivo = 0
    for i in lista_valores_ativo_circulante:
        if i == '-' or i == '':
            continue
        else:
            somaAtivo+= float(i)
    for i in lista_valores_ativo_nao_circulante:
        if i == '-' or i =='':
            continue
        else:
            somaAtivo+= float(i)
    somaPassivo = 0
    for i in lista_valores_passivo_circulante:
        if i == '-' or i == '':
            continue
        else:
            somaPassivo+= float(i)
    for i in lista_valores_passivo_nao_circulante:
        if i == '-' or i =='':
            continue
        else:
            somaPassivo+= float(i)
    somaPatrimonio = 0
    for i in lista_valores_patrimonio:
        if i == '-' or i =='':
            continue
        else:
            somaPatrimonio+= float(i)
    tabelaFinal.field_names = ["Tipo",'Valor']
    tabelaFinal.add_row(["Ativo ", somaAtivo])
    tabelaFinal.add_row(["Passivo ", somaPassivo])
    tabelaFinal.add_row(["Patrimonio", somaPatrimonio])
    
    
   

    

    


    def gerar_relatio():
        print(tabela_ativo)
        print(tabela_ativo_nao)

    titulo = tk.Label(janela_filha, font=('Helvetica', 14, 'bold'), text="Relatório Final", bg = "#FFCC99")
    titulo.place(relx = 0.05, rely = 0.01, relheight=0.1, relwidth=0.9)

    b2 = tk.Button(janela_filha, text=' Fechar Tudo', bg = "#808080", command=janela.destroy)
    b2.place(relx = 0.63, rely = 0.93, relwidth=0.12 , relheight = 0.05)

    b3 = tk.Button(janela_filha, text=' Fechar Atual',  bg = "#808080", command=janela_filha.destroy)
    b3.place(relx = 0.4, rely = 0.93, relwidth=0.12 , relheight = 0.05)

    b4 = tk.Button(janela_filha, text=' Gerar PDF',  bg = "#808080", command=gerar_relatio)
    b4.place(relx = 0.20, rely = 0.93, relwidth=0.12 , relheight = 0.05)

    quadro1 = tk.Text(janela_filha, bg = "#FFCC99")
    quadro1.place(relx = 0.01, rely = 0.1, relwidth=0.92, relheight=0.38)
    quadro1.insert(tk.END, tabelaN)

    quadro2 = tk.Text(janela_filha, bg = "#FFCC99")
    quadro2.place(relx = 0.01, rely = 0.50, relwidth=0.6, relheight=0.38)
    quadro2.insert(tk.END, tabela)
    
    quadro3 = tk.Text(janela_filha, bg = "red")
    quadro3.place(relx = 0.63, rely = 0.60, relwidth=0.23, relheight=0.18)
    quadro3.insert(tk.END, tabelaFinal)

    #quadro2 = tk.Label(janela_filha, text = tabela_ativo_nao, bg = "#FFCC99")
    #quadro2.place(relx = 0.38, rely = 0.3, relwidth=0.3, relheight=0.3)

    #quadro3 = tk.Label(janela_filha, text = tabela_passivo, bg = "#FFCC99")
    #quadro3.place(relx = 0.74, rely = 0.3, relwidth=0.3, relheight=0.3)

    #quadro4 = tk.Label(janela_filha, text = tabela_passivo_nao, bg = "#FFCC99")
    #quadro4.place(relx = 0.89, rely = 0.3, relwidth=0.3, relheight=0.3)
    



    

janela.mainloop()
