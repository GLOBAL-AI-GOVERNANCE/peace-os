#!/usr/bin/env python3
from generate_manifest import ROOT, controlled_files

CANONICAL = 'Peace OS: Crisis Room'
SLUG = 'peace-os-crisis-room'
REPOSITORY = 'GLOBAL-AI-GOVERNANCE/peace-os'
VERSION = '0.3.0-rc3'
DISCLAIMER = 'Peace OS is the product name. This project is not a computer operating system.'

for rel in ('README.md', 'game/project.godot', 'RELEASE_NOTES.md', 'web/index.html'):
    if CANONICAL not in (ROOT / rel).read_text(encoding='utf-8'):
        raise SystemExit(f'{rel} missing canonical product name')

if DISCLAIMER not in (ROOT / 'README.md').read_text(encoding='utf-8'):
    raise SystemExit('README missing the non-operating-system clarification')
if REPOSITORY not in (ROOT / 'scripts/publish_to_github.sh').read_text(encoding='utf-8'):
    raise SystemExit('Publication script does not target the canonical repository')
if (ROOT / 'VERSION').read_text(encoding='utf-8').strip() != VERSION:
    raise SystemExit('Unexpected VERSION')

historical_name_allowlist = {
    'CHANGELOG.md',
    'RELEASE_NOTES.md',
    'docs/architecture/ADR-001-canonical-identity.md',
    'docs/audit/v0.2.1-public-scoring-audit-summary.md',
    'tests/test_program_lineage_contract.py',
}

text_suffixes = {'.md', '.txt', '.py', '.gd', '.json', '.cfg', '.godot', '.yml', '.yaml', '.sh', '.cff', '.html', '.js', '.css', '.example'}

for rel in controlled_files():
    path = ROOT / rel
    if rel.as_posix() == 'tools/check_naming.py':
        continue
    rel_text = rel.as_posix()
    if rel.suffix.lower() not in text_suffixes and rel.name not in {'VERSION', 'LICENSE'}:
        continue
    text = path.read_text(encoding='utf-8', errors='ignore')
    if 'peace-governance-crisis-room' in text:
        raise SystemExit(f'Retired repository slug in {rel_text}')
    if 'Peace_Governance_Crisis_Room' in text:
        raise SystemExit(f'Retired filename-form identity in {rel_text}')
    if 'Peace Governance Crisis Room' in text and rel_text not in historical_name_allowlist:
        raise SystemExit(f'Historical product name outside the allowed record in {rel_text}')
    for stale in ('0.3.0-rc4', '0.3.0-rc5'):
        if stale in text and not rel_text.startswith('docs/audit/'):
            raise SystemExit(f'Internal candidate version leaked into {rel_text}')


FORMER_REPOSITORY = 'GLOBAL-AI-GOVERNANCE/peace-os-crisis-room'
FORMER_PAGES = 'https://global-ai-governance.github.io/peace-os-crisis-room/'
CURRENT_REPOSITORY_URL = 'https://github.com/GLOBAL-AI-GOVERNANCE/peace-os'
CURRENT_PAGES_URL = 'https://global-ai-governance.github.io/peace-os/'
HISTORICAL_IDENTITY_ALLOWLIST = {
    'CHANGELOG.md',
    'docs/architecture/ADR-001-canonical-identity.md',
    'VERIFICATION.md',
    'PUBLIC_RELEASE_GATE.md',
}
IDENTITY_CHECK_EXCLUSIONS = {
    'tools/check_naming.py',
    'tests/test_current_repository_identity.py',
}


def current_identity_violation(text, rel):
    """Return a failure when a former full repository or Pages identity is current."""
    if rel in HISTORICAL_IDENTITY_ALLOWLIST or rel in IDENTITY_CHECK_EXCLUSIONS:
        return None
    if FORMER_REPOSITORY in text:
        return f'Former repository identity remains current in {rel}'
    if FORMER_PAGES in text:
        return f'Former Pages identity remains current in {rel}'
    return None


for rel in controlled_files():
    if rel.as_posix() in IDENTITY_CHECK_EXCLUSIONS:
        continue
    if rel.suffix.lower() not in text_suffixes and rel.name not in {'VERSION', 'LICENSE'}:
        continue
    violation = current_identity_violation((ROOT / rel).read_text(encoding='utf-8', errors='ignore'), rel.as_posix())
    if violation:
        raise SystemExit(violation)

if CURRENT_REPOSITORY_URL not in (ROOT / 'CITATION.cff').read_text(encoding='utf-8'):
    raise SystemExit('CITATION.cff does not name the current repository')
if CURRENT_PAGES_URL not in (ROOT / 'CITATION.cff').read_text(encoding='utf-8'):
    raise SystemExit('CITATION.cff does not name the current Pages location')

print('Canonical Peace OS identity, repository, clarification, and version checks passed.')
