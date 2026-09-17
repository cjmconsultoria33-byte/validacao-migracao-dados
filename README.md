# Validação e Auditoria de Migração de Dados (ERP Rollout)

Conjunto de validações e rotinas de auditoria criadas para identificar inconsistências cadastrais, duplicidades e campos nulos críticos antes da carga final de dados em implantações de novos sistemas.

---

### 🎯 Problemas Prevenidos
* **Inconsistência de Cadastros:** Detecção prévia de registros sem documentação válida (CPF/CNPJ) ou cadastros incompletos que quebram rotinas de faturamento e agendamento.
* **Duplicidades de Itens:** Identificação de duplicidade de códigos ou descrições em cadastros de estoque (MatMed) e convênios.
* **Segurança no Go Live:** Relatório claro com contagem de registros aptos vs. inconsistentes para homologação junto aos gestores.

---

### 📂 Conteúdo
* `/scripts/validar_consistencia_carga.py`: Script de validação e geração de relatório de inconsistências cadastrais.
