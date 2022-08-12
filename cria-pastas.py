from dataclasses import replace
import os
from time import sleep



class comandos_cmd():

    def gera_lista():
        os.system('dir "C:\\Users\\gusta\\Desktop\\html-css" /b > "C:\\Users\\gusta\\Desktop\\html-css\\Projeto-C\\list_files.txt"')
        return 0
    
    def importa_lista():
        lista_arquivos = []
        arquivos = open(r"C:\Users\gusta\Desktop\html-css\Projeto-C\list_files.txt").read().splitlines()
        for x in range(0,len(arquivos)):
            if len(arquivos[x]) == 5:
                lista_arquivos.append(arquivos[x])
        return lista_arquivos

    def cria_nome():
        nome_pasta = comandos_cmd.importa_lista()
        nome_pasta = nome_pasta[len(nome_pasta) - 1]
        numero_pasta = int(nome_pasta[3:5]) + 1

        nome_pasta = nome_pasta[0:2]+f'{numero_pasta:03d}'
        return nome_pasta

    def cria_pasta():
        nome = comandos_cmd.cria_nome()
        os.system(f'mkdir "C:\\Users\\gusta\\Desktop\\html-css\\{nome}"')
        os.system(f'type nul > "C:\\Users\\gusta\\Desktop\\html-css\\{nome}\index.html"')
        sleep(2)
        print(f'"C:\\Users\\gusta\\Desktop\\html-css\\{nome}\\"')
        comandos_cmd.abre_com_vscode(f'"C:\\Users\\gusta\\Desktop\\html-css\\{nome}\\"')
    
    def abre_com_vscode(caminho):
        os.system(f'start "" code {caminho}')
        return 0


comandos_cmd.gera_lista()
comandos_cmd.importa_lista()
comandos_cmd.cria_nome()
comandos_cmd.cria_pasta()
            
