# Permissões Especiais

A permissão **Set User ID upon Execution** (`setuid`) permite que um usuário execute um programa com as permissões efetivas do dono do arquivo (geralmente `root`). No Linux, esse bit especial aparece como `s` na posição de execução do dono.

## Enumerando binários setuid

```bash
JLMreal@htb[/htb]$ find / -user root -perm -4000 -exec ls -ldb {} \; 2>/dev/null
```

```text
-rwsr-xr-x 1 root root 16728 Sep  1 19:06 /home/htb-student/shared_obj_hijack/payroll
-rwsr-xr-x 1 root root 16728 Sep  1 22:05 /home/mrb3n/payroll
-rwSr--r-- 1 root root 0 Aug 31 02:51 /home/cliff.moore/netracer
-rwsr-xr-x 1 root root 40152 Nov 30  2017 /bin/mount
-rwsr-xr-x 1 root root 40128 May 17  2017 /bin/su
-rwsr-xr-x 1 root root 27608 Nov 30  2017 /bin/umount
...SNIP...
```

## Aprofundando: pontos importantes sobre setuid

1. **`s` vs `S`**  
   `-rwsr-xr-x` indica setuid ativo com permissão de execução para o dono.  
   `-rwSr--r--` indica setuid ativo, mas sem bit de execução do dono (maiúsculo `S`), então normalmente não executa diretamente.
2. **UID real vs UID efetivo**  
   Em binários setuid, o usuário real continua o mesmo, mas o **UID efetivo** do processo vira o dono do arquivo. Quase toda escalada por setuid depende disso.
3. **Scripts vs binários**  
   Em kernels Linux modernos, setuid em scripts costuma ser ignorado por segurança; em binários ELF continua relevante.
4. **Indicadores de risco**  
   Binários customizados em diretórios de usuário, caminhos graváveis, carregamento inseguro de bibliotecas, chamadas de comando e shell escapes são sinais fortes para escalada.

Pode ser possível fazer engenharia reversa em um binário setuid, identificar comportamentos inseguros (como `system()`, confiança em PATH, carregamento de biblioteca, injeção de comando) e escalar privilégios.

---

A permissão **Set Group ID** (`setgid`) permite executar binários com o grupo efetivo do dono do arquivo. Ela também tem efeito em diretórios: arquivos criados dentro de diretório com setgid herdam o grupo desse diretório.

## Enumerando binários setgid

```bash
JLMreal@htb[/htb]$ find / -user root -perm -6000 -exec ls -ldb {} \; 2>/dev/null
```

```text
-rwsr-sr-x 1 root root 85832 Nov 30  2017 /usr/lib/snapd/snap-confine
```

## Aprofundando: pontos importantes sobre setgid

1. **setgid em arquivos** concede privilégios de grupo ao processo, podendo liberar acesso a arquivos, sockets e recursos de serviço.
2. **setgid em diretórios** é comum para colaboração, mas pode virar risco quando combinado com permissões de escrita fracas e automações privilegiadas.
3. **Caminhos de exploração** costumam envolver scripts, logs, sockets ou recursos IPC pertencentes a grupos sensíveis com escrita indevida.

---

## GTFOBins

O projeto **GTFOBins** é uma lista curada de binários Unix que podem ser abusados para:

- Escalada de privilégios
- Escape de shell restrito
- Leitura/escrita de arquivos
- Execução de comandos
- Shell reverso/bind shell (dependendo do contexto)

Cada entrada do GTFOBins mapeia técnicas por contexto (execução normal, `sudo`, SUID, capabilities).  
Esse contexto é decisivo: uma técnica que funciona com `sudo` pode falhar sem `sudo`.

### Fluxo prático de triagem com GTFOBins

1. Enumerar binários candidatos (`sudo -l`, lista SUID, capabilities, ferramentas no PATH).
2. Cruzar cada binário no GTFOBins pelo nome exato.
3. Confirmar o contexto correto de abuso (`sudo`/SUID/capabilities).
4. Validar restrições (uso de caminho absoluto, `noexec`, sanitização de ambiente, diferenças de versão).
5. Aplicar a técnica mínima necessária para obter acesso elevado estável.

Exemplo: `apt-get` pode ser abusado (em certos contextos) para abrir shell com pre-invoke:

```bash
JLMreal@htb[/htb]$ sudo apt-get update -o APT::Update::Pre-Invoke::=/bin/sh
```

```bash
# id
uid=0(root) gid=0(root) groups=0(root)
```

Conhecer GTFOBins acelera muito a triagem de escalada de privilégios em avaliações reais, porque ajuda a separar rapidamente binários pouco úteis de caminhos de exploração realmente viáveis.
