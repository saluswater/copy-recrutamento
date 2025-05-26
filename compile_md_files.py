#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para compilar múltiplos arquivos Markdown em um único arquivo TXT
Mantém os arquivos originais intactos
"""

import os
from datetime import datetime

def compile_markdown_files():
    """
    Compila todos os arquivos Markdown especificados em um único arquivo TXT
    """
    
    # Lista dos arquivos Markdown a serem compilados
    markdown_files = [
        "1.metodologia-marcelo-costa.md",
        "2.fundamentos-da-agua-da-florida.md", 
        "3.processo-salus-vendas-consultivas.md",
        "4.etapa1-apresentacao-rapport.md",
        "5.etapa2-analise-demonstracoes-cientificas.md",
        "6.etapa3-construcao-necessidade-calculos.md",
        "7.etapa4-apresentacao-solucao.md",
        "8.tratamento-avancado-objecoes.md",
        "9.fechamento-investimento.md",
        "10.ferramentas-kits-demonstracao.md",
        "escopo-landing-page.md",
        "mentoria-oscar.md",
        "escopo-treinamento-salus.md",
        "mentoria-jaime.md",
        "reuniao-23-05.md",
        "prompt-recrutador.md"
    ]
    
    # Nome do arquivo de saída
    output_file = "metodologia_salus_completa.txt"
    
    # Contador de arquivos processados
    processed_files = 0
    missing_files = []
    
    try:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            # Cabeçalho do arquivo compilado
            outfile.write("=" * 80 + "\n")
            outfile.write("METODOLOGIA SALUS WATER AI - COMPILAÇÃO COMPLETA\n")
            outfile.write("=" * 80 + "\n")
            outfile.write(f"Compilado em: {datetime.now().strftime('%d/%m/%Y às %H:%M:%S')}\n")
            outfile.write(f"Total de arquivos: {len(markdown_files)}\n")
            outfile.write("=" * 80 + "\n\n")
            
            # Processar cada arquivo Markdown
            for i, filename in enumerate(markdown_files, 1):
                print(f"Processando {i}/{len(markdown_files)}: {filename}")
                
                if os.path.exists(filename):
                    try:
                        with open(filename, 'r', encoding='utf-8') as infile:
                            content = infile.read()
                            
                            # Separador entre arquivos
                            outfile.write("\n" + "=" * 80 + "\n")
                            outfile.write(f"ARQUIVO {i}: {filename.upper()}\n")
                            outfile.write("=" * 80 + "\n\n")
                            
                            # Conteúdo do arquivo
                            outfile.write(content)
                            outfile.write("\n\n")
                            
                            processed_files += 1
                            
                    except Exception as e:
                        error_msg = f"Erro ao ler {filename}: {str(e)}"
                        print(f"❌ {error_msg}")
                        outfile.write(f"\n[ERRO] {error_msg}\n\n")
                        missing_files.append(filename)
                        
                else:
                    error_msg = f"Arquivo não encontrado: {filename}"
                    print(f"❌ {error_msg}")
                    outfile.write(f"\n[ARQUIVO NÃO ENCONTRADO] {filename}\n\n")
                    missing_files.append(filename)
            
            # Rodapé com estatísticas
            outfile.write("\n" + "=" * 80 + "\n")
            outfile.write("ESTATÍSTICAS DA COMPILAÇÃO\n")
            outfile.write("=" * 80 + "\n")
            outfile.write(f"Arquivos processados com sucesso: {processed_files}\n")
            outfile.write(f"Arquivos com problemas: {len(missing_files)}\n")
            outfile.write(f"Total de arquivos: {len(markdown_files)}\n")
            
            if missing_files:
                outfile.write(f"\nArquivos com problemas:\n")
                for file in missing_files:
                    outfile.write(f"- {file}\n")
            
            outfile.write(f"\nCompilação finalizada em: {datetime.now().strftime('%d/%m/%Y às %H:%M:%S')}\n")
            outfile.write("=" * 80 + "\n")
    
    except Exception as e:
        print(f"❌ Erro ao criar arquivo de saída: {str(e)}")
        return False
    
    # Relatório final
    print("\n" + "=" * 60)
    print("📋 RELATÓRIO DE COMPILAÇÃO")
    print("=" * 60)
    print(f"✅ Arquivos processados: {processed_files}/{len(markdown_files)}")
    print(f"📁 Arquivo de saída: {output_file}")
    
    if missing_files:
        print(f"❌ Arquivos com problemas: {len(missing_files)}")
        for file in missing_files:
            print(f"   - {file}")
    
    # Verificar tamanho do arquivo gerado
    if os.path.exists(output_file):
        file_size = os.path.getsize(output_file)
        print(f"📊 Tamanho do arquivo: {file_size:,} bytes ({file_size/1024:.1f} KB)")
    
    print("=" * 60)
    
    return True

def main():
    """
    Função principal
    """
    print("🚀 Iniciando compilação dos arquivos Markdown...")
    print("📝 Mantendo arquivos originais intactos")
    print("-" * 60)
    
    success = compile_markdown_files()
    
    if success:
        print("\n✅ Compilação concluída com sucesso!")
        print("📄 Arquivo 'metodologia_salus_completa.txt' criado")
    else:
        print("\n❌ Erro durante a compilação")
    
    return success

if __name__ == "__main__":
    main() 