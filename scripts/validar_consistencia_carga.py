"""
Projeto: Validador de Carga e Migração de Dados para ERP
Autor: Cristiano Silva
Descrição: Analisa lista de registros cadastrais e gera relatório
           de integridade (campos nulos, duplicidades e prontidão para Go Live).
"""

import sys

def validar_registros(dados_cadastrais):
    print("=" * 65)
    print("INICIANDO AUDITORIA PRÉ-CARGA DE DADOS - NASSAU TECNOLOGIA")
    print("=" * 65)
    
    total_registros = len(dados_cadastrais)
    registros_validos = 0
    inconsistencias = []
    documentos_vistos = set()

    for item in dados_cadastrais:
        id_item = item.get("id")
        nome = item.get("nome", "").strip()
        doc = str(item.get("documento", "")).strip()
        categoria = item.get("categoria", "").strip()

        erros = []

        # Validação 1: Nome ou Descrição obrigatória
        if not nome:
            erros.append("Nome/Descrição ausente")

        # Validação 2: Documento ou Código de identificação
        if not doc or len(doc) < 5:
            erros.append("Documento/Código inválido ou incompleto")

        # Validação 3: Categoria/Subgrupo associado
        if not categoria:
            erros.append("Categoria/Subgrupo não parametrizado")

        # Validação 4: Duplicidade de documento
        if doc in documentos_vistos:
            erros.append(f"Documento duplicado ({doc})")
        else:
            if doc:
                documentos_vistos.add(doc)

        if erros:
            inconsistencias.append({
                "id": id_item,
                "registro": nome or "REGISTRO_SEM_NOME",
                "erros": ", ".join(erros)
            })
        else:
            registros_validos += 1

    # Relatório de Execução
    print(f"\n📊 RESUMO DA AUDITORIA:")
    print(f"Total de registros analisados : {total_registros}")
    print(f"Registros APTOS para migração  : {registros_validos} ({(registros_validos/total_registros)*100:.1f}%)")
    print(f"Registros com INCONSISTÊNCIAS : {len(inconsistencias)}")

    if inconsistencias:
        print("\n⚠️ DETALHE DAS DIVERGÊNCIAS ENCONTRADAS:")
        for inc in inconsistencias:
            print(f" - ID {inc['id']} [{inc['registro']}]: {inc['erros']}")
    else:
        print("\n✅ Base 100% íntegra para carga no ERP!")
    print("=" * 65)


if __name__ == "__main__":
    # Massa de dados de teste (simulando extração de cadastro legada)
    amostra_dados = [
        {"id": 101, "nome": "Consulta Cardiologia", "documento": "PROC001", "categoria": "Eletivo"},
        {"id": 102, "nome": "Seringa Descartável 10ml", "documento": "MAT0452", "categoria": "Material"},
        {"id": 103, "nome": "", "documento": "MAT0453", "categoria": "Material"},  # Erro: Sem nome
        {"id": 104, "nome": "Paracetamol 500mg", "documento": "", "categoria": "Medicamento"},  # Erro: Sem doc
        {"id": 105, "nome": "Dipirona 500mg", "documento": "MAT0452", "categoria": "Medicamento"},  # Erro: Doc duplicado
        {"id": 106, "nome": "Hemograma Completo", "documento": "PROC089", "categoria": "Laboratório"}
    ]
    
    validar_registros(amostra_dados)
