#requires -Version 7
$ErrorActionPreference = 'Stop'
$staged = git diff --cached --name-only --diff-filter=ACMR
if (-not $staged) { exit 0 }

$patterns = @(
    'InstrumentationKey='
    'AKIA[0-9A-Z]{16}'
    'ASIA[0-9A-Z]{16}'
    'xoxb-[0-9]+-[0-9]+-[a-zA-Z0-9]+'
    'sk_live_[0-9a-zA-Z]+'
    'sk-ant-[0-9a-zA-Z_-]+'
    'ghp_[0-9a-zA-Z]{36,}'
    '-----BEGIN (RSA|OPENSSH|EC|PGP) PRIVATE KEY-----'
) -join '|'

$fail = $false
foreach ($f in $staged) {
    if (-not (Test-Path $f)) { continue }
    $hits = Select-String -Path $f -Pattern $patterns -AllMatches 2>$null
    if ($hits) {
        Write-Host "BLOCKED: $f" -ForegroundColor Red
        $hits | ForEach-Object { Write-Host "  line $($_.LineNumber): $($_.Line.Trim())" }
        $fail = $true
    }
}
if ($fail) { exit 1 }
