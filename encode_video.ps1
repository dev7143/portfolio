param(
    [Parameter(Mandatory = $true, Position = 0)][string]$Source,
    [string]$OutDir = $null,
    [int]$Crf = 20,
    [switch]$Poster
)

$ErrorActionPreference = 'Continue'
if (-not $OutDir) { $OutDir = Join-Path $PSScriptRoot 'videos' }
$ff = Join-Path $PSScriptRoot 'node_modules\@ffmpeg-installer\win32-x64\ffmpeg.exe'
if (-not (Test-Path $ff)) { throw 'ffmpeg not found under node_modules/@ffmpeg-installer' }
if (-not (Test-Path $Source)) { throw "source not found: $Source" }
New-Item -ItemType Directory -Force -Path $OutDir | Out-Null

# ---- probe source ----
$info = (& $ff -hide_banner -i $Source 2>&1) -join "`n"
$m = [regex]::Match($info, '(\d{2,5})x(\d{2,5})')
if (-not $m.Success) { throw 'cannot parse source resolution' }
$w = [int]$m.Groups[1].Value
$h = [int]$m.Groups[2].Value
$fps = 0.0
$fm = [regex]::Match($info, '([\d.]+) fps')
if ($fm.Success) { $fps = [double]$fm.Groups[1].Value }

$base = [System.IO.Path]::GetFileNameWithoutExtension($Source)
$out = Join-Path $OutDir ($base + '.mp4')

# ---- decide filters / level / keyframes ----
if ($h -ge 1080 -and $w -ge 1920) {
    $vf = 'fps=60,scale=1920:1080:flags=lanczos,unsharp=5:5:0.5:5:5:0.0'
    $level = '4.2'
    $keyint = 'keyint=120:min-keyint=30'
    $outFps = '60'
} else {
    $vf = 'unsharp=5:5:0.5:5:5:0.0'
    $level = '4.0'
    $keyint = 'keyint=60:min-keyint=15'
    $outFps = 'same'
}

Write-Output ("source: {0}x{1} @ {2}fps  ->  {3}" -f $w, $h, $fps, $out)
$start = Get-Date
& $ff -y -hide_banner -loglevel error -stats -i $Source `
    -c:v libx264 -preset slow -crf $Crf -maxrate 10M -bufsize 20M `
    -profile:v high -level $level -pix_fmt yuv420p -vf $vf `
    -x264-params $keyint -c:a aac -b:a 128k -ac 2 -movflags +faststart $out
if ($LASTEXITCODE -ne 0) { throw 'encode failed' }

$sec = [math]::Round(((Get-Date) - $start).TotalSeconds, 1)
$mb = [math]::Round((Get-Item $out).Length / 1MB, 2)
$oi = (& $ff -hide_banner -i $out 2>&1) -join "`n"
$br = [regex]::Match($oi, 'bitrate: (\d+) kb/s').Groups[1].Value
Write-Output ("done in {0}s  size {1}MB  bitrate {2}kbps" -f $sec, $mb, $br)

if ($Poster) {
    $posterDir = Join-Path $OutDir 'posters'
    New-Item -ItemType Directory -Force -Path $posterDir | Out-Null
    $durM = [regex]::Match($oi, 'Duration: (\d+):(\d+):([\d.]+)')
    $total = [double]$durM.Groups[1].Value * 3600 + [double]$durM.Groups[2].Value * 60 + [double]$durM.Groups[3].Value
    $at = [math]::Round($total * 0.2, 2)
    $posterPath = Join-Path $posterDir ($base + '.jpg')
    & $ff -y -hide_banner -loglevel error -ss $at -i $out -frames:v 1 -q:v 3 $posterPath
    Write-Output ("poster: {0}" -f $posterPath)
}
