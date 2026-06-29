Add-Type -AssemblyName System.Drawing
$img = [System.Drawing.Image]::FromFile("c:\Users\miriam.castro\.gemini\antigravity\scratch\iao-website\products_boiler_v2.png")
$bmp = New-Object System.Drawing.Bitmap($img)
$pixel = $bmp.GetPixel(0, 0)
Write-Host "Color: R=$($pixel.R) G=$($pixel.G) B=$($pixel.B) A=$($pixel.A)"
$img.Dispose()
$bmp.Dispose()
