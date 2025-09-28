#!/usr/bin/env node

const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');

const args = process.argv.slice(2);
const analyserPath = path.join(__dirname, 'midknight.py');

// Prefer venv Python if present (.venv or venv; Unix or Windows)
const venvCandidates = [
  path.join(__dirname, '.venv', 'bin', 'python3'),
  path.join(__dirname, '.venv', 'bin', 'python'),
  path.join(__dirname, 'venv',  'bin', 'python3'),
  path.join(__dirname, 'venv',  'bin', 'python'),
  path.join(__dirname, '.venv', 'Scripts', 'python.exe'),   // Windows
  path.join(__dirname, 'venv',  'Scripts', 'python.exe'),   // Windows
];

const venvPython = venvCandidates.find(p => fs.existsSync(p));
const systemPython = process.platform === 'win32' ? 'python' : 'python3';
const pythonCmd = venvPython || systemPython;

if (!fs.existsSync(analyserPath)) {
  console.error('Could not find analyser.py next to index.js');
  process.exit(1);
}

// IMPORTANT: pass env so GEMINI_API_KEY from MidKnight reaches the analyser
const py = spawn(pythonCmd, [analyserPath, ...args], {
  stdio: 'inherit',
  env: process.env,
});

// Bubble up errors & exit code
py.on('error', (err) => {
  console.error('Failed to start Python process. Ensure Python 3 is installed and venv deps are installed.');
  console.error(err);
  process.exit(1);
});

py.on('close', (code) => {
  process.exit(code);
});
