#Requires -Version 7
<#
.SYNOPSIS
  PostToolUse — runs ruff (check --fix + format) on edited Python files.
#>
$ErrorActionPreference = 'SilentlyContinue'

try { $payload = [Console]::In.ReadToEnd() | ConvertFrom-Json } catch { exit 0 }

$path = $payload.tool_input.file_path
if (-not $path) { exit 0 }
if ($path -notmatch '\.(py|pyi)$') { exit 0 }
if (-not (Test-Path -LiteralPath $path)) { exit 0 }
if (-not (Get-Command ruff -ErrorAction SilentlyContinue)) { exit 0 }

& ruff check --fix --quiet $path 2>&1 | Out-Null
& ruff format --quiet $path 2>&1 | Out-Null

exit 0
