#!/bin/bash
# Install script for pi-dashboard on Raspberry Pi
set -e

# Ensure running on Raspberry Pi OS
if ! grep -q 'Raspbian\|Raspberry Pi' /etc/os-release; then
  echo "This script is intended for Raspberry Pi OS."
  exit 1
fi

# Update and install system dependencies
sudo apt-get update
sudo apt-get install -y python3 python3-pip python3-venv

# Create Python virtual environment
python3 -m venv ~/pi-dashboard-venv
source ~/pi-dashboard-venv/bin/activate

# Install Python dependencies
pip install --upgrade pip
pip install -r hardware_tester/requirements.txt


# Create Applications menu entry for Pi Dashboard Tests
mkdir -p ~/.local/share/applications
cat <<EOF > ~/.local/share/applications/pi-dashboard-tests.desktop
[Desktop Entry]
Type=Application
Name=Pi Dashboard Tests
Exec=bash -c 'source ~/pi-dashboard-venv/bin/activate && cd ~/pi-dashboard/hardware_tester && python -m unittest discover'
Icon=utilities-terminal
Terminal=true
Categories=PiDashboard;Testing;
EOF
chmod +x ~/.local/share/applications/pi-dashboard-tests.desktop

echo "Installation complete! You can now run the tests from the Applications menu under 'Pi Dashboard'."
