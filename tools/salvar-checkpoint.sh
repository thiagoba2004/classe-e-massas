#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

# Classe e Massas — salvamento seguro de checkpoint
# Uso:
#   bash tools/salvar-checkpoint.sh "descrição do checkpoint"
#
# Faz quatro coisas:
#   1. cria snapshot local externo ao repositório;
#   2. verifica nomes potencialmente sensíveis antes de publicar;
#   3. cria commit Git com todas as mudanças do projeto;
#   4. envia ao origin e confirma que o SHA remoto é o mesmo SHA local.
#
# O snapshot é criado ANTES de qualquer operação Git, inclusive quando o
# procedimento interrompe por segurança.

MENSAGEM="${*:-checkpoint de segurança}"

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "ERRO: execute este comando dentro do repositório Classe e Massas."
  exit 1
fi

ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

BRANCH="$(git symbolic-ref --quiet --short HEAD || true)"
if [ -z "$BRANCH" ]; then
  echo "ERRO: HEAD destacado. O checkpoint remoto não será feito nessa condição."
  exit 1
fi

TIMESTAMP="$(date '+%Y%m%d-%H%M%S')"
BACKUP_DIR="${CEM_BACKUP_DIR:-$(dirname "$ROOT")/classe-e-massas-backups}"

# O backup deve ficar fora do próprio repositório para não depender da mesma
# árvore de trabalho que está protegendo.
case "$(cd "$(dirname "$BACKUP_DIR")" 2>/dev/null && pwd || dirname "$BACKUP_DIR")/$([ -d "$BACKUP_DIR" ] && basename "$BACKUP_DIR" || basename "$BACKUP_DIR")/" in
  "$ROOT"/*)
    echo "ERRO: CEM_BACKUP_DIR deve apontar para fora do repositório."
    exit 1
    ;;
esac

mkdir -p "$BACKUP_DIR"
BACKUP="$BACKUP_DIR/classe-e-massas-${TIMESTAMP}.tar.gz"

# Snapshot de todo o conteúdo visível do projeto, incluindo arquivos ainda não
# rastreados pelo Git. A pasta .git fica de fora porque o histórico já possui
# seu próprio mecanismo de recuperação.
tar --exclude='./.git' -czf "$BACKUP" .

if command -v sha256sum >/dev/null 2>&1; then
  sha256sum "$BACKUP" > "${BACKUP}.sha256"
fi

echo "SNAPSHOT LOCAL CRIADO: $BACKUP"

# Barreira simples contra publicação acidental de arquivos com nomes típicos
# de segredo. O snapshot local já existe mesmo se esta barreira interromper.
SENSIVE_RE='(^|/)(\.env($|\.)|id_rsa($|\.)|id_ed25519($|\.)|credentials?($|[._-])|secrets?($|[._-]))|\.(pem|key|p12|pfx)$'
STATUS_NAMES="$(git status --porcelain=v1 | sed -E 's/^.. //' || true)"

if printf '%s\n' "$STATUS_NAMES" | grep -Eiq "$SENSIVE_RE"; then
  echo "ATENÇÃO: foi encontrado nome de arquivo potencialmente sensível."
  echo "Nada foi enviado ao GitHub. O snapshot local foi preservado."
  printf '%s\n' "$STATUS_NAMES" | grep -Ei "$SENSIVE_RE" || true
  exit 2
fi

if [ -z "$(git status --porcelain)" ]; then
  echo "Nenhuma alteração pendente no repositório."
else
  git add -A

  if git diff --cached --quiet; then
    echo "Nenhuma alteração staged para commit."
  else
    git commit -m "checkpoint: ${TIMESTAMP} — ${MENSAGEM}"
  fi
fi

LOCAL_SHA="$(git rev-parse HEAD)"

echo "COMMIT LOCAL: $LOCAL_SHA"

if ! git remote get-url origin >/dev/null 2>&1; then
  echo "ATENÇÃO: remoto origin não configurado."
  echo "O snapshot local e o commit local continuam preservados."
  exit 3
fi

if ! git push origin "$BRANCH"; then
  echo "ATENÇÃO: o push falhou."
  echo "O snapshot local e o commit local continuam preservados."
  exit 4
fi

REMOTE_SHA="$(git ls-remote origin "refs/heads/$BRANCH" | awk '{print $1}')"

if [ "$REMOTE_SHA" != "$LOCAL_SHA" ]; then
  echo "ERRO DE VERIFICAÇÃO: o SHA remoto não coincide com o SHA local."
  echo "LOCAL : $LOCAL_SHA"
  echo "REMOTO: ${REMOTE_SHA:-não localizado}"
  exit 5
fi

echo "CHECKPOINT CONFIRMADO."
echo "Branch : $BRANCH"
echo "SHA    : $LOCAL_SHA"
echo "Backup : $BACKUP"
echo "Remoto : origin/$BRANCH verificado"
