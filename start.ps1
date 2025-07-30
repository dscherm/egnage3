# Classroom Cube System Startup Script
Write-Host "🎲 Classroom Cube System" -ForegroundColor Blue
Write-Host "=========================" -ForegroundColor Blue

# Check if in correct directory
if (-not (Test-Path "teacher-hub") -or -not (Test-Path "cube-client")) {
    Write-Host "❌ Please run this script from the project root directory" -ForegroundColor Red
    exit 1
}

Write-Host "Choose what to run:" -ForegroundColor Yellow
Write-Host "1. Teacher Hub" -ForegroundColor White
Write-Host "2. Cube Client (Simulation)" -ForegroundColor White
Write-Host "3. Both (for testing)" -ForegroundColor White

$choice = Read-Host "Enter choice (1-3)"

switch ($choice) {
    "1" {
        Write-Host "🏫 Starting Teacher Hub..." -ForegroundColor Green
        cd teacher-hub
        python main.py
    }
    "2" {
        Write-Host "🎲 Starting Cube Client in simulation mode..." -ForegroundColor Green
        cd cube-client
        python main.py --simulation
    }
    "3" {
        Write-Host "🚀 Starting both components for testing..." -ForegroundColor Green
        Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd teacher-hub; python main.py"
        Start-Sleep -Seconds 2
        cd cube-client
        python main.py --simulation
    }
    default {
        Write-Host "❌ Invalid choice" -ForegroundColor Red
    }
}
