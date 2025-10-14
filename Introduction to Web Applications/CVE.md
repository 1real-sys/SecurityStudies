# CVE e CVSS

Sistema padronizado para identificar e classificar vulnerabilidades de segurança em software e hardware.

## CVE - Common Vulnerabilities and Exposures

### **O que é CVE**
Dicionário público de vulnerabilidades com identificador único:
```
CVE-[ANO]-[NÚMERO]
Exemplo: CVE-2021-44228 (Log4Shell)
```

**Componentes:**
- ID único e permanente
- Descrição da vulnerabilidade
- Referências e patches
- CWE (tipo de vulnerabilidade)

## CVSS - Common Vulnerability Scoring System

Sistema de pontuação de 0 a 10 para avaliar gravidade.

### **Classificação de Severidade**

| Score | Severidade | Ação |
|-------|------------|------|
| 0.1-3.9 | Low | Baixa prioridade |
| 4.0-6.9 | Medium | Corrigir em semanas |
| 7.0-8.9 | High | Corrigir em dias |
| 9.0-10.0 | Critical | Corrigir imediatamente |

## CVSS v2 (Legado)

### **Métricas Principais**
- **Access Vector**: Local, Adjacent, Network
- **Access Complexity**: High, Medium, Low
- **Authentication**: Multiple, Single, None
- **Impact (C/I/A)**: None, Partial, Complete

**Fórmula Conceitual:**
```
Score = (0.6 × Impact) + (0.4 × Exploitability) - 1.5
```

## CVSS v3 (Atual)

### **Métricas Base**

**Attack Vector (AV)**:
- Network (N), Adjacent (A), Local (L), Physical (P)

**Attack Complexity (AC)**:
- Low (L), High (H)

**Privileges Required (PR)**:
- None (N), Low (L), High (H)

**User Interaction (UI)** - *Nova em v3*:
- None (N), Required (R)

**Scope (S)** - *Nova em v3*:
- Unchanged (U), Changed (C)

**Impact (C/I/A)**:
- None (N), Low (L), High (H)

### **Principais Diferenças v2 vs v3**
- **User Interaction**: Não existia em v2
- **Scope**: Nova métrica para impacto além do componente
- **Impact**: 3 níveis em v3 vs 3 em v2 (mais granular)

## Exemplos de Vulnerabilidades

### **Critical (10.0) - Log4Shell**
```
CVE-2021-44228
CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H

Por que Critical?
✓ Exploração remota (Network)
✓ Sem autenticação (PR:None)
✓ Fácil de explorar (AC:Low)
✓ Scope Changed (compromete outros sistemas)
✓ Impacto total (High em C/I/A)
```

### **High (8.1) - EternalBlue**
```
CVE-2017-0144
CVSS:3.0/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H

Por que não é Critical?
✗ Attack Complexity High
✗ Scope Unchanged
```

### **Medium (5.5) - Zerologon**
```
CVE-2020-1472
CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N

Por que Medium?
✗ Requer acesso Local
✗ Requer Privilégios
✗ Impacto apenas em Confidentiality
```

### **Low (3.7) - Information Disclosure**
```
CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:N/A:N

Por que Low?
✗ Difícil de explorar (AC:High)
✗ Impacto Low apenas em Confidentiality
✗ Informações não críticas
```

## Cálculo CVSS v3 - Exemplo Prático

### **SQL Injection em Web App**

**1. Determinar métricas:**
- AV:N (acessível via internet)
- AC:L (fácil de explorar)
- PR:N (sem autenticação)
- UI:N (exploit automático)
- S:U (banco de dados local)
- C:H / I:H / A:H (acesso total aos dados)

**2. Vetor:**
```
CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
```

**3. Score: 9.8 (Critical)**

## Uso Prático

### **Priorização de Patches**
```
Critical (9-10)  → Corrigir em 24-48h
High (7-8.9)     → Corrigir em 7 dias
Medium (4-6.9)   → Corrigir em 30 dias
Low (0.1-3.9)    → Corrigir quando possível
```

### **Limitações**
- Não considera contexto organizacional
- Score ≠ Impacto real no negócio
- Deve ser combinado com threat intelligence
- Não substitui análise de risco completa

## Ferramentas e Recursos

**Calculadoras:**
- FIRST CVSS Calculator: https://www.first.org/cvss/calculator
- NVD Calculator: https://nvd.nist.gov/vuln-metrics/cvss

**Bases de Dados:**
- NVD: https://nvd.nist.gov/
- MITRE CVE: https://cve.mitre.org/
- Exploit-DB: https://www.exploit-db.com/

**Scanners:**
- Nessus, OpenVAS, Qualys (priorizam por CVSS)

## Conclusão

CVE fornece identificação única de vulnerabilidades, enquanto CVSS quantifica sua gravidade. A evolução do v2 para v3 trouxe métricas como Scope e User Interaction, permitindo avaliações mais precisas. Entender essas métricas é essencial para priorizar patches e gerenciar riscos de segurança efetivamente.